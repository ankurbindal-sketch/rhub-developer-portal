---
title: "Source coverage notes"
sidebar_label: "Source coverage notes"
description: "Audit trail: source integrity, publication status, conflicts, gaps and the source-to-page map."
unlisted: true
---

# Source coverage notes

This page is the audit trail for RHUB Developer Portal 1.0: what the source contains, where each file landed, and every point at which the source does not establish something.

## Export integrity

| Check | Result |
|---|---|
| Source | `https://docs.remittanceshub.com/` |
| Exported at | 2026-08-12T15:28:20.509Z |
| Markdown files in export | 29 |
| Fetch failures | 0 (all 29 files returned HTTP 200) |
| Empty source files | 0 |
| Total source characters | 685293 |

## Supplemental authoritative sources

Material supplied directly by the RHUB team, outside the documentation export, is kept in its own data file so it can be updated independently and republished by re-running the generator.

| Supplemental source | Supplied by | Received | Portal page |
|---|---|---|---|
| `source/RHUB_CURRENT_ERROR_CODES.json` | RHUB team | 2026-08-12 | [Current API error codes](/docs/errors/current-error-codes) |

## Publication status in the source sidebar

The export includes the site sidebar. Fourteen files are linked from it; the other fifteen are served but their sidebar entries are commented out. This portal reproduces all 29 and labels the difference rather than assuming one.

| Source file | Linked in live sidebar |
|---|---|
| `AUTH.md` | Yes |
| `COUNTRYVALIDATIONS.md` | Yes |
| `CURRENCYVALIDATIONS.md` | Yes |
| `CUSTOMEREGIS.md` | Yes |
| `DocumentUpload.md` | Yes |
| `ENQUIRY.md` | Yes |
| `ErrorCodes.md` | No — REVIEW REQUIRED |
| `PAYOUT-Api.md` | Yes |
| `PAYOUT-WPT.md` | Yes |
| `QUOTA.md` | Yes |
| `README.md` | Yes |
| `WPT.md` | No — REVIEW REQUIRED |
| `apisequence.md` | Yes |
| `balance.md` | No — REVIEW REQUIRED |
| `customerInquiry.md` | No — REVIEW REQUIRED |
| `customerRegistration.md` | No — REVIEW REQUIRED |
| `finalQuotation.md` | No — REVIEW REQUIRED |
| `footer.md` | Yes |
| `loginauthentication.md` | No — REVIEW REQUIRED |
| `master.md` | Yes |
| `ownerDetails.md` | No — REVIEW REQUIRED |
| `payout.md` | No — REVIEW REQUIRED |
| `payoutValidator.md` | No — REVIEW REQUIRED |
| `quotation.md` | No — REVIEW REQUIRED |
| `responseCodes.md` | Yes |
| `template.md` | No — REVIEW REQUIRED |
| `transactionInquiry.md` | No — REVIEW REQUIRED |
| `transactionflow.md` | No — REVIEW REQUIRED |
| `updateCustomerDetails.md` | No — REVIEW REQUIRED |

## Commented-out source content

HTML-commented blocks are not live documentation, so they are not rendered as such. Substantive commented API contracts are reproduced in [Unpublished master APIs](/docs/appendix/unpublished-master-apis) and [Unpublished API sections](/docs/appendix/unpublished-apis). The table shows how much of each source file is commented out.

