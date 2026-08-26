---
title: "Remittance Purpose"
sidebar_label: "Remittance Purpose"
description: "RHUB Remittance Purpose master API."
---

# Remittance Purpose

<span className="rhub-method rhub-method--get">GET</span>

[Payout API](/docs/payout/payout#transactioninfo-req-param)
[WPT Payout API](/docs/payout/wpt-payout#transactioninfo-req-param)

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/purposeOfRemittance/RHUB/{transactionType}/{countryCode}'}</code>
  </div>
</div>

The Remittance Purpose API is used to fetch the purpose to send the remittance.

## Request Parameter

| Parameters      | Input Type | Length | Requirement | Description                                                                                                  |
|-----------------|:-----------:|:-----------:|:-----------:|--------------------------------------------------------------------------------------------------------------|
| transactionType | Alphanumeric | 03 | M | The harmonized Transaction Type. Fixed default value B2C, B2B, C2C, C2B. |
| countryCode | Alpha | 03 | M | The country code of reciever. eg: ARE,IND |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.X.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/purposeOfRemittance/RHUB/B2B/ARE
```

## Response Parameter

| Parameters        |        Data Type | Requirement | Description                                                                 |
|-------------------|:----------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | The unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Result** |  |  |  |
| Result - data | String | M |  |
| Result - value | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"requestTime": "Tue Jan 28 13:10:40 IST 2025",
"responseTime": "Tue Jan 28 13:10:40 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction Successful",
"result": [
    {
        "data": "RHP002",
        "value": "INVESTMENT | BUSINESS PROFITS | SAVINGS"
    },
    {
        "data": "RHP001",
        "value": "MAINTENANCES | BUSINESS EXPENSES"
    },
    {
        "data": "RHP004",
        "value": "OTHER EXPENSES | SALARY PAYMENTS"
    },
    {
        "data": "RHP003",
        "value": "TRADE | SERVICE PAYMENTS"
    }
]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
