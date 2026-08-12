---
title: "Unpublished API sections"
sidebar_label: "Unpublished API sections"
description: "API sections that are commented out in the RHUB source files."
---

# Unpublished API sections

:::warning[REVIEW REQUIRED — not published by the source]

Every section on this page exists in the RHUB source **inside an HTML comment**, so the live documentation does not render it. The content is reproduced verbatim so that no source material is lost. The source does not establish whether these contracts are current, forthcoming or withdrawn — confirm with RHUB before use.

:::

## Customer Enquiry (from ENQUIRY.md)

### Customer Enquiry

`GET` — status: **REVIEW REQUIRED (commented out in source)**

## Final Quotation (from QUOTA.md)

### Final Quotation

`POST` — status: **REVIEW REQUIRED (commented out in source)**

:::info[Endpoint]

`POST`  `http://host/ewallet/api/v1/fxratequotation/api`

:::

The Quotation API is used to fetch the forex rate between the payin and payout currencies. This is the final price.

##### Request Parameter

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
| senderCode | String | M | The send partner code |
| receiverCode | String | M | The payout partner code |
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

##### Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/fxratequotation/api
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

##### Response Parameter

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
| senderCode | String | M | The send partner code |
| receiverCode | String | M | The payout partner code |
| sendCurrencyCode | String | M | The code of the currency in which the sender transferred or sent the money to the receiver. |
| receiveCurrencyCode | String | M | The code of the currency in which the receiver will receive the money. |
| sendCurrencyName | String | M | The name of the currency in which the sender sends the money. |
| receiveCurrencyName | String | M | The name of the currency in which the receiver receives the money. |
| transactionLimit | String | M | To fetch the minimum or maximum transaction limit based on the currency for the client. |
| validityPeriod | String | M | The duration up to when the exchange rate is valid. The duration or validity can be in minutes, hours, days, or months. |
| payinAmount | String | M | The payin amount from the end sender. |
| payoutAmount | String | M | The amount that will be credited to the end receiver’s account. |
| sendClientFee | String | M | The fee payable by the send client. |
| settlementCurrencyCode | String | M | The code of the currency in which the settlement is done. |
| settlementAmount | String | M | The settlement amount |
| duration | String | M | Duration of fx quotation (in mins) |
| timeLeft | String | M | Remaining time for the quotation to get expire |
| paymentMode | String | M | Type of payment i.e. bank account or mode using the swift network. The following modes that can be used for payment. <br /> • Cash <br /> • Cheque <br /> • Bank Account |
| quoteid | String | M | The quotation id |
| quotestatus | String | M | The status of requested quotation |
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

##### Response Details

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

## WPT sections (from WPT.md)

### Authentication

`POST` — status: **REVIEW REQUIRED (commented out in source)**

:::info[Endpoint]

`POST`  `http://host/ewallet/oauth/token`

:::

The Login API is used to authenticate and authorize the user.

##### Request Parameter

| Parameters     | Data Type | Requirement | Description |
|----------|:-----:|:-----------:|--------|
| grant_type | String | M | URL parameter |
| scope | String | M | It is the read and write access to the endpoints |
| username | String | M | The user ID or username |
| password | String | M | The password in unreadable format |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Header Parameter
| Parameters     | Data Type  | Requirement | Description |
|----------|:------------:|:-----:|--------|
| authorization | String | M | URL parameter |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/oauth/token
FormData : grant_type=password&scope=read%20write&username=1000008340
password : 21ED0D51*****FB437*****8ED2123B6
```

##### Response Parameter

| Parameters     | Data Type  | Requirement | Description |
|----------|:-----:|:------------:|--------|
| access_token | String | M | Token to identify and authorize the user. |
| token_type | String | M | Type of the access token. |
| expires_in | String | M | Duration of time in seconds within which the access token expires. |
| scope | String | M |  |
| clientCode | String | M |  |
| locale | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Response Details

```json
{
"access_token": "15*****f-54fe-43d9-***7-b7dc****1b9",
"token_type": "bearer",
"expires_in": 21150,
"scope": "read write trust",
"clientCode": "1000008483",
"locale": "en"
}
```

### Update Customer Details

`PUT` — status: **REVIEW REQUIRED (commented out in source)**

:::info[Endpoint]

`PUT`  `http://host/ewallet/api/v1/customer-registration/{customerCode}`

