---
title: "Edit business VA customer"
sidebar_label: "Edit"
description: "RHUB Virtual Account — Edit business VA customer."
---

# Edit business VA customer

<span className="rhub-method rhub-method--put">PUT</span>

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

**What this does:** Updates an existing Business customer, or converts an existing Remittance customer into a Virtual customer — same as the Individual edit flow ([Edit individual VA customer](/docs/virtual-accounts/individual/edit)), one level up.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--put">PUT</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/customer-registration/{code}'}</code>
  </div>
</div>

:::warning

**Same payload shape as Create ([Create business VA customer](/docs/virtual-accounts/business/create)), with these differences:** `code` is now **REQUIRED** (existing customer's `code`, returned by Create/Receipt — note the field is named `customerCode` in the Create payload but `code` here, confirmed by IT) `ownerDetailList` becomes **OPTIONAL** on Edit — send `null` if the ownership structure hasn't changed, or the full array to replace it

:::

### Fields That Can Actually Be Updated

| Field | Payload Key |
|---|---|
| Mobile Number | `mobileNumber` |
| Nature Of Business | `natureOfBusinessCode` |
| Email | `email` |
| Address Line 1 | `addressLine1` |
| Country | `countryCode` |
| State | `state` |
| City | `city` |
| Pincode | `pincode` |

:::warning

All other fields (trade name, legal status, business relationship, ID details, `ownerDetailList`, etc.) are **not** updatable through this endpoint, even if included in the payload — only the fields listed above will actually change.

:::

### Payload Diff vs Create

```http
"code": "1000000857",   // was "customerCode": "" on Create — field renamed to "code" on Edit
"noIssueDate": true, "noIdExpiry": true,   // flags flipped true...
"idIssuedBy": "", "issueDate": "", "idExpiryDate": "",  // ...so these become empty, not omitted
"ownerDetailList": null   // unchanged owners — send null instead of the array
```

## Related

- [VA integration flow](/docs/virtual-accounts/integration-flow)
- [VA document requirements](/docs/virtual-accounts/document-requirements)
- [VA request status](/docs/virtual-accounts/va-request-status)
