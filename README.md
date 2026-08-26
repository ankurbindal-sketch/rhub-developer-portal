# RHUB Developer Portal 1.0

A production-ready [Docusaurus 3](https://docusaurus.io/) documentation site for the **RHUB
(RemittancesHub)** cross-border remittance APIs.

Live URL once Pages is enabled:
`https://ankurbindal-sketch.github.io/rhub-developer-portal/`

---

## What this repository is

The portal is a **re-presentation** of the authoritative RHUB technical documentation, rebuilt
around the integration journey (authentication → quotation → payout → transaction enquiry) with
search, breadcrumbs, previous/next navigation, syntax-highlighted copyable examples and
responsive API tables.

It is not a rewrite. The rules the content follows:

- Every endpoint, HTTP method, header, field name, type, length, requirement flag (M / O / C),
  validation rule, transaction status, error code and example comes from the authoritative RHUB
  source export. Nothing is inferred from general REST conventions.
- The source distinction between **Mandatory**, **Conditional** and **Optional** is preserved;
  conditional fields are never promoted to mandatory.
- Where the source does not establish something, the page says **REVIEW REQUIRED** rather than
  filling the gap. Rate limits, idempotency, retry semantics, webhooks, SDKs, pagination, token
  refresh behaviour and SLAs are absent from the source and therefore absent here.
- Conflicts and ambiguities between source files are reported, not resolved. See
  `docs/appendix/source-notes.md`.
- No RHUB brand assets are bundled: the source export contains no logo, icon or diagram binaries,
  so the site uses a typographic wordmark and flags the missing images.

## Requirements

- Node.js 18 or newer (CI uses Node 20)
- npm

## Local development

```bash
npm install
npm start          # dev server on http://localhost:3000/rhub-developer-portal/
```

## Spell check

Editorial text is checked with [codespell](https://github.com/codespell-project/codespell).
`.codespellrc` holds the configuration, including an allow-list for RHUB's own vocabulary —
field names and response values such as `recieverCode` and `Comission Wallet` are reproduced
exactly as the API has them and must not be "corrected".

```bash
pip install codespell
codespell            # reads .codespellrc; exits non-zero on a hit
```

`.github/workflows/spellcheck.yml` runs the same command on every push and pull request. It
is independent of the Pages deployment workflow, so a spelling hit never blocks a deploy.

## Production build

```bash
npm run build      # outputs to ./build
npm run serve      # preview the production build locally
```

The build runs Docusaurus' broken-link and MDX checks with `onBrokenLinks: 'throw'` and
`markdown.hooks.onBrokenMarkdownLinks: 'throw'`, so a green build means no broken internal links
and no MDX errors.

## Deployment

`.github/workflows/deploy.yml` builds the site and publishes it with the official GitHub Pages
actions on every push to `main`. To activate it:

1. In the repository, open **Settings → Pages**.
2. Set **Source** to **GitHub Actions**.
3. Push to `main` (or run the workflow manually via **Actions → Deploy RHUB Developer Portal to
   GitHub Pages → Run workflow**).

If the repository name or owner changes, update `url`, `baseUrl`, `organizationName` and
`projectName` in `docusaurus.config.js` to match.

## Project layout

```
docs/                        Documentation pages (generated from the source export)
  intro.md                   Portal overview
  getting-started/           Integration flow, transaction flows, reading conventions
  authentication/            Authentication API
  quotation/                 Quotation API
  payout/                    Payout API, WPT Payout API
  transactions/              Transaction Enquiry API
  balance/                   Balance Enquiry API
  customers/                 Customer Registration API
  documents/                 Document Upload API
  master-apis/               Overview + 14 published master APIs
  validation/                Currency (LOCAL rail) and country (SWIFT rail) requirements
  errors/                    Transaction status codes; HTTP and application error codes
  wpt/                       WPT integration set
  template-management/       Service fee, transaction limit, forex margin APIs
  legacy/                    Source pages served but not linked in the live RHUB sidebar
  appendix/                  Source coverage notes, unpublished sections, licence
  api-index.md               Every documented API in one table
src/pages/index.js           Landing page
src/css/custom.css           Theme (design tokens, method badges, API tables)
sidebars.js                  Explicit navigation hierarchy
docusaurus.config.js         Site configuration
.github/workflows/deploy.yml GitHub Pages deployment
```

## Regenerating the documentation

The pages under `docs/` are produced from the source export by two scripts kept in `tools/`:

```bash
python3 tools/generate.py     # rewrites docs/ from RHUB_FULL_SOURCE_EXPORT.json
```

- `tools/rhubconv.py` — converts the legacy docsify Markdown/HTML into MDX-safe Markdown:
  HTML tables become Markdown tables, "tap to open" widgets become fenced code blocks,
  "About the API / Request URL / Request Method" tables become endpoint callouts, and source
  cross-links are remapped to portal routes. Only presentation changes.
- `tools/generate.py` — assembles the information architecture, the API index, the appendices and
  the source coverage audit trail.

`tools/generate.py` expects the source export at the path set in its `SRC_JSON` constant. Point it
at your copy of `RHUB_FULL_SOURCE_EXPORT.json` before running.

Regenerating is the supported way to update content: editing `docs/` by hand will be overwritten
on the next run, and hand edits bypass the source-fidelity rules above.

## Licence

RemittancesHub holds the entire intellectual property rights of this documentation. See
`docs/appendix/licence.md` for the published statement, and `docs/appendix/source-notes.md`
for the internal provenance record.
