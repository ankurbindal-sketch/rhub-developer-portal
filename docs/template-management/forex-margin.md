---
title: "Forex Margin"
sidebar_label: "Forex Margin"
description: "RHUB Template Management — Forex Margin API."
unlisted: true
---

# Forex Margin

<span className="rhub-method rhub-method--get">GET</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `template.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/sendClientMarginTemplate/getWalletOwner/{senderCode}'}</code>
  </div>
</div>

This API is used to get the forex margin set by client.

## Request Parameter

| Parameters     | Data Type | Requirement | Description |
|----------|:-----:|:-----------:|--------|
| senderCode | String | M | The sending partner Code |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/sendClientMarginTemplate/getWalletOwner/1000009093
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| id | String | M |  |
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
"transactionId": "8782269",
"requestTime": "Tue Oct 29 18:31:25 IST 2024",
"responseTime": "Tue Oct 29 18:31:25 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"sendClientMarginTemplateBeanList": [
    {
        "id": 140,
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
]
}
```

## Related APIs

- [Template management overview](/docs/template-management)
- [Quotation](/docs/quotation/quotation)
