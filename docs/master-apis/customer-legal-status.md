---
title: "Customer Legal Status"
sidebar_label: "Customer Legal Status"
description: "RHUB Customer Legal Status master API."
---

# Customer Legal Status

<span className="rhub-method rhub-method--get">GET</span>

[Go To Customer Registration(Business)](/docs/customers/customer-registration#request-parameter-of-business-customer)

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/customerLegalStatus/getByCustomerTypeCode/{customerTypeCode}'}</code>
  </div>
</div>

The Customer Type API is used to fetch the legal status of the customer.

## Request Parameter of the Customer Legal Status

| Parameters       | Input Type | Length | Requirement | Description                          |
|------------------|:------------:|:------------:|:------------:|--------------------------------------|
| customerTypeCode | Numeric | 06 | M | The unique code of the customer type, for Business:100002 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details of the Customer Legal Status

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET -
http://host/ewallet/api/v1/customerLegalStatus/getByCustomerTypeCode/100002
```

## Response Parameter of the Customer Legal Status

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **customerLegalStatusList** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the record, which needs to be passed while customer registration process. |  |
| customerTypeCode | String | M | The unique code of the customer type. |  |
| name | String | M | The name of the legal status. |  |
| status | String | M | The status of the customer. note: Only records with status "Active" needs to be used |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

Note: The response may include records with `"status": "Inactive"`. These should be ignored. Only the data with `"status": "Active"` must be filtered and used.

## Response Details of the Customer Legal Status

```json
{
"transactionId": "8301030",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"customerLegalStatusList": [
{
  "id": 6,
  "code": "RHB001",
  "customerTypeCode": "100002",
  "name": "Partnership",
  "status": "Active",
  "creationDate": "2024-04-15T00:00:00.000+0530"
},
{
  "id": 13,
  "code": "RHB002",
  "customerTypeCode": "100002",
  "name": "Corporation",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 7,
  "code": "RHB003",
  "customerTypeCode": "100002",
  "name": "Proprietorship",
  "status": "Active",
  "creationDate": "2024-04-15T00:00:00.000+0530"
},
{
  "id": 8,
  "code": "RHB004",
  "customerTypeCode": "100002",
  "name": "Govt. Entity",
  "status": "Active",
  "creationDate": "2024-04-15T00:00:00.000+0530"
},
{
  "id": 9,
  "code": "RHB005",
  "customerTypeCode": "100002",
  "name": "Private ltd",
  "status": "Active",
  "creationDate": "2024-04-15T00:00:00.000+0530"
},
{
  "id": 11,
  "code": "RHB006",
  "customerTypeCode": "100002",
  "name": "WLL",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 12,
  "code": "RHB007",
  "customerTypeCode": "100002",
  "name": "BSC",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
}]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
