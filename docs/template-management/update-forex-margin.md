---
title: "Update Forex Margin"
sidebar_label: "Update Forex Margin"
description: "RHUB Template Management — Update Forex Margin API."
---

# Update Forex Margin

<span className="rhub-method rhub-method--post">POST</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `template.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `http://host/ewallet/api/v1/sendClientMarginTemplate`

:::

The API to add forex margin.

## Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| calculationTypeCode | String | M | Fixed:100001, Percentage:100002 |
| createdBy | String | O |  |
| fixedFeeValue | String | M | If calculation type is fixed, then give the value otherwise give 0 |
| payInCurrencyCode | String | M |  |
| payOutCurrencyCode | String | M |  |
| percentFeeValue | String | C | If calculation type is percentage, then give the value otherwise give 0 |
| pin | String | M | The pin provided by Rhub. |
| serviceCategoryCode | String | M |  |
| serviceCode | String | M |  |
| serviceProviderCode | String | M |  |
| serviceTypeCode | String | M | B2B:100000, B2C:100001, C2C:100002, C2B:100003, WPT:100004, FXB2B:100005 |
| state | String | M |  |
| status | String | M |  |
| walletOwnerCode | String | M | The sending partner code. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/sendClientMarginTemplate
{
calculationTypeCode: "100002"
createdBy: ""
fixedFeeValue: "0"
payInCurrencyCode: "100069"
payOutCurrencyCode: "100061"
percentFeeValue: 2
pin: "2C4F28E2BCAA9**********C4940"
serviceCategoryCode: "100018"
serviceCode: "100056"
serviceProviderCode: "100158"
serviceTypeCode: "100000"
state: "IN"
status: "Y"
walletOwnerCode: "1000009093"
}
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| code | String | M |  |
| serviceCode | String | M |  |
| serviceCategoryCode | String | M |  |
| serviceProviderCode | String | M |  |
| calculationTypeCode | String | M | Fixed:100001, Percentage:100002 |
| calculationTypeName | String | M | Fixed or Percentage |
| fixedFeeValue | Number | C | If calculation type is fixed, then gives the value otherwise gives 0 |
| percentFeeValue | Number | C | If calculation type is percentage, then give the value otherwise give 0 |
| status | String | M |  |
| state | String | M |  |
| createdBy | String | M |  |
| creationDate | String | M | Creation time of respected request. |
| sendCurrencyName | String | M |  |
| walletOwnerCode | String | M | The sending partner code. |
| payInCurrencyCode | String | M |  |
| payInCurrencyISOCode | String | M |  |
| payInCurrencyName | String | M |  |
| payOutCurrencyCode | String | M |  |
| payOutCurrencyName | String | M |  |
| payOutCurrencyISOCode | String | M |  |
| serviceTypeCode | String | M | B2B:100000, B2C:100001, C2C:100002, C2B:100003, WPT:100004, FXB2B:100005 |
| serviceTypeName | String | M | Business to Business, Business to Customer, Customer to Customer, Customer to Business, Wallet Payout, Africa FX Change B2B |
| serviceTypeShortName | String | M | B2B, B2C, C2C, C2B, WPT, FXB2B |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"transactionId": "8782253",
"requestTime": "Tue Oct 29 18:25:19 IST 2024",
"responseTime": "Tue Oct 29 18:25:19 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"sendClientMarginTemplateBean": {
    "code": "100154",
    "serviceCode": "100056",
    "serviceCategoryCode": "100018",
    "serviceProviderCode": "100158",
    "calculationTypeCode": "100002",
    "calculationTypeName": "Percentage",
    "fixedFeeValue": 0.0,
    "percentFeeValue": 2.0,
    "status": "Y",
    "state": "A",
    "createdBy": "105926",
    "creationDate": "2024-10-29T18:25:19.900+0530",
    "sendCurrencyName": "GBP",
    "walletOwnerCode": "1000009093",
    "payInCurrencyCode": "100069",
    "payOutCurrencyCode": "100061",
    "payInCurrencyISOCode": "INR",
    "payInCurrencyName": "Indian Rupee",
    "payOutCurrencyISOCode": "GBP",
    "serviceTypeCode": "100000",
    "serviceTypeName": "Business to Business",
    "serviceTypeShortName": "B2B",
    "payOutCurrencyName": "British Pound"
}
}
```

## Related APIs

- [Template management overview](/docs/template-management)
- [Quotation](/docs/quotation/quotation)
