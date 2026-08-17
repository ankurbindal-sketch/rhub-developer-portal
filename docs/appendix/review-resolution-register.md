---
title: "Review resolution register"
sidebar_label: "Review resolution register"
description: "Internal record of REVIEW REQUIRED issues and their dispositions."
unlisted: true
---

# Review resolution register

Internal record of every REVIEW REQUIRED issue raised during the build of RHUB Developer Portal 1.0, what resolved it, and how it is now presented. Nothing was removed without a disposition recorded here.

Baseline audit: 175 occurrences, 14 unique issues, 12 on client-facing pages.

| ID | Issue | Status |
|---|---|---|
| R1 | Access token transport | **RESOLVED** |
| R2 | scope inconsistency in Authentication | **RESOLVED** |
| R3 | Environment / base URL | **RESOLVED (Sandbox only)** |
| R4 | C2C requirement for sendClientTrxReference | **RESOLVED** |
| R5 | sendClientTrxReference vs sendClientTxnReference | **RESOLVED WITH CURRENT-BEHAVIOUR NOTE** |
| R6 | Wallet Not Found has no resultCode | **RESOLVED** |
| R7 | HTTP status vs resultCode overlap | **RESOLVED** |
| R8 | Transaction status lifecycle | **DEFERRED** |
| R9 | Bank and wallet payout flow diagrams | **ORIGINAL ASSET UNAVAILABLE / INTERNALLY RECORDED** |
| R10 | apiseq.png | **HIDDEN/LEGACY** |
| R11 | TABLE_OF_VALIDATIONS.xlsx | **HIDDEN/LEGACY** |
| R12 | Duplicate warning on the errors overview | **RESOLVED / CONSOLIDATED** |
| R13 | Publication-status warnings on unlisted pages | **HIDDEN/LEGACY** |
| R15 | Authentication request example sent `scope` | **RESOLVED** |
| R16 | Legacy HTTP/application error page in the client journey | **HIDDEN/LEGACY** |
| R17 | Example payload data | **RESOLVED** |
| R14 | Internal migration and audit warnings | **INTERNAL** |

## R1 — Access token transport

**Status:** RESOLVED

| | |
|---|---|
| Original page(s) | docs/authentication/authentication.md |
| Original wording | "The source does not describe how the access token is subsequently presented on other API calls... REVIEW REQUIRED." |
| Evidence / decision | RHUB decision D1 (2026-08-17). |
| Resolution | Subsequent calls carry `Authorization: Bearer <access_token>`. |
| Documentation change | Authentication page gained a "Using the access token" block; the convention is also documented centrally under "Authorising requests" in the conventions page. |
| Final public treatment | Client-facing INFO note on Authentication + central conventions section. |

## R2 — scope inconsistency in Authentication

**Status:** RESOLVED

| | |
|---|---|
| Original page(s) | docs/authentication/authentication.md |
| Original wording | No rendered marker; found during audit. Request table omitted `scope` (row commented out in source), request example sent `scope=read%20write`, response table lists `scope` as M. |
| Evidence / decision | RHUB decision D3 (2026-08-17). |
| Resolution | `scope` is a response field. Clients need not send it on the token request. |
| Documentation change | Note added stating scope is returned, not required on the request. The source request example is reproduced unchanged. |
| Final public treatment | Client-facing NOTE on Authentication. |

## R3 — Environment / base URL

**Status:** RESOLVED (Sandbox only)

| | |
|---|---|
| Original page(s) | docs/getting-started/conventions.md (prose list) |
| Original wording | No rendered marker; endpoints written `http://host/...` with no base URL established. |
| Evidence / decision | RHUB decision D2 (2026-08-17). |
| Resolution | Sandbox base URL is `https://sandbox-client.remittanceshub.com:8030`. No UAT or production URL confirmed. |
| Documentation change | Conventions page gained an Environments table and an explanation that `host` stands for the environment base URL, with a worked Sandbox example. Endpoint paths unchanged. |
| Final public treatment | Client-facing documentation section. |

## R4 — C2C requirement for sendClientTrxReference

**Status:** RESOLVED

| | |
|---|---|
| Original page(s) | docs/payout/payout.md |
| Original wording | "REVIEW REQUIRED — C2C value for `sendClientTrxReference`. The contract marks the field Mandatory while the invoice requirement excludes C2C." |
| Evidence / decision | RHUB decision D6 (2026-08-17). |
| Resolution | Required for B2B, B2C and C2B. For C2C it may be omitted or sent blank. |
| Documentation change | Warning replaced with a conditional-requirement INFO block. The transactionInfo field table still shows the original `M` flag, and the block states which rule to follow. |
| Final public treatment | Client-facing CONDITIONAL REQUIREMENT on Payout. |

## R5 — sendClientTrxReference vs sendClientTxnReference

**Status:** RESOLVED WITH CURRENT-BEHAVIOUR NOTE

