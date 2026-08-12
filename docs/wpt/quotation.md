---
title: "WPT — Quotation"
sidebar_label: "Quotation"
description: "RHUB WPT Quotation API."
---

# WPT — Quotation

<span className="rhub-method rhub-method--post">POST</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `WPT.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `http://host/ewallet/api/v1/fxratequotation/api`

:::

The Quotation API is used to fetch the forex rate between the payin and payout currencies. This is an indicative price and transaction limit.

## Request Parameter

| Parameters     | Data Type  | Requirement | Description |
|----------|:---------:|:-------:|--------|
| payinAmount | String | C | The payin amount from the end sender. |
| payoutAmount | String | C | The amount that will be credited to the end receiver’s account. |
| sendCurrencyCode | String | M | The code of the currency in which the sender sends the money. |
| destinationCountryCode | String | M | The code of the country in which the sender sends the money. |
| receiveCurrencyCode | String | M | The code of the currency in which the receiver receives the money. |
| serviceTypeCode | String | M | The following are the service types<br /> • B2B<br /> • C2C<br /> • B2C<br /> • C2B<br /> • WPT |
| settlementCurrencyCode | String | M | The code of the currency in which the settlement is done. |
| paymentMode | String | M | The following modes that can be used for payment.<br /> • Cash <br /> • Bank Account |
| sourceCountry | String | M | Country ISO Code |
| senderCode | String | M | The send partner code |
| customerWalletDebit | Boolean | O | true, false |
| customerCode | String | O | The registered customer code. (If customerWalletDebit is true, than it's mandatory.) |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/fxratequotation/api
{
      "payinAmount": "80",
      "payoutAmount": "",
      "sendCurrencyCode": "USD-USA",
      "destinationCountryCode": "HKG",
      "receiveCurrencyCode": "HKD",
      "settlementCurrencyCode": "USD-USA",
      "paymentMode": "Cash",
      "sourceCountry": "HKG",
      "senderCode": "1000008444",
      "serviceTypeCode": "B2B",
      "customerCode": "1000008444"
}
```

## Response Parameter

| Parameters     | Data Type  | Requirement | Description |
|----------|:-----:|:-----------:|--------|
| transactionId | String | M | The transaction ID. |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime |  |  | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | The code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Forex Rate Quotation** |  |  |  |
| Code | String | M | The specific quote Id to be used for the transaction. This quote Id is generated when a quotation is created and it is returned on the quotation response. |
| fxRateValue | String | M | Current exchange rate w.r.t to the sending currency and receive currency. |
| senderMargin | String | M | The margin of send partner. (In case of 0 it will reflect the fxRateValue) |
| senderCode | String | M | The send partner code |
| receiverCode | String | M | The payout partner code |
| sendCurrencyCode | String | M | The code of the currency in which the sender transferred or sent the money to the receiver. |
| receiveCurrencyCode | String | M | The code of the currency in which the receiver will receive the money. |
| sendCurrencyName | String | M | The name of the currency in which the sender sends the money. |
| receiveCurrencyName | String | M | The name of the currency in which the receiver receives the money. |
| validityPeriod | String | M | The duration up to when the exchange rate is valid. The duration or validity can be in minutes, hours, days, or months. |
| payinAmount | String | M | The payin amount from the end sender. |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |
| fee | String | M | The fee applied by us |
| senderClientFee | String | M | The fee set by the send client |
| sourceCountry | String | M | ISO Code |
| duration | String | M | Duration of fx quotation (in mins) |
| timeLeft | String | M | Remaining time for the quotation to get expire |
| paymentMode | String | M | The following modes that can be used for payment. <br /> • Cash <br /> • Bank Account |
| sendClientMarginValue | String | M | The margin set by the send client |
| customerRegistrationAllowed | String | M | Customer registration service is enabled or not |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"transactionId": "7558887",
"requestTime": "Thu Aug 03 11:57:04 IST 2023",
"responseTime": "Thu Aug 03 11:57:05 IST 2023",
"resultCode": "0",
"resultDescription": "Transaction Successful",
"fxRateQuotation": {
"code": "106244",
"fxRateValue": "469.4200000000",
"senderMargin": "469.4200000000",
"senderCode": "1000008444",
"receiverCode": "1000008397",
"sendCurrencyCode": "100003",
"receiveCurrencyCode": "100106",
"sendCurrencyName": "USD-USA",
"receiveCurrencyName": "NGN",
"validityPeriod": "1970-01-01T05:30:00.005+0530",
"payinAmount": "21.30",
"payoutAmount": "10000.00",
"fee": "2.0",
"senderClientFee": "0.0",
"duration": 5,
"timeLeft": 1,
"paymentMode": "Cash",
"sendClientMarginValue": "0.0",
"customerRegistrationAllowed": false
}
}
```

## Related APIs

- [WPT overview](/docs/wpt)
- [WPT Payout (published)](/docs/payout/wpt-payout)
- [WPT Wallet List (master)](/docs/master-apis/wpt-wallet-list)
