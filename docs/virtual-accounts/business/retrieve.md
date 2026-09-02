---
title: "Retrieve business VA customer"
sidebar_label: "Retrieve"
description: "RHUB Virtual Account — Retrieve business VA customer."
---

# Retrieve business VA customer

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

**What this does:** Same idea as the Individual Receipt ([Retrieve individual VA customer](/docs/virtual-accounts/individual/retrieve)), but for Business — returns the full registration plus enriched fields, including the resolved `ownerDetailList[]` with each owner's screening state.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/customer-registration/{code}'}</code>
  </div>
</div>

- **Path Parameter** — **REQUIRED** `code`

### Additional Fields vs Create

| Field | Notes |
|---|---|
| customerId / fullName | System-generated ID and resolved display name |
| legalStatusName / natureOfBusinessName / businessRelationshipName | Human-readable labels for the codes you submitted |
| screeningStatus / customerState / customerStateCode | AML/approval lifecycle |
| ownerDetailList[].ownerId / ownerState / ownerStateCode / screeningStatus | Per-owner screening result — each owner is independently screened |
| virtualAccountCurrencyCodes / virtualAccountCurrencyName | Provisioned VA currencies |

## Related

- [VA integration flow](/docs/virtual-accounts/integration-flow)
- [VA document requirements](/docs/virtual-accounts/document-requirements)
- [VA request status](/docs/virtual-accounts/va-request-status)
