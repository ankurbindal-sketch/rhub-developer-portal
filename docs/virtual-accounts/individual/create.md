---
title: "Create individual VA customer"
sidebar_label: "Create / register"
description: "RHUB Virtual Account — Create individual VA customer."
---

# Create individual VA customer

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

**What this does:** Registers a natural person as a Virtual Account customer. Requires the `docReferenceNumber` from the document uploads in [Upload VA documents](/docs/virtual-accounts/upload-documents) — upload the 3 mandatory Individual documents first.

:::

### Endpoint

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/customer-registration'}</code>
  </div>
</div>

### Request Fields

| Field | Required? | Notes |
|---|---|---|
| customerTypeCode | **REQUIRED** | Fixed: `100001` for Individual |
| customerSubTypeCode | **REQUIRED** | e.g. `100001` |
| serviceTypeCode | **REQUIRED** | Fixed: `VIRTUAL` |
| source | **OPTIONAL** | e.g. `WEB` |
| docReferenceNumber | **REQUIRED** | From the Upload VA Document response ([Upload VA documents](/docs/virtual-accounts/upload-documents)) |
| walletOwnerCode | **REQUIRED** | Your 10-digit send client code |
| firstName / lastName | **REQUIRED** | Legal name |
| middleName | **OPTIONAL** | — |
| dateOfBirth | **REQUIRED** | Format: `YYYY-MM-DD` |
| gender | **REQUIRED** | `male` / `female` |
| nationality | **REQUIRED** | ISO 3166-1 alpha-3, e.g. `IND` |
| mobileNumber | **REQUIRED** | — |
| dialCode | **OPTIONAL** | e.g. `+91` |
| email | **REQUIRED** | — |
| occupationCode | **REQUIRED** | e.g. `RHO015` (Consultant) |
| jobTitle / jobIndustry | **REQUIRED** | — |
| addressLine1 | **REQUIRED** | — |
| addressLine2 | **OPTIONAL** | — |
| countryCode / state / city / pincode | **REQUIRED** | countryCode is ISO alpha-3, e.g. `IND` |
| residenceStatusCode | **REQUIRED** | e.g. `100006` |
| idTypeCode / idNumber / idCountry | **REQUIRED** | idTypeCode e.g. `RHD002` |
| idIssuedBy | **OPTIONAL** | — |
| issueDate | **REQUIRED** | Format `YYYY-MM-DD` |
| idExpiryDate | **REQUIRED** | Format `YYYY-MM-DD` |
| noIssueDate / noIdExpiry | **OPTIONAL** | Boolean flags — set `true` when the ID has no issue date / never expires. |
| thirdPartyDetermination | **OPTIONAL** | Boolean — is this a third-party registration? |
| declaration | **OPTIONAL** | Boolean — customer declaration accepted |
| transactionVolumeCode | **OPTIONAL** | e.g. `100002` |
| isSenderPep | **OPTIONAL** | Boolean — Politically Exposed Person flag |
| customerCode | **OPTIONAL** | Leave empty `""` on Create — the system assigns and returns it as `code` ([Retrieve individual VA customer](/docs/virtual-accounts/individual/retrieve)). That `code` value becomes REQUIRED on Edit ([Edit individual VA customer](/docs/virtual-accounts/individual/edit)) — note the field is named `code` there, not `customerCode`. |
| customerStatus | **OPTIONAL** | Leave empty — system-managed |
| ownerDetailList | **OPTIONAL** | Send `null` — this is only used for Business customers ([Create business VA customer](/docs/virtual-accounts/business/create)) |
| isPayoutBanned | **OPTIONAL** | Default `false` |
| payoutClientCodes | **OPTIONAL** | Default empty array `[]` |

### Complete Request Example

Individual customer
Show
▼

```json
{
  "customerTypeCode": "100001",
  "customerSubTypeCode": "100001",
  "serviceTypeCode": "VIRTUAL",
  "docReferenceNumber": "GGGFDAAABB",
  "walletOwnerCode": "1000008547",
  "firstName": "Madhurans",
  "lastName": "Doe",
  "dateOfBirth": "1981-08-21",
  "occupationCode": "RHO010",
  "jobTitle": "Job Titlee",
  "jobIndustry": "Job Industrye",
  "gender": "male",
  "nationality": "CAN",
  "mobileNumber": "9899990099",
  "addressLine1": "canada",
  "email": "pankaj.Doe@remittanceshub.com",
  "issueDate": "1988-08-22",
  "idCountry": "MWI",
  "countryCode": "CAN",
  "state": "canada",
  "city": "canada",
  "pincode": "232222",
  "idTypeCode": "RHD002",
  "idNumber": "ID8888780077",
  "idExpiryDate": "2027-02-09"
}
```

:::info

ℹ This example shows **mandatory fields only**. Optional fields (`source`, `middleName`, `dialCode`, `addressLine2`, `idIssuedBy`, `noIssueDate`, `noIdExpiry`, `thirdPartyDetermination`, `declaration`, `transactionVolumeCode`, `isSenderPep`, `customerCode`, `customerStatus`, `ownerDetailList`, `isPayoutBanned`, `payoutClientCodes`) may still be sent per the Request Fields table above.

:::

## Related

- [VA integration flow](/docs/virtual-accounts/integration-flow)
- [VA document requirements](/docs/virtual-accounts/document-requirements)
- [VA request status](/docs/virtual-accounts/va-request-status)
