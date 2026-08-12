---
title: "Final Quotation API"
sidebar_label: "Final Quotation API"
description: "RHUB Final Quotation API (source page not linked in the live documentation sidebar)."
unlisted: true
---

# Final Quotation API

<span className="rhub-method rhub-method--post">POST</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `finalQuotation.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/fxratequotation`

:::

The Quotation API is used to fetch the forex rate between the payin and payout currencies. This is the final price.

## Request Parameter

| Parameters     | Data Type | Requirement | Description |
|----------|:-------------:|:-----:|--------|
| requestDate | String | M | This is the requested date and time in the YYYY-DD-MM HH:MM:SS |
| payinAmount | String | C | The payin amount from the end sender. |
| payoutAmount | String | C | The amount that will be credited to the end receiver’s account. |
| sendCurrencyCode | String | M | The code of the currency in which the sender sends the money. |
| destinationCountryCode | String | M | The code of the country where the money is sent or transferred. |
| receiveCurrencyCode | String | M | The code of the currency in which the receiver receives the money. |
| settlementCurrencyCode | String | M | The code of the currency in which the settlement is done. |
| paymentMode | String | M | The following modes that can be used for payment.<br /> • Cash <br /> • Cheque <br /> • Bank Account |
| senderCode | String | M |  |
| receiverCode | String | M |  |
| serviceTypeCode | String | M | The following are the service types<br /> • B2B<br /> • C2C<br /> • B2C<br /> • C2B<br /> • WPT |
| senderMobile | String | O | The mobile number of the sender sending the money. |
| beneficiaryMobile | String | C | The mobile number of the beneficiary in case of wallet payout (WPT). |
| beneficiaryName | String | M | The name of the beneficiary. |
| beneficiarybankAccount | String | M | The bank account number of the beneficiary. |
| beneficiarybankName | String | M | The name of the bank where the beneficiary has the account. |
| beneficiarybankCode | String | M | The code of the bank where the beneficiary has the account. |
| beneficiarybanksubCode | String | M | The sub code of the bank where the beneficiary has the account. |
| beneficiaryWalletProvider | String | C | The name of the wallet provider of the beneficiary.(in case of wallet payout (WPT)) |
| beneficiaryaccountType | String | O | The type of the account of the beneficiary. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/fxratequotation
{
    "requestDate: "2017-05-03 11:00:00"
    "payinAmount": "",
    "payoutAmount": "120",
    "sendCurrencyCode": "USD-USA",
    "destinationCountryCode": "CHN",
    "receiveCurrencyCode": "USD-CHINA",
    "settlementCurrencyCode": "USD-USA",
    "paymentMode": "Cash",
    "senderCode": "1000008867",
    "receiverCode": "1000008853",
    "serviceTypeCode": "B2B"
    "senderMobile - 9899075658
    "beneficiaryMobile -9899075658
    "beneficiaryName - Lily Esatate
    "beneficiarybankAccount - 017777777777777777
    "beneficiarybankName -
    "beneficiarybankCode -
    "beneficiarybanksubCode -
    "beneficiaryWalletProvider -
    "beneficiaryaccountType -
}
```

## Response Parameter

| Parameters     | Data Type | Requirement | Description |
|----------|:-----:|:------------:|--------|
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
| validityPeriod | String | M | The duration up to when the exchange rate is valid. The duration or validity can be in minutes, hours, days, or months. |
| payinAmount | String | M | The payin amount from the end sender. |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |
| sendClientFee | String | M | The fee payable by the send client. |
| settlementCurrencyCode | String | M |  |
| settlementAmount | String | M |  |
| duration | String | M |  |
| timeLeft | String | M |  |
| paymentMode | String | M | Type of payment i.e. bank account or mode using the swift network. The following modes that can be used for payment. <br /> • Cash <br /> • Cheque <br /> • Bank Account |
| quoteid | String | M |  |
| quotestatus | String | M |  |
| senderMobile | String | M | The mobile number of the sender. |
| beneficiaryMobile | String | M | The mobile number of the beneficiary. |
| beneficiaryName | String | M | The name of the beneficiary. |
| beneficiarybankAccount | String | M | The bank account number of the beneficiary. |
| beneficiarybankName | String | M | The name of the bank where the beneficiary has the account. |
| beneficiarybankCode | String | M | The code of the bank where the beneficiary has the account. |
| beneficiarybanksubCode | String | M | The sub code of the bank where the beneficiary has the account. |
| beneficiaryWalletProvider | String | M | The name of the wallet provider of the beneficiary. |
| beneficiaryaccountType | String | M | The type of the account of the beneficiary. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
   {
   "transactionId": "8301725",
   "requestTime": "Thu Apr 18 13:07:22 IST 2024",
   "responseTime": "Thu Apr 18 13:07:28 IST 2024",
   "resultCode": "0",
   "resultDescription": "Transaction successful",
   "fxRateQuotation": {
       "code": "107880",
       "fxRateValue": "81.3105999999",

       "senderCode": "1000008852",
       "receiverCode": "1000008853",
       "sendCurrencyCode": "100003",
       "receiveCurrencyCode": "100069",
       "sendCurrencyName": "USD-USA",
       "receiveCurrencyName": "INR",
       " transactionLimit ": "1000000",
       "validityPeriod": "1970-01-01T05:30:00.004+0530",
       "payinAmount": "1.1068667553813485",
       "payoutAmount": "90.0",
       "sendClientFee":"",
        "settlementCurrencyCode": "100003",
        "settlementAmount": 101.45,

       "duration": 4,
       "timeLeft": 1,
       "paymentMode": "Cash",
"quoteid" : "11ww122ssssss"
"quotestatus" : "success / fail"

"senderMobile - 9899075658
 	"beneficiaryMobile -9899075658
 	"beneficiaryName - Lily Esatate
 	"beneficiarybankAccount - 017777777777777777
 	"beneficiarybankName -
 	"beneficiarybankCode -
 	"beneficiarybanksubCode -
 	"beneficiaryWalletProvider -
 	"beneficiaryaccountType -

   }
   }
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
