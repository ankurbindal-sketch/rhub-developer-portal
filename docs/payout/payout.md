---
title: "Payout"
sidebar_label: "Payout"
slug: "/payout/payout"
description: "RHUB Payout API — perform B2B, C2C, C2B and B2C transactions."
---

# Payout

<span className="rhub-method rhub-method--post">POST</span>

Initiate a fund transfer for a completed quotation.

## Before you initiate a payout

<div className="rhub-checklist">

1. Authenticate and obtain an access token.
2. Determine customer status: use the existing customer code, or pre-register the customer, or use the supported on-the-fly registration path in the Payout request.
3. Ensure the required KYC/KYB documentation has been uploaded and the applicable `docReferenceNumber` is available.
4. For B2B, B2C and C2B, ensure the required invoice documentation is available and the applicable `sendClientTrxReference` value is used.
5. Obtain a valid quotation.
6. Obtain the master, reference, bank or validation data your route and use case require — only the ones you actually need, not every master API.
7. Submit the Payout request.

</div>

You do not need to call every master API for every payout — fetch only the reference data
your route and use case require.

### Transaction types and documentation

| Transaction type | Sender | Receiver | KYC/KYB | Invoice |
|---|---|---|---|---|
| B2B | Business | Business | Required | Required |
| B2C | Business | Individual | Required | Required |
| C2B | Individual | Business | Required | Required |
| C2C | Individual | Individual | Required | Not applicable as an invoice requirement |

### Document references in the request

- `docReferenceNumber` — the KYC/KYB document reference.
- `sendClientTrxReference` — the invoice reference for B2B, B2C and C2B.

:::info[Conditional requirement — `sendClientTrxReference`]

**Required for B2B, B2C and C2B**, where invoice documentation is mandatory.

**Not required for C2C** — omit the parameter, or send it blank.

In the `transactionInfo` field table below the field is marked `M` and its name is split
across two lines, both exactly as the original contract has them. The conditional rule above
is RHUB's current guidance and is what your integration should follow.

:::

:::note[Field name in validation messages]

The Payout request field is `sendClientTrxReference`. Some current validation messages refer
to it as `sendClientTxnReference`; the
[error code reference](/docs/errors/current-error-codes) reproduces those messages as the API
returns them today.

:::

## Contract

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/payoutProcess/api'}</code>
  </div>
</div>

The Payout API is used to perform all types of transactions (B2B,C2C,C2B,B2C).

This API ensures a seamless payout experience by validating sender and receiver details, performing compliance checks, and processing transactions securely and efficiently.

**Request Structure**

The payout request is composed of four main objects, each serving a specific purpose in the transaction workflow:
- transactionInfo -
Contains detailed information about the transaction, such as quotation details (received from the Quotation API), currency pair, transaction amount, and payout type.
This section helps the system identify exchange rates, fees, and payout mode for the transaction.

- sender -
Provides complete details of the sender, whether it’s a business entity or an individual customer.
Includes information like name, ID and country of origin. This ensures the sender is properly verified before initiating a payout.

- receiver -
Defines the beneficiary details, which could also be an individual or a business.
It includes recipient information like bank account or wallet details, country, and other receiver details. The receiver object ensures funds are routed accurately to the intended destination.

- compliance -
Contains compliance and regulatory information, including purpose codes, source of funds, and AML/KYC verification details.
This helps ensure all transactions adhere to legal and jurisdictional requirements, reducing the risk of fraud or financial misuse.