:::

The Update Customer API is used to update the details of the registered customer.

##### Request Parameter

| Parameters     | Data Type |  Requirement | Description |
|----------|:-----:|:----------:|--------|
| customerCode | String | M | Customer code of registered customer. |
| customerTypeCode | String | M | Individual : 100001, Business : 100002 |
| customerSubTypeCode | String | M | 100001 |
| docReferenceNumber | String | M | Customer registration unique number. |
| walletOwnerCode | String | M | Send Client Code |
| firstName | String | M |  |
| middleName | String | M |  |
| lastName | String | M |  |
| dateOfBirth | String | M |  |
| gender | String | M |  |
| nationality | String | M |  |
| mobileNumber | String | M |  |
| dialCode | String | M |  |
| email | String | M |  |
| occupationCode | String | M |  |
| jobTitle | String | M |  |
| jobIndustry | String | M |  |
| addressLine1 | String | M |  |
| addressLine2 | String | M |  |
| countryCode | String | M |  |
| residenceStatusCode | String | M |  |
| city | String | M |  |
| state | String | M |  |
| pincode | String | M |  |
| idTypeCode | String | M |  |
| idNumber | String | M |  |
| idIssuedBy | String | M |  |
| idCountry | String | M |  |
| thirdPartyDetermination | String | M |  |
| declaration | String | M |  |
| customerCode | String | M |  |
| customerStatus | String | M |  |
| transactionVolumeCode | String | M |  |
| isSenderPep | String | M |  |
| ownerDetailList | String | M | null(in case of individual) |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Request Details

```http
PUT /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
PUT http://host/ewallet/api/v1/customer-registration/10000***71
{
"customerTypeCode": "100001",
"customerSubTypeCode": "100001",
"docReferenceNumber": "CUSE6N1GF5",
"walletOwnerCode": "1000008929",
"firstName": "Rajat",
"middleName": "kumar",
"lastName": "singh",
"dateOfBirth": "2007-01-11",
"gender": "male",
"nationality": "AIA",
"mobileNumber": "8767655555",
"dialCode": "265",
"email": "mailto:pankaj.singh@remittanceshub.com",
"occupationCode": "100002",
"jobTitle": "estel",
"jobIndustry": "estel",
"addressLine1": "delhi",
"addressLine2": "alkayda",
"countryCode": "MWI",
"residenceStatusCode": "100004",
"state": "alkayda",
"city": "malawi",
"pincode": "322222",
"idTypeCode": "100002",
"idNumber": "ID121232322323",
"idCountry": "MWI",
"issueDate": "",
"idExpiryDate": "",
"thirdPartyDetermination": true,
"declaration": true,
"customerCode": "1000001971",
"noIssueDate": true,
"noIdExpiry": true,
"customerStatus": "Y",
"transactionVolumeCode": "100002",
"isSenderPep": true,
"ownerDetailList": null
}
```

##### Response Parameter

