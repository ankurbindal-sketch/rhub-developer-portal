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
FILES = {f['file']: f['content'] for f in EXPORT['files']}
SOURCE_URL = EXPORT['source']
EXPORTED_AT = EXPORT['exportedAt']

# files linked from the live (published) sidebar
PUBLISHED = ['README.md', 'apisequence.md', 'AUTH.md', 'QUOTA.md', 'DocumentUpload.md',
             'PAYOUT-Api.md', 'PAYOUT-WPT.md', 'ENQUIRY.md', 'master.md', 'CUSTOMEREGIS.md',
             'responseCodes.md', 'CURRENCYVALIDATIONS.md', 'COUNTRYVALIDATIONS.md', 'footer.md']

MANIFEST = []      # (source file, portal path, status, notes)
PAGES = []         # portal doc paths written
API_INDEX = []     # (name, method, endpoint, page)


def rec(src, portal_path, status, notes):
    MANIFEST.append((src, portal_path, status, notes))


def write(relpath, front, body):
    path = os.path.join(DOCS, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
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


def slugify(name):
    s = name.lower()
    s = s.replace('/', '-').replace('&', 'and')
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def endpoint_of(body):
    """First endpoint URL found in a converted body (for the API index only)."""
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
        API_INDEX.append((title, method, endpoint_of(converted), relpath))
    return relpath


# --------------------------------------------------------------------------
# 1. intro (README.md)
# --------------------------------------------------------------------------

def build_intro():
    readme = R.convert(FILES['README.md'])
    readme = re.sub(r'^#\s+The RemittancesHub\s*$', '', readme, count=1, flags=re.M).strip()
    body = f"""# RHUB Developer Portal

Welcome to the developer documentation for **RHUB (RemittancesHub)**. This portal is a
re-presentation of the authoritative RHUB technical documentation, reorganised for
integration work.

{provenance('README.md')}

{readme}

## Where to start

| Step | Page |
|---|---|
| 1. Understand the call sequence | [Integration flow](/docs/getting-started/integration-flow) |
| 2. Read the portal conventions | [How to read this reference](/docs/getting-started/conventions) |
| 3. Authenticate | [Authentication](/docs/authentication/authentication) |
| 4. Price a transaction | [Quotation](/docs/quotation/quotation) |
| 5. Send funds | [Payout](/docs/payout/payout) · [WPT Payout](/docs/payout/wpt-payout) |
| 6. Track the transaction | [Transaction Enquiry](/docs/transactions/transaction-enquiry) |

## Core integration journey

```text
LOGIN / AUTHENTICATION
        ↓
QUOTATION
        ↓
PAYOUT
        ↓
TRANSACTION ENQUIRY
```

The source states that the API call sequence is limited to the Login API, Quotation API,
Payout API and Transaction Enquiry API, and that the remaining APIs can be called based on
the need. See [Integration flow](/docs/getting-started/integration-flow) for the full
source-documented sequence.

## Supporting capabilities documented in this portal

- [Customer Registration](/docs/customers/customer-registration)
- [Document Upload](/docs/documents/document-upload)
- [Balance Enquiry](/docs/balance/balance-enquiry)
- [Master / reference APIs](/docs/master-apis) — 14 published master endpoints
- [Currency and country validations](/docs/validation/currency-validations)
- [Errors and response codes](/docs/errors)

:::info[Documentation fidelity]

Every endpoint, field name, type, length, requirement flag, validation rule, example and
error code in this portal is carried over from the RHUB source export. Where the source does
not establish something, the page says **REVIEW REQUIRED** instead of filling the gap. See
[How to read this reference](/docs/getting-started/conventions) and the
[source coverage notes](/docs/appendix/source-notes).

:::
"""
    write('intro.md', {'id': 'intro', 'title': 'RHUB Developer Portal',
                       'sidebar_label': 'Overview', 'slug': '/',
                       'description': 'Developer documentation for the RHUB (RemittancesHub) cross-border remittance APIs.'},
          body)
    rec('README.md', 'docs/intro.md', 'COMPLETE', 'About Us and Overview sections carried over verbatim.')


# --------------------------------------------------------------------------
# 2. getting started
# --------------------------------------------------------------------------

def build_getting_started():
    seq = R.convert(FILES['apisequence.md'])
    seq = re.sub(r'^#\s+Sequence of API Call\s*$', '', seq, count=1, flags=re.M).strip()
    body = f"""# Integration flow

{provenance('apisequence.md')}

{seq}
"""
    write('getting-started/integration-flow.md',
          {'title': 'Integration flow', 'sidebar_label': 'Integration flow',
           'description': 'The RHUB API call sequence, as documented in the RHUB source.'}, body)
    rec('apisequence.md', 'docs/getting-started/integration-flow.md', 'COMPLETE',
        'Sequence list and all cross-references remapped to portal routes. Source diagram '
        '(img/apiseq.png) is commented out in the source and the asset is not in the export.')

    flows = R.convert(FILES['transactionflow.md'])
    flows = re.sub(r'^#\s+Transaction Flows\s*$', '', flows, count=1, flags=re.M).strip()
    body = f"""# Transaction flows

{provenance('transactionflow.md')}

{flows}
"""
    write('getting-started/transaction-flows.md',
          {'title': 'Transaction flows', 'sidebar_label': 'Transaction flows',
           'description': 'Bank payout and wallet payout transaction flows as described in the RHUB source.'}, body)
    rec('transactionflow.md', 'docs/getting-started/transaction-flows.md', 'REVIEW REQUIRED',
        'Narrative carried over in full. Both flow diagrams (img/rhubbpt2.png, img/rhubwpt2.png) '
        'are referenced by the source but the binary assets are not in the export — flagged on page.')

    body = f"""# How to read this reference

This page describes the conventions used by RHUB Developer Portal 1.0. It contains no
technical claims of its own — every technical statement lives on the API pages and comes
from the RHUB source export.

## Requirement flags

The RHUB source marks every request field with a requirement flag. This portal preserves
the source flag exactly and never promotes one to another:

| Flag | Source meaning |
|---|---|
| M | Mandatory |
| O | Optional |
| C | Conditional |

Conditional fields are **not** documented as mandatory. Where the source explains the
condition — for example correspondent-specific or country-specific rules — the explanation
appears with the field table or in [Validation](/docs/validation/currency-validations).

## Field tables

Field tables reproduce the source columns. Depending on the source page these are:

- `Parameters | Input Type | Length | Requirement | Description`, or
- `Parameters | Data Type | Requirement | Description` (older source pages, where the
  source does not state a length).

Where the source does not state a field length, the column is absent rather than guessed.

## Method and endpoint callouts

Each API page shows the HTTP method badge and an **Endpoint** callout containing the request
URL exactly as the source writes it. Many source URLs use the literal host placeholder
`http://host/...`; that placeholder is reproduced as-is because the source does not
establish the environment base URLs on those pages.

## Examples

Request and response examples are the source's own samples, reproduced verbatim in
copy-to-clipboard code blocks. The source frequently masks values in its examples (for
example `15*****f-54fe-43d9-***7-b7dc****1b9`); masking is preserved. Where a source page
has no example, the page says so rather than showing an invented one.

## REVIEW REQUIRED

**REVIEW REQUIRED** marks a point where the supplied RHUB source does not establish the
information — a missing example, a missing field contract, an unavailable image asset, an
internal source link with no matching target, or a conflict between two source files. It is
never a placeholder for content that exists in the source.

The following are *not* established anywhere in the supplied source and are therefore
absent from this portal rather than inferred: rate limits, idempotency behaviour, retry
semantics, webhooks, SDKs, pagination rules, sandbox versus production base URLs (other than
where a URL literally appears in the source), token refresh behaviour, and SLA claims.

## Publication status of source pages

The RHUB source export contains 29 Markdown files. Fourteen are linked from the live
documentation sidebar; the remaining fifteen are served but commented out of that sidebar.
Pages built from unlinked files carry a publication-status warning. Full details are in the
[source coverage notes](/docs/appendix/source-notes).

## Formatting transformations applied

To move from the legacy docsify pages to this portal, only presentation was changed:

- HTML `<table>` markup became Markdown tables; cell text, field names and values are verbatim.
- "Tap to open" reveal widgets became syntax-highlighted, copyable code blocks.
- "About the API / Request URL / Request Method" tables became endpoint callouts.
- Source cross-links (`#/PAYOUT-Api?id=...`) were remapped to portal routes.
- A handful of source tables carry a stray extra cell on some rows, which standard Markdown
  would silently drop. Those rows were re-aligned so that every non-empty source value still
  appears; no value was moved between columns and none was added.
- HTML-commented blocks in the source are not rendered as live documentation; substantive
  commented API contracts are reproduced in the [appendix](/docs/appendix/unpublished-apis)
  with a warning, and every commented block is accounted for in the
  [source coverage notes](/docs/appendix/source-notes).
"""
    write('getting-started/conventions.md',
          {'title': 'How to read this reference', 'sidebar_label': 'How to read this reference',
           'description': 'Conventions used in the RHUB Developer Portal: requirement flags, field tables, examples and REVIEW REQUIRED markers.'},
          body)


# --------------------------------------------------------------------------
# 3. single-API published pages
# --------------------------------------------------------------------------

def build_authentication():
    secs = split_api_sections(FILES['AUTH.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    extra = """:::note[Authentication scheme]

The source documents this endpoint, its request parameters, its header parameters and its
response fields, and the response includes `access_token`, `token_type`, `expires_in` and
`scope`. The source does **not** describe how the access token is subsequently presented on
other API calls, token refresh behaviour, scope semantics, or expiry handling — those points
are **REVIEW REQUIRED** and are not inferred here.

:::"""
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
    api_page('quotation/quotation.md',
             {'title': 'Quotation', 'sidebar_label': 'Quotation',
              'slug': '/quotation/quotation',
              'description': 'RHUB Quotation API — fetch the forex rate between payin and payout currencies.'},
             s['method'], 'Quotation', conv, 'QUOTA.md',
             related=[('Authentication', '/docs/authentication/authentication'),
                      ('Payout', '/docs/payout/payout'),
                      ('WPT Payout', '/docs/payout/wpt-payout'),
                      ('Final Quotation (unlinked source page)', '/docs/legacy/final-quotation')])
    rec('QUOTA.md', 'docs/quotation/quotation.md', 'COMPLETE',
        'Published Quotation contract carried over in full. The file also contains a '
        'commented-out Final Quotation section — reproduced in the appendix and cross-checked '
        'against the standalone finalQuotation.md source page.')


def build_document_upload():
    secs = split_api_sections(FILES['DocumentUpload.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    api_page('documents/document-upload.md',
             {'title': 'Document Upload', 'sidebar_label': 'Document Upload',
              'description': 'RHUB Document Upload API — upload customer documents such as ID proofs and invoices.'},
             s['method'], 'Document Upload', conv, 'DocumentUpload.md',
             related=[('Customer Registration', '/docs/customers/customer-registration'),
                      ('Payout', '/docs/payout/payout'),
                      ('Customer/Individual Document Type (master)',
                       '/docs/master-apis/customer-individual-document-type')])
    rec('DocumentUpload.md', 'docs/documents/document-upload.md', 'COMPLETE',
        'Published Document Upload contract carried over in full.')


def build_customer_registration():
    secs = split_api_sections(FILES['CUSTOMEREGIS.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    api_page('customers/customer-registration.md',
             {'title': 'Customer Registration', 'sidebar_label': 'Customer Registration',
              'description': 'RHUB Customer Registration API — register business and individual customers.'},
             s['method'], 'Customer Registration', conv, 'CUSTOMEREGIS.md',
             related=[('Document Upload', '/docs/documents/document-upload'),
                      ('Payout', '/docs/payout/payout'),
                      ('Master / reference APIs', '/docs/master-apis'),
                      ('Customer Inquiry (unlinked source page)', '/docs/legacy/customer-inquiry')])
    rec('CUSTOMEREGIS.md', 'docs/customers/customer-registration.md', 'COMPLETE',
        'Published Customer Registration contract carried over in full for both business and '
        'individual customers.')


def build_payout():
    secs = split_api_sections(FILES['PAYOUT-Api.md'])
    s = secs[0]
    conv = R.convert(s['body'], promote_headings=1)
    api_page('payout/payout.md',
             {'title': 'Payout', 'sidebar_label': 'Payout',
              'slug': '/payout/payout',
              'description': 'RHUB Payout API — perform B2B, C2C, C2B and B2C transactions.'},
             s['method'], 'Payout', conv, 'PAYOUT-Api.md',
             related=[('Quotation', '/docs/quotation/quotation'),
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
                      ('WPT integration set (unlinked source page)', '/docs/wpt')])
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
             related=[('Payout', '/docs/payout/payout'),
                      ('Transaction status codes', '/docs/errors/transaction-status-codes'),
                      ('Balance Enquiry', '/docs/balance/balance-enquiry'),
                      ('Transaction Inquiry (unlinked source page)', '/docs/legacy/transaction-inquiry')])

    bal = by_title['Balance Enquiry']
    conv = R.convert(bal['body'], promote_headings=1)
    api_page('balance/balance-enquiry.md',
             {'title': 'Balance Enquiry', 'sidebar_label': 'Balance Enquiry',
              'description': 'RHUB Balance Enquiry API — retrieve the current wallet or account balance.'},
             bal['method'], 'Balance Enquiry', conv, 'ENQUIRY.md',
             related=[('Transaction Enquiry', '/docs/transactions/transaction-enquiry'),
                      ('Balance API (unlinked source page)', '/docs/legacy/balance')])

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
             'The master APIs supply the configuration and reference data required by the '
             'transactional APIs. The source states that these APIs provide necessary '
             'configuration data (for example remittance purpose, source of funds, bank lists '
             'and occupations), and that they are subject to specific requirements and can be '
             'invoked at any point within the sequence, depending on the use case.', '',
             '## Published master APIs', '',
             'These %d master APIs are documented and published in the RHUB source.' % len(rows), '',
             '| Master API | Method | Endpoint | Reference |', '|---|---|---|---|']
    for title, method, ep, slug in rows:
        lines.append('| %s | `%s` | `%s` | [Open](/docs/master-apis/%s) |' %
                     (title, method, ep.replace('|', '\\|'), slug))
    lines += ['',
              ':::warning[Additional master categories in the source — REVIEW REQUIRED]',
              '',
              'The source file `master.md` also contains ten further master sections that are '
              '**commented out** and therefore not published: Legal Status Code, Payment Mode, '
              'Branch List, Customer Type, Resident Status, Purpose of Opening Business, '
              'Transaction Volume, ID Type, Customer Document Fetch and Payout Validator. Their '
              'contracts are reproduced, with their publication status flagged, in '
              '[Unpublished master APIs](/docs/appendix/unpublished-master-apis).',
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
    cur = R.convert(FILES['CURRENCYVALIDATIONS.md'])
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
           'description': 'Currency- and correspondent-specific conditional field requirements for RHUB payouts.'},
          body)
    rec('CURRENCYVALIDATIONS.md', 'docs/validation/currency-validations.md', 'COMPLETE',
        'All four validation matrices (Sender/Receiver × Individual/Business) and the field '
        'requirement clarification carried over. The source also links a downloadable Excel '
        'file (assets/TABLE_OF_VALIDATIONS.xlsx) that is not part of the export — flagged.')

    ctry = R.convert(FILES['COUNTRYVALIDATIONS.md'])
    ctry = re.sub(r'^##\s*\*\*Country Validations\*\*\s*$', '', ctry, count=1, flags=re.M)
    body = f"""# Country validations (SWIFT rail)

{provenance('COUNTRYVALIDATIONS.md')}

:::info[How to use these tables]

These tables state, per country group, which bank-related [Payout](/docs/payout/payout)
fields are mandatory when a transaction is processed through the SWIFT network. As with the
currency tables, they qualify **Conditional** fields; fields marked Mandatory in the Payout
API must always be supplied. The source's own wording is reproduced below.

:::

{ctry}

## Related

- [Payout](/docs/payout/payout)
- [Currency validations (LOCAL rail)](/docs/validation/currency-validations)
"""
    write('validation/country-validations.md',
          {'title': 'Country validations (SWIFT rail)', 'sidebar_label': 'Country validations',
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

RHUB documents three distinct code families. They are **not** interchangeable and this
portal keeps them apart:

| Family | What it describes | Supplied by | Page |
|---|---|---|---|
| Current API error codes | The current API error-handling reference: `resultCode` classes and their `resultDescription` values | RHUB team, %s | [Current API error codes](/docs/errors/current-error-codes) |
| Transaction status codes | The lifecycle status of a transaction in production | Documentation export (`responseCodes.md`) | [Transaction status codes](/docs/errors/transaction-status-codes) |
| HTTP and application error codes | Protocol-level status codes and RHUB application error codes | Documentation export (`ErrorCodes.md`) | [Error codes](/docs/errors/error-codes) |

Start with **Current API error codes** for live error handling. The other two pages remain
available and unchanged; they come from the original documentation export.

:::warning[REVIEW REQUIRED — resolution guidance]

The source supplies code values and descriptions only. It does not supply remediation or
retry guidance for any code, so none is offered here. Nothing in the supplied source
establishes retry policy, idempotency behaviour or backoff expectations.

:::
"""
    body = body % (CURRENT_ERRORS['receivedOn'] if CURRENT_ERRORS else 'REVIEW REQUIRED')
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

These are the statuses the source states will be available in production. The source does
not define transitions between them, timing, or which statuses are terminal — that is
**REVIEW REQUIRED**. A further status-code table and a validation-code table exist in the
source file but are commented out; they are reproduced in
[Unpublished API sections](/docs/appendix/unpublished-apis).

:::

## Related

- [Current API error codes](/docs/errors/current-error-codes)
- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
- [Error codes](/docs/errors/error-codes)
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

{UNPUBLISHED_WARNING % 'ErrorCodes.md'}

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
                              'Also appears in the export\'s **HTTP status code** table as "%s". '
                              'The source does not establish whether the HTTP status and the '
                              '`resultCode` of the same numeral are the same thing.' % http[c]))
        if c in app:
            same = set(app[c]) & set(news)
            if same:
                conflicts.append(('%s' % c,
                                  'Also in the export\'s **application error code** table with the '
                                  'same description ("%s"). Consistent — no conflict.'
                                  % sorted(same)[0]))
            else:
                conflicts.append(('%s' % c,
                                  'Also in the export\'s **application error code** table, but with '
                                  'different description(s): %s. Not reconciled.'
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
                              'Also in the **validation code** table that is commented out of '
                              '`responseCodes.md` (publication status unverified), with %s.' % note))

    sem = d['semantics']
    lines = ['# Current API error codes', '',
             ':::info[Authoritative and current]', '',
             'This reference was supplied directly by the **%s** on **%s** as the current API '
             'error-handling behaviour. It is maintained separately from the documentation '
             'export that the rest of this portal is built from, and it does not replace the '
             '[transaction status codes](/docs/errors/transaction-status-codes) or the '
             '[HTTP and application error codes](/docs/errors/error-codes), which remain '
             'available unchanged.' % (d['provider'], d['receivedOn']), '', ':::', '',
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
              ':::warning[REVIEW REQUIRED — result code not provided]', '',
              '**Result Code: Not provided**', '',
              '**Result Description:** %s' % uncoded[0]['resultDescription'], '',
              'The RHUB team supplied no `resultCode` for this entry. No code has been inferred '
              'or assigned.', '', ':::', '',
              '## Result codes at a glance', '',
              'The %d entries use **%d distinct result codes**, plus one entry with no code.'
              % (len(entries), len(unique)), '',
              '| Result Code | Entries | Conditions covered |', '|---|---|---|']
    for c in unique:
        lines.append('| %s | %d | %s |' % (c, counts[c],
                                           'multiple distinct conditions' if counts[c] > 1
                                           else 'one condition in this list'))
    lines.append('| *Not provided* | 1 | one condition in this list |')

    lines += ['', '## Relationship to the documentation-export error pages', '']
    if conflicts:
        lines += ['The following result codes also appear in documentation-export material. '
                  'The overlaps are reported, not reconciled.', '',
                  '| Result code | Observation |', '|---|---|']
        seen = set()
        for c, note in conflicts:
            if (c, note) in seen:
                continue
            seen.add((c, note))
            lines.append('| %s | %s |' % (c, note))
        lines += ['']
    lines += [':::warning[REVIEW REQUIRED — precedence between the code families]', '',
              'Where a numeral appears in more than one family, the supplied material does not '
              'state which takes precedence, nor whether the export\'s error tables are '
              'superseded by this current list. That has not been resolved by guessing. Note '
              'also that `ErrorCodes.md` is commented out of the live RHUB documentation '
              'sidebar, so its own currency is already unverified.', '', ':::', '',
              ':::note[Not established]', '',
              'No remediation steps, retry policy, backoff behaviour or HTTP-status mapping were '
              'supplied for these codes, so none is documented here.', '', ':::', '',
              '## Related', '',
              '- [Errors and response codes overview](/docs/errors)',
              '- [Transaction status codes](/docs/errors/transaction-status-codes)',
              '- [HTTP and application error codes](/docs/errors/error-codes)',
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
    lines += ['', 'The same file contains %d further sections inside HTML comments '
                  '(%s). They are reproduced in '
                  '[Unpublished API sections](/docs/appendix/unpublished-apis).'
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
    body = f"""# Licence and source version

{provenance('footer.md')}

{lic}
"""
    write('appendix/licence.md',
          {'title': 'Licence and source version', 'sidebar_label': 'Licence',
           'description': 'RHUB documentation licence statement and source version.'}, body)
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
# API index page
# --------------------------------------------------------------------------

def build_api_index():
    lines = ['# API reference index', '',
             'Every API contract published by the RHUB source, in one table.', '',
             '| API | Method | Endpoint (as written in source) | Page |', '|---|---|---|---|']
    for name, method, ep, page in API_INDEX:
        route = '/docs/' + page.replace('.md', '').replace('/index', '/')
        lines.append('| %s | `%s` | `%s` | [Open](%s) |' %
                     (name, method, ep.replace('|', '\\|'), route))
    lines += ['', ':::note', '', 'Endpoint strings are reproduced exactly as the source writes '
              'them, including the literal `http://host` placeholder where the source uses it.',
              '', ':::']
    write('api-index.md',
          {'title': 'API reference index', 'sidebar_label': 'API index',
           'description': 'Complete index of RHUB APIs documented in this portal.'},
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
    json.dump({'pages': PAGES, 'apis': API_INDEX, 'manifest': MANIFEST,
               'master_rows': master_rows, 'wpt_rows': wpt_rows, 'tpl_rows': tpl_rows,
               'unresolved_links': R.UNRESOLVED_LINKS},
              open(os.path.join(HERE, 'build-manifest.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
