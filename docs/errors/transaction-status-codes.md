---
title: "Transaction status codes"
sidebar_label: "Transaction status codes"
description: "RHUB transaction statuses available in production."
---

# Transaction status codes

In Production, the following statuses will be available:

| Name | Description            |
|------|------------------------|
| In Process | Payload validated and ready for processing. |
| Payout Processing | Transaction validated and sent to the correspondent to credit the beneficiary. |
| Payout Pass | Amount successfully credited to the beneficiary’s account. |
| Payout Fail | Transaction failed. |
| Reverse | Amount credited back to the wallet after failure. |
| Technical Failure | Transaction failed due to timeout, network issue, or uncaught exception. |

:::note[Scope of this list]

These are the statuses the source states will be available in production. The source does
not define transitions between them, timing, or which statuses are terminal — that is
**REVIEW REQUIRED**. A further status-code table and a validation-code table exist in the
source file but are commented out; they are reproduced in
[Unpublished API sections](/docs/appendix/unpublished-apis).

:::

## Related

- [Current API error codes](/docs/errors/current-error-codes)
- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
- [Error codes](/docs/errors/error-codes)