| Parameters     | Data Type| Requirement | Description |
|----------|:-----:|:-----:|--------|
| id | String | M |  |
| code | String | M |  |
| customerTypeCode | String | M | Individual : 100001, Business : 100002 |
| customerSubTypeCode | String | M | 100001 |
| walletOwnerCode | String | M | Send Client Code |
| customerId | String | M | Id of registered customer |
| firstName | String | M |  |
| middleName | String | M |  |
| lastName | String | M |  |
| fullName | String | M |  |
| dateOfBirth | String | M |  |
| gender | String | M |  |
| nationality | String | M |  |
| email | String | M |  |
| mobileNumber | String | M |  |
| occupationCode | String | M |  |
| jobTitle | String | M |  |
| jobIndustry | String | M |  |
| addressline1 | String | M |  |
| city | String | M |  |
| state | String | M |  |
| countryCode | String | M |  |
| residenceStatusCode | String | M |  |
| idTypeCode | String | M |  |
| idNumber | String | M |  |
| idCountry | String | M |  |
| transactionVolumeCode | String | M |  |
| screeningStatus | String | M |  |
| screeningScore | String | M |  |
| screeningUniqueId | String | M |  |
| screeningDate | String | M |  |
| thirdPartyDetermination | String | M |  |
| isSenderPep | String | M |  |
| declaration | String | M |  |
| customerStatus | String | M |  |
| customerState | String | M |  |
| customerStateCode | String | M |  |
| nationalityName | String | M |  |
| countryName | String | M |  |
| idCountryName | String | M |  |
| transactionVolumeName | String | M |  |
| customerTypeName | String | M |  |
| creationDate | String | M |  |
| modificationDate | String | O |  |
| createdBy | String | M |  |
| modifiedBy | String | M |  |
| noIssueDate | String | M |  |
| noIdExpiry | String | M |  |
| dialCode | String | M | Country dial code |
| sendClientName | String | M |  |
| docReferenceNumber | String | M |  |
| walletOwnerName | String | M |  |
| logoUrl | String | M |  |
| sendClientAddress | String | M |  |
| sendClientMobileNo | String | M |  |
| occupationName | String | M |  |
| residenceStatusName | String | M |  |
| idTypeName | String | M |  |
| registrationApprovedBy | String | M |  |
| registrationNumber | String | M |  |
| serviceTypeCode | String | M |  |
| payoutClientCodes | String | M | Array of payout client codes |
| senderPep | String | M |  |
| autoRegistered | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Response Details

```json
{
"transactionId": "9188309",
"requestTime": "Mon Jan 20 17:10:30 IST 2025",
"responseTime": "Mon Jan 20 17:10:30 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"customerRegistration": {
    "id": 1900,
    "code": "1000001971",
    "customerTypeCode": "100001",
    "customerSubTypeCode": "100001",
    "walletOwnerCode": "1000008929",
    "customerId": "100000892911971I",
    "firstName": "Rajat",
    "middleName": "kumar",
    "lastName": "singh",
    "fullName": "Rajat kumar singh",
    "nickName": "Rajat",
    "tradeName": "Rajat kumar singh",
    "gender": "male",
    "nationality": "AIA",
    "dateOfBirth": "2007-01-11",
    "email": "mailto:pankaj.singh@remittanceshub.com",
    "mobileNumber": "8767655555",
    "occupationCode": "100002",
    "jobTitle": "estel",
    "jobIndustry": "estel",
    "addressLine1": "delhi",
    "addressLine2": "alkayda",
    "city": "malawi",
    "state": "alkayda",
    "pincode": "322222",
    "countryCode": "MWI",
    "residenceStatusCode": "100004",
    "idTypeCode": "100002",
    "idNumber": "ID121232322323",
    "idCountry": "MWI",
    "transactionVolumeCode": "100002",
    "screeningStatus": "SP",
    "screeningScore": "100.0",
    "screeningUniqueId": "1000001",
    "screeningDate": "2025-01-16T13:04:00.024+0530",
    "thirdPartyDetermination": true,
    "isSenderPep": true,
    "declaration": true,
    "customerStatus": "Active",
    "customerState": "System Approved",
    "customerStateCode": "AA",
    "nationalityName": "Anguilla",
    "countryName": "Malawi",
    "idCountryName": "Malawi",
    "transactionVolumeName": "Between 10,000 and 1,000,000",
    "customerTypeName": "Individual",
    "creationDate": "2025-01-16T13:03:47.758+0530",
    "modificationDate": "2025-01-20T17:10:30.860+0530",
    "createdBy": "105732",
    "modifiedBy": "105732",
    "noIssueDate": true,
    "noIdExpiry": true,
    "dialCode": "265",
    "sendClientName": "ESTEL",
    "docReferenceNumber": "CUSE6N1GF5",
    "walletOwnerName": "ESTEL",
    "logoUrl": "/fileUpload/download/1000008929/logo 1DADANADA.jpg",
    "businessTransactionVolume": "Between 10,000 and 1,000,000",
    "sendClientAddress": "Malawi, Malawi, Blantyre, Blantyre, Malawi",
    "sendClientMobileNo": "26533545636654",
    "occupationName": "Actor / Actress",
    "residenceStatusName": "National",
    "idTypeName": "Govt Approved ID",
    "registrationApprovedBy": "ESTEL",
    "registrationNumber": "ID121232322323",
    "payoutClientCodes": [
        "1000008926"
    ],
    "senderPep": true,
    "autoRegistered": true
}
}
```

