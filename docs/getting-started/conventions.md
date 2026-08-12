---
title: "How to read this reference"
sidebar_label: "How to read this reference"
description: "Conventions used in the RHUB Developer Portal: requirement flags, field tables, examples and REVIEW REQUIRED markers."
---

# How to read this reference

This page describes the conventions used by RHUB Developer Portal 1.0. It contains no
technical claims of its own — every technical statement lives on the API pages and comes
from the RHUB source export.

## Requirement flags

The RHUB source marks every request field with a requirement flag. This portal preserves
the source flag exactly and never promotes one to another:

| Flag | Source meaning |
|---|---|
| M | Mandatory |
| O | Optional |
| C | Conditional |

Conditional fields are **not** documented as mandatory. Where the source explains the
condition — for example correspondent-specific or country-specific rules — the explanation
appears with the field table or in [Validation](/docs/validation/currency-validations).

## Field tables

Field tables reproduce the source columns. Depending on the source page these are:

- `Parameters | Input Type | Length | Requirement | Description`, or
- `Parameters | Data Type | Requirement | Description` (older source pages, where the
  source does not state a length).

Where the source does not state a field length, the column is absent rather than guessed.

## Method and endpoint callouts

Each API page shows the HTTP method badge and an **Endpoint** callout containing the request
URL exactly as the source writes it. Many source URLs use the literal host placeholder
`http://host/...`; that placeholder is reproduced as-is because the source does not
establish the environment base URLs on those pages.

## Examples

Request and response examples are the source's own samples, reproduced verbatim in
copy-to-clipboard code blocks. The source frequently masks values in its examples (for
example `15*****f-54fe-43d9-***7-b7dc****1b9`); masking is preserved. Where a source page
has no example, the page says so rather than showing an invented one.

## REVIEW REQUIRED

**REVIEW REQUIRED** marks a point where the supplied RHUB source does not establish the
information — a missing example, a missing field contract, an unavailable image asset, an
internal source link with no matching target, or a conflict between two source files. It is
never a placeholder for content that exists in the source.

The following are *not* established anywhere in the supplied source and are therefore
absent from this portal rather than inferred: rate limits, idempotency behaviour, retry
semantics, webhooks, SDKs, pagination rules, sandbox versus production base URLs (other than
where a URL literally appears in the source), token refresh behaviour, and SLA claims.

## Publication status of source pages

The RHUB source export contains 29 Markdown files. Fourteen are linked from the live
documentation sidebar; the remaining fifteen are served but commented out of that sidebar.
Pages built from unlinked files carry a publication-status warning. Full details are in the
[source coverage notes](/docs/appendix/source-notes).

## Formatting transformations applied

To move from the legacy docsify pages to this portal, only presentation was changed:

- HTML `<table>` markup became Markdown tables; cell text, field names and values are verbatim.
- "Tap to open" reveal widgets became syntax-highlighted, copyable code blocks.
- "About the API / Request URL / Request Method" tables became endpoint callouts.
- Source cross-links (`#/PAYOUT-Api?id=...`) were remapped to portal routes.
- A handful of source tables carry a stray extra cell on some rows, which standard Markdown
  would silently drop. Those rows were re-aligned so that every non-empty source value still
  appears; no value was moved between columns and none was added.
- HTML-commented blocks in the source are not rendered as live documentation; substantive
  commented API contracts are reproduced in the [appendix](/docs/appendix/unpublished-apis)
  with a warning, and every commented block is accounted for in the
  [source coverage notes](/docs/appendix/source-notes).
