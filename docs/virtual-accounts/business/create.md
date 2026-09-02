---
title: "Create business VA customer"
sidebar_label: "Create / register"
description: "RHUB Virtual Account — Create business VA customer."
---

# Create business VA customer

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

**What this does:** Registers a company as a Virtual Account customer, including its Ultimate Beneficial Owner(s) (UBOs) via `ownerDetailList`. Requires the `docReferenceNumber` from [Upload VA documents](/docs/virtual-accounts/upload-documents) — upload the 9 mandatory Corporate documents first.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/customer-registration'}</code>
  </div>
</div>

### Request Fields — Business Level

| Field | Required? | Notes |
|---|---|---|
| customerTypeCode | **REQUIRED** | Fixed: `100002` for Business |
| customerSubTypeCode | **REQUIRED** | e.g. `100001` |
| serviceTypeCode | **REQUIRED** | Fixed `VIRTUAL` |
| source | **OPTIONAL** | e.g. `WEB` |
| docReferenceNumber | **REQUIRED** | From Upload VA Document ([Upload VA documents](/docs/virtual-accounts/upload-documents)) |
| walletOwnerCode | **REQUIRED** | — |
| tradeName | **REQUIRED** | Registered/trading company name |
| legalStatusCode | **REQUIRED** | e.g. `RHB002` (Corporation) |
| natureOfBusinessCode | **REQUIRED** | e.g. `RHT005` |
| remarks | **OPTIONAL** | Free text, e.g. industry note |
| businessRelationshipCode | **REQUIRED** | e.g. `100003` |
| businessAuthorizedPerson | **OPTIONAL** | Name of the authorized signatory |
| mobileNumber / email | **REQUIRED** | Business contact details |
| dialCode | **OPTIONAL** | e.g. `+91` |
| addressLine1 | **REQUIRED** | — |
| addressLine2 | **OPTIONAL** | — |
| countryCode / state / city / pincode | **REQUIRED** | countryCode is ISO alpha-3 |
| idNumber | **REQUIRED** | Business registration/license number |
| idCountry | **REQUIRED** | — |
| idIssuedBy | **OPTIONAL** | — |
| issueDate | **REQUIRED** | — |
| idExpiryDate | **REQUIRED** | This is the **business's own** document expiry — note the owner-level field below is named `idExpiry` (no "Date"), not `idExpiryDate`. This naming difference is intentional, confirmed by IT. |
| noIssueDate / noIdExpiry | **OPTIONAL** | Boolean flags controlling the two date fields above |
| thirdPartyDetermination | **OPTIONAL** | Boolean |
| transactionVolumeCode | **OPTIONAL** | e.g. `100005` |
| isSenderPep | **OPTIONAL** | Boolean |
| declaration | **OPTIONAL** | Boolean |
| customerCode | **OPTIONAL** | Empty `""` on Create — returned as `code` in the response. That `code` value becomes REQUIRED on Edit ([Edit business VA customer](/docs/virtual-accounts/business/edit)), where the field is named `code`, not `customerCode`. |
| customerStatus | **OPTIONAL** | System-managed |
| isPayoutBanned / payoutClientCodes | **OPTIONAL** | Default `false` / `[]` |
| ownerDetailList | **REQUIRED** | Array of UBO/owner objects — required for onboarding (matches the mandatory "ID copies of UBOs" document in [VA document requirements](/docs/virtual-accounts/document-requirements)). Required fields per owner differ by `customerTypeCode` — see table below. |

:::warning

Each owner's required fields depend on its own `customerTypeCode` — `100001` (individual owner) and `100002` (business/corporate owner) have different mandatory sets, confirmed from sample payloads. Mixed arrays (some individual, some business owners) are supported.

:::

### Owner Type 100001 · Individual

| Field | Required? |
|---|---|
| customerTypeCode | **REQUIRED** |
| firstName / lastName | **REQUIRED** |
| dateOfBirth / gender | **REQUIRED** |
| companyName | **REQUIRED** |
| addressLine1 / countryCode / state / city / pincode | **REQUIRED** |
| idTypeCode / idNumber / idCountry | **REQUIRED** |
| indexId / customerCode | **OPTIONAL** |
| middleName / nationality | **OPTIONAL** |
| mobileNumber / dialCode / email | **OPTIONAL** |
| addressLine2 / residenceStatusCode | **OPTIONAL** |
| idIssuedBy / issueDate / idExpiry | **OPTIONAL** |
| noIssueDate / noIdExpiry | **OPTIONAL** |
| ownerPercentage / ownerStatus | **OPTIONAL** |

### Owner Type 100002 · Business

| Field | Required? |
|---|---|
| customerTypeCode | **REQUIRED** |
| companyName | **REQUIRED** |
| addressLine1 / countryCode / state / city | **REQUIRED** |
| indexId / customerCode | **OPTIONAL** |
| firstName / lastName / middleName | **OPTIONAL** |
| dateOfBirth / gender / nationality | **OPTIONAL** |
| mobileNumber / dialCode / email | **OPTIONAL** |
| addressLine2 / residenceStatusCode / pincode | **OPTIONAL** |
| idTypeCode / idNumber / idIssuedBy / idCountry | **OPTIONAL** |
| issueDate / idExpiry | **OPTIONAL** |
| noIssueDate / noIdExpiry | **OPTIONAL** |
| ownerPercentage / ownerStatus | **OPTIONAL** |

### Complete Request Example

Business customer with 2 owners (1 individual, 1 business)

```json
{
  "customerTypeCode": "100002",
  "customerSubTypeCode": "100001",
  "serviceTypeCode": "VIRTUAL",
  "docReferenceNumber": "GTGGGG7766",
  "walletOwnerCode": "1000008547",
  "tradeName": "AFREE technology",
  "natureOfBusinessCode": "RHT004",
  "mobileNumber": "9098987711",
  "email": "john.doe@example.com",
  "addressLine1": "12 Example Road",
  "countryCode": "MWI",
  "state": "Central Region",
  "city": "Lilongwe",
  "pincode": "676567",
  "businessRelationshipCode": "100003",
  "legalStatusCode": "RHB002",
  "idNumber": "ID9800000091",
  "idCountry": "MWI",
  "issueDate": "2024-08-22",
  "idExpiryDate": "2028-08-31",
  "ownerDetailList": [
    {
      // Owner 1 — individual owner (customerTypeCode 100001)
      "customerTypeCode": "100001",
      "firstName": "Johnss",
      "lastName": "Doe",
      "dateOfBirth": "2008-08-22",
      "gender": "male",
      "companyName": "FGRTTT technology",
      "addressLine1": "12 Example Road",
      "countryCode": "MWI",
      "state": "Malawi",
      "city": "Lilongwe",
      "pincode": "121122",
      "idTypeCode": "RHD007",
      "idNumber": "ID8887877711",
      "idCountry": "MWI"
    },
    {
      // Owner 2 — business owner (customerTypeCode 100002)
      "customerTypeCode": "100002",
      "companyName": "Estedeee technology",
      "addressLine1": "12 Example Road",
      "countryCode": "MWI",
      "state": "Central Region",
      "city": "Lilongwe"
    }
  ]
}
```

:::info

ℹ This example shows **mandatory fields only**at both the business level and per owner type. Optional fields may still be sent per the Request Fields tables above.

:::

## Related

- [VA integration flow](/docs/virtual-accounts/integration-flow)
- [VA document requirements](/docs/virtual-accounts/document-requirements)
- [VA request status](/docs/virtual-accounts/va-request-status)
