---
title: "Customer Registration"
sidebar_label: "Customer Registration"
description: "RHUB Customer Registration API — register business and individual customers."
---

# Customer Registration

<span className="rhub-method rhub-method--post">POST</span>

*Source of truth: `CUSTOMEREGIS.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

There are two methods for registering a customer:

* Using this API.
* On-the-fly registration during payout.

If you choose auto-registration (on-the-fly registration) during payout, this API is not required.

:::info[Endpoint]

`POST`  `http://host/ewallet/api/v1/customer-registration`

:::

The Customer-Registration API is used to register or create the customer in the system.

## Request Parameter of Business Customer

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| customerTypeCode | Numeric | 06 | M | Individual : 100001, Business : 100002 eg: 100002 |
| customerSubTypeCode | Numeric | 06 | M | 100001 |
| serviceTypeCode | Alpha | 07 | M | REGULAR |
| docReferenceNumber | Alphanumeric | 10 - 30 | M | 10 digit unique doc reference number, used while uploading document. eg: GHJ7K87GJGG6 (should contains 10 to 30 digits alpha numeric only) |
| walletOwnerCode | Numeric | 10 | M | Send Client Code. eg:1000009999 |
| tradeName | Alphanumeric | 01 - 70 | M | Company trade name. eg: Hcl tech |
| natureOfBusinessCode | Alphanumeric | 06 - 10 | M | Select the suited data received from nature of business Api. (eg: RHT011 , refer NatureOfBusinessApi ) |
| dialCode | Alphanumeric with '+' symbol | 02 - 04 | C | Country dial code. eg: +1, +91 note: Required when the contact number dial code does not match the selected country code. |
| mobileNumber | Alphanumeric | 07 - 20 | M | Contact number. eg: 9090909090 |
| email | Alphanumeric + special characters (Email format) | 01 - 50 | M | Email id of customer. eg: hcl@gmail.com |
| addressLine1 | Alphanumeric | 01 - 35 | M | Address detail of business. eg: A455 Wall street |
| countryCode | Alpha | 03 | M | 3-digit Country code of business's address. eg:MWI,DZA etc |
| state | Alpha | 01 - 50 | M | State eg: Delhi |
| city | Alpha | 01 - 50 | M | City eg: Delhi |
| pincode | Alphanumeric | 01 - 10 | M | Pincode eg: SDFC2345 |
| businessRelationshipCode | Numeric | 06 | O | for International Remittance use : 100003, for Others use : 100004 |
| businessAuthorizedPerson | Alpha | 01 - 50 | O | The authorized person in the company. eg: John Wick |
| legalStatusCode | Alphanumeric | 06 - 10 | M | Select the suited data received from Business Registration Type/Legal Status API from Master. (eg: RHB002 , refer LegalStatusApi) |
| idNumber | Alphanumeric | 01 - 50 | M | Business registration/license number. eg: GJJKJHKJH889GJ |
| idCountry | Alpha | 03 | M | Business registration/license country code, eg: MWI,USD etc |
| issueDate | Date | 10 - 19 | M | Business registration/license issue date in yyyy-mm-dd format. eg: 1999-09-12 |
| idExpiryDate | Date | 10 - 19 | M | Business registration/license expiry date in yyyy-mm-dd format. eg: 1999-09-12 |
| **ownerDetailList** |  |  |  |  |
| **//for individual owner** |  |  |  |  |
| customerTypeCode | Numeric | 06 | M | for Individual owner : 100001 |
| firstName | Alpha | 01 - 75 | M | First name of owner. eg: Rahul |
| lastName | Alpha | 02 - 75 | M | Last name of owner. eg: Sharma |
| dateOfBirth | Date | 10 - 19 | M | Date of birth of owner in yyyy-mm-dd format. eg: 1999-09-12 |
| gender | Alpha | 01 - 10 | M | Gender of owner (male, female, other) |
| addressLine1 | Alphanumeric | 01 - 35 | M | Address detail of owner. eg: 89WE jane street |
| countryCode | Alpha | 03 | M | 3-digit Country code of owner's address. eg: MWI,DZA etc |
| state | Alpha | 01 - 50 | M | State. eg: Delhi |
| city | Alpha | 01 - 50 | M | City eg: Delhi |
| pincode | Alphanumeric | 01 - 10 | M | Pincode eg: SDFC2345 |
| idTypeCode | Alphanumeric | 06 - 10 | M | The predefined code corresponding to the different document types for business. eg: eg: RHD006 (for more info, please refer to DocumentTypeApi) |
| idNumber | Alphanumeric | 01 - 50 | M | Id numder of the Id proof provided for Kyc. eg:JHGHG987KIUK |
| idCountry | Alpha | 03 | M | 3-digit Country code of country where id issued. eg: USA, IND |
| **//for business owner** |  |  |  |  |
| customerTypeCode | Numeric | 06 | M | for Business owner : 100002 |
| companyName | Alphanumeric | 01 - 70 | M | Business company/Trade name eg: hcl tech |
| addressLine1 | Alphanumeric | 01 - 35 | M | Address detail of company eg: HG68 WASHINGTON ROAD |
| countryCode | Alpha | 03 | M | 3-digit Country code of company. eg: USA, CHN |
| state | Alpha | 01 - 50 | M | State eg: Delhi |
| city | Alpha | 01 - 50 | M | City eg: New york |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details of Business Customer

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/customer-registration
{
  "customerTypeCode": "100002",
  "customerSubTypeCode": "100001",
  "serviceTypeCode": "REGULAR",
  "docReferenceNumber": "CUSYONEIUK",
  "walletOwnerCode": "1000008398",.
  "tradeName": "Estel technology",
  "natureOfBusinessCode": "RHT010",
  "mobileNumber": "9099998987",
  "email": "pankaj.singh@esteltelecom.com",
  "addressLine1": "malawi",
  "countryCode": "MWI",
  "state": "malawi",
  "city": "malawi",
  "pincode": "676567",
  "businessRelationshipCode": "100003",
  "businessAuthorizedPerson": "Estel",
  "legalStatusCode": "RHB002",
  "idNumber": "ID321412123123",
  "idCountry": "CAN",
  "issueDate": "2024-08-22",
  "idExpiryDate": "2024-08-31",
  "ownerDetailList": [
  {
    "customerTypeCode": "100001",
    "firstName": "Rajesh",
    "lastName": "Mishra",
    "dateOfBirth": "2006-08-22",
    "gender": "male",
    "companyName": "",
    "addressLine1": "malawi",
    "countryCode": "MWI",
    "state": "Malawi",
    "city": "malawi",
    "pincode": "121122",
    "idTypeCode": "RHD002",
    "idNumber": "ID1212121212",
    "idCountry": "IND",
 },
  {
    "customerTypeCode": "100002",
    "companyName": "Estel technology",
    "addressLine1": "malawi",
    "countryCode": "MWI",
    "state": "malawi",
    "city": "malawi",
  }
  ]
  }
