---
id: "intro"
title: "RHUB Developer Portal"
sidebar_label: "Overview"
slug: "/"
description: "Developer documentation for the RHUB (RemittancesHub) cross-border remittance APIs."
---

# RHUB Developer Portal

RHUB (RemittancesHub) is a licensed financial institution operating an Alternate Cross
Border Network for inbound and outbound payments. It moves funds into the bank accounts of
beneficiaries — corporate or individual — in near real time, at lower cost than traditional
channels, with end-to-end transaction tracking.

You integrate over a REST API. Requests and responses are JSON, and every call is
authenticated with an access token.

<div className="rhub-cards">

<div className="rhub-card">
<span className="rhub-card__kicker">Get started</span>

### [Authentication](/docs/authentication/authentication)

Obtain the access token every other call depends on.

</div>

<div className="rhub-card">
<span className="rhub-card__kicker">API reference</span>

### [Explore RHUB API contracts](/docs/api-index)

Every published API, with its method, purpose and integration stage.

</div>

<div className="rhub-card">
<span className="rhub-card__kicker">Integration flow</span>

### [Plan your integration](/docs/getting-started/integration-flow)

The decision points between authenticating and settling a payout.

</div>

<div className="rhub-card">
<span className="rhub-card__kicker">Errors and validation</span>

### [Result codes and field rules](/docs/errors)

Current API error codes, transaction statuses and correspondent validation rules.

</div>

</div>

## Core transaction APIs

Every payout runs through these four calls, in this order.

<div className="rhub-flow">

<div className="rhub-flow__step">
<span className="rhub-flow__index">01</span>

[Authentication](/docs/authentication/authentication)

</div>

<div className="rhub-flow__step">
<span className="rhub-flow__index">02</span>

[Quotation](/docs/quotation/quotation)

</div>

<div className="rhub-flow__step">
<span className="rhub-flow__index">03</span>

[Payout](/docs/payout/payout)

</div>

<div className="rhub-flow__step">
<span className="rhub-flow__index">04</span>

[Transaction Enquiry](/docs/transactions/transaction-enquiry)

</div>

</div>

Customer and document preparation happen around this sequence — what they involve depends on
the customer and the transaction type.

<div className="rhub-cards rhub-cards--two">

<div className="rhub-card">
<span className="rhub-card__kicker">Prepare customer</span>

**Existing customer** — use the customer code you already hold.

**New customer** — register beforehand with
[Customer Registration](/docs/customers/customer-registration), or register on the fly
during [Payout](/docs/payout/payout).

</div>

<div className="rhub-card">
<span className="rhub-card__kicker">Prepare documents</span>

**KYC / KYB** — required for payout. Referenced by `docReferenceNumber`.

**Invoice** — required for B2B, B2C and C2B. Referenced by `sendClient TrxReference`.

</div>

</div>

[Integration flow](/docs/getting-started/integration-flow) sets out the decision points in
full, including where each branch applies.

## Supporting capabilities

These are called when your route or use case needs them, not on every transaction.

- [Master / reference APIs](/docs/master-apis) — remittance purpose, source of fund,
  relationship, occupation, bank list, wallet list and more
- [Balance Enquiry](/docs/balance/balance-enquiry) — current wallet or account balance
- [Currency validations](/docs/validation/currency-validations) and
  [country validations](/docs/validation/country-validations) — correspondent-specific
  conditional field requirements
- [Errors and response codes](/docs/errors) — result codes, transaction statuses and
  HTTP/application error codes

New to the reference? [How to read this reference](/docs/getting-started/conventions)
explains the requirement flags, field tables and REVIEW REQUIRED markers.