| | |
|---|---|
| Original page(s) | docs/payout/payout.md, docs/errors/current-error-codes.md |
| Original wording | "Both spellings are reproduced exactly as RHUB supplied them; which one the API accepts is REVIEW REQUIRED." |
| Evidence / decision | RHUB decisions D4 and D5 (2026-08-17). |
| Resolution | The request field is `sendClientTrxReference`. Some current validation messages say `sendClientTxnReference`; that is what the system returns today, pending a separate backend correction. |
| Documentation change | Payout note states the field name and warns that validation messages may differ. Error code descriptions are reproduced unchanged. |
| Final public treatment | Client-facing NOTE on Payout. |

## R6 — Wallet Not Found has no resultCode

**Status:** RESOLVED

| | |
|---|---|
| Original page(s) | docs/errors/current-error-codes.md |
| Original wording | "REVIEW REQUIRED — result code not provided." |
| Evidence / decision | RHUB decision D7 (2026-08-17). |
| Resolution | Known current API behaviour; no code is to be invented. |
| Documentation change | Warning became a NOTE describing it as current behaviour, advising clients to handle it on `resultDescription`. Table still shows "Not provided". |
| Final public treatment | Client-facing NOTE. |

## R7 — HTTP status vs resultCode overlap

**Status:** RESOLVED

| | |
|---|---|
| Original page(s) | docs/errors/current-error-codes.md, docs/errors/index.md |
| Original wording | "REVIEW REQUIRED — precedence between the code families." |
| Evidence / decision | RHUB decision D8 (2026-08-17). |
| Resolution | Separate namespaces; a shared numeral is not a conflict. |
| Documentation change | Warning replaced with an INFO block explaining the three concepts. The overlap table is now framed as reference, not a conflict register. |
| Final public treatment | Client-facing INFO on the error pages. |

## R8 — Transaction status lifecycle

**Status:** DEFERRED

| | |
|---|---|
| Original page(s) | docs/errors/transaction-status-codes.md |
| Original wording | "Transitions between them, their timing, and which statuses are terminal are not established — that is REVIEW REQUIRED." |
| Evidence / decision | RHUB decision D9 (2026-08-17). |
| Resolution | Not published in Developer Portal 1.0. This is a scope decision, not a resolved lifecycle. No transitions, ordering, timing or terminality have been inferred. |
| Documentation change | Scope note now states values and meanings are documented and lifecycle is out of scope. |
| Final public treatment | Client-facing NOTE. |

## R9 — Bank and wallet payout flow diagrams

**Status:** ORIGINAL ASSET UNAVAILABLE / INTERNALLY RECORDED

| | |
|---|---|
| Original page(s) | docs/getting-started/transaction-flows.md |
| Original wording | "REVIEW REQUIRED — diagram not available" (twice). |
| Evidence / decision | RHUB decision D10 (2026-08-17). Binary assets `img/rhubbpt2.png` and `img/rhubwpt2.png` are absent from the repository and are not exposed by the current RHUB site. |
| Resolution | The originals will not be reconstructed. The surviving prose describes both flows in RHUB's own words and is useful without the images. |
| Documentation change | Production warnings removed from the client-facing page; the prose was retained and a pointer to the integration flow added. The missing assets remain recorded here and in the source coverage notes. |
| Final public treatment | No client-facing warning. Asset gap recorded internally. |

## R10 — apiseq.png

**Status:** HIDDEN/LEGACY

| | |
|---|---|
| Original page(s) | none (never rendered) |
| Original wording | Referenced inside a commented-out block of `apisequence.md`. |
| Evidence / decision | Mechanical inspection of the export: the reference is commented out by RHUB. |
| Resolution | Never published by RHUB. |
| Documentation change | No change. Not exposed. |
| Final public treatment | Not client-facing. |

## R11 — TABLE_OF_VALIDATIONS.xlsx

**Status:** HIDDEN/LEGACY

| | |
|---|---|
| Original page(s) | none (never rendered) |
| Original wording | Referenced inside a commented-out block of `CURRENCYVALIDATIONS.md`. |
| Evidence / decision | Mechanical inspection of the export: the reference is commented out by RHUB. |
| Resolution | Never published by RHUB. |
| Documentation change | No change. Not exposed. |
| Final public treatment | Not client-facing. |

## R12 — Duplicate warning on the errors overview

**Status:** RESOLVED / CONSOLIDATED

| | |
|---|---|
| Original page(s) | docs/errors/index.md |
| Original wording | "REVIEW REQUIRED — resolution guidance." |
| Evidence / decision | The same fact is documented on the current error codes page. |
| Resolution | Duplicate. Consolidated. |
| Documentation change | Overview warning became a NOTE that also explains the two code families; the no-remediation fact remains on the error code page. |
| Final public treatment | Client-facing NOTE. |

## R13 — Publication-status warnings on unlisted pages

**Status:** HIDDEN/LEGACY

