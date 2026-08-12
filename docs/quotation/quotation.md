---
title: "Quotation"
sidebar_label: "Quotation"
slug: "/quotation/quotation"
description: "RHUB Quotation API — fetch the forex rate between payin and payout currencies."
---

# Quotation

<span className="rhub-method rhub-method--post">POST</span>

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/fxratequotation/api'}</code>
  </div>
</div>

The Quotation API is used to fetch the forex rate between the payin and payout currencies. This is an indicative price and transaction limit.

The Quotation API is used to generate a transaction quotation before initiating a payout. It provides an estimated cost, exchange rate, and payout amount based on the transaction parameters shared by the sender. This API ensures transparency by allowing users to view applicable rates, fees, and final payout values before confirming the actual transaction.

## Request Parameter

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| payinAmount | Numeric with decimal | 01 - 16 | C | The payin amount from the end sender. eg: 1500.56 either enter the payinAmount or payoutAmount |
| payoutAmount | Numeric with decimal | 01 - 16 | C | The amount that will be credited to the end receiver’s account. eg: 1500.56 either enter the payinAmount or payoutAmount |
| sendCurrencyCode | Alphanumeric with hyphens | 03 - 15 | M | The code of the currency in which the sender sends the money. eg: USD-USA, EUR |
| destinationCountryCode | Alpha | 03 | M | The 3-digit country code of the country in which the sender sends the money. eg: USA, SGP |
| receiveCurrencyCode | Alphanumeric with hyphens | 03 - 15 | M | The code of the currency in which the receiver receives the money. eg: USD-USA, EUR |
| serviceTypeCode | Alphanumeric | 03 | M | The following are the service types. eg: B2C • B2B • C2C • B2C • C2B • WPT |
| settlementCurrencyCode | Alphanumeric with hyphens | 03 - 15 | M | The code of the currency in which the settlement is done. eg: USD-USA, EUR |
| paymentMode | Alpha | 04 | M | The following modes that can be used for payment. eg: Cash • Cash • Bank |
| sourceCountry | Alpha | 03 | M | Sourcing Country's 3-digit Country Code. eg: USA, SGP |
| senderCode | Numeric | 10 | M | The send partner code. eg:1000009999 |
| customerCode | Numeric | 10 | O | The registered customer code. eg:1000008788 |
| chargeTypeCode | Alpha | 03 - 10 | O | Specifies which charge type has been chosen (BEN, SHA, or OUR), eg: BEN. |

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
      "customerCode": "1000008444",
      "chargeTypeCode": "OUR"
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
| sourceCountry | String | M | 3-digit Country Code |
| duration | String | M | Duration of fx quotation (in mins) |
| timeLeft | String | M | Remaining time for the quotation to get expire |
| paymentMode | String | M | The following modes that can be used for payment. <br /> • Cash <br /> •  Bank |
| sendClientMarginValue | String | M | The margin set by the send client |
| customerRegistrationAllowed | String | M | Customer registration service is enabled or not |
| chargeTypeCode | String | O | Types of charges |

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
"chargeTypeCode": "OUR",
"customerRegistrationAllowed": false
}
}
```

## Related APIs

- [Authentication](/docs/authentication/authentication)
- [Payout](/docs/payout/payout)
- [WPT Payout](/docs/payout/wpt-payout)
- [Final Quotation (unlinked source page)](/docs/legacy/final-quotation)
