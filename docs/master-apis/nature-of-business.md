---
title: "Nature of Business"
sidebar_label: "Nature of Business"
description: "RHUB Nature of Business master API."
---

# Nature of Business

<span className="rhub-method rhub-method--get">GET</span>

[Business fields in the Customer Registration API](/docs/customers/customer-registration#request-parameter-of-business-customer)

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/natureOfBusiness/getByCustomerTypeCode/{customerTypeCode}'}</code>
  </div>
</div>

The Nature of Business API is used to fetch the nature of the business run by the customer.

## Request Parameter of Nature of Business

| Parameters       | Input Type | Length | Requirement | Description                          |
|------------------|:------:|:------:|:------------:|--------------------------------------|
| customerTypeCode | Numeric | 06 | M | The unique code of the customer type, for Business customer : 100002 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details of Nature of Business

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http://host/ewallet/api/v1/natureOfBusiness/getByCustomerTypeCode/100002
```

## Response Parameter of Nature of Business

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Nature of Business List** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the record, which will be passed where required. |  |
| customerTypeCode | String | M | The unique code of the following. • Individual • Business |  |
| name | String | M | The nature of the business run by the customer. |  |
| status | String | M | The status of the record. note: Only records with status "Active" needs to be used |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

Note: The response may include records with `"status": "Inactive"`. These should be ignored. Only the data with `"status": "Active"` must be filtered and used.

## Response Details of Nature of Business

```json
{
"transactionId": "8301042",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"natureOfBusinessList": [
 {
  "id": 34,
  "code": "RHT001",
  "customerTypeCode": "100002",
  "name": "Agriculture",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 35,
  "code": "RHT002",
  "customerTypeCode": "100002",
  "name": "Automotive",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 36,
  "code": "RHT003",
  "customerTypeCode": "100002",
  "name": "Banking",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 37,
  "code": "RHT004",
  "customerTypeCode": "100002",
  "name": "Construction",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 38,
  "code": "RHT005",
  "customerTypeCode": "100002",
  "name": "Education",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 39,
  "code": "RHT006",
  "customerTypeCode": "100002",
  "name": "Information Technology",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 40,
  "code": "RHT007",
  "customerTypeCode": "100002",
  "name": "Manufacturing",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 41,
  "code": "RHT008",
  "customerTypeCode": "100002",
  "name": "Retail",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 42,
  "code": "RHT009",
  "customerTypeCode": "100002",
  "name": "Real Estate",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 44,
  "code": "RHT011",
  "customerTypeCode": "100002",
  "name": "Professional Services",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 43,
  "code": "RHT010",
  "customerTypeCode": "100002",
  "name": "Transportation and Logistics",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 45,
  "code": "RHT012",
  "customerTypeCode": "100002",
  "name": "Others",
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