| Source file | Characters | Commented characters | Commented blocks |
|---|---|---|---|
| `AUTH.md` | 4588 | 1191 (26%) | 6 |
| `COUNTRYVALIDATIONS.md` | 26252 | 1150 (4%) | 5 |
| `CURRENCYVALIDATIONS.md` | 29848 | 3242 (11%) | 27 |
| `CUSTOMEREGIS.md` | 44230 | 15679 (35%) | 8 |
| `DocumentUpload.md` | 7929 | 609 (8%) | 3 |
| `ENQUIRY.md` | 35619 | 9294 (26%) | 18 |
| `ErrorCodes.md` | 18558 | 1889 (10%) | 8 |
| `PAYOUT-Api.md` | 65228 | 13274 (20%) | 48 |
| `PAYOUT-WPT.md` | 42152 | 10484 (25%) | 22 |
| `QUOTA.md` | 20772 | 11463 (55%) | 6 |
| `README.md` | 948 | 0 (0%) | 0 |
| `WPT.md` | 90074 | 57924 (64%) | 21 |
| `apisequence.md` | 1850 | 110 (6%) | 2 |
| `balance.md` | 6084 | 126 (2%) | 2 |
| `customerInquiry.md` | 1852 | 51 (3%) | 1 |
| `customerRegistration.md` | 5271 | 0 (0%) | 0 |
| `finalQuotation.md` | 8488 | 0 (0%) | 0 |
| `footer.md` | 422 | 0 (0%) | 0 |
| `loginauthentication.md` | 3075 | 114 (4%) | 1 |
| `master.md` | 161815 | 84289 (52%) | 70 |
| `ownerDetails.md` | 3352 | 0 (0%) | 0 |
| `payout.md` | 25830 | 70 (0%) | 1 |
| `payoutValidator.md` | 6493 | 225 (3%) | 2 |
| `quotation.md` | 5830 | 0 (0%) | 0 |
| `responseCodes.md` | 4812 | 4133 (86%) | 3 |
| `template.md` | 44233 | 180 (0%) | 2 |
| `transactionInquiry.md` | 16531 | 183 (1%) | 2 |
| `transactionflow.md` | 1073 | 112 (10%) | 2 |
| `updateCustomerDetails.md` | 2084 | 0 (0%) | 0 |

## Overlapping source files — differences preserved, not resolved

:::warning[REVIEW REQUIRED]

Several capabilities are described twice in the source: once in a file linked from the live sidebar and once in an unlinked file. The two versions are not always identical. Per the project rule, the differences below are reported, not merged or silently corrected.

:::

### Authentication — `AUTH.md` vs `loginauthentication.md`

- Portal pages: [AUTH.md](/docs/authentication/authentication) and [loginauthentication.md](/docs/legacy/login-authentication)

| Aspect | `AUTH.md` (linked) | `loginauthentication.md` (unlinked) |
|---|---|---|
| Endpoints appearing in file | `http://host/ewallet/oauth/token` | `https://sandbox-client.remittanceshub.com:8030/ewallet/oauth/token` |
| Field names present only in this file | `channel`, `clientCode`, `locale`, `source` | `authorization`, `firstLoginStatus`, `userCode`, `userCountryCode`, `walletOwnerCode` |

### Quotation — `QUOTA.md` vs `quotation.md`

- Portal pages: [QUOTA.md](/docs/quotation/quotation) and [quotation.md](/docs/legacy/quotation)

| Aspect | `QUOTA.md` (linked) | `quotation.md` (unlinked) |
|---|---|---|
| Endpoints appearing in file | `http://host/ewallet/api/v1/fxratequotation/api` | `https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/fxratequotation` |
| Field names present only in this file | `chargeTypeCode`, `customerCode`, `customerRegistrationAllowed`, `destinationCountryCode`, `fee`, `sendClientMarginValue`, `senderMargin` | `settlementAmount`, `transactionLimit` |

### Payout — `PAYOUT-Api.md` vs `payout.md`

- Portal pages: [PAYOUT-Api.md](/docs/payout/payout) and [payout.md](/docs/legacy/payout)

| Aspect | `PAYOUT-Api.md` (linked) | `payout.md` (unlinked) |
|---|---|---|
| Endpoints appearing in file | `http://host/ewallet/api/v1/payoutProcess/api` | `https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/payoutProcess` |
| Field names present only in this file | `beneficiaryAccountHolderName`, `compliance`, `customerCode`, `customerId`, `declaration`, `destinationCountryCode`, `dialCode`, `docReferenceNumber`, `isAutoRegistered`, `receiverAddressLineOne`, `receiverAddressLineTwo`, `receiverBankCode`, `receiverBankName`, `receiverCountry`, `receiverDOB`, `receiverFirstName`, `receiverGender`, `receiverIdNumber`, `receiverIdType`, `receiverLastName`, `receiverMsisdn`, `receiverNationality`, `receiverOccupation`, `receiverPinCode`, `receiverSwiftCode`, `responseTime`, `sendClientAddress1`, `sendClientMarginValue`, `sendClientName`, `sendClientPhoneNumber`, `senderAddressLineOne`, `senderAddressLineTwo`, `senderCountry`, `senderDOB`, `senderEmail`, `senderFirstName`, `senderGender`, `senderIdNumber`, `senderIdType`, `senderLastName` | `businessDescription`, `businessMsisdn`, `documentUpload`, `invoiceNumber`, `pin`, `tax`, `termAndCondition`, `transactionId`, `udv1`, `udv2`, `udv3`, `udv4`, `udv5` |

