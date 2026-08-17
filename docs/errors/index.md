---
id: "errors-index"
title: "Errors and response codes"
sidebar_label: "Overview"
slug: "/errors"
description: "How RHUB transaction status codes differ from HTTP and application error codes."
---

# Errors and response codes

RHUB documents three distinct code families. They are **not** interchangeable and this
portal keeps them apart:

| Family | What it describes | Supplied by | Page |
|---|---|---|---|
| Current API error codes | The current API error-handling reference: `resultCode` classes and their `resultDescription` values | RHUB team, 2026-08-12 | [Current API error codes](/docs/errors/current-error-codes) |
| Transaction status codes | The lifecycle status of a transaction in production | Documentation export (`responseCodes.md`) | [Transaction status codes](/docs/errors/transaction-status-codes) |
| HTTP and application error codes | Protocol-level status codes and RHUB application error codes | Documentation export (`ErrorCodes.md`) | [Error codes](/docs/errors/error-codes) |

Start with **Current API error codes** for live error handling. The other two pages remain
available and unchanged; they come from the original documentation export.

:::note[How to read these families]

An HTTP status describes the transport-level outcome; a `resultCode` describes the RHUB
application or business error category, and `resultDescription` carries the specific reason.
The same numeral can appear in both families without meaning the same thing.

RHUB supplies code values and descriptions only — no remediation or retry guidance — so none
is offered here.

:::
