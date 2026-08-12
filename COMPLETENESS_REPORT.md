# RHUB Developer Portal 1.0 — Completeness Report

**Build date:** 12 August 2026
**Source of truth:** `RHUB_FULL_SOURCE_EXPORT.json` — 29 Markdown files fetched from
`https://docs.remittanceshub.com/`, exported 2026-08-12T15:28:20Z, 685,293 characters, 0 fetch
failures, 0 empty files.
**Secondary cross-check:** `RHUB_Documentation.txt` (13 of 29 files, 8 of those truncated at
~4,975 characters) — used for spot-checks only, never for completeness.
**Technology:** Docusaurus 3.10.2, Node 22 (CI pinned to Node 20).

---

## 1. Headline numbers

| Metric | Value |
|---|---|
| Source Markdown files | 29 |
| Source files accounted for in the portal | 29 / 29 (100%) |
| Portal documentation pages | 60 |
| Static HTML pages produced by the build | 63 |
| API contracts documented | 31 |
| Master APIs documented (published) | 14 |
| Master API sections reproduced from disabled source | 10 |
| Template-management APIs documented | 6 |
| WPT-set APIs documented (active in source file) | 3 |
| REVIEW REQUIRED markers | 104, across 34 pages |
| Production build | **PASS** |
| Broken internal links | **0** (`onBrokenLinks: 'throw'`) |
| MDX / Markdown link errors | **0** (`markdown.hooks.onBrokenMarkdownLinks: 'throw'`) |
| Sidebar / duplicate-route errors | **0** (`onDuplicateRoutes: 'throw'`) |
| Ragged or headerless Markdown tables remaining | **0** of 164 tables |
| Fabricated endpoints, fields, examples or error codes | **0** |
| GitHub push | **NOT DONE** — no credentials available (see §7) |
| GitHub Pages deployment | **NOT DONE** — depends on the push (see §7) |

---

## 2. Source file → portal location map

Status values: **COMPLETE** (all source content migrated, page is live documentation),
**PARTIAL** (all content migrated, but the source file is commented out of the live RHUB sidebar
so its publication status is unverified), **REVIEW REQUIRED** (content migrated but an
irreplaceable source element — here, diagram binaries — is missing from the export).

| Source File | Portal Location | Status | Notes |
|---|---|---|---|
| `README.md` | `docs/intro.md` | COMPLETE | About Us and Overview carried over verbatim. |
| `apisequence.md` | `docs/getting-started/integration-flow.md` | COMPLETE | Sequence list and all cross-references remapped to portal routes. Source's own diagram reference is commented out in the source. |
| `transactionflow.md` | `docs/getting-started/transaction-flows.md` | REVIEW REQUIRED | Narrative complete. Both flow diagrams (`img/rhubbpt2.png`, `img/rhubwpt2.png`) are referenced by the source but absent from the export; flagged on the page, not recreated. |
| `AUTH.md` | `docs/authentication/authentication.md` | COMPLETE | Request, header and response parameters plus both examples. |
| `QUOTA.md` | `docs/quotation/quotation.md` | COMPLETE | Published Quotation contract in full; commented-out Final Quotation section routed to the appendix. |
| `CUSTOMEREGIS.md` | `docs/customers/customer-registration.md` | COMPLETE | Business and individual customer contracts in full. |
| `DocumentUpload.md` | `docs/documents/document-upload.md` | COMPLETE | Full contract and examples. |
| `PAYOUT-Api.md` | `docs/payout/payout.md` | COMPLETE | `transactionInfo`, `sender`, `receiver`, `compliance` objects, registered-customer variant, response parameters, examples. |
| `PAYOUT-WPT.md` | `docs/payout/wpt-payout.md` | COMPLETE | Full WPT payout contract. |
| `ENQUIRY.md` | `docs/transactions/transaction-enquiry.md`, `docs/balance/balance-enquiry.md` | COMPLETE | Both published sections; commented-out Customer Enquiry routed to the appendix. |
| `master.md` | `docs/master-apis/` (index + 14 pages), `docs/appendix/unpublished-master-apis.md` | COMPLETE | 14 published master APIs documented individually; 10 commented-out master sections reproduced and flagged. |
| `CURRENCYVALIDATIONS.md` | `docs/validation/currency-validations.md` | COMPLETE | All four matrices (Sender/Receiver × Individual/Business) and the field-requirement clarification. |
| `COUNTRYVALIDATIONS.md` | `docs/validation/country-validations.md` | COMPLETE | All eight SWIFT country groups, country lists, field explanations and matrices. |
| `responseCodes.md` | `docs/errors/transaction-status-codes.md` | COMPLETE | Published production status table verbatim; three commented tables routed to the appendix. |
| `footer.md` | `docs/appendix/licence.md` | COMPLETE | IP statement and source version (2.3.0). |
| `ErrorCodes.md` | `docs/errors/error-codes.md` | PARTIAL | Both tables (HTTP status codes, application error codes) in full. PARTIAL because the file is commented out of the live sidebar and the source gives no resolution guidance. |
| `template.md` | `docs/template-management/` (index + 6 pages) | PARTIAL | All six APIs in full: Service Fee, Update Service Fee, Transaction List, Update Transaction Limit, Forex Margin, Update Forex Margin. Unlinked in the live sidebar. |
| `WPT.md` | `docs/wpt/` (index + 3 pages), `docs/appendix/unpublished-apis.md` | PARTIAL | 3 active sections (Customer Registration, Quotation, Payout) in full; 6 commented sections reproduced in the appendix. Unlinked in the live sidebar. |
| `loginauthentication.md` | `docs/legacy/login-authentication.md` | PARTIAL | Full content. Unlinked source page; differs from `AUTH.md` (see §5). |
| `customerRegistration.md` | `docs/legacy/customer-registration.md` | PARTIAL | Full content. Unlinked source page. |
| `customerInquiry.md` | `docs/legacy/customer-inquiry.md` | PARTIAL | Full content. Unlinked source page. |
| `updateCustomerDetails.md` | `docs/legacy/update-customer-details.md` | PARTIAL | Full content. Unlinked source page. |
| `ownerDetails.md` | `docs/legacy/owner-details.md` | PARTIAL | Full content. Unlinked source page. |
| `quotation.md` | `docs/legacy/quotation.md` | PARTIAL | Full content. Unlinked source page. |
| `finalQuotation.md` | `docs/legacy/final-quotation.md` | PARTIAL | Full content. Unlinked source page; the only complete Final Quotation contract in the source. |
| `payout.md` | `docs/legacy/payout.md` | PARTIAL | Full content. Unlinked source page. |
| `transactionInquiry.md` | `docs/legacy/transaction-inquiry.md` | PARTIAL | Full content. Unlinked source page. |
| `balance.md` | `docs/legacy/balance.md` | PARTIAL | Full content (all-currency and single-currency variants). Unlinked source page. |
| `payoutValidator.md` | `docs/legacy/reference-payout-validator.md` | PARTIAL | Full content. Unlinked source page; the only complete Payout Validator contract outside the commented `master.md` section. |

