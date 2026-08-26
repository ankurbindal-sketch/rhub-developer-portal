---
title: "Customer Occupation Type"
sidebar_label: "Customer Occupation Type"
description: "RHUB Customer Occupation Type master API."
---

# Customer Occupation Type

<span className="rhub-method rhub-method--get">GET</span>

[Individual fields in the Customer Registration API](/docs/customers/customer-registration#request-parameter-of-individual-customer)

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/customerOccupationType/getByCustomerTypeCode/{customerTypeCode}'}</code>
  </div>
</div>

The Customer Occupation Type API is used to fetch the occupation of the customer.

## Request Parameter of Customer Occupation

| Parameters | Input Type |  Length | Requirement | Description                        |
|------------|:----------:|:----------:|:------------:|------------------------------------|
| customerTypeCode | Numeric | 06 | M | The unique code of the customer type, for Individual customer : 100001 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details of Customer Occupation

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http://host/ewallet/api/v1/customerOccupationType/getByCustomerTypeCode/100001
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Customer Occupation Type List** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the customer's occupation, which needs to be passed while customer registration process. |  |
| customerTypeCode | String | M | The unique code of the following. • Individual • Business |  |
| name | String | M | The occupation of the customer. |  |
| status | String | M | The status of the record. note: Only records with status "Active" needs to be used |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

Note: The response may include records with `"status": "Inactive"`. These should be ignored. Only the data with `"status": "Active"` must be filtered and used.

## Response Details

```json
{
"transactionId": "8306125",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"customerOccupationTypeList": [
  {
  "id": 77,
  "code": "RHO011",
  "customerTypeCode": "100001",
  "name": "Cashier",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 79,
  "code": "RHO013",
  "customerTypeCode": "100001",
  "name": "Chef",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 80,
  "code": "RHO014",
  "customerTypeCode": "100001",
  "name": "Clerk",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 81,
  "code": "RHO015",
  "customerTypeCode": "100001",
  "name": "Consultant",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 82,
  "code": "RHO016",
  "customerTypeCode": "100001",
  "name": "Cook",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 83,
  "code": "RHO017",
  "customerTypeCode": "100001",
  "name": "Customer Service Executive",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 84,
  "code": "RHO018",
  "customerTypeCode": "100001",
  "name": "Dentist",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 85,
  "code": "RHO019",
  "customerTypeCode": "100001",
  "name": "Designer",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},
{
  "id": 86,
  "code": "RHO020",
  "customerTypeCode": "100001",
  "name": "Doctor",
  "status": "Active",
  "creationDate": "2025-03-19T17:23:54.415+0530"
},........
..........etc
]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