### Owner Details

`POST` — status: **REVIEW REQUIRED (commented out in source)**

:::info[Endpoint]

`POST`  `http://host/api/v1/owner-details`

:::

The Owner Details API is used to create / update the owner in the system.

##### Request Parameter

| Parameters     | Data Type | Requirements | Description |
|----------|:------------:|:-----:|--------|
| customerCode/ID | String | M |  |
| **Owner Details** |  |  |  |
| firstName | String | M |  |
| middleName | String | M |  |
| lastName | String | M |  |
| companyName | String | M |  |
| gender | String | M |  |
| nationality | String | M |  |
| dateOfBirth | String | M |  |
| email | String | M |  |
| mobileNo | String | M |  |
| addressLine1 | String | M |  |
| addressLine2 | String | M |  |
| city | String | M |  |
| state | String | M |  |
| pincode | String | M |  |
| country | String | M |  |
| idNumber | String | M |  |
| idIssuedBy | String | M |  |
| idCountry | String | M |  |
| issueDate | String | M |  |
| idExpiry | String | M |  |
| residenceStatusCode | String | M |  |
| ownerPercentage | String | M |  |
| transactionVolumeCode | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/api/v1/customer-registration
{
 "customerTypeCode": "100002",
 "customerSubTypeCode": "100001",
 "docReferenceNumber": "CUSV122UU1",
 "walletOwnerCode": "1000008960",
 "tradeName": "tech technology",
 "legalStatusCode": "100007",
 "natureOfBusinessCode": "100017",
 "businessRelationshipCode": "100003",
 "businessAuthorizedPerson": "test",
 "mobileNumber": "09098987876",
 "dialCode": "265",
 "email": "pankaj.singh@estelteelcom.com",
 "addressLine1": "malawi",
 "addressLine2": "",
 "countryCode": "MWI",
 "state": "test",
 "city": "test",
 "pincode": "333333",
 "idNumber": "ID7656576767",
 "idIssuedBy": "",
 "idCountry": "IND",
 "issueDate": "2024-09-10",
 "idExpiryDate": "2024-09-30",
 "thirdPartyDetermination": true,
 "transactionVolumeCode": "100005",
 "isSenderPep": true,
 "declaration": true,
 "customerCode": "",
 "noIssueDate": false,
 "noIdExpiry": false,
 "customerStatus": "",
   "ownerDetailList": [
{
 "indexId": 1,
 "customerCode": "",
 "customerTypeCode": "100001",
  "firstName": "Rajesh",
  "middleName": "kumar",
  "lastName": "Singh",
  "dateOfBirth": "2006-09-10",
  "gender": "male",
  "nationality": "MWI",
  "mobileNumber": "9999809898",
  "dialCode": "265",
  "email": "pankaj.singh@remittanceshub.com",
  "companyName": "Infosys technology",
  "addressLine1": "new delhi new",
  "addressLine2": "new delhi new",
  "countryCode": "CAN",
  "residenceStatusCode": "100004",
  "state": "new delhi 2",
  "city": "new delhi 3",
  "pincode": "323434",
  "idTypeCode": "100001",
  "idNumber": "ID7656576767",
  "idIssuedBy": "estel",
  "idCountry": "MWI",
  "issueDate": "2024-09-10",
  "idExpiry": "",
  "noIssueDate": false,
  "noIdExpiry": true,
  "ownerPercentage": 34,
  "ownerStatus": ""
},
{
  "indexId": 2,
  "customerCode": "",
  "customerTypeCode": "100002",
  "firstName": "",
  "middleName": "",
  "lastName": "",
  "nationality": "IND",
  "mobileNumber": "9999098987",
  "dialCode": "265",
  "email": "pankaj.singh@esteltelecom.com",
  "companyName": "estel technology",
  "businessAuthorizedPerson": "trader estel",
  "addressLine1": "resttt",
  "addressLine2": "resttsts",
  "countryCode": "MWI",
  "residenceStatusCode": "100001",
  "state": "reeee",
  "city": "eeeee",
  "pincode": "233232233232",
  "ownerPercentage": 54,
  "ownerStatus": ""
}
]
}
```

### Search Customer

`GET` — status: **REVIEW REQUIRED (commented out in source)**

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/customer-registration/all?{customerId}&{fullName}&{walletOwnerCode}&{customerTypeCode}&{offset}&{limit}`