**Totals:** COMPLETE 14 · PARTIAL 14 · REVIEW REQUIRED 1 · omitted 0.

---

## 3. APIs documented (31)

| Group | APIs |
|---|---|
| Authentication | Authentication |
| Quotation | Quotation |
| Payout | Payout, WPT Payout |
| Transactions | Transaction Enquiry |
| Balance | Balance Enquiry |
| Customers | Customer Registration |
| Documents | Document Upload |
| Master (14) | Remittance Purpose, Source of Fund, Relationship, Document ID Type, Occupation, Business Type, Business Registration Type, Account Type, WPT Wallet List, Bank List, Customer Legal Status, Nature of Business, Customer Occupation Type, Customer/Individual Document Type |
| Template management (6) | Service Fee, Update Service Fee, Transaction List, Update Transaction Limit, Forex Margin, Update Forex Margin |
| WPT set (3) | WPT Customer Registration, WPT Quotation, WPT Payout |

Eleven further contracts from unlinked source pages are documented under `docs/legacy/`, and 17
commented-out source sections are reproduced in the appendix, each flagged REVIEW REQUIRED.

---

## 4. Key structural finding

The export's own sidebar shows that **only 14 of the 29 source files are linked from the live RHUB
documentation**; the other 15 are served but their sidebar entries are commented out. Large
portions of individual files are likewise HTML-commented: 52% of `master.md`, 64% of `WPT.md`, 85%
of `responseCodes.md`, 55% of `QUOTA.md`, 35% of `CUSTOMEREGIS.md`.

The portal treats commented content as **not published** rather than current. It is reproduced in
clearly-warned appendix pages so nothing is lost, and never presented as a live contract. Every
file's commented-character count is tabulated in `docs/appendix/source-notes.md`.

---

## 5. Unresolved source gaps (all surfaced in the portal, none filled in)

**Conflicting duplicate contracts.** Six capabilities are described twice — once in a linked file,
once in an unlinked one — and the versions differ. The portal reports the differences (endpoints
present in each file, field names unique to each) and resolves nothing:

| Capability | Linked source | Unlinked source |
|---|---|---|
| Authentication | `AUTH.md` (`http://host/...`) | `loginauthentication.md` (`https://sandbox-client.remittanceshub.com:8030/...`, different response fields) |
| Quotation | `QUOTA.md` | `quotation.md` |
| Payout | `PAYOUT-Api.md` | `payout.md` |
| Transaction enquiry | `ENQUIRY.md` | `transactionInquiry.md` |
| Balance | `ENQUIRY.md` | `balance.md` |
| Customer registration | `CUSTOMEREGIS.md` | `customerRegistration.md` |

