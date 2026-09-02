---
title: "Edit individual VA customer"
sidebar_label: "Edit"
description: "RHUB Virtual Account — Edit individual VA customer."
---

# Edit individual VA customer

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

**What this does:** Updates an existing Individual customer. This also doubles as "Remittance customer → Virtual customer" conversion — pass a customer code that already exists in the platform and this call promotes/updates it as a VA customer.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--put">PUT</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/customer-registration/{code}'}</code>
  </div>
</div>

:::warning

**Same payload shape as Create ([Create individual VA customer](/docs/virtual-accounts/individual/create)), with one difference:** `code` is now **REQUIRED** — it must be the existing customer's `code` (returned by Create/Receipt), both in the URL path and the payload body.

:::

### Fields That Can Actually Be Updated

| Field | Payload Key |
|---|---|
| Gender | `gender` |
| Mobile Number | `mobileNumber` |
| ID Type | `idTypeCode` |
| ID Number | `idNumber` |
| Occupation | `occupationCode` |
| Job Title | `jobTitle` |
| Job Industry | `jobIndustry` |
| Address Line 1 | `addressLine1` |
| Country | `countryCode` |
| State | `state` |
| City | `city` |
| Pincode | `pincode` |

:::warning

All other fields (name, date of birth, nationality, ID country, issue/expiry dates, etc.) are **not** editable through this endpoint, even if included in the payload — send the full payload as on Create, but only the fields listed above will actually change.

:::

### Payload Diff vs Create

```http
"code": "1000000812",   // was "customerCode": "" on Create — now the existing customer's code, field renamed to "code" on Edit
"docReferenceNumber": "CUS19SCMHK",  // re-upload / re-reference documents if any changed
"firstName": "Rakesh", "lastName": "Doe"  // updated fields
```

## Related

- [VA integration flow](/docs/virtual-accounts/integration-flow)
- [VA document requirements](/docs/virtual-accounts/document-requirements)
- [VA request status](/docs/virtual-accounts/va-request-status)
