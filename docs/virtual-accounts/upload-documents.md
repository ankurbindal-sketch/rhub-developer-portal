---
title: "Upload VA documents"
sidebar_label: "Upload documents"
description: "RHUB Virtual Account — Upload VA documents."
---

# Upload VA documents

<span className="rhub-method rhub-method--post">POST</span>

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

**What this does:** Uploads a single document (one call per document) against a customer type document code from [VA document requirements](/docs/virtual-accounts/document-requirements). Returns a `docReferenceNumber` that you then pass into the Create/Edit Customer payload to link the document to the registration.

:::

:::warning

**Upload constraints:** Accepted file types are `JPEG`, `PNG`, and `PDF`. Maximum file size is **5120 KB**. You cannot upload more than one file under the same `docTypeCode` for a given `docReferenceNumber` — re-uploading against a `docTypeCode` that's already been used will be rejected, not replaced.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/documentUpload/upload/virtualCustomer'}</code>
  </div>
</div>

- **Content-Type** — `multipart/form-data`

### Request Parameters (Form Data)

| Parameter | What It Is | Required? | Notes |
|---|---|---|---|
| file | The document binary | **REQUIRED** | The actual file — not base64. |
| walletOwnerCode | Send client / wallet owner code | **REQUIRED** | e.g. `1000009093` |
| docReferenceNumber | Your unique reference for this document | **REQUIRED** | e.g. `CUSPMAGS1U` — reuse the same value for every document belonging to one customer registration. |
| docType | The Service Type | **REQUIRED** | e.g. VA |
| docTypeCode | Which checklist document this is | **REQUIRED** | Must match a `code` from the [VA document requirements](/docs/virtual-accounts/document-requirements) document type list, e.g. `RHD019`. |
| createdBy | User/agent code performing the upload | **OPTIONAL** | e.g. `1000009093` |
| transId | Internal tracking id | **OPTIONAL** | Left blank in practice — system-generated, no need to send a value. |

### Sample Response

```json
{
  "resultCode": "0",
  "resultDescription": "Transaction successful",
  "docUpload": {
    "walletOwnerCode": "1000009093",
    "docReferenceNumber": "CUSPMAGS1U",      // echoed back — same value you sent; use this in Create/Edit Customer
    "fileName": "image (2)_CUSPMAGS1U_20260630134656.png",
    "docType": "VA",
	"docTypeCode": "RHD019",
    "docTypeName": "Certified ID copy (Government Issued ID cards)",
    "status": "Active"
  }
}
```

### Missing-Document Error Messages — Individual

| Code | Document | Error Message |
|---|---|---|
| RHD019 | Certified ID copy | Please upload mandatory virtual account documents: Certified ID copy (Government Issued ID) |
| RHD020 | Proof of Address | Please upload mandatory virtual account documents: Proof of Address (Utility Bill or Bank statement issued within 90 days) |
| RHD021 | Due Diligence Questionnaire — Individual | Please upload mandatory virtual account documents: Due Diligence Questionnaire Individual |

### Missing-Document Error Messages — Business

| Code | Document | Error Message |
|---|---|---|
| RHD022 | Certificate of Incorporation | Please upload mandatory virtual account documents: Certificate of Incorporation |
| RHD026 | Directors/Shareholders/UBO Registry Document | Please upload mandatory virtual account documents: Company Registry document showing List of Directors, Shareholder(s), Ultimate Beneficial Owner(s) |
| RHD031 | Due Diligence Questionnaire — Corporate | Please upload mandatory virtual account documents: Due Diligence Questionnaire Corporate |
| RHD027 | ID copies of UBOs ≥10% shares | Please upload mandatory virtual account documents: ID copies of UBOs who owns more than 10% of shares with direct and/or indirect ownership |
| RHD023 | Memorandum & Articles of Association | Please upload mandatory virtual account documents: Memorandum and Articles of Association |
| RHD029 | Proof of all Directors' Identity | Please upload mandatory virtual account documents: Proof of all Directors' Identity (Government Issued ID cards) |
| RHD028 | Proof of Beneficial Owners' Address | Please upload mandatory virtual account documents: Proof of Beneficial Owners' Address (Utility bill or bank statement issued within 90 days) |
| RHD025 | Proof of Trading Address | Please upload mandatory virtual account documents: Proof of Trading Address (Utility bill or bank statement issued within 90 days) |
| RHD030 | Authorized Signatory List + ID copies | TBD — not present in the example messages; needs confirmation |

:::info

ℹ If multiple documents are missing, they're combined into **one message**comma-separated: `"Please upload mandatory virtual account documents: &#123;doc 1&#125;, &#123;doc 2&#125;, ..."`

:::

:::warning

**docReferenceNumber is client-generated.** You generate this value yourself and reuse the same one across every document belonging to a single customer registration — it's echoed back unchanged in the upload response. The Create/Edit Customer APIs only accept a single `docReferenceNumber` field, which links back to the full set of documents uploaded under that reference.

:::
