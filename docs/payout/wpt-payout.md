---
title: "WPT Payout"
sidebar_label: "WPT Payout"
description: "RHUB WPT Payout API — wallet payout transactions."
---

# WPT Payout

<span className="rhub-method rhub-method--post">POST</span>

:::info[Endpoint]

`POST`  `http://host/ewallet/api/v1/payoutProcess/api`

:::

This Payout API is used to perform all types of Wallet transactions (C2C).

This API ensures a seamless payout experience by validating sender and receiver details, performing compliance checks, and processing transactions securely and efficiently.

Request Structure

The payout request is composed of four main objects, each serving a specific role in the Customer-to-Customer (C2C) transaction workflow:
- transactionInfo -
Contains detailed information about the transaction, such as quotation details (received from the Quotation API), currency pair, transaction amount, and payout type.
This section helps the system identify exchange rates, fees, and payout mode for the transaction.

- sender -
Provides complete details of the individual initiating the transfer.
Includes information such as full name, identification details, and country of origin. This ensures the sender is properly verified before the transaction is processed.

- receiver -
Defines the beneficiary details, who is also an individual customer.
It includes recipient information such as full name, wallet account or payout method details, country, and other required personal information.
The receiver object ensures funds are routed accurately to the intended individual beneficiary.

- compliance -
Contains regulatory and compliance-related information, including purpose of remittance, source of funds, and AML/KYC verification details.
This ensures that the transaction adheres to legal and jurisdictional requirements and helps reduce the risk of fraud or misuse.