*(field lists truncated at 40 entries per side; full sets are on the two pages themselves)*

### Transaction enquiry / inquiry — `ENQUIRY.md` vs `transactionInquiry.md`

- Portal pages: [ENQUIRY.md](/docs/transactions/transaction-enquiry) and [transactionInquiry.md](/docs/legacy/transaction-inquiry)

| Aspect | `ENQUIRY.md` (linked) | `transactionInquiry.md` (unlinked) |
|---|---|---|
| Endpoints appearing in file | `http://host/ewallet/api/v1/transactionInfo/api?types=all&status=all&transId=1***90`, `http://host/ewallet/api/v1/transactionInfo/api?types=all&status=all&transId={value}`, `http://host/ewallet/api/v1/wallet/walletOwner/{walletOwnerCode}` | `https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/`, `https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/transactionInfo/all?` |
| Field names present only in this file | `currencyCode`, `currencyName`, `currencySymbol`, `maxTransValue`, `maxValue`, `minTransValue`, `minValue`, `value`, `walletOwnerCode`, `walletOwnerMsisdn`, `walletOwnerName`, `walletTypeCode`, `walletTypeName` | `all`, `limit`, `offset` |

### Balance — `ENQUIRY.md` vs `balance.md`

- Portal pages: [ENQUIRY.md](/docs/balance/balance-enquiry) and [balance.md](/docs/legacy/balance)

| Aspect | `ENQUIRY.md` (linked) | `balance.md` (unlinked) |
|---|---|---|
| Endpoints appearing in file | `http://host/ewallet/api/v1/transactionInfo/api?types=all&status=all&transId=1***90`, `http://host/ewallet/api/v1/transactionInfo/api?types=all&status=all&transId={value}`, `http://host/ewallet/api/v1/wallet/walletOwner/{walletOwnerCode}` | `http://host/api/v1/balance/USD`, `http://host/api/v1/balance/all`, `http://host/api/v1/balance/{parameter}` |
| Field names present only in this file | `accountName`, `beneficiaryBankName`, `beneficiaryCode`, `beneficiaryName`, `beneficiaryNumber`, `code`, `creationDate`, `currencyName`, `currencySymbol`, `description`, `exchangeRate`, `fxQuoteid`, `id`, `initiatedUserName`, `maxTransValue`, `maxValue`, `minTransValue`, `minValue`, `payinCurrencyName`, `paymentMode`, `paymentOption`, `payoutAmount`, `payoutCurrency`, `payoutCurrencyName`, `payoutPartnerCode`, `relationship`, `remittancePurpose`, `reverse`, `sendClientAddress1`, `sendClientAddress2`, `sendClientCountry`, `sendClientFee`, `sendClientMarginValue`, `sendClientPhoneNumber`, `senderCode`, `senderExchangeRate`, `senderName`, `senderNumber`, `senderUniqueId`, `sendingAmount` | `all`, `currency`, `currentBalance`, `status` |

*(field lists truncated at 40 entries per side; full sets are on the two pages themselves)*

### Customer registration — `CUSTOMEREGIS.md` vs `customerRegistration.md`

- Portal pages: [CUSTOMEREGIS.md](/docs/customers/customer-registration) and [customerRegistration.md](/docs/legacy/customer-registration)

