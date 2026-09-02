"""
vaconv.py — converts the RHUB Virtual Account source HTML into portal Markdown.

The VA source is a standalone HTML document with its own design system. This module
extracts its content — endpoints, field tables, requiredness pills, code samples and
callouts — and re-emits it as plain Markdown for the RHUB Developer Portal. Only
presentation changes: field names, requiredness classifications, endpoint paths and
sample payloads are carried across verbatim.

Two substitutions are applied on the way through, both of them RHUB decisions rather
than editorial choices:

  * the source's placeholder API-key auth wording is replaced with RHUB's real
    access-token model (see AUTH_SUBS);
  * the source's own "update before publishing" placeholder notice is dropped.

Anything the source marks TBD stays TBD.
"""
import html as _html
import re

from bs4 import BeautifulSoup, NavigableString

# RHUB decision: VA uses the same access token as the rest of the platform.
AUTH_SUBS = [
    ('Authorization: Bearer <sandbox_api_key>', 'Authorization: Bearer <access_token>'),
    ('Authorization: Bearer <production_api_key>', 'Authorization: Bearer <access_token>'),
    ('sandbox_api_key', 'access_token'),
    ('production_api_key', 'access_token'),
]

# Source blocks that must not reach clients: the author's own pre-publication notes and
# speculative environment behaviour that no RHUB source establishes.
DROP_PHRASES = [
    'Placeholder values',
    'update before publishing',
    'Replace them with the actual Sandbox and Production values',
    # RHUB has verified the Required / Optional / Conditional classifications, so the
    # source's note about inferring them from sample payloads is both internal
    # methodology and no longer accurate.
    'How "Required" is determined',
    'inferred from those examples',
]

CALLOUT_KIND = {'tip': 'note', 'warn': 'warning', 'info': 'info', 'ok': 'tip'}

# The source cross-references itself by section number ("see Section 14"). Those numbers
# mean nothing once the content is split across portal pages, so prose references are
# rewritten to the page that now holds that section. Code samples are left verbatim.
SECTION_PAGES = {
    '1': ('Overview', '/docs/virtual-accounts/'),
    '2': ('VA integration flow', '/docs/virtual-accounts/integration-flow'),
    '3': ('API environments', '/docs/getting-started/environments'),
    '4': ('VA currencies', '/docs/virtual-accounts/va-currencies'),
    '5': ('VA document requirements', '/docs/virtual-accounts/document-requirements'),
    '6': ('Upload VA documents', '/docs/virtual-accounts/upload-documents'),
    '7': ('Get uploaded VA documents', '/docs/virtual-accounts/get-documents'),
    '8': ('Create individual VA customer', '/docs/virtual-accounts/individual/create'),
    '9': ('Retrieve individual VA customer', '/docs/virtual-accounts/individual/retrieve'),
    '10': ('Edit individual VA customer', '/docs/virtual-accounts/individual/edit'),
    '11': ('Create business VA customer', '/docs/virtual-accounts/business/create'),
    '12': ('Retrieve business VA customer', '/docs/virtual-accounts/business/retrieve'),
    '13': ('Edit business VA customer', '/docs/virtual-accounts/business/edit'),
    '14': ('VA request status', '/docs/virtual-accounts/va-request-status'),
    '15': ('VA approval process', '/docs/virtual-accounts/va-approval-process'),
    '16': ('VA reference data', '/docs/virtual-accounts/va-reference-data'),
    '17': ('VA responses and errors', '/docs/virtual-accounts/responses-and-errors'),
    '18': ('Overview', '/docs/virtual-accounts/'),
}
SECTION_RE = re.compile(r'\bSections?\s+(\d{1,2})\b')


def _section_link(m):
    entry = SECTION_PAGES.get(m.group(1))
    if not entry:
        return m.group(0)
    label, route = entry
    return '[%s](%s)' % (label, route)


