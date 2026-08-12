---
title: "WPT Wallet List"
sidebar_label: "WPT Wallet List"
description: "RHUB WPT Wallet List master API."
---

# WPT Wallet List

<span className="rhub-method rhub-method--get">GET</span>

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/walletList/{countryCode}/{currencyCode}/{receiverCode}/WPT`

:::

The Wallet list API is used to fetch the list of WPT providers.

## Request Parameter

| Parameters      | Input Type | Length | Requirement | Description                                                                                                  |
|-----------------|:-----------:|:-----------:|:-----------:|--------------------------------------------------------------------------------------------------------------|
| countryCode | Alpha | 03 | M | The 3 digit country code of receiver. eg: USA, CHN |
| currencyCode | Alpha | 03 | M | The 3 digit currency code of receiver. eg: USD, CNY |
| recieverCode | Numeric | 10 | M | The 10-digit code of the payout partner, as provided in the `receiverCode` field of the Quotation API response. eg: 1000009909 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.X.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/walletList/CHN/CNY/100000****/WPT
```

## Response Parameter

| Parameters        |        Data Type | Requirement | Description                                                                 |
|-------------------|:----------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | The unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Wallet List** |  |  |  |
| walletName | String | M | To be passed in WPT payout API as service provider name along with service provider code. eg: ALIPAY-08601 |
| providerCode | String | M | The code which needs to be passed in WPT payout API as service provider code. eg: 08601 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"requestTime": "Tue Jan 28 13:10:40 IST 2025",
"responseTime": "Tue Jan 28 13:10:40 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction Successful",
 "walletListBeanList": [
    {
        "walletName": "ALIPAY",
        "providerCode": "08601"
    },
    {
        "walletName": "TENCENT",
        "providerCode": "08602"
    }
]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