| Aspect | `CUSTOMEREGIS.md` (linked) | `customerRegistration.md` (unlinked) |
|---|---|---|
| Endpoints appearing in file | `http://host/ewallet/api/v1/customer-registration` | `http://host/api/v1/customer-registration` |
| Field names present only in this file | `addressLine1`, `businessAuthorizedPerson`, `countryCode`, `customerSubTypeCode`, `dialCode`, `docReferenceNumber`, `idExpiryDate`, `mobileNumber`, `ownerDetailList`, `serviceTypeCode` | `addressline1`, `addressline2`, `country`, `declaration`, `employerName`, `idExpiry`, `idIssuedBy`, `middleName`, `mobileNo`, `ownerPercentage`, `residenceStatusCode`, `thirdPartyDetermination`, `transactionVolumeCode` |

## Source assets not present in the export

:::warning[REVIEW REQUIRED]

The source references the following binary assets. They are not part of the supplied export and have not been recreated or substituted.

| Asset | Referenced by | Portal treatment |
|---|---|---|
| `img/rhub.png` | every source page (page banner) | Not reproduced; no substitute branding created |
| `img/apiseq.png` | `apisequence.md` (inside a comment) | Not reproduced; source reference retained in text |
| `img/rhubbpt2.png` | `transactionflow.md` (bank payout flow) | REVIEW REQUIRED notice on the page |
| `img/rhubwpt2.png` | `transactionflow.md` (wallet payout flow) | REVIEW REQUIRED notice on the page |
| `assets/TABLE_OF_VALIDATIONS.xlsx` | `CURRENCYVALIDATIONS.md` download link | REVIEW REQUIRED; link points here |

:::

## Source cross-links with no resolvable target

:::warning[REVIEW REQUIRED]

These links exist in the source but point at sections the source does not publish. They have been redirected to the nearest index page rather than invented.

| Source link | Issue |
|---|---|
| `#/master?id=get-customer-document-type` | no matching published section in source |

:::

## Information the source does not establish

These topics are absent from the supplied source and are therefore absent from this portal. They are listed so their absence is visible rather than mistaken for an oversight.

| Topic | Status |
|---|---|
| Rate limits | REVIEW REQUIRED — not in source |
| Idempotency keys / replay behaviour | REVIEW REQUIRED — not in source |
| Retry policy and backoff | REVIEW REQUIRED — not in source |
| Webhooks / callbacks | REVIEW REQUIRED — not in source |
| SDKs and client libraries | REVIEW REQUIRED — not in source |
| Environment base URLs (most pages use the literal placeholder `http://host`) | REVIEW REQUIRED — not in source |
| How the access token is presented on subsequent calls | REVIEW REQUIRED — not in source |
| Token refresh / re-authentication | REVIEW REQUIRED — not in source |
| Pagination for list endpoints | REVIEW REQUIRED — not in source |
| Error-code resolution guidance | REVIEW REQUIRED — not in source |
| SLA / availability commitments | REVIEW REQUIRED — not in source |
| Transaction status transition rules | REVIEW REQUIRED — not in source |

## Source-file to portal-page map