def _text(node):
    t = node.get_text(' ', strip=True) if hasattr(node, 'get_text') else str(node)
    t = _html.unescape(t)
    t = re.sub(r'[\u2500-\u257f\u2600-\u27bf\ufe0f\U0001F000-\U0001FAFF]', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def _inline(node):
    """Inline markdown for a table cell or paragraph: keeps code spans and bold."""
    out = []
    for c in node.children:
        if isinstance(c, NavigableString):
            out.append(_html.unescape(str(c)))
        elif c.name == 'code':
            out.append('`%s`' % _text(c))
        elif c.name in ('strong', 'b'):
            out.append('**%s**' % _text(c))
        elif c.name == 'br':
            out.append(' ')
        elif c.name == 'span' and 'pill' in (c.get('class') or []):
            out.append('**%s**' % _text(c))      # REQUIRED / OPTIONAL / YES / NO
        else:
            out.append(_inline(c) if hasattr(c, 'children') else _text(c))
    t = ''.join(out)
    t = re.sub(r'[\u2500-\u257f\u2600-\u27bf\ufe0f\U0001F000-\U0001FAFF]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t.replace('|', '\\|')


def _code(pre):
    """A <pre class="jcode"> sample, with the syntax spans removed."""
    txt = pre.get_text()
    txt = _html.unescape(txt)
    for a, b in AUTH_SUBS:
        txt = txt.replace(a, b)
    lines = [l.rstrip() for l in txt.split('\n')]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    body = '\n'.join(lines)
    lang = 'json' if body.lstrip()[:1] in '{[' else 'http'
    return '```%s\n%s\n```' % (lang, body)


def _table(tbl):
    """Any source table -> a Markdown table. Cell content is carried over verbatim."""
    head = tbl.select('thead tr')
    rows = tbl.select('tbody tr') or [r for r in tbl.select('tr') if r not in head]
    if head:
        cols = [_inline(c) for c in head[0].find_all(['th', 'td'])]
    else:
        cols = None

    body = []
    for r in rows:
        cells = [_inline(c) for c in r.find_all(['th', 'td'])]
        if any(cells):
            body.append(cells)
    if not body:
        return ''

    if cols is None:
        # a definition-style table (Method / URL / Path Parameter ...)
        width = max(len(r) for r in body)
        cols = ['Item', 'Value'][:width] if width == 2 else [''] * width
    width = max([len(cols)] + [len(r) for r in body])
    cols = cols + [''] * (width - len(cols))
    out = ['| ' + ' | '.join(cols) + ' |', '|' + '|'.join(['---'] * width) + '|']
    for r in body:
        r = r + [''] * (width - len(r))
        out.append('| ' + ' | '.join(r) + ' |')
    return '\n'.join(out)


def _endpoint_block(tbl):
    """The 'Endpoint' card table -> a method + path block plus any extra rows."""
    method = url = None
    extra = []
    for r in tbl.select('tr'):
        cells = r.find_all(['td', 'th'])
        if len(cells) < 2:
            continue
        label = _text(cells[0])
        if label.lower() == 'method':
            method = _text(cells[1])
        elif label.lower() == 'url':
            url = _text(cells[1])
        else:
            extra.append((label, _inline(cells[1])))
    if not url:
        return _table(tbl)
    lines = ['<div className="rhub-endpoint">',
             '  <div className="rhub-endpoint__row">']
    if method:
        lines.append('    <span className="rhub-method rhub-method--%s">%s</span>'
                     % (method.lower(), method))
    lines.append("    <code className=\"rhub-endpoint__url\">{%s}</code>" % repr(url))
    lines += ['  </div>', '</div>', '']
    for label, value in extra:
        lines.append('- **%s** — %s' % (label, value))
    return '\n'.join(lines)


def _drop(text):
    return any(p.lower() in text.lower() for p in DROP_PHRASES)


def _walk(node, out, level):
    """Emit markdown for the children of a section or card body, in document order."""
    for child in node.children:
        if isinstance(child, NavigableString):
            t = _html.unescape(str(child)).strip()
            if t:
                out.append(t)
            continue
        classes = child.get('class') or []
        name = child.name

        if name == 'span' and 'sec-anchor' in classes:
            continue
        if 'sec-hdr' in classes or 'card-hdr' in classes:
            continue
        if name in ('h1', 'h2'):
            continue
        if name == 'h3':
            out += ['', '#' * (level + 1) + ' ' + _text(child), '']
            continue
        if name == 'pre':
            out += ['', _code(child), '']
            continue
        if name == 'table':
            tclass = child.get('class') or []
            is_endpoint = any(_text(c).lower() == 'url' for c in child.select('td'))
            out += ['', _endpoint_block(child) if is_endpoint else _table(child), '']
            continue
        if 'callout' in classes:
            kind = next((CALLOUT_KIND[c] for c in classes if c in CALLOUT_KIND), 'note')
            body = _inline(child)
            body = re.sub(r'^\s*', '', body)
            if _drop(body) or not body:
                continue
            for a, b in AUTH_SUBS:
                body = body.replace(a, b)
            out += ['', ':::%s' % kind, '', body, '', ':::', '']
            continue
        if 'card' in classes:
            hdr = child.select_one('.card-hdr h3')
            if hdr:
                out += ['', '#' * (level + 1) + ' ' + _text(hdr), '']
            body = child.select_one('.card-body')
            _walk(body if body is not None else child, out, level)
            continue
        if name == 'div' or name == 'section':
            _walk(child, out, level)
            continue
        # inline-ish leftovers
        t = _inline(child)
        if t and not _drop(t):
            out.append(t)


def sections(html_text):
    """-> ordered list of dicts: num, title, badge, node."""
    soup = BeautifulSoup(html_text, 'html.parser')
    result = []
    for d in soup.select('div.sec'):
        num = d.select_one('.sec-num')
        title = d.select_one('.sec-title')
        badge = d.select_one('.sec-badge')
        result.append({
            'num': _text(num) if num else '',
            'title': _text(title) if title else '',
            'badge': _text(badge) if badge else '',
            'node': d,
        })
    return result


def section_markdown(section, level=2):
    """Markdown body for one source section, without its own H1/H2 title."""
    out = []
    _walk(section['node'], out, level)
    text = '\n'.join(out)
    for a, b in AUTH_SUBS:
        text = text.replace(a, b)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # MDX safety: protect fenced code and the endpoint JSX, escape the rest
    keep = []

    def stash(m):
        keep.append(m.group(0))
        return '@@VAKEEP%d@@' % (len(keep) - 1)

    text = re.sub(r'```.*?```', stash, text, flags=re.S)
    text = re.sub(r'<div className="rhub-endpoint">.*?\n</div>', stash, text, flags=re.S)
    text = text.replace('{', '&#123;').replace('}', '&#125;')
    text = re.sub(r'<(?!br\s*/?>)', '&lt;', text)
    text = SECTION_RE.sub(_section_link, text)
    for i, block in enumerate(keep):
        text = text.replace('@@VAKEEP%d@@' % i, block)
    return re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'
