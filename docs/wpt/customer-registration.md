---
title: "WPT — Customer Registration"
sidebar_label: "Customer Registration"
description: "RHUB WPT Customer Registration API."
---

# WPT — Customer Registration

<span className="rhub-method rhub-method--post">POST</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `WPT.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `http://host/ewallet/api/v1/customer-registration`

:::

The Customer-Registration API is used to register or create the customer in the system.

## Request Parameter of Business Customer

| Parameters     | Data Type| Requirement | Description |
|----------|:-----:|:-----:|--------|
| customerTypeCode | String | M | Individual : 100001, Business : 100002 |
| customerSubTypeCode | String | M | 100001 |
| docReferenceNumber | String | M | 10 digit unique doc reference number, used while uploading document. |
| walletOwnerCode | String | M | Send Client Code |
| tradeName | String | M | Company trade name. |
| natureOfBusinessCode | String | M |  |
| mobileNumber | String | M |  |
| addressline1 | String | M |  |
| countryCode | String | M |  |
| state | String | M |  |
| city | String | M |  |
| pincode | String | M |  |
| idNumber | String | M |  |
| idCountry | String | M |  |
| issueDate | String | M | yyyy-mm-dd |
| idExpiryDate | String | M | yyyy-mm-dd |
| preFundCurrencyList | String | O | Array of approved currency list. eg: ["USD-USA","EUR","GPB"] |
| **ownerDetailList** |  |  |  |
| customerTypeCode | String | M | for Individual owner : 100001 |
| firstName | String | M | for Individual owner |
| lastName | String | M | As aforesaid |
| dateOfBirth | String | M | As aforesaid |
| gender | String | M | As aforesaid |
| addressline1 | String | M | As aforesaid |
| countryCode | String | M | As aforesaid |
| state | String | M | As aforesaid |
| city | String | M | As aforesaid |
| pincode | String | M | As aforesaid |
| idTypeCode | String | M | The predefined code corresponding to the different document types for business. (for more info, please refer to [Customer Document Type Api](/docs/master-apis)) |
| idNumber | String | M | As aforesaid |
| idCountry | String | M | As aforesaid |
| customerTypeCode | String | M | for Business owner : 100002 |
| companyName | String | M | for Business owner |
| addressline1 | String | M | As aforesaid |
| countryCode | String | M | As aforesaid |
| state | String | M | As aforesaid |
| city | String | M | As aforesaid |

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
  "docReferenceNumber": "CUSYONEIUK",
  "walletOwnerCode": "1000008398",.
  "tradeName": "Estel technology",
  "natureOfBusinessCode": "100019",
  "mobileNumber": "9099998987",
  "addressLine1": "malawi",
  "countryCode": "MWI",
  "state": "malawi",
  "city": "malawi",
  "pincode": "676567",
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
    "idTypeCode": "100001",
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
    "natureOfBusinessCode": "100019",
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
            "idTypeCode": "100001",
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
            "pincode": "",
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

## Related APIs

- [WPT overview](/docs/wpt)
- [WPT Payout (published)](/docs/payout/wpt-payout)
- [WPT Wallet List (master)](/docs/master-apis/wpt-wallet-list)
