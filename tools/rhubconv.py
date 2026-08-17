"""
rhubconv.py — RHUB source-to-portal converter.

Transforms the legacy docsify Markdown/HTML found in RHUB_FULL_SOURCE_EXPORT.json
into clean, MDX-safe Markdown for Docusaurus 3.x.

Transformation rules (formatting only — no technical content is added, removed,
renamed or re-interpreted):
  * HTML <table> markup -> GitHub-flavoured Markdown tables (cell text verbatim)
  * "tap-to-open" reveal widgets -> fenced code blocks (json / http)
  * "About the API | Request URL | Request Method" tables -> endpoint callouts
  * requirement legend (<p class="version">) -> italic legend line
  * textNote / version1 blocks -> Docusaurus admonitions
  * docsify hash links -> portal routes
  * MDX-hostile characters ({ } stray <) escaped outside code blocks
"""
import re
import html as _html

# --------------------------------------------------------------------------
# HTML comments
# --------------------------------------------------------------------------


def comment_spans(text):
    spans = []
    i = 0
    while True:
        s = text.find('<!--', i)
        if s < 0:
            break
        e = text.find('-->', s + 4)
        if e < 0:
            spans.append((s, len(text)))
            break
        spans.append((s, e + 3))
        i = e + 3
    return spans


def strip_comments(text):
    out = []
    i = 0
    for a, b in comment_spans(text):
        out.append(text[i:a])
        i = b
    out.append(text[i:])
    return ''.join(out)


def comment_bodies(text):
    """Inner text of every HTML comment block."""
    return [text[a + 4:b - 3] for a, b in comment_spans(text)]


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

CODE_TOKEN = '@@RHUBCODE%d@@'


def _cell_text(raw):
    """Cell inner HTML -> single-line Markdown-safe text."""
    t = raw
    t = re.sub(r'<\s*br\s*/?\s*>', ' <br /> ', t, flags=re.I)
    t = re.sub(r'</\s*(p|div)\s*>', ' <br /> ', t, flags=re.I)
    t = re.sub(r'<\s*(b|strong)\s*>(.*?)</\s*(b|strong)\s*>', r'**\2**', t, flags=re.I | re.S)
    t = re.sub(r'<\s*li\s*>(.*?)(</\s*li\s*>|$)', r'• \1 <br /> ', t, flags=re.I | re.S)
    t = re.sub(r'<[^>]+>', '', t)
    t = _html.unescape(t)
    t = t.replace('|', '\\|')
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'(\s*<br />\s*)+$', '', t).strip()
    t = re.sub(r'(<br />\s*){2,}', '<br /> ', t)
    return t


IDENT_RE = re.compile(r'^[a-z][A-Za-z0-9]*(\s*,\s*[a-zA-Z][A-Za-z0-9]*)*$')


def _parse_rows(section_html):
    rows = []
    for tr in re.finditer(r'<tr[^>]*>(.*?)</tr>', section_html, re.S | re.I):
        cells = []
        for c in re.finditer(r'<(th|td)([^>]*)>(.*?)</\1>', tr.group(1), re.S | re.I):
            attrs = c.group(2)
            m = re.search(r'colspan\s*=\s*"?(\d+)"?', attrs, re.I)
            span = int(m.group(1)) if m else 1
            cells.append([_cell_text(c.group(3)), span, c.group(1).lower()])
        if cells:
            rows.append(cells)
    return rows


