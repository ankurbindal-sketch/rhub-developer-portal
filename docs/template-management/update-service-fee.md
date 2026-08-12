---
title: "Update Service Fee"
sidebar_label: "Update Service Fee"
description: "RHUB Template Management — Update Service Fee API."
unlisted: true
---

# Update Service Fee

<span className="rhub-method rhub-method--post">POST</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `template.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/senderClientfeeTemplate'}</code>
  </div>
</div>

The API to add client service fees.

## Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| calculationTypeCode | String | M | Fixed:100001, Percentage:100002 |
| createdBy | String | O |  |
| fixedFeeValue | String | C | If calculation type is fixed, then give the value otherwise give 0 |
| maxValue | Number | M | Set the maximum value of allowed transaction. (Transaction range from min to max) |
| minValue | Number | M | Set the minimum value of allowed transaction. (Transaction range from min to max) |
| payOutCurrencyCode | String | M |  |
| percentFeeValue | String | C | If calculation type is percentage, then give the value otherwise give 0 |
| pin | String | M | The pin provided by Rhub. |
| serviceCategoryCode | String | M |  |
| serviceCode | String | M |  |
| serviceProviderCode | String | M |  |
| serviceTypeCode | String | M | B2B:100000, B2C:100001, C2C:100002, C2B:100003, WPT:100004, FXB2B:100005 |
| settlementCurrencyfeeTemp | String | M |  |
| state | String | M |  |
| status | String | M |  |
| vat | String | M |  |
| walletOwnerCode | String | M | The sending partner code. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/senderClientfeeTemplate
{
calculationTypeCode: "100001"
createdBy: ""
fixedFeeValue: "2"
maxValue: 12222222
minValue: 1
payOutCurrencyCode: "100061"
percentFeeValue: "0"
pin: "2C4****E2BCAA*****2F0313496788940"
serviceCategoryCode: "100018"
serviceCode: "100056"
serviceProviderCode: "100158"
serviceTypeCode: "100005"
settlementCurrencyfeeTemp: "100069"
state: "IN"
status: "Y"
vat: "1"
walletOwnerCode: "1000009093"
}
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| serviceCode | String | M |  |
| serviceCategoryCode | String | M |  |
| serviceProviderCode | String | M |  |
| calculationTypeCode | String | M | Fixed:100001, Percentage:100002 |
| calculationTypeName | String | M | Fixed or Percentage |
| minValue | Number | M | Set the minimum value of allowed transaction. (Transaction range from min to max) |
| maxValue | Number | M | Set the maximum value of allowed transaction. (Transaction range from min to max) |
| fixedFeeValue | Number | C | If calculation type is fixed, then gives the value otherwise gives 0 |
| percentFeeValue | Number | C | If calculation type is percentage, then give the value otherwise give 0 |
| status | String | M |  |
| state | String | M |  |
| createdBy | String | M |  |
| creationDate | String | M | Creation time of respected request. |
| sendCurrencyCode | String | M |  |
| sendCurrencyName | String | M |  |
| sendCurrencyExactName | String | M |  |
| walletOwnerCode | String | M | The sending partner code. |
| settlementCurrencyfeeTemp | String | M |  |
| settlementCurrencyName | String | M |  |
| settlementCurrencyExactName | String | M |  |
| payOutCurrencyCode | String | M |  |
| receiveCurrencyName | String | M |  |
| receiveCurrencyExactName | String | M |  |
| serviceTypeCode | String | M | B2B:100000, B2C:100001, C2C:100002, C2B:100003, WPT:100004, FXB2B:100005 |
| serviceTypeName | String | M | Business to Business, Business to Customer, Customer to Customer, Customer to Business, Wallet Payout, Africa FX Change B2B |
| serviceTypeShortName | String | M | B2B, B2C, C2C, C2B, WPT, FXB2B |
| vat | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"transactionId": "8781993",
"requestTime": "Tue Oct 29 16:31:03 IST 2024",
"responseTime": "Tue Oct 29 16:31:03 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"senderClientFeeTemplateBean": {
    "code": "100317",
    "serviceCode": "100056",
    "serviceCategoryCode": "100018",
    "serviceProviderCode": "100158",
    "calculationTypeCode": "100001",
    "minValue": 1.0,
    "maxValue": 1.2222222E7,
    "fixedFeeValue": 2.0,
    "percentFeeValue": 0.0,
    "status": "Y",
    "state": "IN",
    "createdBy": "105926",
    "creationDate": "2024-10-29T16:31:03.354+0530",
    "sendCurrencyCode": "100069",
    "sendCurrencyName": "INR",
    "sendCurrencyExactName": "Indian Rupee",
    "walletOwnerCode": "1000009093",
    "settlementCurrencyfeeTemp": "100069",
    "settlementCurrencyName": "INR",
    "settlementCurrencyExactName": "Indian Rupee",
    "payOutCurrencyCode": "100061",
    "receiveCurrencyName": "GBP",
    "receiveCurrencyExactName": "British Pound",
    "serviceTypeCode": "100005",
    "serviceTypeName": "Africa FX Change B2B",
    "serviceTypeShortName": "FXB2B",
    "vat": "1"
}
}
```

## Related APIs

- [Template management overview](/docs/template-management)
- [Quotation](/docs/quotation/quotation)
