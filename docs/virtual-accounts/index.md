---
id: "va-index"
title: "Virtual Accounts"
sidebar_label: "Overview"
slug: "/virtual-accounts"
description: "Virtual Account onboarding: currencies, documents, customer registration, request status and approval."
---

# Virtual Accounts

A Virtual Account (VA) is a dedicated collection account used for receiving inbound funds.
Onboarding a customer onto a VA follows one shape for both customer types: check the
supported currencies, upload the required documents, register the customer, and RHUB
Admin/Operations then approves the request and links it to a collection bank account.

:::info[Authentication]

Virtual Account APIs use the same access token as the rest of the platform. Obtain it from
the [Authentication API](/docs/authentication/authentication) and send it on every VA call:

```http
Authorization: Bearer <access_token>
```

Base URLs for each environment are listed under
[API environments](/docs/getting-started/environments).

:::

:::note

This API onboards a customer onto a **Virtual Account (VA)** — a dedicated collection account used for receiving inbound funds. There are two customer types — **Individual** and **Business** — and both follow the same shape: check the currency list → upload the required KYC/compliance documents → register the customer → an admin approves the VA request and links it to a real collection bank account.

:::

### Individual Customer

A natural person. Registration collects personal identity (name, DOB, gender, nationality), a single government ID, and a home address. 3 mandatory KYC documents.

### Business Customer

A registered company. Registration collects business/legal identity, a registration document, and a list of
Ultimate Beneficial Owners (UBOs)
in
ownerDetailList
. 8 of 9 corporate documents are mandatory.

## How VA onboarding works

<div className="rhub-journey">

<div className="rhub-journey__step">
<span className="rhub-journey__index">01</span>

**[Currencies](/docs/virtual-accounts/va-currencies)**

Check which settlement currencies support Virtual Accounts.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">02</span>

**[Document checklist](/docs/virtual-accounts/document-requirements)**

Fetch the mandatory/optional document list for Individual or Business.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">03</span>

**[Upload documents](/docs/virtual-accounts/upload-documents)**

Upload the required VA documents.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">04</span>

**Register customer**

Create the [Individual](/docs/virtual-accounts/individual/create) or
[Business](/docs/virtual-accounts/business/create) customer record.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">05</span>
<span className="rhub-journey__kind">RHUB Admin / Operations</span>

**[VA approval](/docs/virtual-accounts/va-approval-process)**

RHUB Admin/Operations links the customer to the applicable collection bank account.

</div>

</div>

## Where to start

| Step | Page |
|---|---|
| Understand the sequence | [VA integration flow](/docs/virtual-accounts/integration-flow) |
| Check supported currencies | [VA currencies](/docs/virtual-accounts/va-currencies) |
| Find the document checklist | [VA document requirements](/docs/virtual-accounts/document-requirements) |
| Register a customer | [Individual](/docs/virtual-accounts/individual/create) · [Business](/docs/virtual-accounts/business/create) |
| Track the request | [VA request status](/docs/virtual-accounts/va-request-status) |
| Understand approval | [VA approval process](/docs/virtual-accounts/va-approval-process) |

## Related

- [Authentication](/docs/authentication/authentication)
- [API environments](/docs/getting-started/environments)
- [VA responses and errors](/docs/virtual-accounts/responses-and-errors)