def html_table_to_md(table_html):
    """Convert one <table>...</table> block into Markdown."""
    inner = re.sub(r'<colgroup[^>]*>.*?</colgroup>', '', table_html, flags=re.S | re.I)

    thead = re.search(r'<thead[^>]*>(.*?)</thead>', inner, re.S | re.I)
    tbody = re.search(r'<tbody[^>]*>(.*?)</tbody>', inner, re.S | re.I)
    if thead:
        head_rows = _parse_rows(thead.group(1))
        body_rows = _parse_rows(tbody.group(1)) if tbody else []
        if not tbody:
            rest = inner[thead.end():]
            body_rows = _parse_rows(rest)
    else:
        all_rows = _parse_rows(inner)
        head_rows, body_rows = [], []
        for r in all_rows:
            if not body_rows and all(c[2] == 'th' for c in r):
                head_rows.append(r)
            else:
                body_rows.append(r)

    captions = []           # full-width header rows (e.g. "Sender (Individual)")
    group_notes = []        # header cells that span >1 column
    header_cells = []

    def expand(row):
        out = []
        for text, span, _k in row:
            for i in range(span):
                out.append(text if i == 0 else '')
        return out

    width = max([sum(c[1] for c in r) for r in (head_rows + body_rows)] or [0])

    real_head = []
    for r in head_rows:
        if len(r) == 1 and r[0][1] >= max(width, 2):
            captions.append(r[0][0])
        else:
            real_head.append(r)

    if real_head:
        grids = [expand(r) for r in real_head]
        for r in real_head:
            for text, span, _k in r:
                if span > 1 and text:
                    group_notes.append((text, span))
        width = max(width, max(len(g) for g in grids))
        for g in grids:
            g += [''] * (width - len(g))
        header_cells = []
        for i in range(width):
            parts = [g[i] for g in grids if g[i]]
            seen, uniq = set(), []
            for p in parts:
                if p not in seen:
                    seen.add(p)
                    uniq.append(p)
            header_cells.append(' · '.join(uniq))

    # promote a leading body row that carries the real column (field) names
    promoted = None
    if body_rows and group_notes:
        first = expand(body_rows[0])
        first += [''] * (width - len(first))
        nonempty = [c for c in first if c]
        idents = [c for c in nonempty if IDENT_RE.match(c.replace('\\|', ','))]
        if len(idents) >= 2 and len(idents) == len(nonempty) and len(nonempty) < width:
            promoted = first
            body_rows = body_rows[1:]

    if promoted:
        merged = []
        for i in range(width):
            merged.append(promoted[i] if promoted[i] else (header_cells[i] if i < len(header_cells) else ''))
        header_cells = merged

    if not header_cells:
        header_cells = [''] * width

    lines = []
    for cap in captions:
        lines.append('**%s**' % cap)
        lines.append('')
    if group_notes and promoted:
        lines.append('*Source column groups: %s*' %
                     '; '.join('%s (%d columns)' % (t, s) for t, s in group_notes))
        lines.append('')

    lines.append('| ' + ' | '.join(header_cells) + ' |')
    lines.append('|' + '|'.join(['---'] * width) + '|')
    for r in body_rows:
        cells = expand(r)
        if len(cells) > width:
            cells = cells[:width]
        # full-width group / label rows
        nonempty = [c for c in cells if c]
        if len(nonempty) == 1 and (len(r) == 1 or r[0][1] >= width):
            cells = ['**%s**' % nonempty[0]] + [''] * (width - 1)
        cells += [''] * (width - len(cells))
        lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines)


def convert_html_tables(text):
    out, pos = [], 0
    for m in re.finditer(r'<table[^>]*>.*?</table>', text, re.S | re.I):
        out.append(text[pos:m.start()])
        out.append('\n\n' + html_table_to_md(m.group(0)) + '\n\n')
        pos = m.end()
    out.append(text[pos:])
    return ''.join(out)


# --------------------------------------------------------------------------
# reveal ("tap-to-open") code widgets
# --------------------------------------------------------------------------


def extract_code_widgets(text, store):
    """Replace <div class="tap-to-open"> ... </div></div> with fenced code tokens."""
    out = []
    pos = 0
    pat = re.compile(r'<div class="tap-to-open">')
    while True:
        m = pat.search(text, pos)
        if not m:
            out.append(text[pos:])
            break
        out.append(text[pos:m.start()])
        cm = re.compile(r'<div class="code"[^>]*>').search(text, m.end())
        if not cm:
            out.append(text[m.start():m.end()])
            pos = m.end()
            continue
        end = text.find('</div>', cm.end())
        if end < 0:
            end = len(text)
        body = text[cm.end():end]
        out.append(_code_token(body, store))
        after = end + len('</div>')
        nxt = text.find('</div>', after)
        pos = (nxt + len('</div>')) if 0 <= nxt <= after + 40 else after
    return ''.join(out)


