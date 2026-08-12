---
title: "Source of Fund"
sidebar_label: "Source of Fund"
description: "RHUB Source of Fund master API."
---

# Source of Fund

<span className="rhub-method rhub-method--get">GET</span>

[Go To Payout](/docs/payout/payout#transactioninfo-req-param)
[Go To WPT](/docs/payout/wpt-payout#transactioninfo-req-param)

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/getSourceOfFund/RHUB/{transactionType}/{countryCode}'}</code>
  </div>
</div>

The Source of Fund API is used to fetch the source of the fund.

## Request Parameter

| Parameters      | Input Type |Length | Requirement | Description                                                                                                         |
|-----------------|:----------:|:----------:|:----------:|-----------------------------------------------------------------------------------------------------------------------|
| transactionType | Alphanumeric | 03 | M | The harmonized Transaction Type. Fixed default value B2C, B2B, C2C, C2B. |
| countryCode | Alpha | 03 | M | The country code of reciever. eg: ARE,IND |
*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/getSourceOfFund/RHUB/B2B/IND
```

## Response Parameter

| Parameters        |        Data Type | Requirement | Description                                                                 |
|-------------------|:-----------:|:------------:|-------------------------------------------------------------------------------|
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
"requestTime": "Tue Jan 28 13:18:40 IST 2025",
"responseTime": "Tue Jan 28 13:18:40 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"result": [
    {
        "data": "RHS005",
        "value": "SAVINGS | OTHERS"
    },
    {
        "data": "RHS004",
        "value": "LOTTERY | GIFT | INTEREST | DIVIDENDS | RENT"
    },
    {
        "data": "RHS003",
        "value": "LOAN | DONATIONS"
    },
    {
        "data": "RHS002",
        "value": "BUSINESS INCOME | FINAL SETTLEMENT"
    },
    {
        "data": "RHS001",
        "value": "SALARY"
    }
]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
