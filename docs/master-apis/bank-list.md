---
title: "Bank List"
sidebar_label: "Bank List"
description: "RHUB Bank List master API."
---

# Bank List

<span className="rhub-method rhub-method--get">GET</span>

*Source of truth: `master.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/payoutbanklist/{country}/{currency}/{recieverCode}`

:::

The Bank List API is used to fetch the list of the bank.

## Request Parameter

| Parameters | Input Type | Length | Requirement | Description            |
|------------|:--------------:|:---------:|:------------:|------------------------|
| country | Alpha | 03 | M | The 3 digit country code of receiver. eg: USA, IND |
| currency | Alpha | 03 | M | The 3 digit currency code of receiver. eg: USD, EUR |
| recieverCode | Numeric | 10 | M | The 10-digit code of the payout partner, as provided in the `receiverCode` field of the Quotation API response. eg: 1000009909 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/payoutbanklist/NGA/NGN/1000008397
```

## Response Parameter

| Parameters        |        Data Type | Requirement | Description                                                                 |
|-------------------|:---------------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | Unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Result** |  |  |  |
| Result - data/code/locationId | String | M | **locationId** - To be used in the Payout request receiver section under tags `businessBankCountry/receiverBankCountry` <br /> **code** - To be used in the Payout request receiver section under tags `businessBankCode/receiverBankCode` |
| Result - value/name | String | M | To be used in the Payout request receiver section under tags `businessBankName/receiverBankName` |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

The response of the Bank List API may differ depending on the correspondent’s configuration or integration settings.

```json
{
"transactionId": "7915642",
"requestTime": "Tue Feb 04 12:09:50 IST 2025",
"responseTime": "Tue Feb 04 12:09:51 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
// The response structure may vary depending on the correspondent.
// For certain correspondents, the response may include the following tags(name,code).
"banksList": [
    {
        "code": "FEDUNGLA",
        "name": "FEDERAL UNIVERSITY DUTSE MFB"
    },
    {
        "code": "OLCKNGLA",
        "name": "Oluchukwu MFB"
    },
    {
        "code": "MKUDNGLA",
        "name": "Mkudi"
    },
    {
        "code": "VISANGLA",
        "name": "Visa Microfinance Bank"
    },
    {
        "code": "MONMNGLA",
        "name": "Money Trust Microfinance Bank"
    },
    {
        "code": "TAJJNGLA",
        "name": "Taj Bank"
    },
    {
        "code": "BNXMNGLA",
        "name": "BANEX Microfinance Bank"
    },
    {
        "code": "LAPMNGLA",
        "name": "Lapo Microfinance Bank"
    },
]

// For certain correspondents, the response may include the following tags(name,locationId).
"banksList": [
{
    "name": "AIRLINE FINANCIAL CREDIT UNION LIMITED",
    "locationId": "CANAir9839"
},
{
    "name": "ALBERTA TREASURY BRANCHES",
    "locationId": "CANAlb9743"
},
{
    "name": "ALL TRANS FINANCIAL SERVICES CREDIT UNION LIMITED",
    "locationId": "CANAll9834"
},
{
    "name": "ALLIANCE DES CAISSES POPULAIRES DE L'ONTARIO LIMITÃ‰E",
    "locationId": "CANAll9849"
},
{
    "name": "ALTERNA SAVINGS AND CREDIT UNION",
    "locationId": "CANAlt9842"
},
{
    "name": "AMEX BANK OF CANADA",
    "locationId": "CANAme9759"
},
{
    "name": "ARNSTEIN COMMUNITY CREDIT UNION LIMITED",
    "locationId": "CANArn9827"
},
{
    "name": "ATLANTIC CENTRAL",
    "locationId": "CANAtl9841"
},
{
    "name": "B2B BANK (FORMERLY B2B TRUST)",
    "locationId": "CANB2B9818"
},
{
    "name": "BANK OF AMERICA, NATIONAL ASSOCIATION",
    "locationId": "CANBan9745"
},
]
}
```


## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
