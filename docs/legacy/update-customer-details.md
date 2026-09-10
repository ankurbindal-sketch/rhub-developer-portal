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

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'/api/v1/customer-registration'}</code>
  </div>
  <div className="rhub-endpoint__envs">
    <span className="rhub-endpoint__env"><span className="rhub-endpoint__envname">Sandbox</span><code>https://sandbox-client.remittanceshub.com:8130/api/v1/customer-registration</code></span>
    <span className="rhub-endpoint__env"><span className="rhub-endpoint__envname">Production</span><code>https://prod-api.remittanceshub.com:9091/api/v1/customer-registration</code></span>
  </div>
</div>

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
   HOST: sandbox-client.remittanceshub.com:8130
   Content-Type: application/json; charset=utf-8
   POST https://sandbox-client.remittanceshub.com:8130/api/v1/customer-registration
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