**Missing binary assets** (referenced by the source, absent from the export, not recreated):
`img/rhub.png`, `img/apiseq.png`, `img/rhubbpt2.png`, `img/rhubwpt2.png`,
`assets/TABLE_OF_VALIDATIONS.xlsx`.

**Unresolvable source cross-link:** 1 — `#/master?id=get-customer-document-type` has no matching
published section in the source; redirected to the Master APIs index and logged rather than guessed.

**Source table defect preserved:** `QUOTA.md`'s `responseTime` row carries a stray extra cell,
leaving Data Type and Requirement blank. The description was preserved rather than dropped; the
blanks were not filled in.

**Topics the source never establishes** (absent from the portal by design, listed on
`docs/getting-started/conventions.md` and `docs/appendix/source-notes.md`): rate limits,
idempotency, retry policy and backoff, webhooks, SDKs, pagination, environment base URLs (most
source endpoints use the literal placeholder `http://host`), how the access token is presented on
subsequent calls, token refresh, error-code resolution guidance, SLA claims, and transaction status
transition rules.

---

## 6. Validation results

| Check | Result |
|---|---|
| Production build (`npm run build`) | PASS — "Generated static files in build" |
| Broken internal links | 0 |
| MDX / Markdown errors | 0 |
| Sidebar doc-ID errors | 0 |
| Duplicate routes | 0 |
| Config deprecation warnings | 0 (migrated to `markdown.hooks`) |
| All 29 source files represented | Yes |
| Every source API section represented | Yes — 31 published + 11 unlinked + 17 commented, none omitted |
| Leftover raw HTML in generated pages | 0 occurrences |
| Table integrity | 164 tables, 0 ragged, 0 headerless |
| Search | Offline index built (`search-index.json`, 1.4 MB) via `@easyops-cn/docusaurus-search-local` |
| Breadcrumbs | Present on doc pages |
| Previous/next navigation | Present on doc pages |
| Syntax highlighting | Prism, with `json`, `http`, `bash`, `java`, `csharp` |
| Copy-to-clipboard | Docusaurus theme default (hydrates client-side on every code block) |
| Responsive layout | Doc tables scroll horizontally below 997 px; the landing-page sequence rail switches from horizontal to vertical; reduced-motion respected |
| Fabricated content scan | 0 invented endpoints, methods, fields, types, lengths, requirement flags, error codes or examples |

---

## 7. GitHub status — push not performed

**Target repository:** `https://github.com/ankurbindal-sketch/rhub-developer-portal`

| Step | Result |
|---|---|
| Repository reachable | Yes — `git ls-remote` succeeded; remote `main` exists at commit `23e4cd170b57e160d4fef526145730ac68fe7296` |
| Local repository initialised and committed | Yes — branch `main`, commit `a826e34`, 74 files |
| Push | **FAILED** |
| Exact error | `fatal: could not read Username for 'https://github.com': No such device or address` |
| Cause | No GitHub credentials are available in this environment: no token in the environment, no credential helper, no SSH key, and no interactive terminal to prompt for one. `curl https://api.github.com/repos/...` returns HTTP 403 (unauthenticated rate-limited). |
| GitHub Pages deployment | **NOT PERFORMED** — it is triggered by a push to `main`, which did not happen. |

**Note on history:** the remote already has a `main` branch whose commit is unrelated to this local
history, so a plain `git push` would be rejected as non-fast-forward even with credentials.

### To publish it yourself

Option A — apply the bundle to a clone:

```bash
git clone https://github.com/ankurbindal-sketch/rhub-developer-portal.git
cd rhub-developer-portal
git fetch ../rhub-developer-portal.bundle main:portal-1.0
git checkout portal-1.0            # inspect, then merge into main or push as a branch
git push origin portal-1.0         # open a PR, or: git push -f origin portal-1.0:main
```

Option B — copy the tree into your clone:

```bash
tar -xzf rhub-developer-portal.tar.gz -C /path/to/your/clone
cd /path/to/your/clone
npm install && npm run build       # confirm the build passes locally
git add -A && git commit -m "RHUB Developer Portal 1.0" && git push
```

Then enable Pages: **Settings → Pages → Source: GitHub Actions**. The included workflow
(`.github/workflows/deploy.yml`) builds and deploys on every push to `main`. The site will serve at
`https://ankurbindal-sketch.github.io/rhub-developer-portal/`; if the repository name or owner
changes, update `url`, `baseUrl`, `organizationName` and `projectName` in `docusaurus.config.js`.

---

## 8. Completeness statement

100% of the information available in the authoritative RHUB source export has been migrated into
the portal: all 29 files, all published API contracts, all field tables with source field names,
types, lengths and requirement flags intact, all source examples, all validation matrices, and all
status and error codes.

The 104 REVIEW REQUIRED markers are not gaps in the migration. Each one records a point where the
**source itself** does not establish something — a missing diagram, an unlinked page of unverified
currency, a source cross-link with no target, a conflict between two source files, or a topic the
source never covers. Removing them would require inventing RHUB technical facts, which the project
rules prohibit.
