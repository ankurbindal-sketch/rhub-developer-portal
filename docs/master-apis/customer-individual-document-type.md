---
title: "Customer/Individual Document Type"
sidebar_label: "Customer/Individual Document Type"
description: "RHUB Customer/Individual Document Type master API."
---

# Customer/Individual Document Type

<span className="rhub-method rhub-method--get">GET</span>

*Source of truth: `master.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

[Go To Customer Registration](/docs/customers/customer-registration)

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/customerDocumentType/getByCustomerTypeCode/{customerTypeCode}`

:::

The Customer Document Type API is used to fetch the ID proof documents of the customer. (for specific customer type)

## Request Parameter

| Parameters       | Input Type | Length | Requirement | Description                          |
|------------------|:------:|:------:|:------------:|--------------------------------------|
| customerTypeCode | Numeric | 06 | M | The unique code of the customer type, for Individual : 100001 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET -
http://host/api/v1/customerDocumentType/getByCustomerTypeCode/100001
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Customer Document Type List** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the customer's document type, which needs to be passed while customer registration process |  |
| customerTypeCode | String | M | The unique code of the following. • Individual • Business |  |
| name | String | M | The name of the ID proof document. |  |
| status | String | M | The status of the record. note: Only records with status "Active" needs to be used |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

Note: The response may include records with `"status": "Inactive"`. These should be ignored. Only the data with `"status": "Active"` must be filtered and used.

## Response Details for Individual Customer

```json
{
"transactionId": "7915555",
"requestTime": "Tue Feb 04 11:47:08 IST 2025",
"responseTime": "Tue Feb 04 11:47:08 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"customerDocumentTypeList": [
        {
  "id": 16,
  "code": "RHD001",
  "customerTypeCode": "100001",
  "name": "National ID Card",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 17,
  "code": "RHD002",
  "customerTypeCode": "100001",
  "name": "DrivingLicense",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 18,
  "code": "RHD003",
  "customerTypeCode": "100001",
  "name": "Passport",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 19,
  "code": "RHD004",
  "customerTypeCode": "100001",
  "name": "Govt.ApprovedID",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 20,
  "code": "RHD005",
  "customerTypeCode": "100001",
  "name": "Citizenship Card",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 21,
  "code": "RHD006",
  "customerTypeCode": "100001",
  "name": "Senior Citizen card",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 22,
  "code": "RHD007",
  "customerTypeCode": "100001",
  "name": "Residence Permit",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 23,
  "code": "RHD008",
  "customerTypeCode": "100001",
  "name": "GCC ID",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 24,
  "code": "RHD009",
  "customerTypeCode": "100001",
  "name": "Emirates ID",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
}
]
}
```


## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
