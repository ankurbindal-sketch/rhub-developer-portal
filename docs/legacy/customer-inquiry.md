---
title: "Customer-Inquiry API"
sidebar_label: "Customer-Inquiry API"
description: "RHUB Customer-Inquiry API (source page not linked in the live documentation sidebar)."
---

# Customer-Inquiry API

<span className="rhub-method rhub-method--get">GET</span>

*Source of truth: `customerInquiry.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `customerInquiry.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/customer-registration/{parameter}?{sortBy}&{sort}&{offset}&{limit}`

:::

The Customer-Inquiry API is used to fetch the details of the customer.

## Request Parameter of all the Customers of the Send Client

| Parameters     | Data Type  | Requirement | Description |
|----------|:-----------:|:-----:|--------|
| all | String | O | To fetch the details of all the customers of the send client. |
| sortBy | String | M | To sort the data based on the creation date of the customer. |
| sort | String | M |  |
| offset | String | M | From where to fetch the data. |
| limit | String | M | The count of the record to be displayed in a single page. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details of all the Customers of the Send Client

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/customer-registration/all?sortBy=creationDate&sort=desc&offset=0&limit=5
```

## Request of the Specific Customer of the Send Client
The details of the specific customer of the send client can be fetched based on the following parameters.
* code
* walletOwnerCode
* customerTypeCode :by default
* customerSubTypeCode
* customerId
* fullName
* mobileNumber
* dateOfBirth
* email
* tradeName

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
