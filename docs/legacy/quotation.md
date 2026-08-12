---
title: "Quotation API"
sidebar_label: "Quotation API"
description: "RHUB Quotation API (source page not linked in the live documentation sidebar)."
---

# Quotation API

<span className="rhub-method rhub-method--post">POST</span>

*Source of truth: `quotation.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `quotation.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/fxratequotation`

:::

The Quotation API is used to fetch the forex rate between the payin and payout currencies. This is an indicative price and transaction limit.

## Request Parameter

| Parameters     | Data Type  | Requirement | Description |
|----------|:---------:|:-------:|--------|
| payinAmount | String | C | The payin amount from the end sender. |
| payoutAmount | String | C | The amount that will be credited to the end receiver’s account. |
| sendCurrencyCode | String | M | The code of the currency in which the sender sends the money. |
| receiveCurrencyCode | String | M | The code of the currency in which the receiver receives the money. |
| serviceTypeCode | String | M | The following are the service types<br /> • B2B<br /> • C2C<br /> • B2C<br /> • C2B<br /> • WPT |
| settlementCurrencyCode | String | M | The code of the currency in which the settlement is done. |
| paymentMode | String | M | The following modes that can be used for payment.<br /> • Cash <br /> • Cheque <br /> • Bank Account |
| sourceCountry | String | M | Country ISO Code |
| senderCode | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/fxratequotation
{
    "payinAmount": "100000",
    "payoutAmount": "",
    "sendCurrencyCode": "MWK",
    "receiveCurrencyCode": "JPY",
    "serviceTypeCode": "B2B"
    "settlementCurrencyCode": "USD-USA",
    "paymentMode": "Cash",
    "SourceCountry": "IN",
    "senderCode": "1000008340"
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
| senderCode | String | M |  |
| receiverCode | String | M |  |
| sendCurrencyCode | String | M | The code of the currency in which the sender transferred or sent the money to the receiver. |
| receiveCurrencyCode | String | M | The code of the currency in which the receiver will receive the money. |
| sendCurrencyName | String | M | The name of the currency in which the sender sends the money. |
| receiveCurrencyName | String | M | The name of the currency in which the receiver receives the money. |
| transactionLimit | String | M | To fetch the minimum or maximum transaction limit based on the currency for the client. |
| validityPeriod | String | C | The duration up to when the exchange rate is valid. The duration or validity can be in minutes, hours, days, or months. |
| payinAmount | String | C | The payin amount from the end sender. |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |
| settlementCurrencyCode | String | M |  |
| settlementAmount | String | M |  |
| senderClientFee | String | M | The fee payable by the send client |
| sourceCountry | String | M | ISO Code |
| duration | String | M |  |
| timeLeft | String | M |  |
| paymentMode | String | M | The following modes that can be used for payment. <br /> • Cash <br /> • Cheque <br /> • Bank Account |

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
"code": "101427",
"fxRateValue": "0.10539",

"senderCode": "1000008340",
"receiverCode": "1000008316",
"sendCurrencyCode": "100091",
"receiveCurrencyCode": "100075",
"sendCurrencyName": "MWK",
"receiveCurrencyName": "JPY",
  " transactionLimit ": "1000000",
"validityPeriod": "1970-01-01T05:30:00.004+0530",
"payinAmount": "100000.0",
"payoutAmount": "10328.0",
"settlementCurrencyCode": "100003",
"settlementAmount": 101.45,

"senderClientFee": "100.0",
"duration": 4,
"timeLeft": 1,
"paymentMode": "Cash"
}
     }
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
