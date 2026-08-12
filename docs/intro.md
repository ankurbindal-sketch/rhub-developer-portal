---
id: "intro"
title: "RHUB Developer Portal"
sidebar_label: "Overview"
slug: "/"
description: "Developer documentation for the RHUB (RemittancesHub) cross-border remittance APIs."
---

# RHUB Developer Portal

Welcome to the developer documentation for **RHUB (RemittancesHub)**. This portal is a
re-presentation of the authoritative RHUB technical documentation, reorganised for
integration work.

## About Us

>RemittancesHub (RHUB) is a licensed financial institution operating an Alternate Cross Border Network for Inbound & Outbound Payments, which enables international fund transfers into Bank Accounts of Beneficiaries (both corporate & individual):

* In near real-time.
* At significantly lower costs vs. traditional channels.
* With end-to-end transaction tracking.
* Visit https://www.remittanceshub.com/ to know more.

## Overview

To integrate the RHUB services the Representational State Transfer (REST) API is used. The HTTP methods POST, GET, PUT, and DELETE HTTP methods are used to send the Request parameter of the API in JavaScript Object Notation (JSON) format.

JSON format is a light weight data interchange format, and text format has multiple name/value pairs, and is independent of language.

The APIs described on this forum are limited to Financial Institution Customer.

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
