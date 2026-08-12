---
title: "Integration flow"
sidebar_label: "Integration flow"
description: "How the RHUB APIs fit together: the core payout flow, conditional preparation steps and supporting reference APIs."
---

# Integration flow

Integrating with RHUB is not a single fixed line of calls. Authentication, quotation, payout
and transaction enquiry are the constant core; what happens around them depends on whether
the customer is already registered and which transaction type you are sending.

## Decision flow

**1. Authenticate**
Obtain an access token with the [Authentication API](/docs/authentication/authentication).

**2. Customer status**

### Existing customer

The customer has already been registered with RHUB. Use the existing customer code for the transaction. Do not register the customer again.

### New customer, registered before payout

The customer is not yet known to RHUB and you want to register them as a separate step. Register the customer with the Customer Registration API, then use the resulting customer code for the payout.

### New customer, registered on the fly

The customer is not yet known to RHUB and you want to register them as part of the payout. RHUB supports customer registration as part of the Payout flow. A separate Customer Registration call is not required on this path; the Payout fields governing it (for example isAutoRegistered, declaration and the sender details) remain exactly as the Payout contract defines them.

**3. KYC / KYB document**
Customer verification documentation is required for payout — KYC for individual customers,
KYB for business customers. Upload it and keep the resulting reference, which the Payout
request carries in `docReferenceNumber`. See
[Document Upload](/docs/documents/document-upload).

**4. Quotation**
Call the [Quotation API](/docs/quotation/quotation) to obtain the rate, charges and quote
identifier for the transaction.

**5. Transaction type**

- **C2C** — no invoice-document requirement applies.
- **B2B, B2C, C2B** — invoice documentation is required. The invoice/transaction reference is
  carried by `sendClient TrxReference` in the Payout request.

**6. Reference and beneficiary preparation**
Fetch only the reference data your route needs — for example the
[Bank List](/docs/master-apis/bank-list) for the beneficiary bank, other
[master APIs](/docs/master-apis) for coded fields, and the
[currency](/docs/validation/currency-validations) or
[country](/docs/validation/country-validations) validation tables for correspondent-specific
conditional fields.

**7. Payout**
Submit the [Payout request](/docs/payout/payout) — or the
[WPT Payout request](/docs/payout/wpt-payout) for wallet payouts.

**8. Transaction Enquiry**
Check the status of the payout with the
[Transaction Enquiry API](/docs/transactions/transaction-enquiry). Statuses are listed under
[transaction status codes](/docs/errors/transaction-status-codes).

## What is core, what is conditional, what is supporting

| Category | APIs | When |
|---|---|---|
| Core transaction flow | Authentication, Quotation, Payout, Transaction Enquiry | Every payout |
| Conditional preparation | Customer Registration, Document Upload | Depends on customer status and transaction type |
| Supporting / reference | Master APIs, Bank List, Balance Enquiry, currency and country validations | As your route or use case requires |

## Supporting capabilities

None of these sit on the critical path of a payout.

- [Master / reference APIs](/docs/master-apis) — configuration data such as remittance
  purpose, source of funds, relationship, occupation, bank list and wallet list. Call them
  when you need the coded values a request expects; there is no requirement to call them all.
- [Balance Enquiry](/docs/balance/balance-enquiry) — the current wallet or account balance.
  It is a supporting call, not a step that closes out a payout.
- [Currency validations](/docs/validation/currency-validations) and
  [country validations](/docs/validation/country-validations) — which conditional fields a
  given correspondent, currency or country requires.

## The API call sequence as documented by RHUB

1. [Login (Authentication) API](/docs/authentication/authentication)
 ➤ Required to authenticate and obtain access tokens for subsequent calls.
 2. [Quotation API](/docs/quotation/quotation)
 ➤ Used to fetch the exchange rate and charges before initiating a payout.
 3. [Bank List API](/docs/master-apis/bank-list)
 ➤ Retrieves the list of bank details and related parameters required by a specific correspondent, based on the provided receiver code.
 4. [Document Upload API](/docs/documents/document-upload)
 ➤ Enables the client to upload customer-related documents, including ID proofs and invoices.
 5. [Payout API](/docs/payout/payout)
 ➤ Initiates the fund transfer based on the selected quotation and beneficiary.
 6. [Transaction Enquiry API](/docs/transactions/transaction-enquiry)
 ➤ Used to check the status of a previously initiated payout.
 7. [Balance API](/docs/balance/balance-enquiry)
 ➤ Retrieves the current wallet or account balance.
 * [Master API](/docs/master-apis)
 ➤ These provide necessary configuration data (e.g., remittance purpose, source of funds, bank lists, occupations etc). This API is subject to specific requirements and can be invoked at any point within the sequence, depending on the use case.

However, the API call sequence is limited to the Login API, Quotation API, Payout API, and Transaction Enquiry API and the remaining APIs can be called based on the need.
