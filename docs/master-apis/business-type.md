---
title: "Business Type"
sidebar_label: "Business Type"
description: "RHUB Business Type master API."
---

# Business Type

<span className="rhub-method rhub-method--get">GET</span>

[Go To Payout](/docs/payout/payout#transactioninfo-req-param)

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/masterBusinessTypes/RHUB/{transactionType}'}</code>
  </div>
</div>

The Business API is used to fetch the Business type of customer.

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
GET http://host/ewallet/api/v1/masterBusinessTypes/RHUB/B2B
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
| name | String | M | The nature of the business run by the customer. |  |
| status | String | M | The status of the customer. |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |
| partnerCode | String | M | The unique code of payout partner (recieverCode). |  |
| serviceTypeCode | String | M | The transaction type code. eg: B2B. |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details of Nature of Business

```json
{
"transactionId": "9217725",
"requestTime": "Tue Jan 28 16:23:11 IST 2025",
"responseTime": "Tue Jan 28 16:23:11 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"masterBusinessTypesBeanList": [
    {
        "id": 654,
        "code": "RHT012",
        "name": "Others",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 653,
        "code": "RHT011",
        "name": "Professional Services",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 652,
        "code": "RHT010",
        "name": "Transportation and Logistics",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 651,
        "code": "RHT009",
        "name": "Real Estate",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 650,
        "code": "RHT008",
        "name": "Retail",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 649,
        "code": "RHT007",
        "name": "Manufacturing",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 648,
        "code": "RHT006",
        "name": "Information Technology",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 647,
        "code": "RHT005",
        "name": "Education",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 646,
        "code": "RHT004",
        "name": "Construction",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 645,
        "code": "RHT003",
        "name": "Banking",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 644,
        "code": "RHT002",
        "name": "Automotive",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    },
    {
        "id": 643,
        "code": "RHT001",
        "name": "Agriculture",
        "status": "Y",
        "creationDate": "2025-01-16T16:49:15.236+0530",
        "partnerCode": "RHUB",
        "serviceTypeCode": "B2B"
    }
]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