def _dedent(body):
    lines = [l.rstrip() for l in body.split('\n')]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    indents = [len(l) - len(l.lstrip()) for l in lines if l.strip()]
    cut = min(indents) if indents else 0
    return '\n'.join(l[cut:] if len(l) >= cut else l for l in lines)


def _code_token(body, store):
    code = _dedent(body)
    code = code.replace('\\[', '[').replace('\\]', ']')
    code = _html.unescape(code)
    stripped = code.lstrip()
    lang = 'json' if stripped[:1] in '{[' else 'http'
    if lang == 'http' and '{' in code and code.lstrip().startswith('{'):
        lang = 'json'
    token = CODE_TOKEN % len(store)
    store.append('```%s\n%s\n```' % (lang, code))
    return '\n\n' + token + '\n\n'


# --------------------------------------------------------------------------
# link mapping
# --------------------------------------------------------------------------

MASTER_SLUGS = {
    'get-remittance-purpose': 'remittance-purpose',
    'get-source-of-fund': 'source-of-fund',
    'get-relationship': 'relationship',
    'get-document-id-type': 'document-id-type',
    'get-occupation': 'occupation',
    'get-business-type': 'business-type',
    'get-business-registration-type': 'business-registration-type',
    'get-account-type': 'account-type',
    'get-wpt-wallet-list': 'wpt-wallet-list',
    'get-bank-list': 'bank-list',
    'get-customer-legal-status': 'customer-legal-status',
    'get-nature-of-business': 'nature-of-business',
    'get-customer-occupation-type': 'customer-occupation-type',
    'get-customerindividual-document-type': 'customer-individual-document-type',
}

UNRESOLVED_LINKS = []


def map_docsify_href(href):
    """Map a docsify hash route to a portal route."""
    h = href.strip()
    if h.startswith('http://') or h.startswith('https://'):
        return None
    h = h.lstrip('#').lstrip('/')
    h = h.replace('??', '?')
    if h.startswith('assets/'):
        UNRESOLVED_LINKS.append(href + ' (asset not present in source export)')
        return '/docs/appendix/source-notes'
    if '?id=' in h:
        page, anchor = h.split('?id=', 1)
    else:
        page, anchor = h, ''
    anchor = anchor.strip('-')
    page = page.replace('.md', '')
    table = {
        'AUTH': '/docs/authentication/authentication',
        'QUOTA': '/docs/quotation/quotation',
        'CUSTOMEREGIS': '/docs/customers/customer-registration',
        'DocumentUpload': '/docs/documents/document-upload',
        'PAYOUT-Api': '/docs/payout/payout',
        'PAYOUT-WPT': '/docs/payout/wpt-payout',
        'ENQUIRY': '/docs/transactions/transaction-enquiry',
        'COUNTRYVALIDATIONS': '/docs/validation/country-validations',
        'CURRENCYVALIDATIONS': '/docs/validation/currency-validations',
        'responseCodes': '/docs/errors/transaction-status-codes',
        'ErrorCodes': '/docs/errors/error-codes',
        'README': '/docs/',
        'apisequence': '/docs/getting-started/integration-flow',
        'transactionflow': '/docs/getting-started/transaction-flows',
        'master': '/docs/master-apis',
        'template': '/docs/template-management',
        'WPT': '/docs/wpt',
    }
    if page == 'ENQUIRY':
        if anchor.startswith('get-balance'):
            return '/docs/balance/balance-enquiry'
        if anchor.startswith('get-customer-enquiry'):
            return '/docs/appendix/unpublished-apis#customer-enquiry'
        return '/docs/transactions/transaction-enquiry'
    if page == 'PAYOUT-Api' and anchor.startswith('post-document-upload'):
        return '/docs/documents/document-upload'
    if page == 'master':
        if not anchor:
            return '/docs/master-apis'
        if anchor in MASTER_SLUGS:
            return '/docs/master-apis/' + MASTER_SLUGS[anchor]
        UNRESOLVED_LINKS.append(href + ' (no matching published section in source)')
        return '/docs/master-apis'
    base = table.get(page)
    if not base:
        UNRESOLVED_LINKS.append(href + ' (unknown source target)')
        return '/docs/appendix/source-notes'
    if anchor and page in ('CUSTOMEREGIS', 'PAYOUT-Api', 'PAYOUT-WPT', 'CURRENCYVALIDATIONS',
                           'COUNTRYVALIDATIONS', 'QUOTA'):
        if anchor.startswith('post-') or anchor.startswith('get-'):
            return base
        return base + '#' + anchor
    return base


