---
title: "Owner Details API"
sidebar_label: "Owner Details API"
description: "RHUB Owner Details API (source page not linked in the live documentation sidebar)."
---

# Owner Details API

<span className="rhub-method rhub-method--post">POST</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `ownerDetails.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `http://host/api/v1/owner-details`

:::

The Owner Details API is used to create / update the owner in the system.

## Request Parameter

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

## Request Details

```http
   POST /services HTTP/1.0
   HOST: XXX.XXX.XXX.XXX:Port
   Content-Type: application/json; charset=utf-8
   POST http://host/api/v1/customer-registration
   {
"customerTypeCode": "100001",

"walletOwnerCode": "1000000291",
"firstName": "Adarsh",
"middleName": "Kumar",
"lastName": "Srivastava",
"tradeName": "",
"legalStatusCode": "100001",
"natureOfBusinessCode": "100001",
"businessRelationshipCode": "100001",
"gender": "Male",
"nationality": "India",
"dateOfBirth": "31-12-1989",
"email": "abc.xyz2009@gmail.com",
"mobileNo": "9999999999",
"occupationCode": "100001",
"jobTitle": "Manager",
"jobIndustry": "IT",
"employerName": "Estel Telecom",
"addressLine1": "Paryavaran Complex",
"addressLine2": "Saket",
"city": "New Delhi",
"state": "Delhi",
"pincode": "110030",
"country": "IND",
"residenceStatusCode": "100001",
"idTypeCode": "100001",
"idNumber": "ABS124483",
"idIssuedBy": "Aadhaar India",
"idCountry": "India",
"issueDate": "10-10-2009",
"idExpiry": "10-10-2079",
"transactionVolumeCode": "100001",
"thirdPartyDetermination": true,
"isSenderPep": true,
"declaration": true,
"ownerDetails": [
	{
		"firstName": "Test",
		"middleName": "yes",
		"lastName": "test",
		"companyName": "Estel Telecom",
		"gender": "Male",
		"nationality": "India",
		"dateOfBirth": "31-01-1998",
		"email": "test@gmail.com",
		"mobileNo": "456784567",
		"addressLine1": "test 1",
		"addressLine2": "test 2",
		"city": "New Delhi",
		"state": "Delhi",
		"pincode": "110030",
		"country": "IND",
		"residenceStatusCode": "100001",
		"ownerPercentage": "10",
		"transactionVolumeCode": "100001"
	}
]
   }
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
