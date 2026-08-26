#!/usr/bin/env python3
"""
generate.py — builds the RHUB Developer Portal docs tree from
RHUB_FULL_SOURCE_EXPORT.json (authoritative source).

Nothing in this script authors technical content: every field table, endpoint,
example and code sample is carried over from the source export. Editorial text
is limited to navigation, provenance notes and clearly-labelled conventions.
"""
import json, os, re, sys, shutil, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rhubconv as R

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_JSON = os.environ.get('RHUB_SOURCE_JSON',
                          os.path.join(os.path.dirname(HERE), 'source', 'RHUB_FULL_SOURCE_EXPORT.json'))
PORTAL = os.path.dirname(HERE)
DOCS = os.path.join(PORTAL, 'docs')

EXPORT = json.load(open(SRC_JSON))

# Supplemental authoritative data supplied directly by the RHUB team, kept in its own
# file so it can be updated independently of the documentation export. Optional: if the
# file is absent the portal simply omits the current-error-code page.
CURRENT_ERRORS_JSON = os.environ.get(
    'RHUB_CURRENT_ERRORS_JSON',
    os.path.join(os.path.dirname(HERE), 'source', 'RHUB_CURRENT_ERROR_CODES.json'))
CURRENT_ERRORS = (json.load(open(CURRENT_ERRORS_JSON))
                  if os.path.exists(CURRENT_ERRORS_JSON) else None)

# RHUB-confirmed operational / integration guidance. Explains how the documented
# contracts are used together; never changes a contract. Optional, like the error file.
GUIDANCE_JSON = os.environ.get(
    'RHUB_GUIDANCE_JSON',
    os.path.join(os.path.dirname(HERE), 'source', 'RHUB_INTEGRATION_GUIDANCE.json'))
GUIDANCE = (json.load(open(GUIDANCE_JSON))
            if os.path.exists(GUIDANCE_JSON) else None)

# Example-data convention: synthetic identities for client-facing examples. Applied to code
# blocks on listed pages only; unlisted audit pages keep the original values as evidence.
EXAMPLE_POLICY_JSON = os.environ.get(
    'RHUB_EXAMPLE_POLICY_JSON',
    os.path.join(os.path.dirname(HERE), 'source', 'RHUB_EXAMPLE_DATA_POLICY.json'))
EXAMPLE_POLICY = (json.load(open(EXAMPLE_POLICY_JSON))
                  if os.path.exists(EXAMPLE_POLICY_JSON) else None)
SANITISED = {'blocks': 0, 'values': 0}


def sanitise_examples(text):
    """Replace personal/company sample values inside fenced code blocks.

    Only example VALUES change. Field names, structure, enums, master data, endpoint paths
    and verbatim API error messages are untouched, and every replacement keeps the character
    class and a length the documented contract still allows.
    """
    if not EXAMPLE_POLICY:
        return text
    pairs = EXAMPLE_POLICY['replacements']

    def fix(m):
        block = m.group(0)
        before = block
        for old, new in pairs:
            if old in block:
                SANITISED['values'] += block.count(old)
                block = block.replace(old, new)
        if block != before:
            SANITISED['blocks'] += 1
        return block

    out = re.sub(r'```[a-z]*\n.*?```', fix, text, flags=re.S)

    # field-table descriptions carry sample values too ("eg: Rahul"); the same policy applies
    def fix_line(line):
        if not line.lstrip().startswith('|'):
            return line
        for old, new in pairs:
            if old in line:
                SANITISED['values'] += line.count(old)
                line = line.replace(old, new)
        return line

    return '\n'.join(fix_line(l) for l in out.split('\n'))


def sequence_steps():
    """The RHUB-confirmed integration sequence, from the guidance source."""
    if not GUIDANCE or 'integrationSequence' not in GUIDANCE:
        return []
    return GUIDANCE['integrationSequence']['steps']


def quotation_behaviour(key, sub=None):
    if not GUIDANCE or 'quotationCustomerBehaviour' not in GUIDANCE:
        return ''
    q = GUIDANCE['quotationCustomerBehaviour']
    v = q.get(key, '')
    return v.get(sub, '') if (sub and isinstance(v, dict)) else v


def customer_paths_block(heading_level=2):
    """The three customer paths as headed sections."""
    if not GUIDANCE:
        return ''
    out = []
    for p in GUIDANCE['customerPaths']:
        out.append('%s %s' % ('#' * (heading_level + 1), p['label']))
        out.append('')
        out.append('%s %s' % (p['summary'], p['action']))
        out.append('')
    return '\n'.join(out)


def customer_paths_cards():
    """The three customer paths as a card row."""
    if not GUIDANCE:
        return ''
    out = ['<div className="rhub-cards rhub-cards--three">', '']
    for p in GUIDANCE['customerPaths']:
        out += ['<div className="rhub-card">',
                '<span className="rhub-card__kicker">%s</span>' % p['label'], '',
                '%s %s' % (p['summary'], p['action']), '',
                '</div>', '']
    out += ['</div>', '']
    return '\n'.join(out)


def document_model_cards():
    """KYC/KYB versus invoice, side by side."""
    if not GUIDANCE:
        return ''
    out = ['<div className="rhub-cards rhub-cards--two">', '']
    for d in GUIDANCE['documentModel']:
        out += ['<div className="rhub-card rhub-card--doc">',
                '<span className="rhub-card__kicker">%s</span>' % d['type'], '',
                '**Purpose** — %s' % d['purpose'], '',
                '**Applies to** — %s' % d['appliesTo'], '',
                '**Requirement** — %s' % d['requirement'], '',
                '**Payout reference** — `%s`' % d['payoutReference'], '',
                '</div>', '']
    out += ['</div>', '']
    return '\n'.join(out)


def document_model_table():
    if not GUIDANCE:
        return ''
    rows = ['| Document type | Purpose | Applies to | Requirement | Payout reference |',
            '|---|---|---|---|---|']
    for d in GUIDANCE['documentModel']:
        rows.append('| %s | %s | %s | %s | `%s` |'
                    % (d['type'], d['purpose'], d['appliesTo'], d['requirement'],
                       d['payoutReference']))
    return '\n'.join(rows)


def transaction_matrix_table():
    if not GUIDANCE:
        return ''
    rows = ['| Transaction type | Sender | Receiver | KYC/KYB | Invoice |', '|---|---|---|---|---|']
    for m in GUIDANCE['transactionMatrix']:
        rows.append('| %s | %s | %s | %s | %s |'
                    % (m['type'], m['sender'], m['receiver'], m['kyc'], m['invoice']))
    return '\n'.join(rows)


def payout_prerequisites_list():
    if not GUIDANCE:
        return ''
    return '\n'.join('%d. %s' % (i, step)
                     for i, step in enumerate(GUIDANCE['payoutPrerequisites'], 1))


def open_question(qid):
    if not GUIDANCE:
        return ''
    for q in GUIDANCE['openQuestions']:
        if q['id'] == qid:
            return q['question']
    return ''
FILES = {f['file']: f['content'] for f in EXPORT['files']}
SOURCE_URL = EXPORT['source']
EXPORTED_AT = EXPORT['exportedAt']

# files linked from the live (published) sidebar
PUBLISHED = ['README.md', 'apisequence.md', 'AUTH.md', 'QUOTA.md', 'DocumentUpload.md',
             'PAYOUT-Api.md', 'PAYOUT-WPT.md', 'ENQUIRY.md', 'master.md', 'CUSTOMEREGIS.md',
             'responseCodes.md', 'CURRENCYVALIDATIONS.md', 'COUNTRYVALIDATIONS.md', 'footer.md']

# Recovery / audit material.
#
# These pages are deliberately kept out of the public developer navigation while
# remaining in the repository for auditability and future RHUB review. The pipeline
# writes them with `unlisted: true`, which keeps them out of the sidebar, the site
# search index and the sitemap, but still builds them and leaves them reachable by
# direct URL. Their content is generated exactly as before — nothing is removed.
#
# This list is the persistent mechanism: regenerating the docs re-applies it, so the
# pages can never drift back into public navigation. sidebars.js also omits the
# matching categories.
HIDDEN_FROM_PUBLIC_NAV = {
    'legacy/index.md',
    'legacy/login-authentication.md',
    'legacy/customer-registration.md',
    'legacy/customer-inquiry.md',
    'legacy/update-customer-details.md',
    'legacy/owner-details.md',
    'legacy/quotation.md',
    'legacy/final-quotation.md',
    'legacy/payout.md',
    'legacy/transaction-inquiry.md',
    'legacy/balance.md',
    'legacy/reference-payout-validator.md',
    'wpt/index.md',
    'wpt/customer-registration.md',
    'wpt/quotation.md',
    'wpt/payout.md',
    'template-management/index.md',
    'template-management/service-fee.md',
    'template-management/update-service-fee.md',
    'template-management/transaction-list.md',
    'template-management/update-transaction-limit.md',
    'template-management/forex-margin.md',
    'template-management/update-forex-margin.md',
    'errors/error-codes.md',
    'appendix/review-resolution-register.md',
    'appendix/source-notes.md',
    'appendix/unpublished-master-apis.md',
    'appendix/unpublished-apis.md',
}

MANIFEST = []      # (source file, portal path, status, notes)
PAGES = []         # portal doc paths written
API_INDEX = []     # (name, method, endpoint, page)


def rec(src, portal_path, status, notes):
    MANIFEST.append((src, portal_path, status, notes))


