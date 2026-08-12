---
title: "How to read this reference"
sidebar_label: "How to read this reference"
description: "Conventions used in the RHUB Developer Portal: requirement flags, field tables, examples and REVIEW REQUIRED markers."
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

## Method and endpoint blocks

Each API page shows its HTTP method and the request URL exactly as RHUB writes it. Many URLs
use the literal host placeholder `http://host/...`; that placeholder is reproduced as-is
because RHUB does not establish environment base URLs on those pages.

## Examples

Request and response examples are RHUB's own samples, reproduced verbatim in copyable code
blocks. Masked values in the originals (for example `15*****f-54fe-43d9-***7-b7dc****1b9`)
stay masked. Where a contract has no example, the page says so rather than showing an
invented one.

## REVIEW REQUIRED

**REVIEW REQUIRED** marks a point where the available RHUB material does not settle
something an integrator may need — a missing example, a contract and an operational rule
that do not fully line up, or an unavailable diagram. It is never a placeholder for content
that exists.

The following are not established by RHUB and are therefore absent rather than inferred:
rate limits, idempotency behaviour, retry semantics, webhooks, SDKs, pagination rules,
environment base URLs beyond those literally documented, token refresh behaviour, and SLA
commitments.