:::

The customer search api is used to search for the registered customer based on the customer id or name.

##### Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| customerId | String | C | The customer id received after successful registration. (customerId or fullName, anyone is mandatory) |
| fullName | String | C | The customer name given while customer registration. (fullName or customerId, anyone is mandatory) |
| walletOwner Code | String | M | Business(send) partner code |
| customerType Code | String | M | Individual : 100001, Business : 100002 |
| offset | String | O | From where to fetch the data. eg: 0. |
| limit | String | O | The count of the record to be displayed in a single page. eg: 5. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET -
http://host/ewallet/api/v1/customer-registration/all?customerId=100000892912003I&fullName=rajesh
&walletOwnerCode=1000008929&customerTypeCode=100001&offset=0&limit=5
```

##### Response Parameter for Individual

| Parameters     | Data Type| Requirement | Description |
|----------|:-----:|:-----:|--------|
| id | String | M |  |
| code | String | M |  |
| customerTypeCode | String | M | Individual : 100001, Business : 100002 |
| customerSubTypeCode | String | M | 100001 |
| walletOwnerCode | String | M | Send Client Code |
| customerId | String | M | Id of registered customer |
| firstName | String | M |  |
| middleName | String | M |  |
| lastName | String | M |  |
| fullName | String | M | Full name of customer |
| tradeName | String | M |  |
| gender | String | M |  |
| nationality | String | M |  |
| dateOfBirth | String | M |  |
| mobileNumber | String | M |  |
| addressline1 | String | M |  |
| city | String | M |  |
| state | String | M |  |
| pincode | String | M |  |
| countryCode | String | M |  |
| idNumber | String | M |  |
| issueDate | String | M |  |
| idExpiryDate | String | M |  |
| declaration | String | M |  |
| customerStatus | String | M |  |
| nationalityName | String | M |  |
| countryName | String | M |  |
| customerTypeName | String | M |  |
| creationDate | String | M |  |
| modificationDate | String | O |  |
| createdBy | String | M |  |
| noIssueDate | String | M |  |
| noIdExpiry | String | M |  |
| dialCode | String | M | Country dial code |
| sendClientName | String | M |  |
| walletOwnerName | String | M |  |
| logoUrl | String | M |  |
| sendClientAddress | String | M |  |
| sendClientMobileNo | String | M |  |
| registrationNumber | String | M |  |
| autoRegistered | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Response Details for Individual

```json
{
"transactionId": "7851173",
"requestTime": "Wed Sep 04 11:03:15 IST 2024",
"responseTime": "Wed Sep 04 11:03:16 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"pageable": {
    "limit": 5,
    "offset": 0,
    "totalRecords": 1
},
"customerRegistrationList": [
    {
        "id": 1843,
        "code": "1000001913",
        "customerTypeCode": "100001",
        "walletOwnerCode": "1000008929",
        "customerId": "100000892911913I",
        "firstName": "Rajesh",
        "lastName": "singh",
        "fullName": "Rajesh singh",
        "gender": "male",
        "nationality": "MWI",
        "dateOfBirth": "2007-01-11",
        "mobileNumber": "9098987888",
        "addressLine1": "malawi",
        "city": "malawi",
        "state": "Delhi",
        "pincode": "malawi",
        "countryCode": "MWI",
        "idNumber": "ID321322332",
        "issueDate": "2025-01-11T05:30:00.000+0530",
        "idExpiryDate": "2025-01-31T05:30:00.000+0530",
        "declaration": true,
        "customerStatus": "Active",
        "nationalityName": "Malawi",
        "countryName": "Malawi",
        "customerTypeName": "Individual",
        "creationDate": "2025-01-12T14:34:23.372+0530",
        "modificationDate": "2025-01-12T14:34:23.435+0530",
        "createdBy": "105732",
        "noIssueDate": false,
        "noIdExpiry": false,
        "dialCode": "265",
        "sendClientName": "ESTEL",
        "walletOwnerName": "ESTEL",
        "logoUrl": "/fileUpload/download/1000008929/logo 1DADANADA.jpg",
        "sendClientAddress": "Malawi, Malawi, Blantyre, Blantyre, Malawi",
        "sendClientMobileNo": "26533545636654",
        "registrationNumber": "ID321322332",
        "autoRegistered": true
    }
  ]
}
```

##### Response Parameter for Business

| Parameters     | Data Type| Requirement | Description |
|----------|:-----:|:-----:|--------|
| id | String | M |  |
| code | String | M |  |
| customerTypeCode | String | M | Individual : 100001, Business : 100002 |
| customerSubTypeCode | String | M | 100001 |
| walletOwnerCode | String | M | Send Client Code |
| customerId | String | M | Id of registered customer |
| fullName | String | M | Full name of customer |
| tradeName | String | M |  |
| addressline1 | String | M |  |
| city | String | M |  |
| state | String | M |  |
| pincode | String | M |  |
| countryCode | String | M |  |
| idNumber | String | M |  |
| idCountry | String | M |  |
| issueDate | String | M |  |
| idExpiryDate | String | M |  |
| thirdPartyDetermination | String | M |  |
| declaration | String | M |  |
| customerStatus | String | M |  |
| customerState | String | M |  |
| countryName | String | M |  |
| idCountryName | String | M |  |
| customerTypeName | String | M |  |
| creationDate | String | M |  |
| modificationDate | String | O |  |
| noIssueDate | String | M |  |
| noIdExpiry | String | M |  |
| sendClientName | String | M |  |
| docReferenceNumber | String | M |  |
| walletOwnerName | String | M |  |
| logoUrl | String | M |  |
| sendClientAddress | String | M |  |
| sendClientMobileNo | String | M |  |
| registrationNumber | String | M |  |
| autoRegistered | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Response Details for Business

```json
{
"transactionId": "7851173",
"requestTime": "Wed Sep 04 11:03:15 IST 2024",
"responseTime": "Wed Sep 04 11:03:16 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"pageable": {
    "limit": 5,
    "offset": 0,
    "totalRecords": 1
},
"customerRegistrationList": [
    {
         "id": 1851,
        "code": "1000001921",
        "customerTypeCode": "100002",
        "customerSubTypeCode": "100001",
        "walletOwnerCode": "1000008929",
        "customerId": "100000892911921B",
        "fullName": " Infosys Technology",
        "tradeName": " Infosys Technology",
        "dateOfBirth": "2025-01-10",
        "addressLine1": "new delhi new",
        "city": "new delhi",
        "state": "new delhi",
        "pincode": "323434",
        "countryCode": "MWI",
        "idNumber": "9099998988",
        "idCountry": "MWI",
        "issueDate": "2025-01-10T05:30:00.000+0530",
        "idExpiryDate": "2025-01-31T05:30:00.000+0530",
        "thirdPartyDetermination": false,
        "declaration": true,
        "customerStatus": "Active",
        "customerState": "System Approved",
        ""countryName": "Malawi",
        "idCountryName": "Malawi",
        "customerTypeName": "Juridical Owner",
        "creationDate": "2025-01-13T12:41:55.818+0530",
        "modificationDate": "2025-01-13T12:41:56.026+0530",
        "noIssueDate": false,
        "noIdExpiry": false,
        "sendClientName": "ESTEL",
        "docReferenceNumber": "CUS5NBRGUQ",
        "walletOwnerName": "ESTEL",
        "logoUrl": "/fileUpload/download/1000008929/logo 1DADANADA.jpg",
        "sendClientAddress": "Malawi, Malawi, Blantyre, Blantyre, Malawi",
        "sendClientMobileNo": "26533545636654",
        "registrationNumber": "9099998988",
        "autoRegistered": true
    }
  ]
}
```

### Search Beneficiary

`GET` — status: **REVIEW REQUIRED (commented out in source)**

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/customer-registration/beneficiary?{customerTypeCode=value}&{walletOwnerCode=value}&{customerCode=value}&{offset}&{limit}`