## transactionInfo Req Param

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| **transactionInfo** |  |  |  |  |
| payinAmount | Numeric with decimal | 01 - 16 | M | The payin amount from the end sender. eg:1000.50,700 |
| payinCurrency | Alphanumeric with hyphens | 03 - 15 | M | The payin or local currency from the end sender. eg:USD-USA, EUR |
| type | Alphanumeric | 03 | M | The harmonized Transaction Type. eg: WPT |
| requestDate | Date | 10 - 19 | M | dd-mm-yyyy eg: 10-01-2025 |
| sendClient TrxReference | Alphanumeric | 10 - 30 | M | The RHUB transaction reference must contain 10 to 30 alphanumeric characters. eg:DDHD446CNNUY |
| paymentMode | Alpha | 04 | M | The following modes that can be used for payment. eg:Cash • Cash • Bank |
| descriptionText | Alphanumeric | 01 - 25 | M | The text description of the transaction provided by the client. eg:GJGJ877HNGG (maximum 25 alphanumeric characters) |
| sendClientCode | Numeric | 10 | M | The send client’s transaction reference number. eg:1000009999 |
| payoutCurrency | Alphanumeric with hyphens | 03 - 20 | M | The currency in which money is credited to the end receiver’s account. eg: BIF |
| payoutAmount | Numeric with decimal | 01 - 16 | M | The amount that will be credited to the end receiver’s account. eg:16700.50,5666 (including decimal values) |
| destinationCountryCode | Alpha | 03 | M | The 3-dight country code of reciever end. eg: USA, SGP |
| settlement Currency | Alphanumeric with hyphens | 03 - 15 | M | The currency used for internal settlement. eg:USD-USA, EUR |
| source Country | Alpha | 03 | M | 3-dight country code from where payment is initiated. eg: USA, SGP |
| fxRateValue | Numeric with decimal | 01 - 16 | M | The current exchange rate w.r.t to the sending currency and receive currency. eg:2.50 (including decimal values) |
| senderMargin | Numeric with decimal | 01 - 16 | M | Margin applied by sending partner. eg:2.50 (including decimal values) |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## sender Req Param

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| isAutoRegistered | Boolean | 04 - 05 | M | true: in case of on the fly customer registration, false: in case of manual customer registration. eg: true |
| declaration | Boolean | 04 - 05 | M | true: in case of on the fly customer registration, false: in case of manual customer registration. eg: true |
| docReferenceNumber | Alphanumeric | 01 - 30 | M | Should contains 10 to 30 digits alpha numeric only. eg:GJGJ877HNGG |
| senderFirstName | Alpha | 01 - 75 | M | The first name of the end customer sending money. eg: Rahul |
| senderLastName | Alpha | 02 - 75 | M | The last name of the end customer sending money. eg: Sharma |
| senderGender | Alpha | 01 - 10 | M | male, female or others. eg: male, female |
| senderNationality | Alpha | 03 | M | Nationality of sender in 3-dight country code format. eg: MWI, CHN |
| senderDOB | Date | 10 - 19 | M | Sender's birth date in yyyy-mm-dd format. eg: 2012-09-08 |
| senderEmail | Alphanumeric + special characters (Email format) | 01 - 50 | O | Sender's email Id. eg: rahul123@gmail.com |
| senderIdType | Alphanumeric | 06 - 10 | M | Data received for the respective value, using Document Id type master Api. eg: RHD006 IdTypeApi |
| senderIdNumber | Alphanumeric | 01 - 50 | M | The unique no of given id type of the sender. eg: UTYYT544GH65 |
| sender IdCountry | Alpha | 03 | M | The three-letter country code that represents the country Id of the sender. eg: USA, MWI. |
| sender IssueDate | Date | 10 - 19 | M | The issue date of the sender id registration in yyyy-mm-dd format. eg: 2025-10-01 |
| senderId Expiration | Date | 10 - 19 | M | The expiry date of sender's given id in yyyy-mm-dd format. eg: 2025-10-01 |
| dialCode | Alphanumeric with '+' symbol | 02 - 04 | C | Sender country dial code. eg: +1, +91 Note: Required when the contact number dial code does not match the selected country code. |
| senderMsisdn | Numeric | 07 - 20 | M | Sender contact number. eg: 6667778787 note: The number must correspond to the selected country code. |
| senderOccupation | Alphanumeric | 06 - 10 | O | The job profile of the sender. eg: RHO005 OccupationApi |
| senderAddressLineOne | Alphanumeric | 01 - 35 | M | The address line for sender's address. eg: 45D Civil line (Special characters not allowed) |
| senderAddressLineTwo | Alphanumeric | 01 - 35 | O | The address line for sender's address. eg: Vivek Vihar (Special characters not allowed) |
| senderCountry | Alpha | 03 | M | The three-letter country code that represents the country of the sender. eg: USA, MWI. |
| senderAddress State | Alpha | 01 - 50 | M | Sender Registered State. eg: Haryana |
| senderAddresss City | Alpha | 01 - 50 | M | Sender Registered City. eg: Delhi |
| senderPinCode | Alphanumeric | 01 - 10 | M | Pincode of sender. eg: SDFC2345 (space not allowed) |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## receiver Req Param

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| receiverFirstName | Alpha | 01 - 75 | M | The first name of the end customer sending money. eg: Rahul |
| receiverLastName | Alpha | 02 - 75 | M | The last name of the end customer sending money. eg: Sharma |
| receiverDOB | Date | 10 - 19 | O | Date of birth of receiver in yyyy-mm-dd format. eg: 2002-09-08 |
| receiverGender | Alpha | 01 - 10 | M | male, female or others. eg: male, female |
| receiverNationality | Alpha | 03 | M | Nationality of receiver in 3-dight country code format. eg: MWI, CHN |
| receiverIdType | Alphanumeric | 06 - 10 | M | The id type of the receiver. eg: RHD006 IdTypeApi |
| receiverIdNumber | Alphanumeric | 1 - 50 | M | The unique no of given id type of the receiver. eg: UTYYT544GH65 |
| receiverId Expiration | Date | 10 - 19 | M | The expiry date of receiver's given id in yyyy-mm-dd format. eg: 2025-10-01 |
| receiverOccupation | Alphanumeric | 06 - 10 | O | The job profile of the receiver. eg: RHO005 OccupationApi |
| dialCode | Alphanumeric with '+' symbol | 02 - 04 | C | Receiver country dial code. eg: +1, +91 Note: Required when the contact number dial code does not match the selected country code. |
| receiverMsisdn | Numeric | 07 - 20 | M | Receiver's contact number. eg: 9899898980 |
| receiverAddressLineOne | Alphanumeric | 01 - 35 | M | The address line for receiver's address. eg: 45D Civil line (Special characters not allowed) |
| receiverAddressLineTwo | Alphanumeric | 01 - 35 | O | The address line for receiver's address. eg: Civil line (Special characters not allowed) |
| receiverCountry | Alpha | 03 | M | The three-letter country code that represents the country of the receiver. eg: USA, MWI. |
| receiverAddress State | Alpha | 01 - 50 | M | receiver Registered State. eg: Haryana |
| receiverAddresss City | Alpha | 01 - 50 | M | receiver Registered City. eg: Delhi |
| receiverPinCode | Alphanumeric | 01 - 10 | O | Receiver's address pincode. eg: SDFC2345 (space not allowed) |
| receiverServiceProviderName | Alphanumeric with hyphens | 01 - 50 | M | Receiver's Service Provider Name. eg: ECOCASH-25701 WalletList |
| receiverServiceProviderCode | Numeric | 01 - 10 | M | Receiver's Service Provider Code. eg: 25701 WalletList |
| receiverServiceProviderMobile | Numeric | 07 - 20 | M | Receiver's Service Provider Mobile no. eg: 771238165 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## compliance Req Param

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| **compliance** |  |  |  |  |
| forexQuoteId | Numeric | 06 - 10 | M | The specific quote Id to be used for the transaction. This quote Id is generated when a quotation is created and it is returned on the quotation response. eg: 123456 ("code" obtained in quotation api response) |
| remittancePurpose | Alphanumeric | 06 - 10 | M | Reason for the transfer like Investment. eg:PAYP001 RemittancePurposeApi |
| sourceOfFund | Alphanumeric | 06 - 10 | M | Source of funds like Bank Deposit, Loan, and Revenue. eg:PAYS003 SourceOfFundApi |
| relationship | Alphanumeric | 06 - 10 | M | The relation between the sender and the receiver like Vendor, Employee, Employer, or Others. eg:PAYR001 RelationshipApi |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/payoutProcess/api

