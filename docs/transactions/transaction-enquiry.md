---
title: "Transaction Enquiry"
sidebar_label: "Transaction Enquiry"
description: "RHUB Transaction Enquiry API — check the status of a previously initiated payout."
---

# Transaction Enquiry

<span className="rhub-method rhub-method--get">GET</span>

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/transactionInfo/api?types=all&status=all&transId={value}'}</code>
  </div>
</div>

The Transaction Enquiry API is used to fetch the statement for the specified period.

## Request Parameter

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| value | Numeric | 06 | M | To get the details of specific transaction, use the transaction Id in value. eg: 123456 (The trans Id recieved after successful payout) |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET
http://host/ewallet/api/v1/transactionInfo/api?types=all&status=all&transId=1***90
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
| settlementCurrency Code | String | M | The 3-digit Currency code of the send client’s settlement currency. |  |
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
| sourceCountryCode | String | M | The 3-digit Country Code of the source country. |  |
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
    "totalRecords": 1
},
"transactionInfoResponse": [
    {
        "id": 3314,
        "code": "1000003416",
        "senderCode": "1000001716",
        "beneficiaryCode": "1000001717",
        "transId": 351159,
        "transTypeCode": "101442",
        "senderUniqueId": "PAYXPY29FF",
        "sendingPartnerCode": "1000008444",
        "payoutPartnerCode": "1000008437",
        "sendClientName": "Wirease",
        "sendingAmount": 100.35,
        "payoutAmount": 98.34,
        "sourceCurrency": "100003",
        "payoutCurrency": "100461",
        "senderFee": 2.0,
        "payoutFee": 0.0,
        "exchangeRate": 0.98,
        "types": "C2C",
        "paymentMode": "Bank",
        "fxQuoteid": "110503",
        "remittancePurpose": "Foreign direct investment - all other types",
        "sourceFund": "Savings",
        "relationship": "Friend",
        "resultCode": "0",
        "resultDescription": "Transaction Successful",
        "vendorResultCode": "200",
        "vendorResultDescription": "pending_approval",
        "transactionStatus": "IP",
        "creationDate": "2025-02-06 13:30:48",
        "senderScreeningScore": 0.0,
        "senderName": "RamKrishna S S Kumar",
        "beneficiaryName": "Yashpal Singh",
        "beneficiaryScreeningScore": 0.0,
        "beneficiaryAccountNo": "00110260000959024298678",
        "beneficiaryBankName": "HDFC Bank",
        "destinationCountryname": "India",
        "accountName": "Yashpal Singh",
        "statusName": "Payout Processing",
        "payinCurrencyName": "USD-USA",
        "payoutCurrencyName": "USD-GLOBAL",
        "senderScreeningStatus": "Screening Pass",
        "receiverScreeningStatus": "Screening Pass",
        "senderExchangeRate": 0.98,
        "settlementCurrencyCode": "100003",
        "settlementCurrencyName": "USD-USA",
        "settlementCurrencyExactName": "USD-USA",
        "payoutSettlementAmount": 98.34,
        "sendClientFee": 0.0,
        "sendClientMarginValue": 0.0,
        "beneficiaryAccountHolderName": "Yashpal Singh",
        "transactionThrough": "api",
        "sendClientCountry": "Hong Kong",
        "sendClientPhoneNumber": "+85223112745",
        "initiatedUserName": "Wirease",
        "sendClientAddress1": "Hongkong, Hongkong",
        "sendClientAddress2": "Tuen mun, Yau Tsim Mong, Hong Kong",
        "txnProcessedBy": "1000008444",
        "sourceCountry": "Hong Kong",
        "sourceCountryCode": "HKG",
        "beneficiariesId": "c60a4733-c7ab-41fd-a291-76f925f0b62c",
        "beneficiariesAccountId": "77c406d1-7925-4220-bee6-876d547fd443",
        "customerId": "100000844410791I",
        "customerSenderCode": "1000000789",
        "tax": 0.0,
        "txnApprovedBy": "1000008444",
        "txnApprovedByName": "Wirease",
        "receiverSwiftCode": "BARCGB22",
        "settlementcurrency": "100003",
        "amountReceivedFromCustomer": 0.0,
        "balanceToBePaid": 0.0,
        "payoutProcessCode": "1000002365",
        "state": "NA",
        "reverse": false
    }
    ]
  }
```

## Related APIs

- [Payout](/docs/payout/payout)
- [Transaction status codes](/docs/errors/transaction-status-codes)
- [Balance Enquiry](/docs/balance/balance-enquiry)
- [Integration flow](/docs/getting-started/integration-flow)
