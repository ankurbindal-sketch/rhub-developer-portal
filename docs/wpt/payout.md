---
title: "WPT — Payout"
sidebar_label: "Payout"
description: "RHUB WPT Payout API."
---

# WPT — Payout

<span className="rhub-method rhub-method--post">POST</span>

*Source of truth: `WPT.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `WPT.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `http://host/ewallet/api/v1/payoutProcess/api`

:::

The Payout API is used to perform all types of transactions (B2B,C2C,C2B,B2C).

## Request Parameter  B2B (already registered)

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| **Payout : TransactionInfo** |  |  |  |  |
| payinAmount | String | M | The payin amount from the end sender. |  |
| payinCurrency | String | M | The payin or local currency from the end sender. |  |
| type | String | M | The harmonized Transaction Type. Fixed default value B2C B2B, and C2C, C2B. |  |
| requestDate | String | M | dd-mm-yyyy |  |
| sendClient TrxReference | String | M | The RHUB's transaction reference number. |  |
| paymentMode | String | M | The following modes that can be used for payment. • Cash • Bank |  |
| sendClientCode | String | M | The send client’s transaction reference number. |  |
| payoutCurrency | String | M | The currency in which money is credited to the end receiver’s bank account. |  |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |  |
| destinationCountryCode | String | M | The country code of reciever end. |  |
| settlement Currency | String | M |  |  |
| source Country | String | M | Country from where payment is initiated |  |
| fxRateValue | String | M | The current exchange rate w.r.t to the sending currency and receive currency. |  |
| senderMargin | String | M | Margin applied by sending partner |  |
| **Sender : Business** |  |  |  |  |
| isAutoRegistered | String | M | false |  |
| declaration | String | M |  |  |
| docReferenceNumber | String | M |  |  |
| customerCode | String | M | The respective code recieved after successful Customer registration. |  |
| customerWalletDebit | Boolean | M | true |  |
| **Receiver: Business (for saved receiver)** |  |  |  |  |
| recieverCode | String | M | The respective beneficiary code. |  |
| **Receiver: Business (for new receiver)** |  |  |  |  |
| businessName | String | M | The name of the end customer/send business entity sending money. |  |
| businessType | String | M | Type of registration like Partnership, Corporation, Cooperative. |  |
| businessRegistration Type | String | M |  |  |
| businessRegistration IssuedAt | String | M | This is the specific location or jurisdiction where a business registration was issued. |  |
| businessAddress1 | String | M | Company Register Address 1. (Special characters not allowed) |  |
| businessAddress State | String | M | Company Register State. |  |
| businessAddresss City | String | M | Company Register City. |  |
| businessPrimary ContactNumber | String | M | Company Primary Mobile number/Phone number. |  |
| businessCountry Code | String | M | The three-letter country code that represents the country of origin or registration for a company. Like USA, MWI . |  |
| businessAccount Number | String | M | Company Account number/IBAN. |  |
| businessAccount HolderName | String | M | The account name of the end customer/sender company from where the amount is sent to the RHUB send client. |  |
| businessBankName | String | M | The name of the end customer/Company bank to which end client/company receive the money. (Please enter valid receiver bank details for a successful transaction) |  |
| businessBankCode | String | O | Bank Identification Number (BIN). |  |
| businessSwiftCode | String | M | It's a unique alphanumeric code used to identify a specific bank or financial institution in international financial transactions. |  |
| **Compliance** |  |  |  |  |
| forexQuoteId | String | M | The specific quote Id to be used for the transaction. This quote Id is generated when a quotation is created and it is returned on the quotation response. ("code" obtained in quotation api response) |  |
| remittancePurpose | String | M | Reason for the transfer like Investment. |  |
| sourceOfFund | String | M | Source of funds like Bank Deposit, Loan, and Revenue. |  |
| relationship | String | M | The relation between the sender and the receiver like Vendor, Employee, Employer, or Others. |  |

## Request Details  B2B (already registered)

