---
id: "errors-index"
title: "Errors and response codes"
sidebar_label: "Overview"
slug: "/errors"
description: "How RHUB transaction status codes differ from HTTP and application error codes."
---

# Errors and response codes

Two things tell you what happened to a request:

| What it tells you | Where |
|---|---|
| Why a request failed — the `resultCode` category and the `resultDescription` reason | [Current API error codes](/docs/errors/current-error-codes) |
| Where a transaction has reached in processing | [Transaction status codes](/docs/errors/transaction-status-codes) |
| Virtual Account response envelope and its result codes | [VA responses and errors](/docs/virtual-accounts/responses-and-errors) |

Handle failures on the `resultCode` / `resultDescription` pair returned in the response body.
Track a transaction's progress with its status value.

:::note[HTTP status and `resultCode` are separate]

The HTTP status describes the transport-level outcome of the call. `resultCode` is RHUB's
application error category and `resultDescription` is the specific reason, both returned in
the response body. Use `resultCode` for coarse classification and `resultDescription` for the
precise condition.

RHUB supplies code values and descriptions only — no remediation or retry guidance — so none
is offered here.

:::
