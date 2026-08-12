---
title: "Payout API"
sidebar_label: "Payout API"
description: "RHUB Payout API (source page not linked in the live documentation sidebar)."
---

# Payout API

<span className="rhub-method rhub-method--post">POST</span>

*Source of truth: `payout.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `payout.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/payoutProcess`

:::

The Payout API is used to perform the business-to-business (B2B) transaction.

## Request Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| **Payout : Transaction Information** |  |  |  |  |
| payinAmount | String | M | The payin amount from the end sender. |  |
| payinCurrency | String | M | The payin or local currency from the end sender. |  |
| type | String | M | The harmonized Transaction Type. Fixed default value P2P B2B, and C2C, C2B. |  |
| requestDate | String | M |  |  |
| sendClient TrxReference | String | M | The RHUB's transaction reference number. |  |
| paymentMode | String | M | The following modes that can be used for payment. • Cash • Cheque • Bank Account |  |
| descriptionText | String | O | The text description of the transaction provided by the client |  |
| sendClientCode | String | M | The send client’s transaction reference number. |  |
| payoutCurrency | String | M | The currency in which money is credited to the end receiver’s bank account. |  |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |  |
| tax | String | M |  |  |
| settlement Currency | String | M |  |  |
| pin | String | M |  |  |
| fxRateValue | String | M | The current exchange rate w.r.t to the sending currency and receive currency. |  |
| **Sender : Business** |  |  |  |  |
| businessMsisdn | String | M | The mobile number of the sender. |  |
| businessName | String | M | The name of the end customer/send business entity sending money. |  |
| businessType | String | M | Type of registration like Partnership, Corporation, Cooperative. |  |
| business AuthorizedPerson | String | O |  |  |
| businessPinCode | String | M | Company Pin Code. |  |
| Business Registration Number | String | M | The term Company Incorporation Number (CIN) is specific to refer to a identification number assigned to a company at the time of its incorporation. |  |
| Business RegistrationType | String | M |  |  |
| Business Registration IssueDate | String | M | To determine the issue date of the business registration. |  |
| Business Registration IssuedBy | String | M | The government agency or authority responsible for issuing the business registration. |  |
| business Registration IssuedAt | String | M | The specific location or jurisdiction where a business registration was issued. |  |
| businessIdValid Thru | String | M | The company incorporation expiry date. |  |
| businessAddress1 | String | M | Company Register Address 1. |  |
| businessAddress2 | String | M | Company Register Address 2. |  |
| businessAddress State | String | M | Company Register State. |  |
| businessAddresss City | String | M | Company Register City. |  |
| businessPrimary ContactNumber | String | M | Company Primary Mobile number/Phone number. |  |
| businessEmail | String | M | Company mail ID. |  |
| businessCountry Code | String | M | The two-letter country code that represents the country of origin or registration for a company. Like US, GB, JP. |  |
| businessAccount Number | String | C | Company Account number/IBAN. If the payment mode is Cash and the sender is paying &lt;= 25000 CAD, then the bank details are optional. Or, If the payment mode is Cash and the sender is paying > 25000 CAD, then it is not permitted and the sender must perform the transaction through the bank. Therefore, bank details of the sender are mandatory. Or, If the payment mode is Bank then, the bank details of the sender are mandatory. |  |
| businessAccount HolderName | String | M | The account name of the end customer/sender company from where the amount is sent to the RHUB send client. |  |
| businessAccount Type | String | O | The specific category or classification of a bank account based on its features, purpose, and usage like Business Account, Saving Account, Joint Account, and Foreign Currency Account. |  |
| businessBankName | String | M | The name of the end customer/Company bank from which send client/company received the money. |  |
| businessBank Country | String | M | The name of the country where a particular bank is located or based. |  |
| businessBank BranchName | String | M | The name of the bank’s branch where a particular bank is located or based. |  |
| businessBankCode | String | M | The bank code or like a swift code, Bank Identification Number (BIN). |  |
| businessBank Address | String | M | The name of the Bank address details where a particular bank is located or based. |  |
| businessSwiftCode | String | M | It's a unique alphanumeric code used to identify a specific bank or financial institution in international financial transactions. |  |
| businessPep Disclosure | String | M | To disclose that the sender is a Politically Exposed Person (PEP). |  |
| businessThirdParty Determination | String | M | To determine whether the third party has transferred the money to the receiver on behalf of the sender. |  |
| udv1 | String | M | User defined value. |  |
| udv2 | String | M | User defined value. |  |
| udv3 | String | M | User defined value. |  |
| udv4 | String | M | User defined value. |  |
| udv5 | String | M | User defined value. |  |
| **Receiver: Business** |  |  |  |  |
| businessMsisdn | String | M | The mobile number of the sender. |  |
| businessName | String | M | The name of the end customer/send business entity sending money. |  |
| businessType | String | M | Type of registration like Partnership, Corporation, Cooperative. |  |
| businessAuthorized Person | String | M |  |  |
| businessPinCode | String | M | Company Pin Code. |  |
| businessRegistration Number | String | M | The term Company Incorporation Number (CIN) is specific to refer to a unique identification number assigned to a company at the time of its incorporation. |  |
| businessRegistration Type | String | M |  |  |
| businessRegistration IssueDate | String | M | To determine the issue date of the business registration. |  |
| businessRegistration IssuedBy | String | M | This is the government agency or authority responsible for issuing the business registration. |  |
| businessRegistration IssuedAt | String | M | This is the specific location or jurisdiction where a business registration was issued. |  |
| businessIdValidThru | String | M | The company incorporation expiry date. |  |
| businessAddress1 | String | M | Company Register Address 1. |  |
| businessAddress2 | String | M | Company Register Address 2. |  |
| businessAddress State | String | M | Company Register State. |  |
| businessAddresss City | String | M | Company Register City. |  |
| businessPrimary ContactNumber | String | M | Company Primary Mobile number/Phone number. |  |
| businessDescription | String | M | The written statement or summary that provides an overview of a particular business like Products or services, Nature of the business. |  |
| businessEmail | String | M | Company mail ID. |  |
| businessCountry Code | String | M | The two-letter country code that represents the country of origin or registration for a company. Like US, GB, JP. |  |
| businessAccount Number | String | M | Company Account number/IBAN. |  |
| businessAccount HolderName | String | M | The account name of the end customer/sender company from where the amount is sent to the RHUB send client. |  |
| businessAccount Type | String | O | The specific category or classification of a bank account based on its features, purpose, and usage like Business Account, Saving Account, Joint Account, and Foreign Currency Account. |  |
| businessBankName | String | M | The name of the end customer/Company bank from which send client/company received the money. |  |
| businessBank Country | String | M | The name of the country where a particular bank is located or based. |  |
| businessBankCode | String | M | The bank code or like a swift code, Bank Identification Number (BIN). |  |
| businessBank Address | String | M | The name of the Bank address details where a particular bank is located or based. |  |
| businessSwiftCode | String | M | It's a unique alphanumeric code used to identify a specific bank or financial institution in international financial transactions. |  |
| udv1 | String | M | User defined value. |  |
| udv2 | String | M | User defined value. |  |
| udv3 | String | M | User defined value. |  |
| udv4 | String | M | User defined value. |  |
| udv5 | String | M | User defined value. |  |
| **Compliance** |  |  |  |  |
| forexQuoteId | String | M | The specific quote Id to be used for the transaction. This quote Id is generated when a quotation is created and it is returned on the quotation response. |  |
| remittancePurpose | String | M | Reason for the transfer like Investment. |  |
| sourceOfFund | String | M | Source of funds like Bank Deposit, Loan, and Revenue. |  |
| relationship | String | M | The relation between the sender and the receiver like Vendor, Employee, Employer, or Others. |  |
| invoiceNumber | String | M |  |  |
| documentUpload | String | M |  |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST https://sandbox-client.remittanceshub.com:8030/ewallet/api/v1/payoutProcess

{

"payout": {
"transactionInfo": {
"payinAmount": "100000.00",
"payinCurrency": "MWK",
"type": "B2B",
"requestDate": "03-08-2023",
"sendClientTrxReference": "PAYAFMRF61",
"paymentMode": "Bank",
"descriptionText": "Inv12345678",
"sendClientCode": "1000008340",
"payoutCurrency": "JPY",
"payoutAmount": "10328.00",
"tax": 0,
"settlementCurrency": "USD-USA",
"pin": "f6413d85b7cb8ff3fa98327ed0a26d38",
"fxRateValue": "0.10539",
},
"sender": {
"business": {
"businessMsisdn": "",
"businessName": "HCL Technologies",
"businessType": "100055",
"businessAuthorizedPerson": "",
"businessPinCode": "12345678",
"businessRegistrationNumber": "REG12345",
"businessRegistrationType": "100059",
"businessRegistrationIssueDate": "2023-08-03",
"businessRegistrationIssuedBy": "",
"businessRegistrationIssuedAt": "MWI",
"businessIdValidThru": "",
"businessAddress1": "Test Address",
"businessAddress2": "",
"businessAddressState": "Test State",
"businessAddresssCity": "Test City",
"businessPrimaryContactNumber": "+265123456789",
"businessEmail": "abc@gmail.com",
"businessCountryCode": "MWI",
"businessAccountNumber": "12345678",
"businessAccountHolderName": "",
"businessAccountType": "100001",
"businessBankName": "Test Bank",
"businessBankCountry": "MWI",
"businessBankCode": "",
"businessBankAddress": "Test Address",
"businessSwiftCode": "12345678",
"businessPepDisclosure": false,
"businessThirdPartyDetermination": true,
"udv1": "",
"udv2": "",
"udv3": "",
"udv4": "",
"udv5": ""
},
"customer": {
}
},
"receiver": {
"business": {
"businessMsisdn": "",
"businessName": "HCL Software",
"businessType": "100000",
"businessAuthorizedPerson": "",
"businessPinCode": "",
"businessRegistrationNumber": "REG1234567",
"businessRegistrationType": "100059",
"businessRegistrationIssueDate": "2023-08-03",
"businessRegistrationIssuedBy": "",
"businessRegistrationIssuedAt": "JPN",
"businessIdValidThru": "2023-08-04",
"businessAddress1": "Test Address",
"businessAddress2": "",
"businessAddressState": "Test State",
"businessAddresssCity": "Tokyo",
"businessPrimaryContactNumber": "+81123456789",
"businessEmail": "abc@gmail.com",
"businessCountryCode": "JPN",
"businessAccountNumber": "1234567",
"businessAccountHolderName": "Test Name",
"businessAccountType": "100001",
"businessBankName": "Mizuho Bank,Ltd.-0001",
"businessBankCountry": "SAITAMASHINTOSHIN-759",
"businessBankCode": "0001",
"businessBankAddress": "Test Branch Address",
"businessSwiftCode": "ABCD12345",
"udv1": "",
"udv2": "",
"udv3": "",
"udv4": "",
"udv5": ""
},
"customer": {
}
},
"compliance": {
"forexQuoteId": "101436",
"remittancePurpose": "001-02",
"sourceOfFund": "01",
"relationship": "04",
"invoiceNumber": "",
"documentUpload": "",
}
}
}
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M |  |  |
| resultCode | String | M | The unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Payout Response Bean** |  |  |  |  |
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
| termAndCondition | String | M |  |  |
| status | String | M |  |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"transactionId": "7560333",
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
"termAndCondition": " ",
"status": "In Process",
  }
}
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