def convert_anchors(text):
    def repl(m):
        href, label = m.group(1), m.group(2)
        label = re.sub(r'<[^>]+>', '', label)
        label = re.sub(r'\s+', ' ', _html.unescape(label)).strip()
        if href.startswith('http'):
            return '[%s](%s)' % (label or href, href)
        target = map_docsify_href(href)
        if target is None:
            return label
        return '[%s](%s)' % (label or target, target)
    return re.sub(r"<a[^>]*href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>", repl, text, flags=re.S)


# --------------------------------------------------------------------------
# inline / block cleanup
# --------------------------------------------------------------------------

LEGEND = '*Requirement legend: M = Mandatory · O = Optional · C = Conditional*'

FIELD_CLARIFICATION_TITLE = 'Field requirement clarification'


def convert_notes(text):
    # requirement legend
    text = re.sub(r'<p class="version">\s*\*\s*M\s*:.*?</p>', LEGEND, text, flags=re.S | re.I)
    text = re.sub(r'<p class="version">(.*?)</p>', lambda m: '*%s*' % _cell_text(m.group(1)),
                  text, flags=re.S)

    # multi-bullet field clarification block
    def clar(m):
        body = m.group(1)
        body = re.sub(r'<\s*br\s*/?\s*>', '', body, flags=re.I)
        body = re.sub(r'<[^>]+>', '', body)
        lines = [l.strip() for l in body.split('\n') if l.strip()]
        out = [':::info[%s]' % FIELD_CLARIFICATION_TITLE, '']
        for l in lines:
            out.append('- ' + l.lstrip('*').strip() if l.startswith('*') else l)
        out += ['', ':::']
        return '\n'.join(out)
    text = re.sub(r'<span class="version1">(.*?)</span>', clar, text, flags=re.S)

    def note(m):
        body = _cell_text(m.group(1))
        body = body.replace('<br />', '\n')
        if not body.strip():
            return ''
        return ':::note\n\n%s\n\n:::' % body
    text = re.sub(r'<div class="textNote">(.*?)</div>', note, text, flags=re.S)
    text = re.sub(r'<p class="textNote">(.*?)</p>', note, text, flags=re.S)
    text = re.sub(r'<span class="textNote">(.*?)</span>', note, text, flags=re.S)
    return text


def convert_inline(text):
    text = re.sub(r'<ion-icon[^>]*>\s*</ion-icon>', '', text, flags=re.I)
    text = re.sub(r'<ion-icon[^>]*/?>', '', text, flags=re.I)
    text = re.sub(r'<button[^>]*>.*?</button>', '', text, flags=re.S | re.I)
    text = re.sub(r'<span class="textBlue textBold">(.*?)</span>', r'**\1**', text, flags=re.S)
    text = re.sub(r'<span class="textBlue">(.*?)</span>', r'\1', text, flags=re.S)
    text = re.sub(r'<span class="version">(.*?)</span>', r'*\1*', text, flags=re.S)
    text = re.sub(r'<span class="background\w+Btn"[^>]*>(\w+)</span>', r'`\1`', text)
    text = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', text, flags=re.S)
    text = re.sub(r'<\s*(b|strong)\s*>(.*?)</\s*(b|strong)\s*>', r'**\2**', text, flags=re.S | re.I)

    # lists
    def ul(m):
        items = re.findall(r'<li[^>]*>(.*?)</li>', m.group(1), re.S | re.I)
        return '\n\n' + '\n'.join('- ' + _cell_text(i) for i in items) + '\n\n'
    text = re.sub(r'<ul[^>]*>(.*?)</ul>', ul, text, flags=re.S | re.I)

    text = re.sub(r'<\s*hr\s*/?\s*>', '\n\n---\n\n', text, flags=re.I)
    text = re.sub(r'<\s*br\s*/?\s*>', '<br />', text, flags=re.I)
    text = re.sub(r'</?\s*(div|p|section)[^>]*>', '\n\n', text, flags=re.I)
    return text


ENDPOINT_HEADERS = ('about the api',)