:::

The beneficiary search api is used to search for the beneficiary of registered customer.

##### Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| customerType Code | String | M | Individual : 100001, Business : 100002 |
| walletOwner Code | String | M | Business(send) partner code |
| customerCode | String | M | Recieved after successful customer registration or after successful payout(in case of on the fly registration). |
| offset | String | O | From where to fetch the data. eg: 0. |
| limit | String | O | The count of the record to be displayed in a single page. eg: 5. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET -
http://host/ewallet/api/v1/customer-registration/beneficiary?customerTypeCode=100002&walletOwnerCode=1000*****9&customerCode=1000***921&offset=0&limit=5
```

##### Response Parameter

| Parameters     | Data Type| Requirement | Description |
|----------|:-----:|:-----:|--------|
| id | String | M |  |
| code | String | M |  |
| customerId | String | M | Id of registered customer |
| fullName | String | M | Full name of beneficiary |
| tradeName | String | M |  |
| mobileNumber | String | M |  |
| addressline1 | String | M |  |
| city | String | M |  |
| state | String | M |  |
| countryCode | String | M |  |
| idCountry | String | M |  |
| screeningStatus | String | M |  |
| screeningScore | String | M |  |
| screeningUniqueId | String | M |  |
| thirdPartyDetermination | String | M |  |
| isSenderPep | String | M |  |
| declaration | String | M |  |
| countryName | String | M |  |
| creationDate | String | M |  |
| modificationDate | String | O |  |
| dialCode | String | M | Country dial code |
| natureOfBusiness | String | M |  |
| registrationType | String | M |  |
| registrationIssueAt | String | M |  |
| bankFullName | String | M |  |
| bankAccountNo | String | M |  |
| bankAccountHolderName | String | M |  |
| swiftCode | String | M |  |
| receiverPayoutCode | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Response Details

```json
{
"transactionId": "7851173",
"requestTime": "Wed Sep 04 11:03:15 IST 2024",
"responseTime": "Wed Sep 04 11:03:16 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"pageable": {
    "limit": 5,
    "offset": 0,
    "totalRecords": 1
},
"customerRegistrationList": [
    {
        "id": 4405,
        "code": "1000004411",
        "customerId": "100000892911921B",
        "fullName": "Gujarat titans",
        "tradeName": "Gujarat titans",
        "mobileNumber": "9899998988",
        "addressLine1": "new delhi new",
        "city": "new delhi",
        "state": "new delhi",
        "countryCode": "ARE",
        "idCountry": "ARE",
        "screeningStatus": "SP",
        "screeningScore": "0.0",
        "screeningUniqueId": "REC888888UID",
        "thirdPartyDetermination": false,
        "isSenderPep": false,
        "declaration": false,
        "countryName": "United Arab Emirates",
        "creationDate": "2025-01-13T12:41:56.002+0530",
        "modificationDate": "2025-01-13T12:42:00.090+0530",
        "dialCode": "971",
        "natureOfBusiness": "Corporation",
        "registrationType": "Corporation",
        "registrationIssueAt": "ARE",
        "bankFullName": "Emirates NBD",
        "bankAccountNo": "AE110260000959024298101",
        "bankAccountHolderName": "Gujarat titans ",
        "swiftCode": "EBILAEAD",
        "receiverPayoutCode": "1000009019",
        "senderPep": false
    }
  ]
}
```

### Document Upload

`POST` — status: **REVIEW REQUIRED (commented out in source)**

:::info[Endpoint]

`POST`  `http://host/ewallet/api/v1/documentUpload/upload/customer`

