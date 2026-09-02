---
title: "VA responses and errors"
sidebar_label: "Responses and errors"
description: "The VA response envelope and its documented result codes."
---

# VA responses and errors

VA follows the platform error model: `resultCode` is the error category and
`resultDescription` is the specific reason. See
[errors and response codes](/docs/errors) for the wider model and the
[current API error codes](/docs/errors/current-error-codes).

:::note

Every endpoint in this API wraps its payload in the same envelope. Only the payload-specific key changes (`docUpload`, `customerRegistration`, `vaCustomerRegistrationList`, etc.) — the envelope fields below are always present.

:::

### Envelope Fields

| Field | Description |
|---|---|
| transactionId | System-generated call ID, useful for support requests |
| requestTime / responseTime | Server timestamps for the call |
| resultCode | `"0"` = success. Non-zero indicates failure — check `resultDescription` |
| resultDescription | Human-readable outcome, e.g. `"Transaction successful"` |

### Known Error Codes

| resultCode | resultDescription |
|---|---|
| 1097 | Mandatory Values Null |
| 1197 | Invalid Request |
| 1114 | Approval Already Exist |
| 1103 | Record Update Failed |
| 5001 | Customer already registered with customer ID |
| 4114 | Customer Registration Not Found |

### Envelope Shape

```json
{
  "transactionId": "10793472",
  "requestTime": "Mon Jul 13 13:12:53 IST 2026",
  "responseTime": "Mon Jul 13 13:12:53 IST 2026",
  "resultCode": "0",
  "resultDescription": "Transaction successful"
  // ... plus the endpoint-specific payload key
}
```

## Related

- [Errors and response codes](/docs/errors)
- [Current API error codes](/docs/errors/current-error-codes)
- [VA integration flow](/docs/virtual-accounts/integration-flow)
