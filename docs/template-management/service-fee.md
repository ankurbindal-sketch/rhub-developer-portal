---
title: "Service Fee"
sidebar_label: "Service Fee"
description: "RHUB Template Management — Service Fee API."
---

# Service Fee

<span className="rhub-method rhub-method--get">GET</span>

*Source of truth: `template.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `template.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/senderClientfeeTemplate/getWalletOwner/{senderCode}`

:::

The Service Fee API is used to set the service fee by client.

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
GET http://host/ewallet/api/v1/senderClientfeeTemplate/getWalletOwner/1000009093
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
"transactionId": "8782230",
"requestTime": "Tue Oct 29 18:02:41 IST 2024",
"responseTime": "Tue Oct 29 18:02:41 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"senderClientFeeTemplateBeanList": [
    {
        "id": 215,
        "code": "100317",
        "serviceCode": "100056",
        "serviceCategoryCode": "100018",
        "serviceProviderCode": "100158",
        "calculationTypeCode": "100001",
        "calculationTypeName": "Fixed",
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
]
}
```


## Related APIs

- [Template management overview](/docs/template-management)
- [Quotation](/docs/quotation/quotation)