:::

The Document Upload API is used to upload the ID proof documents of the specific customer of the send client.

##### Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| walletOwnerCode | String | M | To unique code of the customer whose ID proof document is to be uploaded. |
| docReference Number | String | M | To unique code of the ID proof document that is to be uploaded. |
| file | String | M | The actual document which needs to be uploaded in pdf, jpg or png format. (not more than 5000kb) |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST -
http://host/ewallet/api/v1/documentUpload/upload/customer
```

##### Response Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Doc Upload** |  |  |  |  |
| code | String | M |  |  |
| walletOwnerCode | String | M | The unique code of the customer or wallet owner whose document is to be fetched. |  |
| docReferenceNumber | String | M | To unique code of the document, recieved after uploading the document. |  |
| transId | String | M |  |  |
| fileName | String | M | The file name of the ID proof document to be fetched. |  |
| byteArr | String | M | The byte array used to store the binary data. |  |
| fileLocation | String | M | The location where the ID proof document is stored. |  |
| createdOn | String | M | The date and time when the ID proof document was uploaded. The date and time conforms the following format. YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |
| status | String | M | The status of the ID proof document. |  |
| createdBy | String | M | The unique code of the agent who uploaded the ID proof document of the customer or wallet owner. |  |
| source | String | M | The source who uploaded the ID proof document of the customer or wallet owner. |  |
| docTypeCode | String | M | The unique code of the ID proof document that was uploaded. |  |
| docTypeName | String | M | The name of the ID proof document that was uploaded. |  |
| sendClientName | String | M | The name of the send client under whom the customer is registered. |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

##### Response Details

```json
{
  transactionId	"8299691"
  requestTime	"Thu Jun 20 15:29:37 IST 2024"
  responseTime	"Thu Jun 20 15:29:37 IST 2024"
  resultCode	"0"
  resultDescription	"Transaction successful"
  docUpload	Object { walletOwnerCode: "1000008998", docReferenceNumber:
   "CUSYC5A3ZH", fileName: "ID_front-960x600_CUSYC5A3ZH_20240620152937.jpg", … }
  code	""
  walletOwnerCode	"1000008998"
  docReferenceNumber	"CUSYC5A3ZH"
  transId	""
  fileName	"ID_front-960x600_CUSYC5A3ZH_20240620152937.jpg"
  byteArr	null
  fileLocation	"/opt/documentUpload/1000008998/CUSYC5A3ZH"
  createdOn	"2024-06-20T15:29:37.584+0530"
  status	"Active"
  createdBy	"105790"
  source	"CLIENT"
  docTypeCode	"100007"
  docTypeName	"Certificate of Incorporation"
  sendClientName	"marvel "
  createdByName	"marvel "
}
```

## Commented code tables (from responseCodes.md)

| Code | Description            |
|------|------------------------|
| PF | Payout Fail |
| PP | Payout Pass |
| RV | Reverse/ Reject |
| IP | In Process |
| -1 | Technical Failure |

```text
 | PI   | Payout Initiated       |
