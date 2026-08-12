---
id: "errors-index"
title: "Errors and response codes"
sidebar_label: "Overview"
slug: "/errors"
description: "How RHUB transaction status codes differ from HTTP and application error codes."
---

# Errors and response codes

The RHUB source documents two distinct code families. They are **not** interchangeable and
this portal keeps them apart:

| Family | What it describes | Source file | Page |
|---|---|---|---|
| Transaction status codes | The lifecycle status of a transaction in production | `responseCodes.md` | [Transaction status codes](/docs/errors/transaction-status-codes) |
| HTTP and application error codes | Protocol-level status codes and RHUB application error codes | `ErrorCodes.md` | [Error codes](/docs/errors/error-codes) |

:::warning[REVIEW REQUIRED — resolution guidance]

The source supplies code values and descriptions only. It does not supply remediation or
retry guidance for any code, so none is offered here. Nothing in the supplied source
establishes retry policy, idempotency behaviour or backoff expectations.

:::
