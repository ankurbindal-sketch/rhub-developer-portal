---
title: "Integration flow"
sidebar_label: "Integration flow"
description: "How the RHUB APIs fit together: the core payout flow, conditional preparation steps and supporting reference APIs."
---

# Integration flow

Authentication, Quotation, Payout and Transaction Enquiry are the constant core of every
integration. What happens around them depends on two questions: is the customer already
registered, and what transaction type are you sending?

## The payout journey

<div className="rhub-journey">

<div className="rhub-journey__step">
<span className="rhub-journey__index">01</span>

**[Authenticate](/docs/authentication/authentication)**

Obtain the access token every other call depends on.

</div>

<div className="rhub-journey__step rhub-journey__step--branch">
<span className="rhub-journey__index">02</span>

**Customer status**

<div className="rhub-branches">

<div className="rhub-branch">
<span className="rhub-branch__label">Existing customer</span>

Use the customer code you already hold. Do not register the customer again.

</div>

<div className="rhub-branch">
<span className="rhub-branch__label">New customer</span>

Either register first with [Customer Registration](/docs/customers/customer-registration),
or register on the fly as part of the Payout request.

</div>

</div>

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">03</span>

**[KYC / KYB document](/docs/documents/document-upload)**

Upload the customer verification documentation required for payout — KYC for individual
customers, KYB for business customers. The Payout request carries the resulting reference in
`docReferenceNumber`.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">04</span>

**[Quotation](/docs/quotation/quotation)**

Obtain the rate, charges and quote identifier for the transaction.

</div>

<div className="rhub-journey__step rhub-journey__step--branch">
<span className="rhub-journey__index">05</span>

**Transaction type**

<div className="rhub-branches">

<div className="rhub-branch">
<span className="rhub-branch__label">C2C</span>

No invoice-document requirement applies.

</div>

<div className="rhub-branch">
<span className="rhub-branch__label">B2B · B2C · C2B</span>

Invoice documentation is required. The invoice reference is carried by
`sendClientTrxReference` in the Payout request.

</div>

</div>

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">06</span>

**Reference and beneficiary preparation**

Fetch only the reference data your route needs — the
[Bank List](/docs/master-apis/bank-list) for the beneficiary bank, other
[master APIs](/docs/master-apis) for coded fields, and the
[currency](/docs/validation/currency-validations) or
[country](/docs/validation/country-validations) tables for correspondent-specific
conditional fields.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">07</span>

**[Payout](/docs/payout/payout)**

Submit the payout request, or [WPT Payout](/docs/payout/wpt-payout) for wallet payouts.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">08</span>

**[Transaction Enquiry](/docs/transactions/transaction-enquiry)**

Check the status of the payout. Statuses are listed under
[transaction status codes](/docs/errors/transaction-status-codes).

</div>

</div>

## What is core, what is conditional, what is supporting

| Category | APIs | When |
|---|---|---|
| Core transaction APIs | Authentication, Quotation, Payout, Transaction Enquiry | Every payout |
| Conditional preparation | Customer Registration, Document Upload | Depends on customer status and transaction type |
| Supporting / reference | Master APIs, Bank List, Balance Enquiry, currency and country validations | As your route or use case requires |

## Supporting capabilities

None of these sit on the critical path of a payout.

- [Master / reference APIs](/docs/master-apis) — configuration data such as remittance
  purpose, source of funds, relationship, occupation, bank list and wallet list. Call the
  ones your request needs; there is no requirement to call them all.
- [Balance Enquiry](/docs/balance/balance-enquiry) — the current wallet or account balance.
  A supporting call, not a step that closes out a payout.
- [Currency validations](/docs/validation/currency-validations) and
  [country validations](/docs/validation/country-validations) — which conditional fields a
  given correspondent, currency or country requires.
