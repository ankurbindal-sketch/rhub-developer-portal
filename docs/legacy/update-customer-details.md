---
title: "Update Customer-Details API"
sidebar_label: "Update Customer-Details API"
description: "RHUB Update Customer-Details API (source page not linked in the live documentation sidebar)."
unlisted: true
---

# Update Customer-Details API

<span className="rhub-method rhub-method--post">POST</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `updateCustomerDetails.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `http://host/api/v1/customer-registration`

:::

The Update Customer-API is used to update the details of the customer in the system.

## Request Parameter

| Parameters     | Data Type |  Requirement | Description |
|----------|:-----:|:----------:|--------|
| customerCode/ID | String | M |  |
| gender | String | O |  |
| nationality | String | O |  |
| dateOfBirth | String | O |  |
| mobileNo | String | O |  |
| email | String | O |  |
| addressLine1 | String | O |  |
| addressLine2 | String | O |  |
| city | String | O |  |
| state | String | O |  |
| pincode | String | O |  |
| country | String | O |  |
| idTypeCode | String | O |  |
| idNumber | String | O |  |
| idIssuedBy | String | O |  |
| idCountry | String | O |  |
| issueDate | String | O |  |
| idExpiry | String | O |  |
| jobTitle | String | O |  |
| jobIndustry | String | O |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
   POST /services HTTP/1.0
   HOST: XXX.XXX.XXX.XXX:Port
   Content-Type: application/json; charset=utf-8
   POST http://host/api/v1/customer-registration
   {
   "gender": "Male",
"nationality": "India",
"dateOfBirth": "31-12-1989",
"email": "abc.xyz2009@gmail.com",
"mobileNo": "9999999999",
"occupationCode": "100001",
"jobTitle": "Manager",
"addressLine1": "Paryavaran Complex",
"addressLine2": "Saket",
"city": "New Delhi",
"state": "Delhi",
"pincode": "110030",
   }
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
