---
title: "Retrieve individual VA customer"
sidebar_label: "Retrieve"
description: "RHUB Virtual Account — Retrieve individual VA customer."
---

# Retrieve individual VA customer

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

**What this does:** Re-fetches the full customer record by code — everything you sent on Create, plus system-computed fields such as screening status and Virtual Account currency assignment.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/customer-registration/{code}'}</code>
  </div>
</div>

- **Path Parameter** — **REQUIRED** `code` — the `customerRegistration.code` returned by Create

### Additional Fields in the Response

| Field | Notes |
|---|---|
| customerId | System-generated unique customer identifier, e.g. `100000909313824I` |
| fullName / nickName / tradeName | Derived display names |
| screeningStatus | AML screening state, e.g. `IP` (in progress) |
| customerStatus / customerState / customerStateCode | Lifecycle status, e.g. `Active` / `System Approved` / `AA` |
| virtualAccountCurrencyCodes / virtualAccountCurrencyName | Currencies this customer's VA is provisioned for, e.g. `EUR, USD-USA, GBP` |
| provider | KYC/screening provider used, e.g. `AiPrise` |
| registrationApprovedBy / creationDate / createdBy | Audit trail fields |

:::info

Response shape is identical to the Business Customer Receipt ([Retrieve business VA customer](/docs/virtual-accounts/business/retrieve)), just without the `ownerDetailList` array.

:::

## Related

- [VA integration flow](/docs/virtual-accounts/integration-flow)
- [VA document requirements](/docs/virtual-accounts/document-requirements)
- [VA request status](/docs/virtual-accounts/va-request-status)