| | |
|---|---|
| Original page(s) | docs/legacy/*, docs/template-management/*, docs/wpt/* |
| Original wording | "REVIEW REQUIRED — publication status" and similar. |
| Evidence / decision | These pages derive from source files RHUB commented out of its live sidebar. |
| Resolution | They stay out of client navigation. Their warnings are correct in context. |
| Documentation change | No change. Pages remain `unlisted: true`: absent from sidebar, API index, search and sitemap, and reachable only by direct URL. |
| Final public treatment | Not client-facing. |

## R15 — Authentication request example sent `scope`

**Status:** RESOLVED

| | |
|---|---|
| Original page(s) | docs/authentication/authentication.md |
| Original wording | No marker. The public request example carried `scope=read%20write` although D3 states scope is a response field. |
| Evidence / decision | RHUB decision D3. |
| Resolution | The client-facing request example now sends `grant_type`, `username` and `password` only. `scope` remains in the response example and response table. |
| Documentation change | Public example corrected at generation time. The original example is preserved unchanged in source/RHUB_FULL_SOURCE_EXPORT.json. |
| Final public treatment | Client-facing example, corrected. |

## R16 — Legacy HTTP/application error page in the client journey

**Status:** HIDDEN/LEGACY

| | |
|---|---|
| Original page(s) | docs/errors/error-codes.md |
| Original wording | No marker. The page derives from the older documentation export and competed with the current resultCode reference. |
| Evidence / decision | Client-readiness decision: the public error model is resultCode + resultDescription, plus transaction status values. |
| Resolution | The page is now unlisted: out of the sidebar, errors overview, related links, search and sitemap. Its content is unchanged and reachable by direct URL. |
| Documentation change | Errors overview rewritten around two families; the migration-era comparison section was removed from the current error codes page. |
| Final public treatment | Not client-facing. |

## R17 — Example payload data

**Status:** RESOLVED

| | |
|---|---|
| Original page(s) | all client-facing pages with examples |
| Original wording | No marker. Examples carried real-looking names, companies, emails and account numbers. |
| Evidence / decision | Client-readiness decision; convention recorded in source/RHUB_EXAMPLE_DATA_POLICY.json. |
| Resolution | Synthetic identities (John/Jane Doe, Example Trading Ltd, example.com, REF/INV/CUS references) applied to code blocks and field-table sample values on listed pages, preserving type, length and format. |
| Documentation change | Sanitisation runs at generation time; unlisted audit pages keep the original values. |
| Final public treatment | Client-facing examples, sanitised. |

## R14 — Internal migration and audit warnings

**Status:** INTERNAL

| | |
|---|---|
| Original page(s) | docs/appendix/*, tools/, COMPLETENESS_REPORT.md |
| Original wording | Audit trail wording: coverage tables, publication status, commented-source accounting. |
| Evidence / decision | Internal traceability for the documentation build. |
| Resolution | Retained internally; no client-facing exposure. |
| Documentation change | No change to the evidence. Client-facing pages were scanned for migration language. |
| Final public treatment | Not client-facing. |

## RHUB decisions applied

Supplied by RHUB team on 2026-08-17 and stored in `source/RHUB_INTEGRATION_GUIDANCE.json` so they stay separable from the original documentation export.

| ID | Decision | Resolves |
|---|---|---|
| D1 | Subsequent API calls carry the access token in the Authorization header as `Authorization: Bearer <access_token>`. | R1 |
| D2 | Sandbox is the only environment RHUB has confirmed. No UAT or production base URL is established. Endpoint paths written as http://host/... in the contracts use `host` as a placeholder for the environment base URL. | R3 |
| D3 | `scope` belongs to the Authentication response. Clients do not need to send it on the token request, even though the historical request example includes scope=read%20write. | R2 |
| D4 | The Payout request field is `sendClientTrxReference`. This spelling is the contract. | R5 |
| D5 | Some current validation messages refer to the field as `sendClientTxnReference`. That is the wording the system returns today and is reproduced unchanged. A backend correction is planned separately. | R5 |
| D6 | For C2C payouts `sendClientTrxReference` is not required: it may be omitted or sent blank. For B2B, B2C and C2B invoice documentation is mandatory and the field carries the invoice reference. | R4 |
| D7 | The 'Wallet Not Found' entry has no resultCode. This is known current API behaviour, published as 'Not provided'. | R6 |
| D8 | HTTP status codes and RHUB resultCode values are separate namespaces. The same numeral may appear in both; that is not a conflict. resultCode is an error category, not a unique key per validation condition; resultDescription carries the specific reason. | R7 |
| D9 | RHUB is not publishing a formal transaction-status transition lifecycle in Developer Portal 1.0. Status values and meanings are documented; transitions, timing and terminality are deliberately out of scope. | R8 |
| D10 | The original bank and wallet payout flow images are unavailable and will not be reconstructed. New Developer Portal visuals may be created only for flows established by authoritative material, and must not be presented as the missing originals. | R9 |