## transactionInfo Req Param

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| **transactionInfo** |  |  |  |  |
| payinAmount | Numeric with decimal | 01 - 16 | M | The payin amount from the end sender. eg:1000.50,700 |
| payinCurrency | Alphanumeric with hyphens | 03 - 15 | M | The payin or local currency from the end sender. eg:USD-USA, EUR |
| type | Alphanumeric | 03 | M | The harmonized Transaction Type. Fixed default value B2C B2B, and C2C, C2B. eg:B2B, B2C |
| requestDate | Date | 10 - 19 | M | dd-mm-yyyy eg: 10-01-2025 |
| sendClient TrxReference | Alphanumeric | 10 - 30 | M | The RHUB transaction reference must contain 10 to 30 alphanumeric characters. eg:DDHD446CNNUY |
| paymentMode | Alpha | 04 | M | The following modes that can be used for payment. eg:Cash • Cash • Bank |
| descriptionText | Alphanumeric | 01 - 25 | M | The text description of the transaction provided by the client. eg:GJGJ877HNGG (maximum 25 alphanumeric characters) |
| sendClientCode | Numeric | 10 | M | The send client’s transaction reference number. eg:1000009999 |
| payoutCurrency | Alphanumeric with hyphens | 03 - 20 | M | The currency in which money is credited to the end receiver’s bank account. eg:USD-USA, EUR |
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
| **sender : business (for B2B,B2C transactions)** |  |  |  |  |
| isAutoRegistered | Boolean | 04 - 05 | M | true: in case of on the fly customer registration, false: in case of manual customer registration. eg:true |
| declaration | Boolean | 04 - 05 | M | true: in case of on the fly customer registration, false: in case of manual customer registration. eg: true |
| docReferenceNumber | Alphanumeric | 10 - 30 | M | Should contains 10 to 30 digits alpha numeric only. eg:GJGJ877HNGG |
| businessName | Alphanumeric | 01 - 70 | M | The name of the business entity sending money, minimum 2 words required. eg: Hcl Tech, Zensar tech pvt ltd |
| businessType | Alphanumeric | 06 - 10 | M | Data received for the respective value, using Business type master Api. eg: RHT011 BusinessTypeApi |
| businessPinCode | Alphanumeric | 01 - 10 | M | Company Pin Code. eg: SDFC2345 (space not allowed) |
| business Registration Number | Alphanumeric | 01 - 50 | M | The term Company Incorporation Number (CIN) is specific to refer to a identification number assigned to a company at the time of its incorporation. eg: DffSSG54hf |
| business Registration IssueDate | Date | 10 - 19 | C | To determine the issue date of the business registration in yyyy-mm-dd format. eg: 2025-10-01 (This information may be requested by certain correspondents.) Local RAIL Validations |
| businessIdValid Thru | Date | 10 - 19 | C | The company incorporation expiry date in yyyy-mm-dd format. eg: 2025-10-01 . (This information may be requested by certain correspondents.) Local RAIL Validations |
| dialCode | Alphanumeric with '+' symbol | 02 - 04 | C | Sender country dial code. eg: +1, +91 note: Required when the contact number dial code does not match the selected country code. |
| businessPrimary ContactNumber | Numeric | 07 - 20 | M | Company Primary Mobile number/Phone number. eg: 9899898980 note: The number must correspond to the selected country code. |
| business RegistrationType | Alphanumeric | 06 - 10 | M | Data received for the respective value, using Business registration type master Api. eg: RHB002 BusinessRegistrationApi |
| business Registration IssuedAt | Alpha | 03 | M | The specific location or jurisdiction where a business registration was issued IN 3-digit country code format eg: USA, IND |
| businessAddress1 | Alphanumeric | 01 - 35 | M | Company Register Address. eg: B 78 Preet vihar (Special characters not allowed) |
| businessAddress2 | Alphanumeric | 01 - 35 | O | Company Register Address. eg: sector 10 (Special characters not allowed) |
| businessAddress State | Alpha | 01 - 50 | M | Company Register State. eg: Haryana |
| businessAddresss City | Alpha | 01 - 50 | M | Company Register City. eg: New Delhi |
| businessEmail | Alphanumeric + special characters (Email format) | 01 - 50 | M | Company mail ID. eg: hcl123@gmail.com |
| businessCountry Code | Alpha | 03 | M | The three-letter country code that represents the country of origin or registration for a company. eg: USA, MWI . |
| **sender : customer (for C2C,C2B transactions)** |  |  |  |  |
| isAutoRegistered | Boolean | 04 - 05 | M | true: in case of on the fly customer registration, false: in case of manual customer registration. eg: true |
| declaration | Boolean | 04 - 05 | M | true: in case of on the fly customer registration, false: in case of manual customer registration. eg: true |
| docReferenceNumber | Alphanumeric | 01 - 30 | M | Should contains 10 to 30 digits alpha numeric only. eg:GJGJ877HNGG |
| senderFirstName | Alpha | 01 - 75 | M | The first name of the end customer sending money. eg: Rahul |
| senderLastName | Alpha | 02 - 75 | M | The last name of the end customer sending money. eg: Sharma |
| senderGender | Alpha | 01 - 10 | M | male, female or others. eg: male, female |
| senderNationality | Alpha | 03 | M | Nationality of sender in 3-dight country code format. eg: MWI, CHN |
| senderDOB | Date | 10 - 19 | M | Sender's birth date in yyyy-mm-dd format. eg: 2012-09-08 |
| senderEmail | Alphanumeric + special characters (Email format) | 01 - 50 | M | Sender's email Id. eg: rahul123@gmail.com |
| senderIdType | Alphanumeric | 06 - 10 | M | Data received for the respective value, using Document Id type master Api. eg: RHD006 IdTypeApi |
| senderIdNumber | Alphanumeric | 01 - 50 | M | The unique no of given id type of the sender. eg: UTYYT544GH65 |
| sender IdCountry | Alpha | 03 | C | The three-letter country code that represents the country Id of the sender. eg: USA, MWI.(This information may be requested by certain correspondents.) Local RAIL Validations |
| sender IssueDate | Date | 10 - 19 | C | The issue date of the sender id registration in yyyy-mm-dd format. eg: 2025-10-01 (This information may be requested by certain correspondents.) Local RAIL Validations |
| senderId Expiration | Date | 10 - 19 | C | The expiry date of sender's given id in yyyy-mm-dd format. eg: 2025-10-01 (This information may be requested by certain correspondents.) Local RAIL Validations |
| dialCode | Alphanumeric with '+' symbol | 02 - 04 | C | Sender country dial code. eg: +1, +91 note: Required when the contact number dial code does not match the selected country code. |
| senderMsisdn | Numeric | 07 - 20 | M | Sender contact number. eg: 6667778787 note: The number must correspond to the selected country code. |
| senderOccupation | Alphanumeric | 06 - 10 | M | The job profile of the sender. eg: RHO005 OccupationApi |
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
| **receiver: business (for B2B/C2B transactions)** |  |  |  |  |
| businessName | Alphanumeric | 01 - 70 | M | The name of the end business entity receiving money, minimum 2 words required. eg: Hcl Tech, Zensar tech pvt ltd. |
| businessType | Alphanumeric | 06 - 10 | M | Data received for the respective value, using Business type master Api. eg: RHT011 BusinessTypeApi |
| businessPinCode | Alphanumeric | 01 - 10 | M | Company Pin Code. eg: SDFC2345 (space not allowed) |
| businessRegistration Number | Alphanumeric | 01 - 50 | C | The term Company Incorporation Number (CIN) is specific to refer to a unique identification number assigned to a company at the time of its incorporation. eg: DffSSG54hf (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| businessRegistration Type | Alphanumeric | 06 - 10 | M | Data received for the respective value, using Business registration type master Api. eg: RHB002 BusinessRegistrationApi |
| businessRegistration IssueDate | Date | 10 - 19 | C | To determine the issue date of the business registration in yyyy-mm-dd format. eg: 2025-10-01 (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| businessRegistration IssuedAt | Alpha | 03 | M | This is the specific location or jurisdiction where a business registration was issued. in 3-digit country code format eg: USA, IND |
| businessIdValidThru | Date | 10 - 19 | C | The company incorporation expiry date in yyyy-mm-dd format. eg: 2025-10-01. (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| businessAddress1 | Alphanumeric | 01 - 35 | M | Company Register Address. eg: B 78 Preet vihar (Special characters not allowed) |
| businessAddress2 | Alphanumeric | 01 - 35 | O | Company Register Address. eg: sector 10 (Special characters not allowed) |
| businessAddress State | Alpha | 01 - 50 | M | Company Register State. eg: Haryana |
| businessAddresss City | Alpha | 01 - 50 | M | Company Register City. eg: New Delhi |
| taxIdNumber | Alphanumeric | 01 - 25 | C | Required for given payout countries. eg: ID64645YEY5 (ARG, THA, BRA, ECU, GTM, HND, KAZ, MEX, PER, CHL, PHL, JPN, URY, COL, CRI, RUS, BLR, PAK) |
| dialCode | Alphanumeric with '+' symbol | 02 - 04 | C | Receiver country dial code. eg: +1, +91 note: Required when the contact number dial code does not match the selected country code. |
| businessPrimary ContactNumber | Numeric | 07 - 20 | C | Company Primary Mobile number/Phone number. eg: 9899898980 (In SWIFT RAIL required for given payout countries Brazil-BRA, Philippines-PHL, China-CHN, Uganda-UGA, Uruguay-URY, Colombia-COL, Mexico-MEX, Hong Kong-HKG, Malaysia-MYS ) for LOCAL RAIL follow Local RAIL Validations |
| businessCountry Code | Alpha | 03 | M | The three-letter country code that represents the country of origin or registration for a company. eg: USA, MWI . |
| businessAccount Number | Alphanumeric | 01 - 50 | M | Company Account number/IBAN. eg: AE110260000959024298101 |
| businessAccount HolderName | Alphanumeric | 01 - 70 | M | The account name of the end customer/receiver company to where the amount is sent. (value should be same as businessName field value) |
| businessAccount Type | Alpha | 01 - 50 | C | The specific category or classification of a bank account based on current or saving. Required in case of BRA,PHL,DOM,URY Transactions. AccountTypeApi |
| businessBankName | Alpha | 01 - 100 | M | The name of the end customer/Company bank to which end client/company receive the money. The value received from the Bank List API response in the **name** tag. eg: Emirates NBD (Please enter valid receiver bank details for a successful transaction) |
| businessBank Country | Alphanumeric | 01 - 20 | C | The name of the country where a particular bank is located or based. This field becomes mandatory when the Bank List API response includes the **locationId** tag, otherwise it's not mandate. eg: JPNAEO724 (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| businessBankCode | Alphanumeric | 01 - 20 | C | Bank Identification Number (BIN). This field becomes mandatory when the Bank List API response includes the **code** tag, otherwise it's not mandate. eg: EQBLKENA (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| businessSwiftCode | Alphanumeric | 01 - 20 | C | It's a unique alphanumeric code used to identify a specific bank or financial institution in international financial transactions. eg: BOJPJPJTXXX (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| **receiver: customer (for B2C/C2C transactions)** |  |  |  |  |
| receiverFirstName | Alpha | 01 - 75 | M | The first name of the end customer sending money. eg: Rahul |
| receiverLastName | Alpha | 02 - 75 | M | The last name of the end customer sending money. eg: Sharma |
| receiverDOB | Date | 10 - 19 | O | Date of birth of receiver in yyyy-mm-dd format. eg: 2002-09-08 |
| receiverGender | Alpha | 01 - 10 | M | male, female or others. eg: male, female |
| receiverNationality | Alpha | 03 | M | Nationality of receiver in 3-dight country code format. eg: MWI, CHN |
| receiverIdType | Alphanumeric | 06 - 10 | C | The id type of the receiver. eg: RHD006 (This information may be requested by certain correspondents.) IdTypeApi Local RAIL Validations SWIFT RAIL Validations |
| receiverIdNumber | Alphanumeric | 01 - 50 | C | The unique no of given id type of the receiver. eg: UTYYT544GH65 (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| receiverId Expiration | Date | 10 - 19 | C | The expiry date of receiver's given id in yyyy-mm-dd format. eg: 2025-10-01 (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| receiverOccupation | Alphanumeric | 06 - 10 | C | The job profile of the receiver. eg: RHO005 (This field is mandatory for all SWIFT transactions across all countries.) OccupationApi |
| taxIdNumber | Alphanumeric | 01 - 25 | C | Required for given payout countries. eg: ID64645YEY5 (ARG, THA, BRA, ECU, GTM, HND, KAZ, MEX, PER, CHL, PHL, JPN, URY, COL, CRI, RUS, BLR, PAK) |
| dialCode | Alphanumeric with '+' symbol | 02 - 04 | C | Receiver country dial code. eg: +1, +91 note: Required when the contact number dial code does not match the selected country code. |
| receiverMsisdn | Numeric | 07 - 20 | C | Receiver's contact number. eg: 9899898980 (In SWIFT RAIL required for given payout countries Brazil-BRA, Philippines-PHL, China-CHN, Uganda-UGA, Uruguay-URY, Colombia-COL, Mexico-MEX, Hong Kong-HKG, Malaysia-MYS ) for LOCAL RAIL follow Local RAIL Validations |
| receiverAddressLineOne | Alphanumeric | 01 - 35 | M | The address line for receiver's address. eg: 45D Civil line (Special characters not allowed) |
| receiverAddressLineTwo | Alphanumeric | 01 - 35 | O | The address line for receiver's address. eg: Civil line (Special characters not allowed) |
| receiverCountry | Alpha | 03 | M | The three-letter country code that represents the country of the receiver. eg: USA, MWI. |
| receiverAddress State | Alpha | 01 - 50 | M | receiver Registered State. eg: Haryana |
| receiverAddresss City | Alpha | 01 - 50 | M | receiver Registered City. eg: Delhi |
| receiverPinCode | Alphanumeric | 01 - 10 | M | Receiver's address pincode. eg: SDFC2345 (space not allowed) |
| receiverAccount Number | Alphanumeric | 01 - 50 | M | Receiver bank account number. eg: AE110260000959024298101 |
| receiverAccount HolderName | Alpha | 01 - 150 | M | The account name of the receiver (beneficiary) to whom the payment is being made. (First name + Last name) |
| receiverAccount Type | Alpha | 01 - 50 | C | The specific category or classification of a bank account based on current or saving. Required in case of BRA,PHL,DOM,URY Transactions. AccountTypeApi |
| receiverBankName | Alpha | 01 - 100 | M | The name of the end customer/Company bank from which send client/company received the money. The value received from the Bank List API response in the **name** tag. eg: Emirates NBD (Please enter valid receiver bank details for a successful transaction) |
| receiverBank Country | Alphanumeric | 01 - 20 | C | The name of the country where a particular bank is located or based. This field becomes mandatory when the Bank List API response includes the **locationId** tag, otherwise it's not mandate. eg: JPNAEO724 (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| receiverBankCode | Alphanumeric | 01 - 20 | C | Bank Identification Number (BIN). This field becomes mandatory when the Bank List API response includes the **code** tag, otherwise it's not mandate. eg: EQBLKENA (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |
| receiverSwiftCode | Alphanumeric | 01 - 20 | C | It's a unique alphanumeric code used to identify a specific bank or financial institution in international financial transactions. eg: BOJPJPJTXXX (This information may be requested by certain correspondents.) Local RAIL Validations SWIFT RAIL Validations |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## compliance Req Param

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| **compliance** |  |  |  |  |
| forexQuoteId | Numeric | 06 - 10 | M | The specific quote Id to be used for the transaction. This quote Id is generated when a quotation is created and it is returned on the quotation response. eg: 123456 ("code" obtained in quotation api response) |
| remittancePurpose | Alphanumeric | 06 - 10 | M | Reason for the transfer like Investment. eg:RHP002 RemittancePurposeApi |
| sourceOfFund | Alphanumeric | 06 - 10 | M | Source of funds like Bank Deposit, Loan, and Revenue. eg: RHS005 SourceOfFundApi |
| relationship | Alphanumeric | 06 - 10 | M | The relation between the sender and the receiver like Vendor, Employee, Employer, or Others. eg: RHR002 RelationshipApi |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details for Payout

Combining all described objects - including transactionInfo, sender, receiver, and compliance details.

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/payoutProcess/api

{
"payout": {
    "transactionInfo": {
        "payinAmount": 122.22,
        "payinCurrency": "USD-USA",
        "type": "B2B",
        "requestDate": "10-01-2025",
        "sendClientTrxReference": "RSGPOD0DS7",
        "descriptionText": "324532423423",
        "paymentMode": "Cash",
        "sendClientCode": "1000008929",
        "payoutCurrency": "USD-GLOBAL",
        "payoutAmount": "121.00",
        "destinationCountryCode": "ARE",
        "settlementCurrency": "USD-USA",
        "sourceCountry": "MWI",
        "fxRateValue": "0.9899999999",
        "senderMargin": "0.9899999999"
        },
    "sender": {
        //for B2B/B2C
        "business": {
            "isAutoRegistered": true,
            "declaration": true,
            "docReferenceNumber": "CUS5NBRGUQ",
            "businessName": "Delhi Daredevils",
            "businessType": "RHT011",
            "businessPinCode": "323434",
            "businessRegistrationNumber": "9099998988",
            "businessPrimaryContactNumber": "9899998988",
            "businessRegistrationType": "RHB002",
            "businessRegistrationIssuedAt": "MWI",
            "businessAddress1": "new delhi new",
            "businessAddressState": "new delhi",
            "businessAddresssCity": "new delhi",
            "businessCountryCode": "MWI",

        }
        //for C2C/C2B
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
            "senderMsisdn": "9098987877",
            "senderAddressLineOne": "malawi",
            "senderAddressLineTwo": "malawi",
            "senderCountry": "MWI",
            "senderAddressState": "malawi",
            "senderAddresssCity": "malawi",
            "senderPinCode": "123456",
            "isSenderPEP": false,
            "thirdPartyDetermination": false
        }
        },
    "receiver": {
        //for B2B/C2B
        "business": {
            "businessName": "Gujarat titans",
            "businessType": "RHT011",
            "businessRegistrationType": "RHB002",
            "businessRegistrationIssuedAt": "ARE",
            "businessAddress1": "new delhi new",
            "businessAddressState": "new delhi",
            "businessAddresssCity": "new delhi",
            "businessPrimaryContactNumber": "9899998988",
            "businessCountryCode": "ARE",
            "businessAccountNumber": "AE110260000959024298101",
            "businessAccountHolderName": "Gujarat titans ",
            "businessBankName": "Emirates NBD",
            "businessBankCode": "",
            "businessSwiftCode": "EBILAEAD"
        }
        //for B2C/C2C
        "customer": {
            "receiverFirstName": "kuldeep",
            "receiverLastName": "singh",
            "receiverGender": "male",
            "receiverNationality": "ARE",
            "receiverAddressLineOne": "dubai",
            "receiverAddressLineTwo": "dubai",
            "receiverCountry": "ARE",
            "receiverAddressState": "dubai",
            "receiverAddresssCity": "dubai",
            "receiverBankName": "Emirates NBD",
            "receiverBankCode": "",
            "receiverAccountNumber": "AE110260000959024298101",
            "receiverAccountHolderName": "kuldeep singh",
            "receiverSwiftCode": "EBILAEAD"
        }
        },
    "compliance": {
        "forexQuoteId": "114672",
        "remittancePurpose": "RHP002",
        "sourceOfFund": "RHS005",
        "relationship": "RHR002"
    }
  }
  }
```

## Registered Customer

In the case of already registered customers, the payout process becomes more streamlined since the system already holds verified sender information.
Instead of providing complete sender details again, only a few key reference parameters are required to identify the registered entities within the system.

This approach reduces redundancy, improves efficiency, and ensures faster transaction initiation while maintaining compliance and traceability.

Rest request details remain same as mentioned above.

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| **sender : business/customer** |  |  |  |  |
| isAutoRegistered | Boolean | 05 | M | false |
| declaration | Boolean | 05 | M | false |
| customerCode | Numeric | 10 | M | The respective code recieved after successful Customer registration. eg: 1000002345 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Registered Customer Request Details

```json
{
"payout": {
  "transactionInfo": {
      "payinAmount": 122.22,
      "payinCurrency": "USD-USA",
      "type": "B2B",
      "requestDate": "17-01-2025",
      "sendClientTrxReference": "ASDEWEDE66",
      "descriptionText": "324532423423",
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
    //for B2B,B2C
      "business": {
        "isAutoRegistered": false,
        "declaration": false,
        "customerCode": "1000002225"
        }
    //for C2C, C2B
       "customer": {
          "isAutoRegistered": false,
          "declaration": false,
          "customerCode": "1000002225"
        }
  },
  "receiver": {
      //for B2B/C2B
      "business": {
          "businessName": "Gujarat titans",
          "businessType": "RHT011",
          "businessRegistrationType": "RHB002",
          "businessRegistrationIssuedAt": "ARE",
          "businessAddress1": "new delhi new",
          "businessAddressState": "new delhi",
          "businessAddresssCity": "new delhi",
          "businessPrimaryContactNumber": "9899998988",
          "businessCountryCode": "ARE",
          "businessAccountNumber": "AE110260000959024298101",
          "businessAccountHolderName": "Gujarat titans ",
          "businessBankName": "Emirates NBD",
          "businessBankCode": "",
          "businessSwiftCode": "EBILAEAD"
      }
      //for B2C/C2C
      "customer": {
          "receiverFirstName": "kuldeep",
          "receiverLastName": "singh",
          "receiverGender": "male",
          "receiverNationality": "ARE",
          "receiverAddressLineOne": "dubai",
          "receiverAddressLineTwo": "dubai",
          "receiverCountry": "ARE",
          "receiverAddressState": "dubai",
          "receiverAddresssCity": "dubai",
          "receiverBankName": "Emirates NBD",
          "receiverBankCode": "",
          "receiverAccountNumber": "AE110260000959024298101",
          "receiverAccountHolderName": "kuldeep singh",
          "receiverSwiftCode": "EBILAEAD"
      }
      },
  "compliance": {
      "forexQuoteId": "114672",
      "remittancePurpose": "RHP002",
      "sourceOfFund": "RHS005",
      "relationship": "RHR002"
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
| descriptionText | String | M | The text description of the transaction provided by the client. |  |

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
"descriptionText": "invoiceno789777",
"sendClientMarginValue": 0.0,
"beneficiaryAccountHolderName": "Gujarat titans ",
"sendClientName": "ESTEL",
"senderCountry": "Malawi",
"sendClientPhoneNumber": "533545636654",
"sendClientAddress1": "Malawi, Malawi",
"customerId": "100000892911850B",
"customerCode": "1000000850",
"paymentMode": "Cash",
  }
}
```

## Related APIs

- [Integration flow](/docs/getting-started/integration-flow)
- [Quotation](/docs/quotation/quotation)
- [Document Upload](/docs/documents/document-upload)
- [Currency validations (LOCAL rail)](/docs/validation/currency-validations)
- [Country validations (SWIFT rail)](/docs/validation/country-validations)
- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
- [WPT Payout](/docs/payout/wpt-payout)