```

## Response Details of Business Customer

```json
{
"transactionId": "7915520",
"requestTime": "Mon Feb 03 11:51:46 IST 2025",
"responseTime": "Mon Feb 03 11:51:47 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"customerRegistration": {
    "code": "1000000645",
    "customerTypeCode": "100002",
    "customerSubTypeCode": "100001",
    "walletOwnerCode": "1000008398",
    "customerId": "100000839810647B",
    "fullName": "Estel technology",
    "tradeName": "Estel technology",
    "natureOfBusinessCode": "RHT010",
    "mobileNumber": "9099998987",
    "addressLine1": "malawi",
    "city": "malawi",
    "state": "malawi",
    "pincode": "676567",
    "countryCode": "MWI",
    "idNumber": "ID321412123103",
    "idCountry": "CAN",
    "issueDate": "2024-08-22T00:00:00.000+0530",
    "idExpiryDate": "2024-08-31T00:00:00.000+0530",
    "screeningStatus": "IP",
    "customerStatus": "Active",
    "customerState": "System Approved",
    "customerStateCode": "AA",
    "countryName": "Malawi",
    "idCountryName": "Canada",
    "natureOfBusinessName": "Banking",
    "customerTypeName": "Juridical Owner",
    "creationDate": "2025-02-03T11:51:46.907+0530",
    "createdBy": "105513",
    "sendClientName": "Estel Technologies",
    "docReferenceNumber": "1234563GFM",
    "walletOwnerName": "Estel Technologies",
    "logoUrl": "/fileUpload/download/1000008398/Estel_logo.jpeg",
    "sendClientAddress": "Street No 5, Park Avenue , Blantyre, Blantyre, Malawi",
    "sendClientMobileNo": "265768568432",
    "registrationApprovedBy": "Wirease",
    "registrationNumber": "ID321412123103",
    "ownerDetailList": [
        {
            "code": "1000000458",
            "customerTypeCode": "100001",
            "ownerId": "100000839810647B00",
            "customerCode": "1000000645",
            "firstName": "Rajesh",
            "middleName": "",
            "lastName": "Mishra",
            "companyName": "",
            "fullName": "Rajesh Mishra",
            "gender": "male",
            "nationality": "",
            "dateOfBirth": "2006-08-22 00:00:00",
            "email": "",
            "mobileNumber": "",
            "addressLine1": "malawi",
            "addressLine2": "",
            "city": "malawi",
            "state": "Malawi",
            "pincode": "121122",
            "countryCode": "MWI",
            "residenceStatusCode": "",
            "transactionVolumeCode": "",
            "idTypeCode": "RHD002",
            "idNumber": "ID1212121212",
            "idIssuedBy": "",
            "idCountry": "IND",
            "screeningStatus": "IP",
            "screeningScore": "",
            "screeningUniqueId": "",
            "screeningUrl": "",
            "creationDate": "2025-02-03T11:51:46.998+0530",
            "ownerStatus": "Active",
            "ownerState": "System Approved",
            "ownerStateCode": "AA",
            "dialCode": "",
            "businessAuthorizedPerson": "",
            "source": ""
        },
        {
            "code": "1000000459",
            "customerTypeCode": "100002",
            "ownerId": "100000839810647B00",
            "customerCode": "1000000645",
            "firstName": "",
            "middleName": "",
            "lastName": "",
            "companyName": "Estel technology",
            "fullName": "",
            "gender": "",
            "nationality": "",
            "email": "",
            "mobileNumber": "",
            "addressLine1": "malawi",
            "addressLine2": "",
            "city": "malawi",
            "state": "malawi",
            "pincode": "121212",
            "countryCode": "MWI",
            "residenceStatusCode": "",
            "transactionVolumeCode": "",
            "idTypeCode": "",
            "idNumber": "",
            "idIssuedBy": "",
            "idCountry": "",
            "screeningStatus": "IP",
            "screeningScore": "",
            "screeningUniqueId": "",
            "screeningUrl": "",
            "creationDate": "2025-02-03T11:51:47.335+0530",
            "ownerStatus": "Active",
            "ownerState": "System Approved",
            "ownerStateCode": "AA",
            "dialCode": "",
            "businessAuthorizedPerson": "",
            "source": ""
        }
    ],
    "autoRegistered": false
}
}
```

## Request Parameter of Individual Customer

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| customerTypeCode | Numeric | 06 | M | Individual : 100001, Business : 100002 eg: 100001 |
| customerSubTypeCode | Numeric | 06 | M | 100001 |
| serviceTypeCode | Alpha | 07 | M | REGULAR |
| docReferenceNumber | Alphanumeric | 10 - 30 | M | 10 digit unique doc reference number, used while uploading document. eg: GHJ7K87GJGG6 (should contains 10 to 30 digits alpha numeric only) |
| walletOwnerCode | Numeric | 10 | M | Send Client Code for which the customer is being registered eg:1000009999 |
| firstName | Alpha | 01 - 75 | M | First name of customer eg: Rahul |
| lastName | Alpha | 02 - 75 | M | Last name of customer eg: Sharma |
| dateOfBirth | Date | 10 - 19 | M | Customer's date of birth in yyyy-mm-dd format. eg: 1999-09-12 |
| gender | Alpha | 01 - 10 | M | Customer's gender. (male, female, other) |
| nationality | Alpha | 03 | M | Nationality of customer in 3-digit Country code format. eg:DZA,USA etc |
| dialCode | Alphanumeric with '+' symbol | 02 - 04 | C | Country dial code. eg: +1, +91 note: Required when the contact number dial code does not match the selected country code. |
| mobileNumber | Alphanumeric | 07 - 20 | M | Contact number. eg: 9090909090 |
| email | Alphanumeric + special characters (Email format) | 01 - 50 | M | Email id of customer. eg: hcl@gmail.com |
| addressLine1 | Alphanumeric | 01 - 35 | M | Address details of customer eg: A455 Wall street |
| countryCode | Alpha | 03 | M | 3-digit Country code of customer's residence. eg:MWI,DZA etc |
| state | Alpha | 01 - 50 | M | State of customer's residence eg: Delhi |
| city | Alpha | 01 - 50 | M | City of customer's residence eg: Delhi |
| pincode | Alphanumeric | 01 - 10 | M | Address pincode eg: SDFC2345 |
| occupationCode | Alphanumeric | 06 - 10 | M | Select the suited data received from Occupation API from Master. ( eg RHO016 refer OccupationApi ) |
| jobTitle | Alpha | 01 - 50 | O | Designation of customer's job profile |
| jobIndustry | Alpha | 01 - 50 | O | Job industry of customer |
| idTypeCode | Alphanumeric | 06 - 10 | M | The predefined code corresponding to the different document types for individual. eg RHD002 (for more info, please refer to DocumentTypeApi) |
| idNumber | Alphanumeric | 01 - 50 | M | Id numder of the Id proof provided for Kyc eg:JHGHG987KIUK |
| issueDate | Date | 10 - 19 | M | Issue date of the Id proof provided for Kyc in yyyy-mm-dd format. eg: 1999-09-12 |
| idExpiryDate | Date | 10 - 19 | M | Expiry date of the Id proof provided for Kyc in yyyy-mm-dd format. eg: 2026-09-12 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details of Individual Customer

```http
 POST /services HTTP/1.0
 HOST: XXX.XXX.XXX.XXX:Port
 Content-Type: application/json; charset=utf-8
 POST http://host/ewallet/api/v1/customer-registration

 {
"customerTypeCode": "100001",
"customerSubTypeCode": "100001",
"docReferenceNumber": "CUSG39VHE7",
"serviceTypeCode": "REGULAR",
"walletOwnerCode": "1000008438",
"firstName": "Rajesh",
"lastName": "Singh",
"dateOfBirth": "2006-08-22",
"occupationCode": "RHO016",
"jobTitle": "Job Title",
"jobIndustry": "Job Industry",
"gender": "female",
"nationality": "IND",
"mobileNumber": "9099998987",
"email": "pankaj.singh@esteltelecom.com",
"addressLine1": "new delhi new",
"countryCode": "TZA",
"state": "tanzania",
"city": "tanzania",
"pincode": "232222",
"idTypeCode": "RHD002",
"idNumber": "ID2121121212",
"issueDate": "2024-08-22",
"idExpiryDate": "2029-01-09"
 }
