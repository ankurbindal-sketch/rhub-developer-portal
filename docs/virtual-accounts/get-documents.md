---
title: "Get uploaded VA documents"
sidebar_label: "Get uploaded documents"
description: "RHUB Virtual Account — Get uploaded VA documents."
---

# Get uploaded VA documents

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

**What this does:** Lists documents already uploaded for a wallet owner — handy for showing an upload-progress checklist against [VA document requirements](/docs/virtual-accounts/document-requirements)'s mandatory list, or confirming a specific document went through.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/documentUpload/virtualDocument/{walletOwnerCode}'}</code>
  </div>
</div>

- **Path Parameter** — **REQUIRED** `walletOwnerCode`

### Query Parameters

| Parameter | What It Is | Required? | Notes |
|---|---|---|---|
| sortBy | Field to sort on | **OPTIONAL** | e.g. `creationDate` |
| sort | Sort direction | **OPTIONAL** | `asc` / `desc` |
| offset | Pagination offset | **OPTIONAL** | Default `0` |
| limit | Page size | **OPTIONAL** | e.g. `10` |
| docReferenceNumber | Filter to one customer's document set | **OPTIONAL** | Recommended — otherwise returns all documents for the wallet owner. |

### Sample Response

```json
{
  "resultCode": "0",
  "resultDescription": "Transaction successful",
  "docUploadList": [
    {
      "code": "107777",
      "walletOwnerCode": "1000009093",
      "docReferenceNumber": "CUS2JAW793",
      "fileName": "image (2)_CUS2JAW793_20260615111649.png",
      "docTypeCode": "RHD019",
      "docTypeName": "Certified ID copy (Government Issued ID cards)",
      "status": "Active"
    }
  ]
}
```
