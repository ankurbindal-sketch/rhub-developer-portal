---
title: "VA document requirements"
sidebar_label: "Document requirements"
description: "RHUB Virtual Account — VA document requirements."
---

# VA document requirements

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

**What this does:** Returns the KYC/compliance document checklist for a customer type — and critically, tells you which documents are **mandatory** vs **optional** via the `mandatory` flag. Drive your document-upload UI directly off this response instead of hardcoding a checklist.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/virtualAccount/customerDocumentType/getByCustomerTypeCode/{customerTypeCode}'}</code>
  </div>
</div>

- **Path Parameter** — **REQUIRED** `customerTypeCode` — `100001` Individual or `100002` Business

### Individual · 100001

| Code | Document | Mandatory? |
|---|---|---|
| RHD019 | Certified ID copy (Government Issued ID) | **YES** |
| RHD020 | Proof of Address (Utility Bill / Bank Statement, within 90 days) | **YES** |
| RHD021 | Due Diligence Questionnaire — Individual | **YES** |

### Business · 100002

| Code | Document | Mandatory? |
|---|---|---|
| RHD024 | Business / Commercial License | **NO** |
| RHD022 | Certificate of Incorporation | **YES** |
| RHD023 | Memorandum & Articles of Association | **YES** |
| RHD025 | Proof of Trading Address | **YES** |
| RHD026 | Directors / Shareholders / UBO Registry Document | **YES** |
| RHD027 | ID copies of UBOs owning ≥10% of shares | **YES** |
| RHD028 | Proof of Beneficial Owners' Address | **YES** |
| RHD029 | Proof of all Directors' Identity | **YES** |
| RHD030 | Authorized Signatory List + ID copies | **YES** |
| RHD031 | Due Diligence Questionnaire — Corporate | **YES** |

:::info

**How to complete the Due Diligence Questionnaire (RHD021 / RHD031):** Click the document name above to download the questionnaire, fill it in completely, get it **signed by an authorized representative**, then upload the signed copy via the Upload VA Document API (Section 06) using the matching `docTypeCode` — `RHD021` for Individual, `RHD031` for Corporate. Unsigned or incomplete questionnaires will be rejected during compliance review.

:::

:::warning

**Business/Commercial License is the one optional document.** Every other document in both checklists is mandatory before a customer registration will pass compliance review — plan your onboarding UI to block progression until all mandatory documents show as uploaded.

:::