{
"payout": {
    "transactionInfo": {
        "payinAmount": 3.93,
        "payinCurrency": "USD-USA",
        "type": "WPT",
        "requestDate": "24-07-2025",
        "paymentMode": "Cash",
        "sendClientCode": "1000008494",
        "payoutCurrency": "BIF",
        "payoutAmount": "11112.00",
        "settlementCurrency": "USD-USA",
        "sourceCountry": "GHA",
        "fxRateValue": "2826.45",
        "senderMargin": "2826.45",
        "destinationCountryCode": "BDI"
    },
    "sender": {
        "customer": {
            "isAutoRegistered": true,
            "declaration": true,
            "docReferenceNumber": "CUS2VAMEHI",
            "senderFirstName": "Rajesh",
            "senderLastName": "singh",
            "senderGender": "male",
            "senderNationality": "MWI",
            "senderDOB":"2012-09-08",
            "senderIdType": "RHD006",
            "senderIdNumber": "ID321322332",
            "senderIssueDate": "2025-07-30",
            "senderIdCountry": "MWI",
            "senderIdExpiration": "2025-07-31",
            "senderMsisdn": "9098987877",
            "senderAddressLineOne": "malawi",
            "senderAddressLineTwo": "malawi",
            "senderCountry": "MWI",
            "senderAddressState": "malawi",
            "senderAddresssCity": "malawi",
            "senderPinCode": "434343",
        }
    },
    "receiver": {
        "customer": {
            "receiverMsisdn": "71238165",
            "dialCode": "+257",
            "receiverFirstName": "SOLANGE",
            "receiverLastName": "NDAYIZEYE",
            "receiverGender": "male",
            "receiverIdType": "RHD005",
            "receiverIdNumber": "ID76558766",
            "receiverIdExpiration": "2028-10-31",
            "receiverNationality": "BDI",
            "receiverAddressLineOne": "burundi",
            "receiverCountry": "BDI",
            "receiverAddressState": "burundi",
            "receiverAddresssCity": "burundi",
            "receiverServiceProviderName": "ECOCASH-25701",
            "receiverServiceProviderCode": "25701",
            "receiverServiceProviderMobile": "771238165"
        }
    },
    "compliance": {
        "forexQuoteId": "116175",
        "remittancePurpose": "RHP003",
        "sourceOfFund": "RHS001",
        "relationship": "RHR004"
    }
}
}
```

  ### Registered Customer

In the case of already registered customers, the payout process becomes more streamlined since the system already holds verified sender information.
Instead of providing complete sender details again, only a few key reference parameters are required to identify the registered entities within the system.

This approach reduces redundancy, improves efficiency, and ensures faster transaction initiation while maintaining compliance and traceability.

Rest request details remain same as mentioned above.

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| **sender : customer** |  |  |  |  |
| isAutoRegistered | Boolean | 05 | M | false |
| declaration | Boolean | 05 | M | false |
| customerCode | Numeric | 10 | M | The respective code recieved after successful Customer registration. eg: 1000002345 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Registered Customer Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/payoutProcess/api

{
"payout": {
    "transactionInfo": {
        "payinAmount": 3.93,
        "payinCurrency": "USD-USA",
        "type": "WPT",
        "requestDate": "24-07-2025",
        "paymentMode": "Cash",
        "sendClientCode": "1000008494",
        "payoutCurrency": "BIF",
        "payoutAmount": "11112.00",
        "settlementCurrency": "USD-USA",
        "sourceCountry": "GHA",
        "fxRateValue": "2826.45",
        "senderMargin": "2826.45",
        "destinationCountryCode": "BDI"
    },
    "sender": {
        "customer": {
            "isAutoRegistered": false,
            "declaration": false,
            "customerCode": "1000001104"
        }
    },
    "receiver": {
        "customer": {
            "receiverMsisdn": "71238165",
            "dialCode": "+257",
            "receiverFirstName": "SOLANGE",
            "receiverLastName": "NDAYIZEYE",
            "receiverGender": "male",
            "receiverIdType": "RHD005",
            "receiverIdNumber": "ID76558766",
            "receiverIdExpiration": "2028-10-31",
            "receiverNationality": "BDI",
            "receiverAddressLineOne": "burundi",
            "receiverCountry": "BDI",
            "receiverAddressState": "burundi",
            "receiverAddresssCity": "burundi",
            "receiverServiceProviderName": "ECOCASH-25701",
            "receiverServiceProviderCode": "25701",
            "receiverServiceProviderMobile": "771238165"
        }
    },
    "compliance": {
        "forexQuoteId": "116175",
        "remittancePurpose": "RHP003",
        "sourceOfFund": "RHS001",
        "relationship": "RHR004"
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
| payoutCurrency | String | M | The currency in which money is credited to the end receiver’s account. |  |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |  |
| serviceType | String | M | The harmonized Transaction Type, WPT. |  |
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
| descriptionText | String | M | The text description of the transaction provided by the client |  |

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
"senderNumber": "5123456789",
"beneficiaryName": "HCL Software",
"beneficiaryNumber": "123456789",
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
"descriptionText": "invoice67676767",
"sendClientPhoneNumber": "533545636654",
"sendClientAddress1": "Malawi, Malawi",
"customerId": "100000892911850B",
"customerCode": "1000000850",
"paymentMode": "Cash",
  }
}
```

## Related APIs

- [Payout](/docs/payout/payout)
- [WPT Wallet List (master)](/docs/master-apis/wpt-wallet-list)
- [Quotation](/docs/quotation/quotation)
- [WPT integration set (unlinked source page)](/docs/wpt)
