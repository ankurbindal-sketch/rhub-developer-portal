---
title: "VA currencies"
sidebar_label: "VA currencies"
description: "RHUB Virtual Account — VA currencies."
---

# VA currencies

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

**What this does:** Returns the list of settlement currencies enabled for Virtual Accounts under a given send client. Use this to know which currencies you can even open a VA in before starting onboarding.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/currency/virtualAccountCurrency/{sendClientCode}'}</code>
  </div>
</div>

- **Path Parameter** — **REQUIRED** `sendClientCode` — your 10-digit client code

### Sample Response

```json
{
  "resultCode": "0",                        // "0" = success, see Section 17
  "resultDescription": "Transaction successful",
  "virtualAccountSettleCurrencyList": [
    {
      "id": 4,
      "code": "100003",
      "name": "United States Dollar",
      "currencyCode": "USD-USA",
      "symbol": "$",
      "status": "Active",
      "vaSettlementFlag": true,               // must be true to be VA-eligible
      "b2b": true, "b2c": true, "c2c": true, "c2b": true, "wpt": true
    }
  ]
}
```

### Key Response Fields

| Field | Notes |
|---|---|
| code | Internal currency code — use this value (not `currencyCode`) where a currency code is expected elsewhere in this API, e.g. `sendClientVaAccountCurrency` in [VA approval process](/docs/virtual-accounts/va-approval-process). |
| currencyCode | Human/ISO-style currency string, format `CCY-COUNTRY` e.g. `USD-USA`. |
| vaSettlementFlag | Only currencies with `true` here can be used for Virtual Account settlement. |
| status | `Active` / `Inactive` — inactive currencies should be hidden from selection UIs. |
