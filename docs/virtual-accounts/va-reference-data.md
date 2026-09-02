---
title: "VA reference data"
sidebar_label: "VA reference data"
description: "RHUB Virtual Account — VA reference data."
---

# VA reference data

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

**What this covers:** Every coded field used across this doc (`occupationCode`, `legalStatusCode`, `natureOfBusinessCode`, `businessRelationshipCode`, `customerTypeCode`, `residenceStatusCode`, `idTypeCode`) is backed by its own lookup endpoint. Call these to get the full list of valid codes and their display names — don't hardcode a single example value from elsewhere in this doc.

:::

### Individual Customer Lookups

| Field | Endpoint (GET) | List Key |
|---|---|---|
| occupationCode | `/ewallet/api/v1/customerOccupationType/getByCustomerTypeCode/100001` | `customerOccupationTypeList` |
| transactionVolumeCode | `/ewallet/api/v1/businessTxnVolume/getByCustomerTypeCode/100001` | `businessTxnVolumeList` |
| idTypeCode | `/ewallet/api/v1/customerDocumentType/getByCustomerTypeCode/100001` | `customerDocumentTypeList` |

### Business Customer Lookups

| Field | Endpoint (GET) | List Key |
|---|---|---|
| legalStatusCode | `/ewallet/api/v1/customerLegalStatus/getByCustomerTypeCode/100002` | `customerLegalStatusList` |
| natureOfBusinessCode | `/ewallet/api/v1/natureOfBusiness/getByCustomerTypeCode/100002` | `natureOfBusinessList` |
| businessRelationshipCode | `/ewallet/api/v1/purposeOfOpeningBusiness/getByCustomerTypeCode/100002` | `purposeOfOpeningBusinessList` |
| transactionVolumeCode | `/ewallet/api/v1/businessTxnVolume/getByCustomerTypeCode/100002` | `businessTxnVolumeList` |

### Owner (UBO) Lookups

| Field | Endpoint (GET) | List Key |
|---|---|---|
| customerTypeCode | `/ewallet/api/v1/customerType/all` | `customerTypeList` |
| residenceStatusCode | `/ewallet/api/v1/residenceStatus/customerTypeCode/100001` | `residenceStatusList` |
| idTypeCode | `/ewallet/api/v1/idType/getByCustomerTypeCode/100002` | `idTypeList` |

### Sample Response Shape

```json
{
  "resultCode": "0",
  "resultDescription": "Transaction successful",
  "customerOccupationTypeList": [
    {
      "id": 81,
      "code": "RHO015",
      "customerTypeCode": "100001",
      "name": "Consultant",
      "status": "Active",
      "creationDate": "2025-03-19T17:23:54.415+0530"
    }
    // ...full list
  ]
}
```

:::warning

**One endpoint mislabeled in the source:** "Corporate Customer Document Type List" is documented against `customerDocumentType/getByCustomerTypeCode/ 100001` (the Individual code) rather than `100002`. This looks like a copy-paste in the source material — worth confirming with IT before publishing, rather than assuming it's correct as-is.

:::

## Shared master APIs

Several of the lookups above are the platform's own master APIs, used here in a VA context rather than duplicated: [Occupation](/docs/master-apis/occupation), [Document ID Type](/docs/master-apis/document-id-type), [Customer Legal Status](/docs/master-apis/customer-legal-status), [Nature of Business](/docs/master-apis/nature-of-business) and the rest of the [master / reference APIs](/docs/master-apis). Where the VA source lists an endpoint not documented there, use the path shown above.