def write(relpath, front, body):
    path = os.path.join(DOCS, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if relpath in HIDDEN_FROM_PUBLIC_NAV:
        front = dict(front)
        front['unlisted'] = True
    else:
        body = sanitise_examples(body)
    fm = ['---']
    for k, v in front.items():
        if v is None:
            continue
        if isinstance(v, bool):
            fm.append('%s: %s' % (k, 'true' if v else 'false'))
        elif isinstance(v, int):
            fm.append('%s: %d' % (k, v))
        else:
            fm.append('%s: "%s"' % (k, str(v).replace('"', '\\"')))
    fm.append('---')
    text = '\n'.join(fm) + '\n\n' + collapse_blank_lines(body).strip() + '\n'
    open(path, 'w').write(text)
    PAGES.append(relpath)
    return relpath


def collapse_blank_lines(text):
    """Collapse runs of 3+ blank lines outside fenced code blocks.

    Needed because disabling the provenance line leaves an empty slot in the
    page templates. Content inside code fences is never touched.
    """
    out = []
    in_code = False
    blanks = 0
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            in_code = not in_code
            blanks = 0
            out.append(line)
            continue
        if not in_code and not line.strip():
            blanks += 1
            if blanks > 1:
                continue
        else:
            blanks = 0
        out.append(line)
    return '\n'.join(out)


def provenance(files):
    """Per-page source-of-truth metadata line — intentionally disabled.

    This helper used to inject a line of the form
    "Source of truth: <file> — from the RHUB documentation export of <date> (<url>)"
    at the top of every generated page. That was build metadata rather than RHUB
    documentation, so it is no longer emitted on the public pages.

    The helper is retained (returning an empty string) so that all call sites stay
    intact and no page structure changes. Source-file provenance is still recorded,
    in full, in docs/appendix/source-notes.md, and the source export itself remains
    in source/ — nothing about the audit trail is lost.

    Note: this is not the same as the source references that belong to the RHUB
    documentation itself (for example the publication-status warnings that name a
    source file, or the source-to-page map in the appendix). Those are unaffected.
    """
    return ''


UNPUBLISHED_WARNING = """:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `%s`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::"""


# --------------------------------------------------------------------------
# section splitting
# --------------------------------------------------------------------------

API_HEAD = re.compile(r'^[ \t]*##\s*<span class="background(\w+?)Btn"[^>]*>\s*(\w+)\s*</span>\s*(.*)$',
                      re.M)


def split_api_sections(src_text):
    """-> list of dicts(method, title, body) for ACTIVE (non-commented) ## API sections."""
    text = R.strip_comments(src_text)
    marks = list(API_HEAD.finditer(text))
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        title = re.sub(r'<[^>]+>', '', m.group(3)).replace('*', '').strip()
        out.append({'method': m.group(2).upper(), 'title': title,
                    'body': text[m.end():end], 'preamble': text[:marks[0].start()]})
    return out


def commented_api_sections(src_text):
    """-> list of dicts(method, title, body) for API sections inside HTML comments."""
    out = []
    for block in R.comment_bodies(src_text):
        m = API_HEAD.search(block) or re.search(
            r'##\s*<span class="background(\w+?)Btn"[^>]*>\s*(\w+)\s*</span>\s*(.*)', block)
        if not m:
            continue
        title = re.sub(r'<[^>]+>', '', m.group(3)).replace('*', '').strip()
        out.append({'method': m.group(2).upper(), 'title': title, 'body': block[m.end():]})
    return out


MATRIX_STATS = {'tables': 0, 'entries': 0, 'groups': 0, 'values': 0, 'void_columns': 0}

def matrix_to_details(md, entity):
    """Re-present a wide validation matrix as one expandable entry per row.

    Presentation only. Every source cell is carried across: the identifier and
    rail become the summary, and each remaining column becomes a Field /
    Requirement row inside the expanded panel, using the source header as the
    field name and the source cell as the requirement, both verbatim.

    Columns whose header is empty *and* whose every cell is empty carry no
    information; they are dropped and counted in MATRIX_STATS so the drop is
    reported rather than silent. A column with a header is always kept, and a
    blank cell inside a kept column is rendered as an em dash so the blank is
    still visible.
    """
    lines = md.split('\n')
    out, i = [], 0
    while i < len(lines):
        if not lines[i].strip().startswith('|'):
            out.append(lines[i])
            i += 1
            continue
        block = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            block.append(lines[i])
            i += 1
        cells = lambda r: [c.strip() for c in r.strip().strip('|').split('|')]
        header = cells(block[0])
        rows = [cells(r) for r in block[2:]]
        if len(header) < 3 or header[0] != entity:
            out.extend(block)          # not a matrix; leave untouched
            continue
        keep = [c for c in range(len(header))
                if c < 2 or header[c] or any(c < len(r) and r[c] for r in rows)]
        MATRIX_STATS['void_columns'] += len(header) - len(keep)
        MATRIX_STATS['tables'] += 1
        out.append('<div className="rhub-reqs">')
        out.append('')
        for r in rows:
            r = r + [''] * (len(header) - len(r))
            filled = [c for c in r if c]
            if len(filled) == 1 and r[0]:
                MATRIX_STATS['groups'] += 1
                out += ['<p className="rhub-reqs__group">%s</p>' % r[0], '']
                continue
            MATRIX_STATS['entries'] += 1
            out += ['<details className="rhub-req">',
                    '<summary>'
                    '<span className="rhub-req__code">%s</span>'
                    '<span className="rhub-req__rail">%s</span>'
                    '<span className="rhub-req__cta">View requirements</span>'
                    '</summary>' % (r[0], r[1]),
                    '',
                    '| Field | Requirement |',
                    '|---|---|']
            for c in keep[2:]:
                value = r[c] if r[c] else '—'
                MATRIX_STATS['values'] += 1
                out.append('| %s | %s |' % (header[c], value))
            out += ['', '</details>', '']
        out += ['</div>', '']
    return '\n'.join(out)


def wrap_tables(md, cls):
    """Wrap every Markdown table in a scroll container with the given class."""
    lines = md.split('\n')
    out, i, in_code = [], 0, False
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            in_code = not in_code
        if not in_code and line.strip().startswith('|'):
            block = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                block.append(lines[i])
                i += 1
            out += ['<div className="%s">' % cls, ''] + block + ['', '</div>', '']
            continue
        out.append(line)
        i += 1
    return '\n'.join(out)


def slugify(name):
    s = name.lower()
    s = s.replace('/', '-').replace('&', 'and')
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def purpose_of(body):
    """The API's own 'About the API' sentence, as written by RHUB.

    It is the first prose paragraph after the endpoint block. Trimmed to one sentence for
    the index; never reworded.
    """
    tail = body.split('</div>', 1)[-1]
    for para in tail.split('\n\n'):
        para = para.strip()
        if not para or para.startswith(('#', '|', '`', ':::', '<', '*', '-')):
            continue
        sentence = re.split(r'(?<=[.!])\s', para)[0].strip()
        sentence = re.sub(r'\s+', ' ', sentence)
        return sentence
    return 'REVIEW REQUIRED'


def endpoint_of(body):
    """First endpoint URL found in a converted body (for the API index only).

    Matches the endpoint block emitted by rhubconv.render_endpoint first, then falls
    back to a plain backticked URL. The value itself is never rewritten.
    """
    m = re.search(r'rhub-endpoint__url">\{\'([^\']+)\'\}', body)
    if m:
        return m.group(1)
    m = re.search(r'`(https?://[^`]+)`', body)
    return m.group(1) if m else 'REVIEW REQUIRED'


def api_page(relpath, front, method, title, converted, source_file, extra_top='',
             related=None, register=True):
    parts = []
    parts.append('# %s' % title)
    parts.append('')
    parts.append('<span className="rhub-method rhub-method--%s">%s</span>' %
                 (method.lower(), method))
    parts.append('')
    parts.append(provenance(source_file))
    parts.append('')
    if extra_top:
        parts.append(extra_top)
        parts.append('')
    parts.append(converted)
    if related:
        parts.append('')
        parts.append('## Related APIs')
        parts.append('')
        for label, target in related:
            parts.append('- [%s](%s)' % (label, target))
    body = '\n'.join(parts)
    write(relpath, front, body)
    if register:
        API_INDEX.append((title, method, endpoint_of(converted), relpath,
                          purpose_of(converted)))
    return relpath


# --------------------------------------------------------------------------
# 1. intro (README.md)
# --------------------------------------------------------------------------

def build_intro():
    body = """# RHUB API Documentation

Reference documentation for the RHUB (RemittancesHub) payout APIs: contracts, field tables,
examples, validation rules and error codes. New to RHUB? Start with the
[integration flow](/docs/getting-started/integration-flow), which sets out where each API
fits and where the decisions are.

<div className="rhub-cards rhub-cards--two">

<div className="rhub-card">
<span className="rhub-card__kicker">Getting started</span>

- [Integration flow](/docs/getting-started/integration-flow)
- [Transaction flows](/docs/getting-started/transaction-flows)
- [How to read this reference](/docs/getting-started/conventions)
- [Authentication](/docs/authentication/authentication)

</div>

<div className="rhub-card">
<span className="rhub-card__kicker">API reference</span>

- [API index](/docs/api-index)
- [Quotation](/docs/quotation/quotation)
- [Payout](/docs/payout/payout) · [WPT Payout](/docs/payout/wpt-payout)
- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
- [Balance Enquiry](/docs/balance/balance-enquiry)
- [Customer Registration](/docs/customers/customer-registration)
- [Document Upload](/docs/documents/document-upload)

</div>

<div className="rhub-card">
<span className="rhub-card__kicker">Reference and validation</span>

- [Master / reference APIs](/docs/master-apis)
- [Currency validations](/docs/validation/currency-validations)
- [Country validations](/docs/validation/country-validations)

</div>

<div className="rhub-card">
<span className="rhub-card__kicker">Errors and response codes</span>

- [Current API error codes](/docs/errors/current-error-codes)
- [Transaction status codes](/docs/errors/transaction-status-codes)

</div>

</div>
"""
    write('intro.md', {'id': 'intro', 'title': 'RHUB API Documentation',
                       'sidebar_label': 'Documentation home', 'slug': '/',
                       'description': 'Directory of the RHUB API documentation: getting started, API reference, validation and error codes.'},
          body)
    rec('README.md', 'docs/intro.md, src/pages/index.js', 'COMPLETE',
        'About Us and Overview content presented on the portal landing page; /docs is the '
        'documentation directory.')


# --------------------------------------------------------------------------
# 2. getting started
# --------------------------------------------------------------------------

def build_getting_started():
    steps = sequence_steps()
    journey = ['<div className="rhub-journey">', '']
    for st in steps:
        journey += ['<div className="rhub-journey__step">',
                    '<span className="rhub-journey__index">%02d</span>' % st['n'],
                    '<span className="rhub-journey__kind">%s</span>' % st['kind'], '']
        if st['name'] == 'Quotation':
            journey += ['**[Quotation](/docs/quotation/quotation)**', '',
                        st['summary'], '',
                        '<div className="rhub-branches">', '',
                        '<div className="rhub-branch">',
                        '<span className="rhub-branch__label">Registered customer</span>', '',
                        'Send the existing RHUB customer code in `customerCode`.', '',
                        '</div>', '',
                        '<div className="rhub-branch">',
                        '<span className="rhub-branch__label">Unregistered customer</span>', '',
                        'Send `customerCode` as an empty value. Registration happens later.', '',
                        '</div>', '', '</div>', '']
        elif st['name'] == 'Customer registration decision':
            journey += ['**Customer registration decision**', '',
                        'Resolve the customer before payout — not before the quotation.', '',
                        '<div className="rhub-branches">', '',
                        '<div className="rhub-branch">',
                        '<span className="rhub-branch__label">Already registered</span>', '',
                        'Continue with the customer code you hold.', '',
                        '</div>', '',
                        '<div className="rhub-branch">',
                        '<span className="rhub-branch__label">Not registered</span>', '',
                        'Register with the '
                        '[Customer Registration API](/docs/customers/customer-registration), or '
                        'use on-the-fly registration in the '
                        '[Payout](/docs/payout/payout) request.', '',
                        '</div>', '', '</div>', '']
        else:
            links = {
                'Authentication': '/docs/authentication/authentication',
                'Document Upload': '/docs/documents/document-upload',
                'Bank List': '/docs/master-apis/bank-list',
                'Master / reference data': '/docs/master-apis',
                'Payout': '/docs/payout/payout',
                'Transaction Enquiry': '/docs/transactions/transaction-enquiry',
                'Balance': '/docs/balance/balance-enquiry',
            }
            target = links.get(st['name'])
            title = '**[%s](%s)**' % (st['name'], target) if target else '**%s**' % st['name']
            journey += [title, '', st['summary'], '']
        journey += ['</div>', '']
    journey.append('</div>')

    body = """# Integration flow

Authentication, Quotation, Payout and Transaction Enquiry are the constant core of every
integration. What happens between them depends on the customer and the transaction type.

One point is worth stating up front: **a quotation does not require a registered customer**.
You can price a transaction first and resolve registration afterwards.

## The integration sequence

%s

## What is core, what is conditional, what is supporting

| Category | APIs | When |
|---|---|---|
| Core transaction APIs | Authentication, Quotation, Payout, Transaction Enquiry | Every payout |
| Conditional preparation | Document Upload, Customer Registration | Depends on the customer and the transaction type |
| Preparation / reference | Bank List, other master APIs, currency and country validations | As the route and payload require |
| Final / supporting | Balance | The final API in the documented sequence |

## Supporting capabilities

- [Master / reference APIs](/docs/master-apis) — fetch the coded values your transaction type,
  route and payload require. There is no requirement to call them all.
- [Balance Enquiry](/docs/balance/balance-enquiry) — the current wallet or account balance.
- [Currency validations](/docs/validation/currency-validations) and
  [country validations](/docs/validation/country-validations) — which conditional fields a
  given correspondent, currency or country requires.
""" % '\n'.join(journey)
    write('getting-started/integration-flow.md',
          {'title': 'Integration flow', 'sidebar_label': 'Integration flow',
           'description': 'The RHUB integration sequence: authenticate, quote, prepare documents and customer, then pay out.'}, body)
    rec('apisequence.md', 'docs/getting-started/integration-flow.md', 'COMPLETE',
        'Sequence list and all cross-references remapped to portal routes. Source diagram '
        '(img/apiseq.png) is commented out in the source and the asset is not in the export.')

    # The original bank/wallet diagrams are unavailable and are recorded in the internal
    # review resolution register. The prose below stands on its own, so the client-facing
    # pages carry no documentation-production warning.
    R.IMAGE_NOTICE_MODE = 'silent'
    flows = R.convert(FILES['transactionflow.md'])
    R.IMAGE_NOTICE_MODE = 'admonition'
    flows = re.sub(r'^#\s+Transaction Flows\s*$', '', flows, count=1, flags=re.M).strip()
    body = f"""# Transaction flows

RHUB settles a payout to one of two destinations: the beneficiary's bank account, or the
beneficiary's wallet. Which one applies determines the payout API you call —
[Payout](/docs/payout/payout) for bank transfers and
[WPT Payout](/docs/payout/wpt-payout) for wallet transfers — and, for wallet transfers, the
[WPT Wallet List](/docs/master-apis/wpt-wallet-list) master API supplies the wallet values.

{flows}

## Where these flows meet the APIs

Both settlement flows use the same integration sequence — authenticate, quote, prepare
documents and the customer, then pay out and check the transaction. See the
[integration flow](/docs/getting-started/integration-flow) for the decision points.
"""
    write('getting-started/transaction-flows.md',
          {'title': 'Transaction flows', 'sidebar_label': 'Transaction flows',
           'description': 'Bank payout and wallet payout transaction flows as described by RHUB.'},
          body)
    rec('transactionflow.md', 'docs/getting-started/transaction-flows.md', 'REVIEW REQUIRED',
        'Narrative carried over in full. Both flow diagrams (img/rhubbpt2.png, img/rhubwpt2.png) '
        'are referenced by the source but the binary assets are not in the export — flagged on page.')

    body = f"""# How to read this reference

This page explains the conventions used throughout the reference. It makes no technical
claims of its own — those live on the API pages.

## Where the content comes from

The portal draws on three authoritative RHUB inputs:

- the original RHUB documentation source, which supplies the API contracts;
- current supplemental RHUB data, such as the
  [current API error codes](/docs/errors/current-error-codes);
- operational and integration guidance confirmed directly by the RHUB team, which explains
  how the contracts are used together — for example the customer-registration paths and the
  KYC/KYB and invoice document model.

The governing principle is unchanged: **no undocumented technical behaviour is invented**.
Guidance explains how documented contracts fit together; it never adds fields, endpoints,
values or rules that RHUB has not established.

## Requirement flags

Every request field carries a requirement flag, reproduced exactly as RHUB states it. A
Conditional field is never presented as Mandatory.

| Flag | Meaning |
|---|---|
| M | Mandatory |
| O | Optional |
| C | Conditional |

Where the condition is explained — typically correspondent-specific or country-specific —
it appears with the field table or under
[Validation](/docs/validation/currency-validations).

## Field tables

Field tables reproduce the source columns, which are either
`Parameters | Input Type | Length | Requirement | Description` or, on older contracts,
`Parameters | Data Type | Requirement | Description`. Where a field length is not stated,
the column is absent rather than guessed.

Field names, endpoint strings and example values are reproduced literally, including
spellings that look inconsistent. If a field is written one way in a table and another way
in an example, both are preserved and the difference is noted rather than corrected.

## Environments and base URLs

RHUB has confirmed one environment for Developer Portal 1.0:

| Environment | Base URL |
|---|---|
| Sandbox | `https://sandbox-client.remittanceshub.com:8030` |

No UAT or production base URL is published here. Ask RHUB for the base URL of any other
environment you are given access to.

## Method and endpoint blocks

Each API page shows its HTTP method and the request path exactly as the contract writes it.
Most paths are written as `http://host/ewallet/api/v1/...`, where **`host` stands for the
base URL of your environment**. Against Sandbox, for example,
`http://host/ewallet/oauth/token` is
`https://sandbox-client.remittanceshub.com:8030/ewallet/oauth/token`. The paths themselves are
reproduced unchanged.

## Authorising requests

[Authentication](/docs/authentication/authentication) returns an `access_token`. Every
subsequent call carries it in the `Authorization` header:

```http
Authorization: Bearer <access_token>
```

## Examples

Request and response examples are RHUB's own samples, reproduced verbatim in copyable code
blocks. Masked values in the originals (for example `15*****f-54fe-43d9-***7-b7dc****1b9`)
stay masked. Where a contract has no example, the page says so rather than showing an
invented one.

## Notes, limitations and conditional rules

Where a requirement depends on the transaction, the page states the condition rather than
generalising it — for example `sendClientTrxReference` is required for B2B, B2C and C2B but
not for C2C. Where RHUB's current behaviour differs from what an older contract table shows,
the page says which one your integration should follow.

Requirement flags, field names, endpoint paths, examples and error text are reproduced from
RHUB's material rather than tidied, so a table and an example occasionally spell the same
thing differently. Where that matters for integration, the page says so.

The following are not documented by RHUB and are therefore absent rather than inferred:
rate limits, idempotency behaviour, retry semantics, webhooks, SDKs, pagination rules, token
refresh behaviour, and SLA commitments.
"""
    write('getting-started/conventions.md',
          {'title': 'How to read this reference', 'sidebar_label': 'How to read this reference',
           'description': 'How to read the RHUB API reference: environments, authorisation, requirement flags, field tables and examples.'},
          body)


# --------------------------------------------------------------------------
# 3. single-API published pages
# --------------------------------------------------------------------------

def build_authentication():
    secs = split_api_sections(FILES['AUTH.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    # Public example correction (RHUB decision D3): `scope` is a response field, so the
    # client-facing request example no longer sends it. The original example is preserved in
    # source/RHUB_FULL_SOURCE_EXPORT.json and recorded in the review resolution register.
    conv = conv.replace('grant_type=password&scope=read%20write&username=',
                        'grant_type=password&username=')
    extra = """Authenticate and obtain the access token that every other RHUB API call requires.

:::info[Using the access token]

Send the token on subsequent API calls in the `Authorization` header:

```http
Authorization: Bearer <access_token>
```

The response also returns `token_type`, `expires_in` and `scope`.

:::

:::note[`scope` is a response field]

Send `grant_type`, `username` and `password` on the token request. `scope` is returned in the
response and does not need to be sent.

:::

## Contract"""
    api_page('authentication/authentication.md',
             {'title': 'Authentication', 'sidebar_label': 'Authentication',
              'slug': '/authentication/authentication',
              'description': 'RHUB Login (Authentication) API — obtain an access token.'},
             s['method'], 'Authentication', conv, 'AUTH.md', extra_top=extra,
             related=[('Quotation', '/docs/quotation/quotation'),
                      ('Payout', '/docs/payout/payout'),
                      ('Integration flow', '/docs/getting-started/integration-flow')])
    rec('AUTH.md', 'docs/authentication/authentication.md', 'COMPLETE',
        'Published Authentication contract carried over in full (request, header and response '
        'parameters, request and response examples).')


def build_quotation():
    secs = split_api_sections(FILES['QUOTA.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    extra = """Price a transaction before you initiate it.

Call Quotation immediately after authenticating. It returns the forex rate between the payin
and payout currencies together with the applicable charges, so the sender can see the rate,
fees and resulting payout amount before the transaction is confirmed. RHUB describes this as
an indicative price and transaction limit, not a guaranteed final price.

`payinAmount` and `payoutAmount` are conditional alternatives: supply one or the other, as
the field table below states. The quotation data returned here is then used by the
[Payout request](/docs/payout/payout).

## Customer registration and quotation

**You can request a quotation before the customer is registered.** Registration is resolved
later, between the quotation and the payout.

- **Existing customer** — send the RHUB `customerCode` you already hold.
- **New or unregistered customer** — send `customerCode` as an empty value.

`customerCode` is Optional in the contract below; that flag is unchanged.

Unregistered customer:

```json
{
  "payinAmount": "",
  "payoutAmount": "200",
  "sendCurrencyCode": "USD-USA",
  "customerCode": "",
  "destinationCountryCode": "IND",
  "receiveCurrencyCode": "USD-GLOBAL",
  "settlementCurrencyCode": "USD-USA",
  "paymentMode": "Cash",
  "sourceCountry": "MWI",
  "senderCode": "1000008960",
  "serviceTypeCode": "C2C"
}
```

Already registered customer:

```json
{
  "payinAmount": "",
  "payoutAmount": "200",
  "sendCurrencyCode": "USD-USA",
  "customerCode": "1000008989",
  "destinationCountryCode": "IND",
  "receiveCurrencyCode": "USD-GLOBAL",
  "settlementCurrencyCode": "USD-USA",
  "paymentMode": "Cash",
  "sourceCountry": "MWI",
  "senderCode": "1000008960",
  "serviceTypeCode": "C2C"
}
```

After the quotation, register a new customer either through the
[Customer Registration API](/docs/customers/customer-registration) or on the fly during
[Payout](/docs/payout/payout).

## Contract"""
    api_page('quotation/quotation.md',
             {'title': 'Quotation', 'sidebar_label': 'Quotation',
              'slug': '/quotation/quotation',
              'description': 'RHUB Quotation API — fetch the forex rate between payin and payout currencies.'},
             s['method'], 'Quotation', conv, 'QUOTA.md', extra_top=extra,
             related=[('Integration flow', '/docs/getting-started/integration-flow'),
                      ('Authentication', '/docs/authentication/authentication'),
                      ('Payout', '/docs/payout/payout'),
                      ('WPT Payout', '/docs/payout/wpt-payout')])
    rec('QUOTA.md', 'docs/quotation/quotation.md', 'COMPLETE',
        'Published Quotation contract carried over in full. The file also contains a '
        'commented-out Final Quotation section — reproduced in the appendix and cross-checked '
        'against the standalone finalQuotation.md source page.')


def build_document_upload():
    secs = split_api_sections(FILES['DocumentUpload.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    extra = """Upload the documents a payout depends on and obtain the reference the Payout request
carries. Document upload follows the [quotation](/docs/quotation/quotation) and precedes the
[payout](/docs/payout/payout).

## Two document purposes

RHUB payouts involve two distinct kinds of document. They are often confused, so it is worth
being explicit about which is which.

%s
**KYC / KYB** is customer verification: KYC for individual customers, KYB for business
customers. It is required for payout on every transaction type, and the resulting reference
is passed to Payout in `docReferenceNumber`.

**Invoice** documentation supports business-related transactions. It is required for B2B,
B2C and C2B payout processing, and the invoice/transaction reference is represented in the
Payout request by `sendClientTrxReference`. It does not apply as an invoice requirement to
C2C.

The source establishes a single document upload contract, reproduced below; it does not
define a separate invoice endpoint or separate invoice-specific request fields. Where your
implementation needs that distinction at endpoint level, confirm it with RHUB.

## Contract""" % document_model_cards()
    api_page('documents/document-upload.md',
             {'title': 'Document Upload', 'sidebar_label': 'Document Upload',
              'description': 'RHUB Document Upload API — KYC/KYB and invoice documentation for payout.'},
             s['method'], 'Document Upload', conv, 'DocumentUpload.md', extra_top=extra,
             related=[('Integration flow', '/docs/getting-started/integration-flow'),
                      ('Customer Registration', '/docs/customers/customer-registration'),
                      ('Payout', '/docs/payout/payout'),
                      ('Customer/Individual Document Type (master)',
                       '/docs/master-apis/customer-individual-document-type')])
    rec('DocumentUpload.md', 'docs/documents/document-upload.md', 'COMPLETE',
        'Published Document Upload contract carried over in full.')


def build_customer_registration():
    secs = split_api_sections(FILES['CUSTOMEREGIS.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    extra = """Register an individual or business customer with RHUB and obtain the customer code used
on subsequent transactions.

## When to use this API

Customer Registration is not a mandatory call before every payout, and it is **not** a
prerequisite for a quotation — you can price a transaction first with a blank `customerCode`
and resolve registration afterwards. Which path applies depends on whether RHUB already knows
the customer.

%s
Coded fields in the request draw their values from the master APIs — for example
[Business Type](/docs/master-apis/business-type),
[Business Registration Type](/docs/master-apis/business-registration-type),
[Nature of Business](/docs/master-apis/nature-of-business),
[Customer Legal Status](/docs/master-apis/customer-legal-status),
[Occupation](/docs/master-apis/occupation) and
[Document ID Type](/docs/master-apis/document-id-type).

## Contract""" % customer_paths_cards()
    api_page('customers/customer-registration.md',

             {'title': 'Customer Registration', 'sidebar_label': 'Customer Registration',
              'description': 'RHUB Customer Registration API — register business and individual customers.'},
             s['method'], 'Customer Registration', conv, 'CUSTOMEREGIS.md', extra_top=extra,
             related=[('Integration flow', '/docs/getting-started/integration-flow'),
                      ('Document Upload', '/docs/documents/document-upload'),
                      ('Payout', '/docs/payout/payout'),
                      ('Master / reference APIs', '/docs/master-apis')])
    rec('CUSTOMEREGIS.md', 'docs/customers/customer-registration.md', 'COMPLETE',
        'Published Customer Registration contract carried over in full for both business and '
        'individual customers.')


def build_payout():
    secs = split_api_sections(FILES['PAYOUT-Api.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    extra = """Initiate a fund transfer for a completed quotation.

## Before you initiate a payout

<div className="rhub-checklist">

%s

</div>

You do not need to call every master API for every payout — fetch only the reference data
your route and use case require.

### Transaction types and documentation

%s

### Document references in the request

- `docReferenceNumber` — the KYC/KYB document reference.
- `sendClientTrxReference` — the invoice reference for B2B, B2C and C2B.

:::info[Conditional requirement — `sendClientTrxReference`]

**Required for B2B, B2C and C2B**, where invoice documentation is mandatory.

**Not required for C2C** — omit the parameter, or send it blank.

In the `transactionInfo` field table below the field is marked `M` and its name is split
across two lines, both exactly as the original contract has them. The conditional rule above
is RHUB's current guidance and is what your integration should follow.

:::

:::note[Field name in validation messages]

The Payout request field is `sendClientTrxReference`. Some current validation messages refer
to it as `sendClientTxnReference`; the
[error code reference](/docs/errors/current-error-codes) reproduces those messages as the API
returns them today.

:::

## Contract""" % (payout_prerequisites_list(), transaction_matrix_table())
    doc_note = (':::note[Two different references]\n\n'
                '`docReferenceNumber` carries the uploaded **KYC/KYB document** reference for '
                'the payout. `sendClientTrxReference` carries the **invoice** reference for '
                'business transactions (B2B, B2C, C2B); for C2C it is not required and may be '
                'omitted or sent blank. They are not interchangeable.\n\n:::\n\n')
    conv = conv.replace('## transactionInfo Req Param',
                        doc_note + '## transactionInfo Req Param', 1)
    api_page('payout/payout.md',
             {'title': 'Payout', 'sidebar_label': 'Payout',
              'slug': '/payout/payout',
              'description': 'RHUB Payout API — perform B2B, C2C, C2B and B2C transactions.'},
             s['method'], 'Payout', conv, 'PAYOUT-Api.md', extra_top=extra,
             related=[('Integration flow', '/docs/getting-started/integration-flow'),
                      ('Quotation', '/docs/quotation/quotation'),
                      ('Document Upload', '/docs/documents/document-upload'),
                      ('Currency validations (LOCAL rail)', '/docs/validation/currency-validations'),
                      ('Country validations (SWIFT rail)', '/docs/validation/country-validations'),
                      ('Transaction Enquiry', '/docs/transactions/transaction-enquiry'),
                      ('WPT Payout', '/docs/payout/wpt-payout')])
    rec('PAYOUT-Api.md', 'docs/payout/payout.md', 'COMPLETE',
        'Published Payout contract carried over in full: transactionInfo, sender, receiver and '
        'compliance request objects, registered-customer variant, response parameters and examples.')

    secs = split_api_sections(FILES['PAYOUT-WPT.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    api_page('payout/wpt-payout.md',
             {'title': 'WPT Payout', 'sidebar_label': 'WPT Payout',
              'description': 'RHUB WPT Payout API — wallet payout transactions.'},
             s['method'], 'WPT Payout', conv, 'PAYOUT-WPT.md',
             related=[('Payout', '/docs/payout/payout'),
                      ('WPT Wallet List (master)', '/docs/master-apis/wpt-wallet-list'),
                      ('Quotation', '/docs/quotation/quotation'),
                      ('Integration flow', '/docs/getting-started/integration-flow')])
    rec('PAYOUT-WPT.md', 'docs/payout/wpt-payout.md', 'COMPLETE',
        'Published WPT Payout contract carried over in full.')


def build_enquiry():
    secs = split_api_sections(FILES['ENQUIRY.md'])
    by_title = {s['title'].replace('*', '').strip(): s for s in secs}
    preamble = secs[0]['preamble'] if secs else ''

    tx = by_title['Transaction Enquiry']
    conv = R.convert(tx['body'], promote_headings=1)
    api_page('transactions/transaction-enquiry.md',
             {'title': 'Transaction Enquiry', 'sidebar_label': 'Transaction Enquiry',
              'description': 'RHUB Transaction Enquiry API — check the status of a previously initiated payout.'},
             tx['method'], 'Transaction Enquiry', conv, 'ENQUIRY.md',
             extra_top='Check the state of a transaction after the '
                       '[payout](/docs/payout/payout) has been submitted.\n\n## Contract',
             related=[('Payout', '/docs/payout/payout'),
                      ('Transaction status codes', '/docs/errors/transaction-status-codes'),
                      ('Balance Enquiry', '/docs/balance/balance-enquiry'),
                      ('Integration flow', '/docs/getting-started/integration-flow')])

    bal = by_title['Balance Enquiry']
    conv = R.convert(bal['body'], promote_headings=1)
    api_page('balance/balance-enquiry.md',
             {'title': 'Balance Enquiry', 'sidebar_label': 'Balance Enquiry',
              'description': 'RHUB Balance Enquiry API — retrieve the current wallet or account balance.'},
             bal['method'], 'Balance Enquiry', conv, 'ENQUIRY.md',
             extra_top='Retrieve the current balance. Balance is the final API in the '
                       '[documented integration sequence](/docs/getting-started/integration-flow); '
                       'call it when you need the current balance rather than after every '
                       'transaction.\n\n## Contract',
             related=[('Transaction Enquiry', '/docs/transactions/transaction-enquiry'),
                      ('Integration flow', '/docs/getting-started/integration-flow')])

    note = ''
    pre = R.convert(preamble)
    pre = re.sub(r'^#{1,3}.*$', '', pre, flags=re.M).strip()
    rec('ENQUIRY.md',
        'docs/transactions/transaction-enquiry.md, docs/balance/balance-enquiry.md',
        'COMPLETE',
        'Both published sections (Transaction Enquiry, Balance Enquiry) carried over in full. '
        'The file also contains a commented-out Customer Enquiry section, reproduced in the appendix.')
    return pre


# --------------------------------------------------------------------------
# 4. master APIs
# --------------------------------------------------------------------------

MASTER_ORDER = []


def build_master():
    secs = split_api_sections(FILES['master.md'])
    rows = []
    for s in secs:
        title = s['title']
        slug = R.MASTER_SLUGS.get('get-' + slugify(title).replace('-', ''), None)
        slug = slugify(title)
        if title == 'Customer/Individual Document Type':
            slug = 'customer-individual-document-type'
        conv = R.convert(s['body'], promote_headings=1)
        ep = endpoint_of(conv)
        MASTER_ORDER.append(slug)
        api_page('master-apis/%s.md' % slug,
                 {'title': title, 'sidebar_label': title,
                  'description': 'RHUB %s master API.' % title},
                 s['method'], title, conv, 'master.md',
                 related=[('All master APIs', '/docs/master-apis'),
                          ('Payout', '/docs/payout/payout'),
                          ('Customer Registration', '/docs/customers/customer-registration')])
        rows.append((title, s['method'], ep, slug))

    lines = ['# Master / reference APIs', '',
             provenance('master.md'), '',
             'Master APIs supply the coded values the transactional APIs expect — remittance '
             'purpose, source of funds, relationship, occupation, bank lists and more. Fetch '
             'the master and reference values required by the selected transaction type, route '
             'and payout payload; there is no requirement to call them all. In the '
             '[integration sequence](/docs/getting-started/integration-flow) they sit between '
             'the customer-registration decision and the payout request, alongside the '
             '[Bank List](/docs/master-apis/bank-list), which supplies the beneficiary bank '
             'information a payout route requires.', '',
             '## Published master APIs', '',
             'These %d master APIs are documented and published in the RHUB source.' % len(rows), '',
             '| Master API | Method | Endpoint | Reference |', '|---|---|---|---|']
    for title, method, ep, slug in rows:
        lines.append('| %s | `%s` | `%s` | [Open](/docs/master-apis/%s) |' %
                     (title, method, ep.replace('|', '\\|'), slug))
    lines += ['',
              ':::note[Master APIs RHUB does not publish]',
              '',
              'RHUB defines ten further master categories that it does not publish: '
              'Legal Status Code, Payment Mode, Branch List, Customer Type, Resident Status, '
              'Purpose of Opening Business, Transaction Volume, ID Type, Customer Document Fetch '
              'and Payout Validator. They are not documented here — confirm with RHUB before '
              'relying on any of them.',
              '',
              ':::']
    write('master-apis/index.md',
          {'id': 'master-index', 'title': 'Master / reference APIs',
           'sidebar_label': 'Overview', 'slug': '/master-apis',
           'description': 'Inventory of the RHUB master / reference APIs.'},
          '\n'.join(lines))

    # appendix: commented master sections
    blocks = commented_api_sections(FILES['master.md'])
    ap = ['# Unpublished master APIs', '', provenance('master.md'), '',
          ':::warning[REVIEW REQUIRED — not published by the source]', '',
          'Each section below is present in `master.md` **inside an HTML comment**, which means '
          'it is not rendered by the live RHUB documentation. The contracts are reproduced here '
          'verbatim so that no source content is lost, but the source does not establish whether '
          'they are current, forthcoming or withdrawn. Confirm with RHUB before using them.', '',
          ':::', '']
    for b in blocks:
        conv = R.convert(b['body'], promote_headings=0)
        conv = re.sub(r'^(#{2,6})', r'#\1', conv, flags=re.M)
        ap += ['## %s' % b['title'], '',
               '`%s` — status: **REVIEW REQUIRED (commented out in source)**' % b['method'], '',
               conv, '']
    write('appendix/unpublished-master-apis.md',
          {'title': 'Unpublished master APIs', 'sidebar_label': 'Unpublished master APIs',
           'description': 'Master API sections that are commented out in the RHUB source.'},
          '\n'.join(ap))

    rec('master.md', 'docs/master-apis/ (index + %d API pages), docs/appendix/unpublished-master-apis.md'
        % len(rows), 'COMPLETE',
        '%d published master APIs documented individually with full request/response contracts '
        'and examples; %d commented-out master sections reproduced in the appendix and flagged '
        'REVIEW REQUIRED.' % (len(rows), len(blocks)))
    return rows


# --------------------------------------------------------------------------
# 5. validation
# --------------------------------------------------------------------------

def build_validation():
    cur = matrix_to_details(R.convert(FILES['CURRENCYVALIDATIONS.md']), 'Currency')
    cur = re.sub(r'^##\s*\*\*Currency Validations\*\*\s*$', '', cur, count=1, flags=re.M)
    body = f"""# Currency validations (LOCAL rail)

{provenance('CURRENCYVALIDATIONS.md')}

:::info[How to use these tables]

These tables state, per currency and rail, which [Payout](/docs/payout/payout) fields the
correspondent requires. They qualify **Conditional** fields only — the source is explicit
that fields marked Mandatory in the Payout API must always be supplied regardless of
correspondent. The source's own wording is reproduced below.

:::

{cur}

## Related

- [Payout](/docs/payout/payout)
- [Country validations (SWIFT rail)](/docs/validation/country-validations)
- [WPT Payout](/docs/payout/wpt-payout)
"""
    write('validation/currency-validations.md',
          {'title': 'Currency validations (LOCAL rail)', 'sidebar_label': 'Currency validations',
           # TOC restored: the page is no longer a wide matrix, and its four section
           # headings (sender/receiver, individual/business) are worth navigating.
           'description': 'Currency- and correspondent-specific conditional field requirements for RHUB payouts.'},
          body)
    rec('CURRENCYVALIDATIONS.md', 'docs/validation/currency-validations.md', 'COMPLETE',
        'All four validation matrices (Sender/Receiver × Individual/Business) and the field '
        'requirement clarification carried over. The source also links a downloadable Excel '
        'file (assets/TABLE_OF_VALIDATIONS.xlsx) that is not part of the export — flagged.')

    ctry = matrix_to_details(R.convert(FILES['COUNTRYVALIDATIONS.md']), 'Country')
    ctry = re.sub(r'^##\s*\*\*Country Validations\*\*\s*$', '', ctry, count=1, flags=re.M)
    body = f"""# Country validations (SWIFT rail)

{provenance('COUNTRYVALIDATIONS.md')}

## How to use this page

Country requirements vary with the destination country and the transaction rail. You do not
need to know the field names in advance: find the destination country below and expand it to
see the requirements that apply when the transaction is processed through the SWIFT network.

As with the currency rules, these qualify **Conditional** fields only — fields marked
Mandatory in the [Payout API](/docs/payout/payout) must always be supplied.

:::info[Note]

RHUB's own wording for these rules is reproduced below, unchanged.

:::

{ctry}

## Related

- [Payout](/docs/payout/payout)
- [Currency validations (LOCAL rail)](/docs/validation/currency-validations)
"""
    write('validation/country-validations.md',
          {'title': 'Country validations (SWIFT rail)', 'sidebar_label': 'Country validations',
           # Matrix reference page. Its TOC held a single "Related" entry, so the column
           # was costing table width for no navigation value.
           'hide_table_of_contents': True,
           'description': 'Country-specific SWIFT field requirements for RHUB payouts.'},
          body)
    rec('COUNTRYVALIDATIONS.md', 'docs/validation/country-validations.md', 'COMPLETE',
        'All eight SWIFT country groups, their country lists, field explanations and matrices '
        'carried over.')


# --------------------------------------------------------------------------
# 6. errors
# --------------------------------------------------------------------------

def build_errors():
    body = """# Errors and response codes

Two things tell you what happened to a request:

| What it tells you | Where |
|---|---|
| Why a request failed — the `resultCode` category and the `resultDescription` reason | [Current API error codes](/docs/errors/current-error-codes) |
| Where a transaction has reached in processing | [Transaction status codes](/docs/errors/transaction-status-codes) |

Handle failures on the `resultCode` / `resultDescription` pair returned in the response body.
Track a transaction's progress with its status value.

:::note[HTTP status and `resultCode` are separate]

The HTTP status describes the transport-level outcome of the call. `resultCode` is RHUB's
application error category and `resultDescription` is the specific reason, both returned in
the response body. Use `resultCode` for coarse classification and `resultDescription` for the
precise condition.

RHUB supplies code values and descriptions only — no remediation or retry guidance — so none
is offered here.

:::
"""
    write('errors/index.md',
          {'id': 'errors-index', 'title': 'Errors and response codes',
           'sidebar_label': 'Overview', 'slug': '/errors',
           'description': 'How RHUB transaction status codes differ from HTTP and application error codes.'},
          body)

    rc = R.convert(FILES['responseCodes.md'])
    rc = re.sub(r'^##\s*Transaction Status Code\s*$', '', rc, count=1, flags=re.M).strip()
    body = f"""# Transaction status codes

{provenance('responseCodes.md')}

{rc}

:::note[Scope of this list]

These are the statuses RHUB makes available in production, with the meanings RHUB gives them.
Transition rules, timing and terminality are not part of Developer Portal 1.0 and are not
documented here.

:::

## Related

- [Current API error codes](/docs/errors/current-error-codes)
- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
"""
    write('errors/transaction-status-codes.md',
          {'title': 'Transaction status codes', 'sidebar_label': 'Transaction status codes',
           'description': 'RHUB transaction statuses available in production.'}, body)
    rec('responseCodes.md', 'docs/errors/transaction-status-codes.md', 'COMPLETE',
        'The published production status table carried over verbatim. Three commented-out '
        'tables (short status codes, partner status codes, validation codes) reproduced in the '
        'appendix and flagged.')

    ec = R.convert(FILES['ErrorCodes.md'])
    ec = re.sub(r'^##\s*\*\*(HTTP Error Codes|Application Error Codes)\*\*\s*$',
                lambda m: '## ' + m.group(1), ec, flags=re.M)
    body = f"""# Error codes

{provenance('ErrorCodes.md')}

{ec}

## Related

- [Current API error codes](/docs/errors/current-error-codes)
- [Transaction status codes](/docs/errors/transaction-status-codes)
- [Payout](/docs/payout/payout)
"""
    write('errors/error-codes.md',
          {'title': 'Error codes', 'sidebar_label': 'HTTP and application error codes',
           'description': 'RHUB HTTP status codes and application error codes.'}, body)
    rec('ErrorCodes.md', 'docs/errors/error-codes.md', 'PARTIAL',
        'Both source tables (HTTP status codes, application error codes) carried over in full. '
        'Marked PARTIAL because the file is commented out of the live sidebar, so its '
        'publication status is REVIEW REQUIRED, and because the source gives no resolution guidance.')



# --------------------------------------------------------------------------
# 6b. current API error codes (supplemental authoritative data)
# --------------------------------------------------------------------------


def existing_code_index():
    """Codes already documented by the documentation export, for conflict checking."""
    app, http, validation = {}, {}, {}
    ec = R.strip_comments(FILES['ErrorCodes.md'])
    section = ec.split('Application Error Codes', 1)
    for m in re.finditer(r'<tr[^>]*>(.*?)</tr>', section[0], re.S | re.I):
        cells = [re.sub(r'<[^>]+>', '', c).strip()
                 for c in re.findall(r'<td[^>]*>(.*?)</td>', m.group(1), re.S | re.I)]
        if len(cells) >= 3 and re.match(r'^\d+$', cells[0]):
            http[cells[0]] = cells[2]
    if len(section) > 1:
        for m in re.finditer(r'<tr[^>]*>(.*?)</tr>', section[1], re.S | re.I):
            cells = [re.sub(r'<[^>]+>', '', c).strip()
                     for c in re.findall(r'<td[^>]*>(.*?)</td>', m.group(1), re.S | re.I)]
            if len(cells) >= 2 and re.match(r'^\d+$', cells[0]):
                app.setdefault(cells[0], set()).add(cells[1])
    for block in R.comment_bodies(FILES['responseCodes.md']):
        for m in re.finditer(r'^\|\s*(\d{4})\s*\|\s*(.+?)\s*\|\s*$', block, re.M):
            validation.setdefault(m.group(1), set()).add(m.group(2).strip())
    return http, app, validation


def build_current_error_codes():
    if not CURRENT_ERRORS:
        return None
    d = CURRENT_ERRORS
    entries = d['entries']
    coded = [e for e in entries if e['resultCode'] is not None]
    uncoded = [e for e in entries if e['resultCode'] is None]
    unique = sorted(set(e['resultCode'] for e in coded), key=lambda c: (len(c), c))
    counts = collections.Counter(e['resultCode'] for e in coded)

    http, app, validation = existing_code_index()
    conflicts = []
    for c in unique:
        news = sorted(set(e['resultDescription'] for e in coded if e['resultCode'] == c))
        if c in http:
            conflicts.append(('%s' % c,
                              'Also appears in the **HTTP status code** table as "%s". Whether the '
                              'HTTP status and the `resultCode` of the same numeral mean the same '
                              'thing is not established.' % http[c]))
        if c in app:
            same = set(app[c]) & set(news)
            if same:
                conflicts.append(('%s' % c,
                                  'Also in the **application error code** table with the same '
                                  'description ("%s"). Consistent — no conflict.'
                                  % sorted(same)[0]))
            else:
                conflicts.append(('%s' % c,
                                  'Also in the **application error code** table, but with a '
                                  'different description: %s. Not reconciled.'
                                  % ', '.join('"%s"' % x for x in sorted(app[c]))))
        if c in validation:
            same = set(validation[c]) & set(news)
            ci = {x.casefold() for x in validation[c]} & {x.casefold() for x in news}
            if same:
                note = 'the same description ("%s")' % sorted(same)[0]
            elif ci:
                note = ('the same description apart from letter case ("%s")'
                        % sorted(validation[c])[0])
            else:
                note = ('a different description: %s'
                        % ', '.join('"%s"' % x for x in sorted(validation[c])))
            conflicts.append(('%s' % c,
                              'Also appears in an RHUB validation code table that RHUB does not '
                              'publish, with %s.' % note))

    sem = d['semantics']
    lines = ['# Current API error codes', '',
             ':::info[Authoritative and current]', '',
             'These are the error codes the RHUB API returns today, supplied by the **%s** on '
             '**%s**. Handle failures on the `resultCode` and `resultDescription` pair below; '
             'use [transaction status codes](/docs/errors/transaction-status-codes) to follow '
             'a transaction through processing.' % (d['provider'], d['receivedOn']), '',
             ':::', '',
             '## %s' % sem['heading'], '']
    for para in sem['paragraphs'][:2]:
        lines += [para, '']
    lines += ['Examples:', '']
    for ex in sem['examples']:
        lines.append('- **%s** — %s.' % (ex['resultCode'], ex['meaning']))
    lines += ['']
    for para in sem['paragraphs'][2:]:
        lines += [para, '']
    lines += [':::caution[Do not key on resultCode alone]', '',
              sem['caution'],
              'Handle `resultCode` coarsely and branch on `resultDescription` for the specific '
              'condition.', '', ':::', '',
              '## Error code reference', '',
              'All %d entries as supplied. Rows that share a `resultCode` are listed separately '
              'and are **not** merged, because one code covers many distinct conditions.'
              % len(entries), '',
              '| S. No. | Result Code | Result Description |', '|---|---|---|']
    for e in entries:
        code = e['resultCode'] if e['resultCode'] is not None else '*Not provided*'
        desc = e['resultDescription'].replace('|', '\\|')
        lines.append('| %d | %s | %s |' % (e['sNo'], code, desc))

    lines += ['', '### Entry %d — no result code supplied' % uncoded[0]['sNo'], '',
              ':::note[No result code for this entry]', '',
              '**Result Code: Not provided**', '',
              '**Result Description:** %s' % uncoded[0]['resultDescription'], '',
              'This is current API behaviour: the entry has no `resultCode`. Handle it on the '
              '`resultDescription`. No code has been inferred or assigned.', '', ':::', '',
              '## Result codes at a glance', '',
              'The %d entries use **%d distinct result codes**, plus one entry with no code.'
              % (len(entries), len(unique)), '',
              '| Result Code | Entries | Conditions covered |', '|---|---|---|']
    for c in unique:
        lines.append('| %s | %d | %s |' % (c, counts[c],
                                           'multiple distinct conditions' if counts[c] > 1
                                           else 'one condition in this list'))
    lines.append('| *Not provided* | 1 | one condition in this list |')

    lines += ['', ':::info[HTTP status codes and result codes are separate]', '',
              'An HTTP status describes the transport-level outcome of a request. A '
              '`resultCode` describes the RHUB application or business error category, and '
              '`resultDescription` carries the specific reason. The same numeral can appear '
              'in both without the two meaning the same thing.', '', ':::', '',
              ':::note[No remediation guidance]', '',
              'RHUB supplies code values and descriptions only, so no remediation steps, retry '
              'policy or backoff behaviour is documented here.', '', ':::', '',
              '## Related', '',
              '- [Errors and response codes overview](/docs/errors)',
              '- [Transaction status codes](/docs/errors/transaction-status-codes)',
              '- [Payout](/docs/payout/payout)',
              '- [Transaction Enquiry](/docs/transactions/transaction-enquiry)']

    write('errors/current-error-codes.md',
          {'title': 'Current API error codes', 'sidebar_label': 'Current API error codes',
           'description': 'Current RHUB API error-handling reference: resultCode classes and '
                          'resultDescription values, supplied by the RHUB team.'},
          '\n'.join(lines))

    rec(os.path.basename(CURRENT_ERRORS_JSON), 'docs/errors/current-error-codes.md', 'COMPLETE',
        'Supplemental authoritative data supplied directly by the RHUB team (not part of the '
        '29-file documentation export). All %d entries published, duplicates preserved as '
        'separate rows, %d distinct result codes, 1 entry published with "Not provided".'
        % (len(entries), len(unique)))
    return {'entries': len(entries), 'unique': len(unique), 'uncoded': len(uncoded),
            'conflicts': conflicts}


# --------------------------------------------------------------------------
# 7. WPT integration set (WPT.md) and template management (template.md)
# --------------------------------------------------------------------------

def build_wpt():
    secs = split_api_sections(FILES['WPT.md'])
    rows = []
    for s in secs:
        slug = slugify(s['title'])
        conv = R.convert(s['body'], promote_headings=1)
        api_page('wpt/%s.md' % slug,
                 {'title': 'WPT — %s' % s['title'], 'sidebar_label': s['title'],
                  'description': 'RHUB WPT %s API.' % s['title']},
                 s['method'], 'WPT — %s' % s['title'], conv, 'WPT.md',
                 extra_top=UNPUBLISHED_WARNING % 'WPT.md',
                 related=[('WPT overview', '/docs/wpt'),
                          ('WPT Payout (published)', '/docs/payout/wpt-payout'),
                          ('WPT Wallet List (master)', '/docs/master-apis/wpt-wallet-list')])
        rows.append((s['title'], s['method'], slug))

    lines = ['# WPT integration set', '', provenance('WPT.md'), '',
             UNPUBLISHED_WARNING % 'WPT.md', '',
             'The source file `WPT.md` groups a wallet-payout (WPT) integration set. The '
             'following sections are active in the file:', '',
             '| API | Method | Reference |', '|---|---|---|']
    for title, method, slug in rows:
        lines.append('| %s | `%s` | [Open](/docs/wpt/%s) |' % (title, method, slug))
    blocks = commented_api_sections(FILES['WPT.md'])
    lines += ['', 'The same source file carries %d further sections that RHUB does not '
                  'publish (%s); they are therefore not documented here.'
              % (len(blocks), ', '.join(b['title'] for b in blocks)), '',
              '## Related', '',
              '- [WPT Payout (published page)](/docs/payout/wpt-payout)',
              '- [WPT Wallet List master API](/docs/master-apis/wpt-wallet-list)']
    write('wpt/index.md',
          {'id': 'wpt-index', 'title': 'WPT integration set', 'sidebar_label': 'Overview',
           'slug': '/wpt', 'description': 'RHUB WPT (wallet payout) integration set.'},
          '\n'.join(lines))
    rec('WPT.md', 'docs/wpt/ (index + %d API pages), docs/appendix/unpublished-apis.md' % len(rows),
        'PARTIAL',
        '%d active sections (%s) documented in full; %d commented-out sections reproduced in the '
        'appendix. Marked PARTIAL because the whole file is commented out of the live sidebar '
        '(publication status REVIEW REQUIRED).'
        % (len(rows), ', '.join(r[0] for r in rows), len(blocks)))
    return rows


def build_template():
    secs = split_api_sections(FILES['template.md'])
    rows = []
    for s in secs:
        slug = slugify(s['title'])
        conv = R.convert(s['body'], promote_headings=1)
        api_page('template-management/%s.md' % slug,
                 {'title': s['title'], 'sidebar_label': s['title'],
                  'description': 'RHUB Template Management — %s API.' % s['title']},
                 s['method'], s['title'], conv, 'template.md',
                 extra_top=UNPUBLISHED_WARNING % 'template.md',
                 related=[('Template management overview', '/docs/template-management'),
                          ('Quotation', '/docs/quotation/quotation')])
        rows.append((s['title'], s['method'], slug))
    lines = ['# Template management', '', provenance('template.md'), '',
             UNPUBLISHED_WARNING % 'template.md', '',
             'The source file `template.md` documents client template configuration APIs — '
             'service fee, transaction limit and forex margin.', '',
             '| API | Method | Reference |', '|---|---|---|']
    for title, method, slug in rows:
        lines.append('| %s | `%s` | [Open](/docs/template-management/%s) |' % (title, method, slug))
    write('template-management/index.md',
          {'id': 'template-index', 'title': 'Template management', 'sidebar_label': 'Overview',
           'slug': '/template-management',
           'description': 'RHUB template management APIs: service fee, transaction limit, forex margin.'},
          '\n'.join(lines))
    rec('template.md', 'docs/template-management/ (index + %d API pages)' % len(rows), 'PARTIAL',
        'All %d sections documented in full (%s). Marked PARTIAL because the file is commented '
        'out of the live sidebar, so its publication status is REVIEW REQUIRED.'
        % (len(rows), ', '.join(r[0] for r in rows)))
    return rows


# --------------------------------------------------------------------------
# 8. legacy (unlinked) single-API source pages
# --------------------------------------------------------------------------

LEGACY = [
    ('loginauthentication.md', 'login-authentication', 'Login (Authentication) API', 'POST',
     'Superseded by the published [Authentication](/docs/authentication/authentication) page? '
     'The source does not say. Field-level differences are listed in the '
     '[source coverage notes](/docs/appendix/source-notes).'),
    ('customerRegistration.md', 'customer-registration', 'Customer-Registration API', 'POST', ''),
    ('customerInquiry.md', 'customer-inquiry', 'Customer-Inquiry API', 'GET', ''),
    ('updateCustomerDetails.md', 'update-customer-details', 'Update Customer-Details API', 'POST', ''),
    ('ownerDetails.md', 'owner-details', 'Owner Details API', 'POST', ''),
    ('quotation.md', 'quotation', 'Quotation API', 'POST', ''),
    ('finalQuotation.md', 'final-quotation', 'Final Quotation API', 'POST', ''),
    ('payout.md', 'payout', 'Payout API', 'POST', ''),
    ('transactionInquiry.md', 'transaction-inquiry', 'Transaction Inquiry API', 'GET', ''),
    ('balance.md', 'balance', 'Balance API', 'GET', ''),
    ('payoutValidator.md', 'reference-payout-validator', 'Reference API (Payout Validator)', 'GET', ''),
]


def build_legacy():
    rows = []
    for src, slug, title, method, note in LEGACY:
        text = FILES[src]
        conv = R.convert(text, drop_first_h1=True)
        conv = re.sub(r'^#\s+.*$', '', conv, count=1, flags=re.M).strip()
        extra = UNPUBLISHED_WARNING % src
        api_page('legacy/%s.md' % slug,
                 {'title': title, 'sidebar_label': title,
                  'description': 'RHUB %s (source page not linked in the live documentation sidebar).' % title},
                 method, title, conv, src, extra_top=extra,
                 related=[('Unlinked source pages overview', '/docs/legacy'),
                          ('Source coverage notes', '/docs/appendix/source-notes')],
                 register=False)
        rows.append((title, method, slug, src))
        rec(src, 'docs/legacy/%s.md' % slug, 'PARTIAL',
            'Page content carried over in full. Marked PARTIAL because the source file is '
            'commented out of the live documentation sidebar, so whether the contract is current '
            'is REVIEW REQUIRED.')
    lines = ['# Unlinked source pages', '',
             'These pages come from source files that the RHUB documentation site **serves but '
             'does not link** from its live sidebar. They are reproduced so that the portal '
             'accounts for the complete source export.', '',
             ':::warning[REVIEW REQUIRED — publication status]', '',
             'The source does not state whether these contracts are current, superseded or '
             'withdrawn. Where a page overlaps a published page, the two source files are not '
             'always identical; the differences are catalogued in the '
             '[source coverage notes](/docs/appendix/source-notes) rather than resolved here.', '',
             ':::', '',
             '| Page | Method | Source file |', '|---|---|---|']
    for title, method, slug, src in rows:
        lines.append('| [%s](/docs/legacy/%s) | `%s` | `%s` |' % (title, slug, method, src))
    write('legacy/index.md',
          {'id': 'legacy-index', 'title': 'Unlinked source pages', 'sidebar_label': 'Overview',
           'slug': '/legacy',
           'description': 'RHUB source pages that are served but not linked from the live documentation sidebar.'},
          '\n'.join(lines))
    return rows


# --------------------------------------------------------------------------
# 9. appendix: unpublished sections from published files, licence, source notes
# --------------------------------------------------------------------------

def build_unpublished_apis():
    parts = ['# Unpublished API sections', '',
             ':::warning[REVIEW REQUIRED — not published by the source]', '',
             'Every section on this page exists in the RHUB source **inside an HTML comment**, so '
             'the live documentation does not render it. The content is reproduced verbatim so '
             'that no source material is lost. The source does not establish whether these '
             'contracts are current, forthcoming or withdrawn — confirm with RHUB before use.', '',
             ':::', '']

    groups = [('ENQUIRY.md', 'Customer Enquiry (from ENQUIRY.md)'),
              ('QUOTA.md', 'Final Quotation (from QUOTA.md)'),
              ('WPT.md', 'WPT sections (from WPT.md)')]
    for src, label in groups:
        blocks = commented_api_sections(FILES[src])
        if not blocks:
            continue
        parts += ['## %s' % label, '', provenance(src), '']
        for b in blocks:
            conv = R.convert(b['body'])
            conv = re.sub(r'^(#{2,6})', r'##\1', conv, flags=re.M)
            parts += ['### %s' % b['title'], '',
                      '`%s` — status: **REVIEW REQUIRED (commented out in source)**' % b['method'],
                      '', conv, '']

    # responseCodes commented tables
    parts += ['## Commented code tables (from responseCodes.md)', '', provenance('responseCodes.md'), '']
    for block in R.comment_bodies(FILES['responseCodes.md']):
        conv = R.convert(block)
        conv = re.sub(r'^(#{2,6})', r'##\1', conv, flags=re.M)
        if conv.strip():
            parts += [conv, '']

    write('appendix/unpublished-apis.md',
          {'title': 'Unpublished API sections', 'sidebar_label': 'Unpublished API sections',
           'description': 'API sections that are commented out in the RHUB source files.'},
          '\n'.join(parts))


def build_licence():
    lic = R.convert(FILES['footer.md'])
    lic = re.sub(r'^#\s+All Rights Reserved\.\s*$', '', lic, count=1, flags=re.M).strip()
    # The source version marker is documentation provenance, not client-facing licence
    # text. It stays in the internal source notes and register instead.
    lic = re.sub(r'^\*Version [0-9.]+\*\s*$', '', lic, flags=re.M).strip()
    body = f"""# Licence

{lic}
"""
    write('appendix/licence.md',
          {'title': 'Licence', 'sidebar_label': 'Licence',
           'description': 'RemittancesHub licence statement.'}, body)
    rec('footer.md', 'docs/appendix/licence.md', 'COMPLETE',
        'Intellectual-property statement and source version marker (Version 2.3.0) carried over.')


# --------------------------------------------------------------------------
# 10. source coverage notes (conflict + gap register)
# --------------------------------------------------------------------------

def field_names(src_text):
    """Field names from the first column of every table in a source file."""
    text = R.strip_comments(src_text)
    names = set()
    for m in re.finditer(r'<tr[^>]*>(.*?)</tr>', text, re.S | re.I):
        c = re.search(r'<td[^>]*>(.*?)</td>', m.group(1), re.S | re.I)
        if c:
            v = re.sub(r'<[^>]+>', '', c.group(1)).strip()
            if re.match(r'^[a-z][A-Za-z0-9_]*$', v):
                names.add(v)
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('|'):
            cells = [x.strip() for x in line.strip('|').split('|')]
            if cells and re.match(r'^[a-z][A-Za-z0-9_]*$', cells[0]):
                names.add(cells[0])
    return names


def endpoints_in(src_text):
    text = R.strip_comments(src_text)
    return sorted(set(re.findall(r'https?://[^\s|<]+', text)))


CONFLICT_PAIRS = [
    ('AUTH.md', 'loginauthentication.md', 'Authentication',
     '/docs/authentication/authentication', '/docs/legacy/login-authentication'),
    ('QUOTA.md', 'quotation.md', 'Quotation',
     '/docs/quotation/quotation', '/docs/legacy/quotation'),
    ('PAYOUT-Api.md', 'payout.md', 'Payout',
     '/docs/payout/payout', '/docs/legacy/payout'),
    ('ENQUIRY.md', 'transactionInquiry.md', 'Transaction enquiry / inquiry',
     '/docs/transactions/transaction-enquiry', '/docs/legacy/transaction-inquiry'),
    ('ENQUIRY.md', 'balance.md', 'Balance',
     '/docs/balance/balance-enquiry', '/docs/legacy/balance'),
    ('CUSTOMEREGIS.md', 'customerRegistration.md', 'Customer registration',
     '/docs/customers/customer-registration', '/docs/legacy/customer-registration'),
]


def build_source_notes(master_rows, wpt_rows, tpl_rows):
    lines = ['# Source coverage notes', '',
             'This page is the audit trail for RHUB Developer Portal 1.0: what the source '
             'contains, where each file landed, and every point at which the source does not '
             'establish something.', '',
             provenance(sorted(FILES.keys())[:0] or ['RHUB_FULL_SOURCE_EXPORT.json']), '',
             '## Export integrity', '',
             '| Check | Result |', '|---|---|',
             '| Source | `%s` |' % SOURCE_URL,
             '| Exported at | %s |' % EXPORTED_AT,
             '| Markdown files in export | %d |' % len(FILES),
             '| Fetch failures | 0 (all 29 files returned HTTP 200) |',
             '| Empty source files | 0 |',
             '| Total source characters | %d |' % sum(len(v) for v in FILES.values()),
             '',
             '## Supplemental authoritative sources', '',
             'Material supplied directly by the RHUB team, outside the documentation export, is '
             'kept in its own data file so it can be updated independently and republished by '
             're-running the generator.', '',
             '| Supplemental source | Supplied by | Received | Portal page |', '|---|---|---|---|']
    if CURRENT_ERRORS:
        lines.append('| `source/%s` | %s | %s | [Current API error codes](/docs/errors/current-error-codes) |'
                     % (os.path.basename(CURRENT_ERRORS_JSON), CURRENT_ERRORS['provider'],
                        CURRENT_ERRORS['receivedOn']))
    else:
        lines.append('| — | — | — | none present at build time |')
    lines += ['',
             '## Publication status in the source sidebar', '',
             'The export includes the site sidebar. Fourteen files are linked from it; the other '
             'fifteen are served but their sidebar entries are commented out. This portal '
             'reproduces all 29 and labels the difference rather than assuming one.', '',
             '| Source file | Linked in live sidebar |', '|---|---|']
    for f in sorted(FILES.keys()):
        lines.append('| `%s` | %s |' % (f, 'Yes' if f in PUBLISHED else 'No — REVIEW REQUIRED'))

    lines += ['', '## Commented-out source content', '',
              'HTML-commented blocks are not live documentation, so they are not rendered as '
              'such. Substantive commented API contracts are reproduced in '
              '[Unpublished master APIs](/docs/appendix/unpublished-master-apis) and '
              '[Unpublished API sections](/docs/appendix/unpublished-apis). The table shows how '
              'much of each source file is commented out.', '',
              '| Source file | Characters | Commented characters | Commented blocks |',
              '|---|---|---|---|']
    for f in sorted(FILES.keys()):
        c = FILES[f]
        sp = R.comment_spans(c)
        commented = sum(b - a for a, b in sp)
        lines.append('| `%s` | %d | %d (%d%%) | %d |' %
                     (f, len(c), commented, round(commented * 100 / max(len(c), 1)), len(sp)))

    lines += ['', '## Overlapping source files — differences preserved, not resolved', '',
              ':::warning[REVIEW REQUIRED]', '',
              'Several capabilities are described twice in the source: once in a file linked from '
              'the live sidebar and once in an unlinked file. The two versions are not always '
              'identical. Per the project rule, the differences below are reported, not merged '
              'or silently corrected.', '', ':::', '']
    for a, b, label, pa, pb in CONFLICT_PAIRS:
        fa, fb = field_names(FILES[a]), field_names(FILES[b])
        ea, eb = endpoints_in(FILES[a]), endpoints_in(FILES[b])
        only_a = sorted(fa - fb)
        only_b = sorted(fb - fa)
        lines += ['### %s — `%s` vs `%s`' % (label, a, b), '',
                  '- Portal pages: [%s](%s) and [%s](%s)' % (a, pa, b, pb), '',
                  '| Aspect | `%s` (linked) | `%s` (unlinked) |' % (a, b), '|---|---|---|',
                  '| Endpoints appearing in file | %s | %s |' %
                  (', '.join('`%s`' % x for x in ea) or '—', ', '.join('`%s`' % x for x in eb) or '—'),
                  '| Field names present only in this file | %s | %s |' %
                  (', '.join('`%s`' % x for x in only_a[:40]) or '—',
                   ', '.join('`%s`' % x for x in only_b[:40]) or '—'),
                  '']
        if len(only_a) > 40 or len(only_b) > 40:
            lines += ['*(field lists truncated at 40 entries per side; full sets are on the two '
                      'pages themselves)*', '']

    lines += ['## Source assets not present in the export', '',
              ':::warning[REVIEW REQUIRED]', '',
              'The source references the following binary assets. They are not part of the '
              'supplied export and have not been recreated or substituted.', '',
              '| Asset | Referenced by | Portal treatment |', '|---|---|---|',
              '| `img/rhub.png` | every source page (page banner) | Not reproduced; no substitute branding created |',
              '| `img/apiseq.png` | `apisequence.md` (inside a comment) | Not reproduced; source reference retained in text |',
              '| `img/rhubbpt2.png` | `transactionflow.md` (bank payout flow) | REVIEW REQUIRED notice on the page |',
              '| `img/rhubwpt2.png` | `transactionflow.md` (wallet payout flow) | REVIEW REQUIRED notice on the page |',
              '| `assets/TABLE_OF_VALIDATIONS.xlsx` | `CURRENCYVALIDATIONS.md` download link | REVIEW REQUIRED; link points here |',
              '', ':::', '']

    seen = []
    for u in R.UNRESOLVED_LINKS:
        if u not in seen:
            seen.append(u)
    lines += ['## Source cross-links with no resolvable target', '']
    if seen:
        lines += [':::warning[REVIEW REQUIRED]', '',
                  'These links exist in the source but point at sections the source does not '
                  'publish. They have been redirected to the nearest index page rather than '
                  'invented.', '',
                  '| Source link | Issue |', '|---|---|']
        for u in seen:
            link, _, reason = u.partition(' (')
            lines.append('| `%s` | %s |' % (link, reason.rstrip(')')))
        lines += ['', ':::', '']
    else:
        lines += ['All source cross-links resolved to a portal target.', '']

    lines += ['## Information the source does not establish', '',
              'These topics are absent from the supplied source and are therefore absent from '
              'this portal. They are listed so their absence is visible rather than mistaken '
              'for an oversight.', '',
              '| Topic | Status |', '|---|---|',
              '| Rate limits | REVIEW REQUIRED — not in source |',
              '| Idempotency keys / replay behaviour | REVIEW REQUIRED — not in source |',
              '| Retry policy and backoff | REVIEW REQUIRED — not in source |',
              '| Webhooks / callbacks | REVIEW REQUIRED — not in source |',
              '| SDKs and client libraries | REVIEW REQUIRED — not in source |',
              '| Environment base URLs (most pages use the literal placeholder `http://host`) | REVIEW REQUIRED — not in source |',
              '| How the access token is presented on subsequent calls | REVIEW REQUIRED — not in source |',
              '| Token refresh / re-authentication | REVIEW REQUIRED — not in source |',
              '| Pagination for list endpoints | REVIEW REQUIRED — not in source |',
              '| Error-code resolution guidance | REVIEW REQUIRED — not in source |',
              '| SLA / availability commitments | REVIEW REQUIRED — not in source |',
              '| Transaction status transition rules | REVIEW REQUIRED — not in source |',
              '']

    lines += ['## Source-file to portal-page map', '',
              '| Source file | Portal location | Status | Notes |', '|---|---|---|---|']
    for src, loc, status, notes in sorted(MANIFEST):
        lines.append('| `%s` | %s | %s | %s |' % (src, loc, status, notes))

    write('appendix/source-notes.md',
          {'title': 'Source coverage notes', 'sidebar_label': 'Source coverage notes',
           'description': 'Audit trail: source integrity, publication status, conflicts, gaps and the source-to-page map.'},
          '\n'.join(lines))



# --------------------------------------------------------------------------
# 10b. Review Resolution Register (internal, unlisted)
# --------------------------------------------------------------------------

REGISTER = [
    ('R1', 'Access token transport',
     'docs/authentication/authentication.md',
     '"The source does not describe how the access token is subsequently presented on other '
     'API calls... REVIEW REQUIRED."',
     'RHUB decision D1 (2026-08-17).',
     'Subsequent calls carry `Authorization: Bearer <access_token>`.',
     'Authentication page gained a "Using the access token" block; the convention is also '
     'documented centrally under "Authorising requests" in the conventions page.',
     'Client-facing INFO note on Authentication + central conventions section.',
     'RESOLVED'),
    ('R2', 'scope inconsistency in Authentication',
     'docs/authentication/authentication.md',
     'No rendered marker; found during audit. Request table omitted `scope` (row commented out '
     'in source), request example sent `scope=read%20write`, response table lists `scope` as M.',
     'RHUB decision D3 (2026-08-17).',
     '`scope` is a response field. Clients need not send it on the token request.',
     'Note added stating scope is returned, not required on the request. The source request '
     'example is reproduced unchanged.',
     'Client-facing NOTE on Authentication.',
     'RESOLVED'),
    ('R3', 'Environment / base URL',
     'docs/getting-started/conventions.md (prose list)',
     'No rendered marker; endpoints written `http://host/...` with no base URL established.',
     'RHUB decision D2 (2026-08-17).',
     'Sandbox base URL is `https://sandbox-client.remittanceshub.com:8030`. No UAT or '
     'production URL confirmed.',
     'Conventions page gained an Environments table and an explanation that `host` stands for '
     'the environment base URL, with a worked Sandbox example. Endpoint paths unchanged.',
     'Client-facing documentation section.',
     'RESOLVED (Sandbox only)'),
    ('R4', 'C2C requirement for sendClientTrxReference',
     'docs/payout/payout.md',
     '"REVIEW REQUIRED — C2C value for `sendClientTrxReference`. The contract marks the field '
     'Mandatory while the invoice requirement excludes C2C."',
     'RHUB decision D6 (2026-08-17).',
     'Required for B2B, B2C and C2B. For C2C it may be omitted or sent blank.',
     'Warning replaced with a conditional-requirement INFO block. The transactionInfo field '
     'table still shows the original `M` flag, and the block states which rule to follow.',
     'Client-facing CONDITIONAL REQUIREMENT on Payout.',
     'RESOLVED'),
    ('R5', 'sendClientTrxReference vs sendClientTxnReference',
     'docs/payout/payout.md, docs/errors/current-error-codes.md',
     '"Both spellings are reproduced exactly as RHUB supplied them; which one the API accepts '
     'is REVIEW REQUIRED."',
     'RHUB decisions D4 and D5 (2026-08-17).',
     'The request field is `sendClientTrxReference`. Some current validation messages say '
     '`sendClientTxnReference`; that is what the system returns today, pending a separate '
     'backend correction.',
     'Payout note states the field name and warns that validation messages may differ. Error '
     'code descriptions are reproduced unchanged.',
     'Client-facing NOTE on Payout.',
     'RESOLVED WITH CURRENT-BEHAVIOUR NOTE'),
    ('R6', 'Wallet Not Found has no resultCode',
     'docs/errors/current-error-codes.md',
     '"REVIEW REQUIRED — result code not provided."',
     'RHUB decision D7 (2026-08-17).',
     'Known current API behaviour; no code is to be invented.',
     'Warning became a NOTE describing it as current behaviour, advising clients to handle it '
     'on `resultDescription`. Table still shows "Not provided".',
     'Client-facing NOTE.',
     'RESOLVED'),
    ('R7', 'HTTP status vs resultCode overlap',
     'docs/errors/current-error-codes.md, docs/errors/index.md',
     '"REVIEW REQUIRED — precedence between the code families."',
     'RHUB decision D8 (2026-08-17).',
     'Separate namespaces; a shared numeral is not a conflict.',
     'Warning replaced with an INFO block explaining the three concepts. The overlap table is '
     'now framed as reference, not a conflict register.',
     'Client-facing INFO on the error pages.',
     'RESOLVED'),
    ('R8', 'Transaction status lifecycle',
     'docs/errors/transaction-status-codes.md',
     '"Transitions between them, their timing, and which statuses are terminal are not '
     'established — that is REVIEW REQUIRED."',
     'RHUB decision D9 (2026-08-17).',
     'Not published in Developer Portal 1.0. This is a scope decision, not a resolved '
     'lifecycle. No transitions, ordering, timing or terminality have been inferred.',
     'Scope note now states values and meanings are documented and lifecycle is out of scope.',
     'Client-facing NOTE.',
     'DEFERRED'),
    ('R9', 'Bank and wallet payout flow diagrams',
     'docs/getting-started/transaction-flows.md',
     '"REVIEW REQUIRED — diagram not available" (twice).',
     'RHUB decision D10 (2026-08-17). Binary assets `img/rhubbpt2.png` and `img/rhubwpt2.png` '
     'are absent from the repository and are not exposed by the current RHUB site.',
     'The originals will not be reconstructed. The surviving prose describes both flows in '
     'RHUB\'s own words and is useful without the images.',
     'Production warnings removed from the client-facing page; the prose was retained and a '
     'pointer to the integration flow added. The missing assets remain recorded here and in '
     'the source coverage notes.',
     'No client-facing warning. Asset gap recorded internally.',
     'ORIGINAL ASSET UNAVAILABLE / INTERNALLY RECORDED'),
    ('R10', 'apiseq.png',
     'none (never rendered)',
     'Referenced inside a commented-out block of `apisequence.md`.',
     'Mechanical inspection of the export: the reference is commented out by RHUB.',
     'Never published by RHUB.',
     'No change. Not exposed.',
     'Not client-facing.',
     'HIDDEN/LEGACY'),
    ('R11', 'TABLE_OF_VALIDATIONS.xlsx',
     'none (never rendered)',
     'Referenced inside a commented-out block of `CURRENCYVALIDATIONS.md`.',
     'Mechanical inspection of the export: the reference is commented out by RHUB.',
     'Never published by RHUB.',
     'No change. Not exposed.',
     'Not client-facing.',
     'HIDDEN/LEGACY'),
    ('R12', 'Duplicate warning on the errors overview',
     'docs/errors/index.md',
     '"REVIEW REQUIRED — resolution guidance."',
     'The same fact is documented on the current error codes page.',
     'Duplicate. Consolidated.',
     'Overview warning became a NOTE that also explains the two code families; the '
     'no-remediation fact remains on the error code page.',
     'Client-facing NOTE.',
     'RESOLVED / CONSOLIDATED'),
    ('R13', 'Publication-status warnings on unlisted pages',
     'docs/legacy/*, docs/template-management/*, docs/wpt/*',
     '"REVIEW REQUIRED — publication status" and similar.',
     'These pages derive from source files RHUB commented out of its live sidebar.',
     'They stay out of client navigation. Their warnings are correct in context.',
     'No change. Pages remain `unlisted: true`: absent from sidebar, API index, search and '
     'sitemap, and reachable only by direct URL.',
     'Not client-facing.',
     'HIDDEN/LEGACY'),
    ('R18', 'Integration sequence ordering',
     'homepage, docs overview, integration flow, quotation, customer registration, document '
     'upload, payout, API index',
     'No marker. The portal documented the sequence as authenticate, customer status, KYC/KYB, '
     'quotation, transaction type, reference data, payout, transaction enquiry.',
     'RHUB operational clarification, decisions D11 and D12 (2026-08-17), recorded in '
     'source/RHUB_INTEGRATION_GUIDANCE.json.',
     'Corrected sequence: Authentication, Quotation, Document Upload, customer-registration '
     'decision, Bank List, master/reference data, Payout, Transaction Enquiry, Balance. A '
     'quotation does not require a registered customer: pass an existing `customerCode` or '
     'send it blank; registration is resolved before or during payout.',
     'All public flow guidance regenerated from the corrected sequence in the guidance source. '
     'No API contract changed; `customerCode` remains Optional on the Quotation contract.',
     'Client-facing flow guidance, corrected.',
     'RESOLVED'),
    ('R15', 'Authentication request example sent `scope`',
     'docs/authentication/authentication.md',
     'No marker. The public request example carried `scope=read%20write` although D3 states '
     'scope is a response field.',
     'RHUB decision D3.',
     'The client-facing request example now sends `grant_type`, `username` and `password` '
     'only. `scope` remains in the response example and response table.',
     'Public example corrected at generation time. The original example is preserved '
     'unchanged in source/RHUB_FULL_SOURCE_EXPORT.json.',
     'Client-facing example, corrected.',
     'RESOLVED'),
    ('R16', 'Legacy HTTP/application error page in the client journey',
     'docs/errors/error-codes.md',
     'No marker. The page derives from the older documentation export and competed with the '
     'current resultCode reference.',
     'Client-readiness decision: the public error model is resultCode + resultDescription, '
     'plus transaction status values.',
     'The page is now unlisted: out of the sidebar, errors overview, related links, search '
     'and sitemap. Its content is unchanged and reachable by direct URL.',
     'Errors overview rewritten around two families; the migration-era comparison section was '
     'removed from the current error codes page.',
     'Not client-facing.',
     'HIDDEN/LEGACY'),
    ('R17', 'Example payload data',
     'all client-facing pages with examples',
     'No marker. Examples carried real-looking names, companies, emails and account numbers.',
     'Client-readiness decision; convention recorded in '
     'source/RHUB_EXAMPLE_DATA_POLICY.json.',
     'Synthetic identities (John/Jane Doe, Example Trading Ltd, example.com, REF/INV/CUS '
     'references) applied to code blocks and field-table sample values on listed pages, '
     'preserving type, length and format.',
     'Sanitisation runs at generation time; unlisted audit pages keep the original values.',
     'Client-facing examples, sanitised.',
     'RESOLVED'),
    ('R14', 'Internal migration and audit warnings',
     'docs/appendix/*, tools/, COMPLETENESS_REPORT.md',
     'Audit trail wording: coverage tables, publication status, commented-source accounting.',
     'Internal traceability for the documentation build.',
     'Retained internally; no client-facing exposure.',
     'No change to the evidence. Client-facing pages were scanned for migration language.',
     'Not client-facing.',
     'INTERNAL'),
]


def build_review_register():
    lines = ['# Review resolution register', '',
             'Internal record of every REVIEW REQUIRED issue raised during the build of RHUB '
             'Developer Portal 1.0, what resolved it, and how it is now presented. Nothing was '
             'removed without a disposition recorded here.', '',
             'Baseline audit: 175 occurrences, 14 unique issues, 12 on client-facing pages.', '',
             '| ID | Issue | Status |', '|---|---|---|']
    for r in REGISTER:
        lines.append('| %s | %s | **%s** |' % (r[0], r[1], r[8]))
    lines += ['']
    for (rid, issue, pages, wording, evidence, resolution, change, treatment, status) in REGISTER:
        lines += ['## %s — %s' % (rid, issue), '',
                  '**Status:** %s' % status, '',
                  '| | |', '|---|---|',
                  '| Original page(s) | %s |' % pages,
                  '| Original wording | %s |' % wording.replace('|', '\\|'),
                  '| Evidence / decision | %s |' % evidence,
                  '| Resolution | %s |' % resolution,
                  '| Documentation change | %s |' % change,
                  '| Final public treatment | %s |' % treatment,
                  '']
    lines += ['## RHUB decisions applied', '']
    if GUIDANCE and 'decisions' in GUIDANCE:
        d = GUIDANCE['decisions']
        lines += ['Supplied by %s on %s and stored in `source/RHUB_INTEGRATION_GUIDANCE.json` '
                  'so they stay separable from the original documentation export.'
                  % (d.get('provider', 'RHUB'), d.get('receivedOn', '')), '',
                  '| ID | Decision | Resolves |', '|---|---|---|']
        for key, val in d.items():
            if isinstance(val, dict) and 'rule' in val:
                lines.append('| %s | %s | %s |' % (val.get('id', ''), val['rule'],
                                                   val.get('resolves', '')))
    write('appendix/review-resolution-register.md',
          {'title': 'Review resolution register', 'sidebar_label': 'Review resolution register',
           'description': 'Internal record of REVIEW REQUIRED issues and their dispositions.'},
          '\n'.join(lines))


# --------------------------------------------------------------------------
# API index page
# --------------------------------------------------------------------------

INDEX_STAGES = {
    'authentication/authentication.md': 'Start',
    'quotation/quotation.md': 'Pricing / pre-registration',
    'documents/document-upload.md': 'Payout preparation',
    'customers/customer-registration.md': 'Conditional customer setup',
    'payout/payout.md': 'Transaction',
    'payout/wpt-payout.md': 'Transaction',
    'transactions/transaction-enquiry.md': 'Post-payout',
    'balance/balance-enquiry.md': 'Final / supporting',
}

# Sections excluded from the public index: they are not part of public navigation.
INDEX_EXCLUDE_PREFIXES = ('template-management/', 'legacy/', 'appendix/', 'wpt/')


def build_api_index():
    core, masters = [], []
    for name, method, ep, page, purpose in API_INDEX:
        if page.startswith(INDEX_EXCLUDE_PREFIXES):
            continue
        stage = INDEX_STAGES.get(page,
                                 'Payout preparation / reference'
                                 if page.startswith('master-apis/')
                                 else 'Supporting / reference')
        row = (name, method, purpose, stage, ep, page)
        (masters if page.startswith('master-apis/') else core).append(row)

    order = ['Start', 'Pricing / pre-registration', 'Payout preparation',
             'Conditional customer setup', 'Payout preparation / reference', 'Transaction',
             'Post-payout', 'Final / supporting', 'Supporting / reference']
    core.sort(key=lambda r: order.index(r[3]) if r[3] in order else len(order))

    def render(rows):
        out = ['| API | Method | Purpose | Integration stage | Endpoint | Page |',
               '|---|---|---|---|---|---|']
        for name, method, purpose, stage, ep, page in rows:
            route = '/docs/' + page.replace('.md', '')
            out.append('| %s | `%s` | %s | %s | `%s` | [Open](%s) |'
                       % (name, method, purpose.replace('|', '\\|'), stage,
                          ep.replace('|', '\\|'), route))
        return out

    lines = ['# API index', '',
             'Every API in the public reference, with the stage of an integration at which it '
             'is typically used. Purposes are RHUB\'s own descriptions.', '',
             '## Transaction APIs', '']
    lines += ['<div className="rhub-apitable">', ''] + render(core) + ['', '</div>', '']
    lines += ['', '## Master / reference APIs', '',
              'Master APIs supply the coded values other requests expect. They are need-based: '
              'call the ones your route and use case require, in whatever order suits your '
              'implementation. They are not a sequence.', '']
    lines += ['<div className="rhub-apitable">', ''] + render(masters) + ['', '</div>', '']
    lines += ['', ':::note', '',
              'Endpoint strings are reproduced exactly as RHUB writes them, including the literal '
              '`http://host` placeholder where RHUB uses it.', '', ':::', '',
              '## Related', '',
              '- [Integration flow](/docs/getting-started/integration-flow)',
              '- [How to read this reference](/docs/getting-started/conventions)',
              '- [Errors and response codes](/docs/errors)']
    write('api-index.md',
          {'title': 'API index', 'sidebar_label': 'API index',
           'description': 'Index of the public RHUB APIs, with purpose, integration stage and endpoint.'},
          '\n'.join(lines))


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    if os.path.isdir(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS, exist_ok=True)

    build_intro()
    build_getting_started()
    build_authentication()
    build_customer_registration()
    build_quotation()
    build_payout()
    build_enquiry()
    build_document_upload()
    master_rows = build_master()
    build_validation()
    build_errors()
    build_current_error_codes()
    wpt_rows = build_wpt()
    tpl_rows = build_template()
    build_legacy()
    build_unpublished_apis()
    build_licence()
    build_review_register()
    build_api_index()
    build_source_notes(master_rows, wpt_rows, tpl_rows)

    covered = {m[0] for m in MANIFEST}
    supplemental = sorted(covered - set(FILES))
    missing = sorted(set(FILES) - covered)
    print('pages written: %d' % len(PAGES))
    print('APIs indexed : %d' % len(API_INDEX))
    print('export source files accounted for: %d/%d' % (len(covered & set(FILES)), len(FILES)))
    if supplemental:
        print('supplemental authoritative sources: %s' % ', '.join(supplemental))
    if missing:
        print('MISSING:', missing)
    print('validation matrices -> %d tables, %d expandable entries, %d field values, '
          '%d group rows, %d void columns dropped'
          % (MATRIX_STATS['tables'], MATRIX_STATS['entries'], MATRIX_STATS['values'],
             MATRIX_STATS['groups'], MATRIX_STATS['void_columns']))
    json.dump({'pages': PAGES, 'apis': API_INDEX, 'manifest': MANIFEST,
               'master_rows': master_rows, 'wpt_rows': wpt_rows, 'tpl_rows': tpl_rows,
               'unresolved_links': R.UNRESOLVED_LINKS},
              open(os.path.join(HERE, 'build-manifest.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
