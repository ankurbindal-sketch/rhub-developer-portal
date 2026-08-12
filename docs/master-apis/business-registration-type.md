---
title: "Business Registration Type"
sidebar_label: "Business Registration Type"
description: "RHUB Business Registration Type master API."
---

# Business Registration Type

<span className="rhub-method rhub-method--get">GET</span>

[Go To Payout](/docs/payout/payout#transactioninfo-req-param)

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/masterBusinessRegistrationTypes/RHUB/{transactionType}'}</code>
  </div>
</div>

The Business registration type API is used to fetch the registration type of business customers.

## Request Parameter

| Parameters | Input Type | Length | Requirement | Description            |
|------------|:-------------:|:-------------:|:------------:|------------------------|
| transactionType | Alphanumeric | 03 | M | The harmonized Transaction Type. Fixed default value B2C, B2B, C2C, C2B. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/masterBusinessRegistrationTypes/RHUB/B2B
```

## Response Parameter of Business Registration Type

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
| name | String | M | The nature of the business run by the customer. |  |
| status | String | M | The status of the customer. |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details of Business Registration Type

```json
{
"transactionId": "9217696",
"requestTime": "Tue Jan 28 16:15:34 IST 2025",
"responseTime": "Tue Jan 28 16:15:34 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"masterBusinessRegistrationTypesList": [
    {
        "id": 274,
        "code": "RHB007",
        "name": "BSC",
        "status": "Y",
        "creationDate": "2025-03-20T16:55:43.831+0530"
    },
    {
        "id": 259,
        "code": "RHB002",
        "name": "Corporation",
        "status": "Y",
        "creationDate": "2025-01-15T19:35:15.295+0530"
    },
    {
        "id": 271,
        "code": "RHB004",
        "name": "Govt. Entity",
        "status": "Y",
        "creationDate": "2025-03-20T16:55:43.831+0530"
    },
    {
        "id": 258,
        "code": "RHB001",
        "name": "Partnership",
        "status": "Y",
        "creationDate": "2025-01-15T19:35:15.295+0530"
    },
    {
        "id": 272,
        "code": "RHB005",
        "name": "Private ltd",
        "status": "Y",
        "creationDate": "2025-03-20T16:55:43.831+0530"
    },
    {
        "id": 270,
        "code": "RHB003",
        "name": "Proprietorship",
        "status": "Y",
        "creationDate": "2025-03-20T16:55:43.831+0530"
    },
    {
        "id": 273,
        "code": "RHB006",
        "name": "WLL",
        "status": "Y",
        "creationDate": "2025-03-20T16:55:43.831+0530"
    }
]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