def md_table_rows(block):
    rows = []
    for line in block.strip().split('\n'):
        line = line.strip()
        if not line.startswith('|'):
            return None
        cells = [c.strip() for c in line.strip('|').split('|')]
        rows.append(cells)
    return rows


def convert_endpoint_tables(text, ep_store):
    """Markdown tables of the form 'About the API | Request URL | Request Method'."""
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('|') and 'about the api' in lines[i].lower():
            j = i
            block = []
            while j < len(lines) and lines[j].strip().startswith('|'):
                block.append(lines[j])
                j += 1
            rows = md_table_rows('\n'.join(block))
            if rows and len(rows) >= 3:
                header = rows[0]
                data_rows = rows[2:]
                out.extend(render_endpoint(header, data_rows, ep_store))
                i = j
                continue
        out.append(lines[i])
        i += 1
    return '\n'.join(out)


def render_endpoint(header, data_rows, ep_store):
    """Render an 'About the API / Request URL / Request Method' table as an endpoint block.

    Presentation only: the method string and the URL string are reproduced exactly as the
    source writes them. The URL is emitted inside a JSX string expression so that path
    placeholders such as {countryCode} survive MDX untouched.
    """
    lines = ['']
    hl = [h.lower() for h in header]
    for row in data_rows:
        row = row + [''] * (len(header) - len(row))
        about = ''
        methods = []
        urls = []
        for k, cell in zip(hl, row):
            if 'about' in k:
                about = cell
            elif 'method' in k:
                methods.append(cell)
            elif 'url' in k:
                label = re.sub(r'^request url\s*', '', k, flags=re.I).strip()
                urls.append((label, cell))
        method = (methods[0] if methods else '').strip()
        lines.append('<div className="rhub-endpoint">')
        for label, url in urls:
            clean = url.replace('<br />', '').replace('\\|', '|').strip()
            clean = re.sub(r'\s+', '', clean)
            if label:
                lines.append('  <div className="rhub-endpoint__label">%s</div>'
                             % label.strip().capitalize())
            lines.append('  <div className="rhub-endpoint__row">')
            if method:
                lines.append('    <span className="rhub-method rhub-method--%s">%s</span>'
                             % (method.lower(), method))
            lines.append("    <code className=\"rhub-endpoint__url\">{%s}</code>"
                         % repr(clean))
            lines.append('  </div>')
        lines.append('</div>')
        token = '@@RHUBEP%d@@' % len(ep_store)
        ep_store.append('\n'.join(lines[1:]))
        out = ['', token, '']
        if about:
            out.append(about.replace('<br />', ' ').strip())
            out.append('')
        return out
    return lines


# --------------------------------------------------------------------------
# MDX safety
# --------------------------------------------------------------------------


def escape_mdx(text):
    """Escape MDX-hostile characters outside fenced/inline code."""
    parts = re.split(r'(```.*?```|`[^`\n]*`|@@RHUBCODE\d+@@|@@RHUBEP\d+@@)', text, flags=re.S)
    for idx in range(0, len(parts)):
        if idx % 2 == 1:
            continue
        seg = parts[idx]
        seg = seg.replace('<br />', '@@BR@@')
        seg = seg.replace('{', '&#123;').replace('}', '&#125;')
        seg = seg.replace('<', '&lt;')
        seg = seg.replace('@@BR@@', '<br />')
        parts[idx] = seg
    return ''.join(parts)


def restore_code(text, store):
    for i, block in enumerate(store):
        text = text.replace(CODE_TOKEN % i, block)
    return text


def tidy(text):
    text = re.sub(r'[ \t]+$', '', text, flags=re.M)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'(\|\n)\n+(\|)', r'\1\2', text)
    return text.strip() + '\n'


IMAGE_NOTES = {
    './img/rhubbpt2.png': 'Bank payout transaction flow diagram',
    './img/rhubwpt2.png': 'Wallet payout transaction flow diagram',
    './img/apiseq.png': 'API call sequence diagram',
}


# How an unavailable source image is handled:
#   'admonition' -> a REVIEW REQUIRED callout at the point of the image
#   'silent'     -> the reference is dropped. Used where the page text stands on its own and
#                   the missing asset is recorded in the internal review resolution register.
IMAGE_NOTICE_MODE = 'admonition'


