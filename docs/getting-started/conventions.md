---
title: "How to read this reference"
sidebar_label: "How to read this reference"
description: "How to read the RHUB API reference: environments, authorisation, requirement flags, field tables and examples."
---

# How to read this reference

This page explains the conventions used throughout the reference. It makes no technical
claims of its own — those live on the API pages.

## Where the content comes from

The portal draws on three authoritative RHUB inputs:

- the original RHUB documentation source, which supplies the API contracts;
- current supplemental RHUB data, such as the
  [current API error codes](/docs/errors/current-error-codes);
- operational and integration guidance confirmed directly by the RHUB team, which explains
  how the contracts are used together — for example the customer-registration paths and the
  KYC/KYB and invoice document model.

The governing principle is unchanged: **no undocumented technical behaviour is invented**.
Guidance explains how documented contracts fit together; it never adds fields, endpoints,
values or rules that RHUB has not established.

## Requirement flags

Every request field carries a requirement flag, reproduced exactly as RHUB states it. A
Conditional field is never presented as Mandatory.

| Flag | Meaning |
|---|---|
| M | Mandatory |
| O | Optional |
| C | Conditional |

Where the condition is explained — typically correspondent-specific or country-specific —
it appears with the field table or under
[Validation](/docs/validation/currency-validations).

## Field tables

Field tables reproduce the source columns, which are either
`Parameters | Input Type | Length | Requirement | Description` or, on older contracts,
`Parameters | Data Type | Requirement | Description`. Where a field length is not stated,
the column is absent rather than guessed.

Field names, endpoint strings and example values are reproduced literally, including
spellings that look inconsistent. If a field is written one way in a table and another way
in an example, both are preserved and the difference is noted rather than corrected.

## Environments and base URLs

RHUB has confirmed one environment for Developer Portal 1.0:

Base URLs for Sandbox and Production are listed under
[API environments](/docs/getting-started/environments).

## Method and endpoint blocks

Each API page shows its HTTP method and the request path exactly as the contract writes it.
Most paths are written as `http://host/ewallet/api/v1/...`, where **`host` stands for the
base URL of your environment**. Substitute the base URL of your
environment — see [API environments](/docs/getting-started/environments). The paths
themselves are reproduced unchanged.

## Authorising requests

[Authentication](/docs/authentication/authentication) returns an `access_token`. Every
subsequent call carries it in the `Authorization` header:

```http
Authorization: Bearer <access_token>
```

## Examples

Request and response examples are RHUB's own samples, reproduced verbatim in copyable code
blocks. Masked values in the originals (for example `15*****f-54fe-43d9-***7-b7dc****1b9`)
stay masked. Where a contract has no example, the page says so rather than showing an
invented one.

## Notes, limitations and conditional rules

Where a requirement depends on the transaction, the page states the condition rather than
generalising it — for example `sendClientTrxReference` is required for B2B, B2C and C2B but
not for C2C. Where RHUB's current behaviour differs from what an older contract table shows,
the page says which one your integration should follow.

Requirement flags, field names, endpoint paths, examples and error text are reproduced from
RHUB's material rather than tidied, so a table and an example occasionally spell the same
thing differently. Where that matters for integration, the page says so.

The following are not documented by RHUB and are therefore absent rather than inferred:
rate limits, idempotency behaviour, retry semantics, webhooks, SDKs, pagination rules, token
refresh behaviour, and SLA commitments.
