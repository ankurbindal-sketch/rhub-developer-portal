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

:::warning[REVIEW REQUIRED — resolution guidance]

The source supplies code values and descriptions only. It does not supply remediation or
retry guidance for any code, so none is offered here. Nothing in the supplied source
establishes retry policy, idempotency behaviour or backoff expectations.

:::
