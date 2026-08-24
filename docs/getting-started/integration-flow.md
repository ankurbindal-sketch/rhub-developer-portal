---
title: "Integration flow"
sidebar_label: "Integration flow"
description: "The RHUB integration sequence: authenticate, quote, prepare documents and customer, then pay out."
---

# Integration flow

Authentication, Quotation, Payout and Transaction Enquiry are the constant core of every
integration. What happens between them depends on the customer and the transaction type.

One point is worth stating up front: **a quotation does not require a registered customer**.
You can price a transaction first and resolve registration afterwards.

## The integration sequence

<div className="rhub-journey">

<div className="rhub-journey__step">
<span className="rhub-journey__index">01</span>
<span className="rhub-journey__kind">Core transaction API</span>

**[Authentication](/docs/authentication/authentication)**

Obtain the access token; send it as `Authorization: Bearer <access_token>` on every later call.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">02</span>
<span className="rhub-journey__kind">Core transaction API</span>

**[Quotation](/docs/quotation/quotation)**

Price the transaction. The customer does not need to be registered first: pass an existing `customerCode`, or send it blank.

<div className="rhub-branches">

<div className="rhub-branch">
<span className="rhub-branch__label">Registered customer</span>

Send the existing RHUB customer code in `customerCode`.

</div>

<div className="rhub-branch">
<span className="rhub-branch__label">Unregistered customer</span>

Send `customerCode` as an empty value. Registration happens later.

</div>

</div>

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">03</span>
<span className="rhub-journey__kind">Preparation</span>

**[Document Upload](/docs/documents/document-upload)**

Upload the KYC/KYB documentation payout requires, and invoice documentation for B2B, B2C and C2B.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">04</span>
<span className="rhub-journey__kind">Conditional / decision</span>

**Customer registration decision**

Resolve the customer before payout — not before the quotation.

<div className="rhub-branches">

<div className="rhub-branch">
<span className="rhub-branch__label">Already registered</span>

Continue with the customer code you hold.

</div>

<div className="rhub-branch">
<span className="rhub-branch__label">Not registered</span>

Register with the [Customer Registration API](/docs/customers/customer-registration), or use on-the-fly registration in the [Payout](/docs/payout/payout) request.

</div>

</div>

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">05</span>
<span className="rhub-journey__kind">Preparation / reference</span>

**[Bank List](/docs/master-apis/bank-list)**

Fetch the beneficiary bank information the payout route requires.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">06</span>
<span className="rhub-journey__kind">Preparation / reference</span>

**[Master / reference data](/docs/master-apis)**

Fetch the master and reference values required by the selected transaction type, route and payout payload.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">07</span>
<span className="rhub-journey__kind">Core transaction API</span>

**[Payout](/docs/payout/payout)**

Submit the payout request.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">08</span>
<span className="rhub-journey__kind">Core transaction API</span>

**[Transaction Enquiry](/docs/transactions/transaction-enquiry)**

Retrieve the state of the transaction.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">09</span>
<span className="rhub-journey__kind">Final / supporting</span>

**[Balance](/docs/balance/balance-enquiry)**

The final API in the documented sequence; may be used to retrieve the current balance.

</div>

</div>

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
