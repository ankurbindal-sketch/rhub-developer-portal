---
title: "VA request status"
sidebar_label: "VA request status"
description: "RHUB Virtual Account — VA request status."
---

# VA request status

<span className="rhub-method rhub-method--get">GET</span>

:::info[Authentication]

Virtual Account APIs use the same access token as the rest of the platform. Obtain it from
the [Authentication API](/docs/authentication/authentication) and send it on every VA call:

```http
Authorization: Bearer <access_token>
```

Base URLs for each environment are listed under
[API environments](/docs/getting-started/environments).

:::
:::note

**What this does:** An ops/admin-side queue view of Virtual Account requests — every customer registered in [Create individual VA customer](/docs/virtual-accounts/individual/create)–13 lands here awaiting a collection bank account to be linked, then approved ([VA approval process](/docs/virtual-accounts/va-approval-process)). **One endpoint serves both customer types** — despite "individual" appearing in the URL, the response mixes Individual and Business records (filter with `customerTypeCode` if you only want one). This is confirmed intentional, not a bug.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/collectionBank/individual/virtualAccount/customer/all'}</code>
  </div>
</div>

### Query Parameters

| Parameter | Required? | Notes |
|---|---|---|
| sortBy / sort / offset / limit | **OPTIONAL** | Standard pagination — e.g. `sortBy=creationDate&sort=desc&offset=0&limit=10` |
| sendClientCode | **OPTIONAL** | Filter to one client |
| sendClientCustomerId | **OPTIONAL** | Filter to one customer |
| customerTypeCode | **OPTIONAL** | Filter to `100001` Individual or `100002` Business |

### Sample Response

```json
{
  "resultCode": "0",
  "pageable": { "limit": 10, "offset": 0, "totalRecords": 96 },
  "vaCustomerRegistrationList": [
    {
      // newly registered, not yet linked to a collection bank
      "code": "100159",
      "customerId": "100000908810856B",
      "customerName": "Trustweb services Pvt Ltd",
      "customerTypeCode": "100002",
      "currencyName": "USD-USA,EUR",
      "state": "U",                   // U = Unapproved / pending
      "stateName": "Created"
    },
    {
      // already approved and linked to a bank
      "code": "100155",
      "customerId": "100000896010857I",
      "customerName": "Swati Shukla",
      "customerTypeCode": "100001",
      "collectionBankCode": "1000009132",
      "collectionBankName": "HDFC Bank",
      "accountNumber": "11345034123607",
      "accountFormat": "IBAN",
      "currencyName": "EUR,USD-USA,AED",
      "state": "A",                   // A = Approved
      "stateName": "Approved",
      "comment": "Approved and linked to primary collection account"
    }
  ]
}
```

### State Reference

| state | stateName | Meaning |
|---|---|---|
| `U` | Created | Customer registered; no collection bank account linked yet. |
| `A` | Approved | Linked to a collection bank account via [VA approval process](/docs/virtual-accounts/va-approval-process) — the Virtual Account is live. |

:::note

ℹ **screeningStatus vs. VA approval — two different checks:** `screeningStatus` (seen on the customer record, e.g. `IP`) is the AML screening result. The `state`/`stateName` shown here is a separate, later step — whether the VA request has been approved and linked to a real collection bank account via a pooling API ([VA approval process](/docs/virtual-accounts/va-approval-process)). **This endpoint is poll-only** — there is no webhook or callback notification when either status changes; integrators must poll [VA request status](/docs/virtual-accounts/va-request-status) to detect state changes.

:::