| PN   | Payout Pending         |
| RA/TSS/TSA/IFSA/PC/SBOK/IDSA/BRQSA <br /> (Depending upon the partner) | Payout Processing      |
| 00   | Transaction Successful |
```

*Source fragment: this table has no header row in the RHUB source (it is a continuation of a preceding table). It is reproduced verbatim rather than given an invented header — REVIEW REQUIRED.*

#### Validation Code

| Code | Description                                                                                                                            |
|------|----------------------------------------------------------------------------------------------------------------------------------------|
| 1358 | Fx quotation config not found for specific code |
| 1360 | Payout partner does not exist |
| 1361 | Margin not configured for specific currency |
| 1362 | Fxvalidity not configured for specific currency |
| 1363 | Similar max and min value configuration already exist |
| 1364 | Master business type not found |
| 1365 | Exchange Rate not found |
| 1366 | Transaction not allowed, please contact support@remittanceshub.com for assistance |
| 1367 | Payout bank list not found |
| 1368 | Some parameters are missing in quotation request |
| 1369 | Invalid Payin currency |
| 1370 | Invalid Payout currency |
| 1371 | Invalid Payin settlement currency |
| 1372 | Forex quote id expired |
| 1373 | Forex quote id already used |
| 1374 | Invalid Client Code |
| 1375 | Invalid Email |
| 1376 | Template already exist for specific client |
| 1377 | Service to Beneficiary Country are temporarily unavailable |
| 1378 | Service to Sender Country are temporarily unavailable |
| 1379 | Service to Beneficiary Currency are temporarily unavailable |
| 1380 | Your transaction limit is exceeding the permissible cash limit, please select Bank Transfer/Cheque as mode to proceed with transaction |
| 1381 | Role inactive, please contact your administrator to enable the same |
