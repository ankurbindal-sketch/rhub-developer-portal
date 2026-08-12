---
title: "Transaction Inquiry API"
sidebar_label: "Transaction Inquiry API"
description: "RHUB Transaction Inquiry API (source page not linked in the live documentation sidebar)."
unlisted: true
---

# Transaction Inquiry API

<span className="rhub-method rhub-method--get">GET</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `transactionInquiry.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/transactionInfo/{parameter}?{fromDate}&{toDate}&{types}&{status}&{sendingPartnerCode}&{offset}&{limit}'}</code>
  </div>
</div>

The Transaction Inquiry API is used to fetch the statement for the specified period.

## Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| all | String | M | To fetch all the statement. |
| sendingPartner Code | String | M |  |
| offset | String | M | From where to fetch the data. |
| limit | String | M | The count of the record to be displayed in a single page. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET
https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/transactionInfo/all?
fromDate=2023-10-01&toDate=2023-10-27&types=all&status=all&sendingPartnerCode=1000008863&offset=0&limit=
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | The unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Pageable** |  |  |  |  |
| totalRecords | String | M | Count of the records. |  |
| **Transaction Info Response** |  |  |  |  |
| id | String | M |  |  |
| code | String | M |  |  |
| senderCode | String | M | The system generated sender code. |  |
| beneficiaryCode | String | M | The system generated beneficiary code. |  |
| transId | String | M |  |  |
| transTypeCode | String | M |  |  |
| senderUniqueId | String | M |  |  |
| sendingPartnerCode | String | M |  |  |
| payoutPartnerCode | String | M |  |  |
| sendingAmount | String | M |  |  |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |  |
| sourceCurrency | String | M |  |  |
| payoutCurrency | String | M | The currency in which money is credited to the end receiver’s bank account. |  |
| exchangeRate | String | M |  |  |
| types | String | M | The harmonized Transaction Type. Fixed default value in transfer or P2P for person to person transfers. B2B, and C2C. |  |
| description | String | M |  |  |
| paymentMode | String | M | The following modes that can be used for payment. • Cash • Cheque • Bank Account |  |
| paymentOption | String | M | The use of the Mobile Wallet or Account Credit. |  |
| fxQuoteid | String | M | The specific quote Id to be used for the transaction. This quote Id is generated when a quotation is created and it is returned on the quotation response. |  |
| remittancePurpose | String | M | Reason for the transfer like Investment. |  |
| sourceFund | String | M | Source of funds like Bank Deposit, Loan, and Revenue. |  |
| relationship | String | M | The relation between the sender and the receiver like Vendor, Employee, Employer, or Others. |  |
| resultCode | String | M | The code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| transactionStatus | String | M |  |  |
| creationDate | String | M |  |  |
| senderName | String | M | The name of the sender. |  |
| senderNumber | String | M | The mobile number of the sender. |  |
| beneficiaryName | String | M | The name of the beneficiary. |  |
| beneficiaryNumber | String | M | The mobile number of the beneficiary. |  |
| beneficiaryAccount No | String | M | Company Account number/IBAN |  |
| beneficiaryBankName | String | M | The name of the end customers/company bank from which send client/company received the money. |  |
| destinationCountry name | String | M | The name of the destination country to which the money is sent. |  |
| accountName | String | M | The name of the bank account holder. |  |
| statusName | String | M |  |  |
| payinCurrencyName | String | M | The name of the payin currency |  |
| payoutCurrencyName | String | M | The name of the payout currency |  |
| senderExchangeRate | String | M | The exchange rate valid for the sender. |  |
| settlementCurrency Code | String | M | The ISO code of the send client’s settlement currency. |  |
| settlementCurrency Name | String | M | The name of the send client’s settlement currency. |  |
| payoutSettlement Amount | String | M | The settlement amount payable to the beneficiary. |  |
| sendClientFee | String | M | The fee payable by the send client. |  |
| sendClientMarginValue | String | M | The margin of the send client. |  |
| beneficiaryAccount HolderName | String | M | The name of the beneficiary account holder. |  |
| transactionThrough | String | M | The name of the service provider. |  |
| sendClientCountry | String | M | The country of origin of the send client. |  |
| sendClientPhoneNumber | String | M | The mobile number of the send client. |  |
| initiatedUserName | String | M | The username through which the transaction was initiated. |  |
| sendClientAddress1 | String | M | The address of the send client. |  |
| sendClientAddress2 | String | M | The address of the send client. |  |
| txnProcessedBy | String | M | The name of the agent who processed the transaction. |  |
| sourceCountry | String | M | The name of the source country. |  |
| sourceCountryCode | String | M | The ISO country code of the source country. |  |
| receiverService ProviderCode | String | M | The code of the receiver’s service provider. |  |
| receiverService ProviderMobile | String | M | The name of the receiver’s service provider. |  |
| reverse | String | M | Use to identify whether the transaction is reverse transaction based on the following values. • False. The transaction is not reverse transaction. Therefore, it is a normal transaction. • True. The transaction is reverse transaction. Therefore, it is not a normal transaction. |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
   {

"requestTime": "Thu Aug 03 12:28:16 IST 2023",

"responseTime": "Thu Aug 03 12:28:17 IST 2023",

"resultCode": "0",

"resultDescription": "Transaction Successful",

"pageable": {

"totalRecords": 10

},

"transactionInfoResponse": [

{

"id": 347,

"code": "1000000395",

"senderCode": "1000000461",

"beneficiaryCode": "1000000462",

"transId": 197930,

"transTypeCode": "101442",

"senderUniqueId": "PAYAFMRF61",

"sendingPartnerCode": "1000008340",

"payoutPartnerCode": "1000008316",

"sendingAmount": 100000,

"payoutAmount": 10539,

"sourceCurrency": "100091",

"payoutCurrency": "100075",

"exchangeRate": 0.10539,

"types": "B2B",

"description": "Inv12345678",

"paymentMode": "Bank",

"paymentOption": "Account",

"fxQuoteid": "101436",

"remittancePurpose": "001-02",

"sourceFund": "01",

"relationship": "04",

"resultCode": "0",

"resultDescription": "Transaction Successfull",

"transactionStatus": "IP",

"creationDate": "2023-08-03 12:22:10",

"senderName": "HCL Technologies",

"senderNumber": "+265123456789",

"beneficiaryName": "HCL Software",

"beneficiaryNumber": "+81123456789",

"beneficiaryAccountNo": "1234567",

"beneficiaryBankName": "Mizuho Bank,Ltd.-0001",

"destinationCountryname": "Japan",

"payinCurrencyName": "MWK",

"payoutCurrencyName": "JPY",

"senderExchangeRate": 0.10328,

"settlementCurrencyCode": "100003",

"payoutSettlementAmount": 101.45,

"sendClientFee": 100.0,

"reverse": false,

},

{

"id": 344,

"code": "1000000392",

"senderCode": "1000000457",

"beneficiaryCode": "1000000458",

"transId": 197920,

"transTypeCode": "101442",

"senderUniqueId": "PAY532BLG5",

"sendingPartnerCode": "1000008340",

"payoutPartnerCode": "1000008316",

"sendingAmount": 100000,

"payoutAmount": 10539,

"sourceCurrency": "100091",

"payoutCurrency": "100075",

"exchangeRate": 0.10539,

"types": "B2B",

"description": "IN",

"paymentMode": "Cash",

"paymentOption": "Account",

"fxQuoteid": "101424",

"remittancePurpose": "001-01",

"sourceFund": "01",

"relationship": "04",

"resultCode": "0",

"resultDescription": "Transaction Successfull",

"transactionStatus": "IP",

"creationDate": "2023-08-02 18:02:45",

"senderName": "EMQ Corp",

"senderNumber": "+265656434343",

"beneficiaryName": "Emcure Corp",

"beneficiaryNumber": "+81656232333",

"beneficiaryScreeningScore": 0.0,

"beneficiaryAccountNo": "1234567",

"beneficiaryBankName": "Mizuho Bank,Ltd.-0001",

"destinationCountryname": "Japan",

"statusName": "Pass",

"payinCurrencyName": "MWK",

"payoutCurrencyName": "JPY",

"senderExchangeRate": 0.10328,

"settlementCurrencyCode": "100004",

"payoutSettlementAmount": 101.45,

"sendClientFee": 100.0,

"reverse": false

},

]

}
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