def convert_images(text):
    text = re.sub(r'!\[[^\]]*\]\(\./img/rhub\.png\)\s*', '', text)

    def img_note(src):
        if IMAGE_NOTICE_MODE == 'silent':
            return ''
        label = IMAGE_NOTES.get(src, src)
        return (':::caution[REVIEW REQUIRED — diagram not available]\n\n'
                'RHUB documents this step with a diagram (%s). The image is not available to '
                'this portal and no replacement has been drawn.\n\n:::' % label)

    text = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', lambda m: img_note(m.group(1)), text)
    text = re.sub(r'!\[[^\]]*\]\((\./img/[^)]+)\)', lambda m: img_note(m.group(1)), text)
    return text


# --------------------------------------------------------------------------
# main entry
# --------------------------------------------------------------------------


def convert(source_text, promote_headings=0, drop_first_h1=False):
    """Convert a source fragment to portal Markdown.

    promote_headings: number of levels to lift headings by (e.g. 1 turns ### into ##).
    """
    t = strip_comments(source_text)
    store = []
    t = extract_code_widgets(t, store)
    t = convert_images(t)
    t = convert_html_tables(t)
    t = convert_notes(t)
    t = convert_anchors(t)
    t = convert_inline(t)
    ep_store = []
    t = convert_endpoint_tables(t, ep_store)

    if promote_headings:
        def lift(m):
            hashes = m.group(1)
            n = max(2, len(hashes) - promote_headings)
            return '#' * n + ' ' + m.group(2).strip()
        t = re.sub(r'^(#{2,6})\s*(.+)$', lift, t, flags=re.M)

    if drop_first_h1:
        t = re.sub(r'^#\s+.*$', '', t, count=1, flags=re.M)

    t = escape_mdx(t)
    t = fix_md_tables(t)
    for i, block in enumerate(ep_store):
        t = t.replace('@@RHUBEP%d@@' % i, block)
    t = restore_code(t, store)
    return tidy(t)


# --------------------------------------------------------------------------
# Markdown table normalisation
# --------------------------------------------------------------------------

SEP_RE = re.compile(r'^\|[\s:|-]+\|$')


def _split_row(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def fix_md_tables(text):
    """Repair ragged Markdown tables inherited from the source.

    The source contains hand-written tables where some rows carry one cell too
    many (usually a stray empty cell), which would make GitHub-flavoured
    Markdown silently drop the last cell — losing a field description. Extra
    *empty* cells are removed so that every non-empty source value survives;
    if a row still has too many non-empty cells, the surplus is appended to the
    final column rather than discarded. Short rows are padded.

    Table fragments that have no header/separator row (the source has a couple,
    left over from split HTML comments) are preserved verbatim inside a code
    block instead of rendering as a stream of pipes.
    """
    lines = text.split('\n')
    out = []
    i = 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            in_code = not in_code
            out.append(line)
            i += 1
            continue
        if in_code or not line.strip().startswith('|'):
            out.append(line)
            i += 1
            continue

        block = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            block.append(lines[i])
            i += 1

        if len(block) < 2 or not SEP_RE.match(block[1].strip()):
            out.append('```text')
            out.extend(block)
            out.append('```')
            out.append('')
            out.append('*Source fragment: this table has no header row in the RHUB source '
                       '(it is a continuation of a preceding table). It is reproduced verbatim '
                       'rather than given an invented header — REVIEW REQUIRED.*')
            continue

        width = len(_split_row(block[0]))
        fixed = [block[0], block[1]]
        for row in block[2:]:
            cells = _split_row(row)
            if len(cells) > width:
                # drop empty cells from the right of the surplus region first
                j = len(cells) - 1
                while len(cells) > width and j >= 0:
                    if cells[j] == '':
                        cells.pop(j)
                    j -= 1
                if len(cells) > width:
                    head = cells[:width - 1]
                    tail = ' '.join(c for c in cells[width - 1:] if c)
                    cells = head + [tail]
            if len(cells) < width:
                cells += [''] * (width - len(cells))
            fixed.append('| ' + ' | '.join(cells) + ' |')
        out.extend(fixed)
    return '\n'.join(out)