```json
{
"payout": {
  "transactionInfo": {
      "payinAmount": 122.22,
      "payinCurrency": "USD-USA",
      "type": "B2B",
      "requestDate": "17-01-2025",
      "sendClientTrxReference": "ASDEWEDE66",
      "paymentMode": "Cash",
      "paymentOption": "Account",
      "sendClientCode": "1000008929",
      "payoutCurrency": "USD-GLOBAL",
      "payoutAmount": "121.00",
      "destinationCountryCode": "ARE",
      "settlementCurrency": "USD-USA",
      "sourceCountry": "MWI",
      "fxRateValue": "0.99",
      "senderMargin": "0.99"
  },
  "sender": {
      "business": {
          "isAutoRegistered": false,
          "declaration": false,
          "docReferenceNumber": "CUSPXWWVD0",
          "customerCode": "1000002225"
          }
  },
  "receiver": {
      // for saved receiver
      "business": {
          "receiverCode": "1000004860"
      }
       // for new receiver
      "business": {
         "businessName": "Gujarat titans",
         "businessType": "Corporation",
         "businessRegistrationType": "Corporation",
         "businessRegistrationIssuedAt": "ARE",
         "businessAddress1": "new delhi new",
         "businessAddressState": "new delhi",
         "businessAddresssCity": "new delhi",
         "businessPrimaryContactNumber": "+9719899998988",
         "businessCountryCode": "ARE",
         "businessAccountNumber": "AE110260000959024298101",
         "businessAccountHolderName": "Gujarat titans ",
         "businessBankName": "Emirates NBD",
         "businessBankCode": "",
         "businessSwiftCode": "EBILAEAD"
      }
  },
  "compliance": {
      "forexQuoteId": "115225",
      "remittancePurpose": "RHP002",
      "sourceOfFund": "RHS005",
      "relationship": "RHR003"
  }
}
}
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| requestTime | String | M |  |  |
| responseTime | String | M |  |  |
| resultCode | String | M | The unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **PayoutResponseBean** |  |  |  |  |
| transReference | String | M |  |  |
| payinDate | String | M | The payin date or transaction creation date. |  |
| clientReference Number | String | M |  |  |
| sendClientCode | String | M |  |  |
| senderName | String | M | The name of the sender. |  |
| senderNumber | String | M | The mobile number of the sender. |  |
| beneficiaryName | String | M | The name of the beneficiary. |  |
| beneficiaryNumber | String | M | The mobile number of the beneficiary. |  |
| beneficiaryBank | String | M | The name of the end customers/company bank from which send client/company received the money. |  |
| accountNumber | String | M | Company Account number/IBAN |  |
| payinCurrency | String | M | The payin or local currency from the end sender. |  |
| payinAmount | String | M | The payin amount from the end sender. |  |
| payoutCurrency | String | M | The currency in which money is credited to the end receiver’s bank account. |  |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |  |
| serviceType | String | M | The harmonized Transaction Type. Fixed default value in transfer or P2P for person to person transfers. B2B. |  |
| status | String | M |  |  |
| senderMargin | String | M |  |  |
| sendClientMarginValue | String | M |  |  |
| beneficiaryAccountHolderName | String | M |  |  |
| sendClientName | String | M |  |  |
| senderCountry | String | M |  |  |
| sendClientPhoneNumber | String | M |  |  |
| sendClientAddress1 | String | M |  |  |
| customerId | String | M |  |  |
| customerCode | String | M |  |  |
| paymentMode | String | M | Cash/Bank |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"requestTime": "Thu Aug 03 12:22:10 IST 2023",
"responseTime": "Thu Aug 03 12:22:10 IST 2023",
"resultCode": "0",
"resultDescription": "Transaction Successful",
"payoutResponseBean": {
"transReference": "197930",
"payinDate": "2023-08-03T12:22:10.904+0530",
"clientReferenceNumber": "PAYAFMRF61",
"sendClientCode": "1000008340",
"senderName": "HCL Technologies",
"senderNumber": "+265123456789",
"beneficiaryName": "HCL Software",
"beneficiaryNumber": "+81123456789",
"beneficiaryBank": "Mizuho Bank,Ltd.-0001",
"accountNumber": "1234567",
"payinCurrency": "MWK",
"payinAmount": 100000.0,
"payoutCurrency": "JPY",
"payoutAmount": 10328.0,
"serviceType": "B2B",
"status": "In Process",
"senderMargin": 0.9899999999,
"sendClientMarginValue": 0.0,
"beneficiaryAccountHolderName": "Gujarat titans ",
"sendClientName": "ESTEL",
"senderCountry": "Malawi",
"sendClientPhoneNumber": "+26533545636654",
"sendClientAddress1": "Malawi, Malawi",
"customerId": "100000892911850B",
"customerCode": "1000000850",
"paymentMode": "Cash",
  }
}
```


## Related APIs

- [WPT overview](/docs/wpt)
- [WPT Payout (published)](/docs/payout/wpt-payout)
- [WPT Wallet List (master)](/docs/master-apis/wpt-wallet-list)