```

## Response Details of Individual Customer

```json
{
"transactionId": "9226196",
"requestTime": "Mon Feb 03 11:49:51 IST 2025",
"responseTime": "Mon Feb 03 11:49:51 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"customerRegistration": {
    "code": "1000002221",
    "customerTypeCode": "100001",
    "customerSubTypeCode": "100001",
    "walletOwnerCode": "1000008929",
    "customerId": "100000892912221I",
    "firstName": "ASEWE",
    "lastName": "singh",
    "fullName": "ASEWE singh",
    "nickName": "ASEWE",
    "tradeName": "ASEWE singh",
    "gender": "male",
    "nationality": "IND",
    "dateOfBirth": "1989-08-28",
    "mobileNumber": "9800000087",
    "addressLine1": "india",
    "city": "delhi",
    "state": "delhi",
    "pincode": "544444",
    "countryCode": "MWI",
    "idTypeCode": "RHD002",
    "idNumber": "ID31232444444",
    "screeningStatus": "IP",
    "customerStatus": "Active",
    "customerState": "System Approved",
    "customerStateCode": "AA",
    "nationalityName": "India",
    "countryName": "Malawi",
    "customerTypeName": "Individual",
    "creationDate": "2025-02-03T11:49:51.259+0530",
    "createdBy": "105732",
    "sendClientName": "ESTEL",
    "docReferenceNumber": "CUSP6RDAA6",
    "walletOwnerName": "ESTEL",
    "logoUrl": "/fileUpload/download/1000008929/logo 1DADANADA.jpg",
    "sendClientAddress": "Malawi, Malawi, Blantyre, Blantyre, Malawi",
    "sendClientMobileNo": "26533545636654",
    "idTypeName": "Passport ",
    "registrationApprovedBy": "ESTEL",
    "registrationNumber": "ID31232444444",
    "createdByCode": "1000008929",
    "createdByName": "ESTEL",
    "autoRegistered": false
    }
  }
```


## Related APIs

- [Document Upload](/docs/documents/document-upload)
- [Payout](/docs/payout/payout)
- [Master / reference APIs](/docs/master-apis)
- [Customer Inquiry (unlinked source page)](/docs/legacy/customer-inquiry)
