---
title: "Document ID Type"
sidebar_label: "Document ID Type"
description: "RHUB Document ID Type master API."
---

# Document ID Type

<span className="rhub-method rhub-method--get">GET</span>

*Source of truth: `master.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

[Go To Payout](/docs/payout/payout#transactioninfo-req-param)
[Go To WPT](/docs/payout/wpt-payout#transactioninfo-req-param)

:::info[Endpoint]

**For document id types**

`GET`  `http://host/ewallet/api/v1/getDocumentIdType/RHUB/{transactionType}`

:::

The Document ID Type API is used to fetch the list of all document types.

## Request Parameter of Document ID Types

| Parameters | Input Type | Length | Requirement | Description           |
|------------|:------------------:|:------------------:|:------------:|-----------------------|
| transactionType | Alphanumeric | 03 | M | The harmonized Transaction Type. Fixed default value B2C, B2B, C2C, C2B. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details of Document ID Types

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - host/ewallet/api/v1/getDocumentIdType/RHUB/C2C
```

## Response Parameter of Document ID Types

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Result** |  |  |  |  |
| data | String | M | Document name tag in DB |  |
| value | String | M | Document name |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details of Document ID Types

```json
{
"requestTime": "Tue Jan 28 16:33:00 IST 2025",
"responseTime": "Tue Jan 28 16:33:00 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"result": [
    {
        "data": "RHD010",
        "value": "CPF/Tax ID No"
    },
    {
        "data": "RHD009",
        "value": "Emirates ID"
    },
    {
        "data": "RHD008",
        "value": "GCC ID"
    },
    {
        "data": "RHD007",
        "value": "Residence Permit"
    },
    {
        "data": "RHD006",
        "value": "Senior Citizen card"
    },
    {
        "data": "RHD005",
        "value": "Citizenship Card"
    },
    {
        "data": "RHD004",
        "value": "Govt.ApprovedID"
    },
    {
        "data": "RHD003",
        "value": "Passport"
    },
    {
        "data": "RHD002",
        "value": "DrivingLicense"
    },
    {
        "data": "RHD001",
        "value": "National ID Card"
    }
]
}
```


## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
