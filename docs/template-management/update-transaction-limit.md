---
title: "Update Transaction Limit"
sidebar_label: "Update Transaction Limit"
description: "RHUB Template Management — Update Transaction Limit API."
unlisted: true
---

# Update Transaction Limit

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
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/sendclienttransactionlimittemplate'}</code>
  </div>
</div>

The API to add transaction limit.

## Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| serviceCode | String | M |  |
| serviceCategoryCode | String | M |  |
| serviceProviderCode | String | M |  |
| serviceTypeCode | String | M | B2B:100000, B2C:100001, C2C:100002, C2B:100003, WPT:100004, FXB2B:100005 |
| pin | String | M | The pin provided by Rhub. |
| settlementCurrencyCode | String | M |  |
| calculationCycleCode | String | M |  |
| calculationTypeCode | String | M | Fixed:100001, Percentage:100002 |
| value | Number | M | The value at which transaction limit is to be set |
| status | String | M |  |
| state | String | M |  |
| walletOwnerCode | String | M | The sending partner code. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/api/v1/sendclienttransactionlimittemplate
{
calculationCycleCode: "100000"
calculationCycleTypeCode: "100000"
pin: "2C4F28E2B************93EC4940"
serviceCategoryCode: "100018"
serviceCode: "100013"
serviceProviderCode: "100158"
serviceTypeCode: "100005"
settlementCurrencyCode: "100069"
state: "Y"
status: "Y"
value: 1000000
walletOwnerCode: "1000009093"
}
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| walletOwnerCode | String | M | The sending partner code. |
| serviceCode | String | M |  |
| serviceCategoryCode | String | M |  |
| serviceProviderCode | String | M |  |
| settlementCurrencyCode | String | M |  |
| settlementCurrencyName | String | M |  |
| settlementCurrencyISOCode | String | M |  |
| calculationCycleCode | String | M |  |
| calculationCycleName | String | M |  |
| calculationTypeCode | String | M | Fixed:100001, Percentage:100002 |
| calculationTypeName | String | M | Fixed or Percentage |
| value | Number | M | The value at which transaction limit is set |
| status | String | M |  |
| state | String | M |  |
| createdBy | String | M |  |
| creationDate | String | M | Creation time of respected request. |
| serviceTypeCode | String | M | B2B:100000, B2C:100001, C2C:100002, C2B:100003, WPT:100004, FXB2B:100005 |
| serviceTypeName | String | M | Business to Business, Business to Customer, Customer to Customer, Customer to Business, Wallet Payout, Africa FX Change B2B |
| serviceTypeShortName | String | M | B2B, B2C, C2C, C2B, WPT, FXB2B |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"transactionId": "8782241",
"requestTime": "Tue Oct 29 18:10:07 IST 2024",
"responseTime": "Tue Oct 29 18:10:07 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"sendClientTransactionLimitTemplate": {
    "code": "100111",
    "walletOwnerCode": "1000009093",
    "serviceCode": "100013",
    "serviceCategoryCode": "100018",
    "serviceProviderCode": "100158",
    "settlementCurrencyCode": "100069",
    "settlementCurrencyName": "Indian Rupee",
    "settlementCurrencyISOCode": "INR",
    "calculationCycleCode": "100000",
    "calculationCycleName": "per_transaction",
    "calculationCycleTypeCode": "100000",
    "calculationCycleTypeName": "Amount",
    "value": 9000000.0,
    "status": "Y",
    "state": "Active",
    "createdBy": "105926",
    "creationDate": "2024-10-29T18:10:07.125+0530",
    "serviceTypeCode": "100005",
    "serviceTypeName": "Africa FX Change B2B",
    "serviceTypeShortName": "FXB2B"
}
}
```

## Related APIs

- [Template management overview](/docs/template-management)
- [Quotation](/docs/quotation/quotation)