| Source file | Portal location | Status | Notes |
|---|---|---|---|
| `AUTH.md` | docs/authentication/authentication.md | COMPLETE | Published Authentication contract carried over in full (request, header and response parameters, request and response examples). |
| `COUNTRYVALIDATIONS.md` | docs/validation/country-validations.md | COMPLETE | All eight SWIFT country groups, their country lists, field explanations and matrices carried over. |
| `CURRENCYVALIDATIONS.md` | docs/validation/currency-validations.md | COMPLETE | All four validation matrices (Sender/Receiver × Individual/Business) and the field requirement clarification carried over. The source also links a downloadable Excel file (assets/TABLE_OF_VALIDATIONS.xlsx) that is not part of the export — flagged. |
| `CUSTOMEREGIS.md` | docs/customers/customer-registration.md | COMPLETE | Published Customer Registration contract carried over in full for both business and individual customers. |
| `DocumentUpload.md` | docs/documents/document-upload.md | COMPLETE | Published Document Upload contract carried over in full. |
| `ENQUIRY.md` | docs/transactions/transaction-enquiry.md, docs/balance/balance-enquiry.md | COMPLETE | Both published sections (Transaction Enquiry, Balance Enquiry) carried over in full. The file also contains a commented-out Customer Enquiry section, reproduced in the appendix. |
| `ErrorCodes.md` | docs/errors/error-codes.md | PARTIAL | Both source tables (HTTP status codes, application error codes) carried over in full. Marked PARTIAL because the file is commented out of the live sidebar, so its publication status is REVIEW REQUIRED, and because the source gives no resolution guidance. |
| `PAYOUT-Api.md` | docs/payout/payout.md | COMPLETE | Published Payout contract carried over in full: transactionInfo, sender, receiver and compliance request objects, registered-customer variant, response parameters and examples. |
| `PAYOUT-WPT.md` | docs/payout/wpt-payout.md | COMPLETE | Published WPT Payout contract carried over in full. |
| `QUOTA.md` | docs/quotation/quotation.md | COMPLETE | Published Quotation contract carried over in full. The file also contains a commented-out Final Quotation section — reproduced in the appendix and cross-checked against the standalone finalQuotation.md source page. |
| `README.md` | docs/intro.md | COMPLETE | About Us and Overview sections carried over verbatim. |
| `RHUB_CURRENT_ERROR_CODES.json` | docs/errors/current-error-codes.md | COMPLETE | Supplemental authoritative data supplied directly by the RHUB team (not part of the 29-file documentation export). All 65 entries published, duplicates preserved as separate rows, 16 distinct result codes, 1 entry published with "Not provided". |
| `WPT.md` | docs/wpt/ (index + 3 API pages), docs/appendix/unpublished-apis.md | PARTIAL | 3 active sections (Customer Registration, Quotation, Payout) documented in full; 6 commented-out sections reproduced in the appendix. Marked PARTIAL because the whole file is commented out of the live sidebar (publication status REVIEW REQUIRED). |
| `apisequence.md` | docs/getting-started/integration-flow.md | COMPLETE | Sequence list and all cross-references remapped to portal routes. Source diagram (img/apiseq.png) is commented out in the source and the asset is not in the export. |
| `balance.md` | docs/legacy/balance.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `customerInquiry.md` | docs/legacy/customer-inquiry.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `customerRegistration.md` | docs/legacy/customer-registration.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `finalQuotation.md` | docs/legacy/final-quotation.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `footer.md` | docs/appendix/licence.md | COMPLETE | Intellectual-property statement and source version marker (Version 2.3.0) carried over. |
| `loginauthentication.md` | docs/legacy/login-authentication.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `master.md` | docs/master-apis/ (index + 14 API pages), docs/appendix/unpublished-master-apis.md | COMPLETE | 14 published master APIs documented individually with full request/response contracts and examples; 10 commented-out master sections reproduced in the appendix and flagged REVIEW REQUIRED. |
| `ownerDetails.md` | docs/legacy/owner-details.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `payout.md` | docs/legacy/payout.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `payoutValidator.md` | docs/legacy/reference-payout-validator.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `quotation.md` | docs/legacy/quotation.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `responseCodes.md` | docs/errors/transaction-status-codes.md | COMPLETE | The published production status table carried over verbatim. Three commented-out tables (short status codes, partner status codes, validation codes) reproduced in the appendix and flagged. |
| `template.md` | docs/template-management/ (index + 6 API pages) | PARTIAL | All 6 sections documented in full (Service Fee, Update Service Fee, Transaction List, Update Transaction Limit, Forex Margin, Update Forex Margin). Marked PARTIAL because the file is commented out of the live sidebar, so its publication status is REVIEW REQUIRED. |
| `transactionInquiry.md` | docs/legacy/transaction-inquiry.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
| `transactionflow.md` | docs/getting-started/transaction-flows.md | REVIEW REQUIRED | Narrative carried over in full. Both flow diagrams (img/rhubbpt2.png, img/rhubwpt2.png) are referenced by the source but the binary assets are not in the export — flagged on page. |
| `updateCustomerDetails.md` | docs/legacy/update-customer-details.md | PARTIAL | Page content carried over in full. Marked PARTIAL because the source file is commented out of the live documentation sidebar, so whether the contract is current is REVIEW REQUIRED. |
