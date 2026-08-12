---
title: "Transaction List"
sidebar_label: "Transaction List"
description: "RHUB Template Management — Transaction List API."
---

# Transaction List

<span className="rhub-method rhub-method--get">GET</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `template.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/sendclienttransactionlimittemplate/walletowner/{senderCode}`

:::

This API is used to get the transaction limit set by client.

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
GET http://host/ewallet/api/v1/sendclienttransactionlimittemplate/walletowner/1000009093
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| id | String | M |  |
| code | String | M |  |
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
"transactionId": "8782236",
"requestTime": "Tue Oct 29 18:06:05 IST 2024",
"responseTime": "Tue Oct 29 18:06:06 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"sendClientTransactionLimitTemplateList": [
    {
        "id": 111,
        "code": "100110",
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
        "value": 1000.0,
        "status": "Y",
        "state": "Active",
        "createdBy": "105926",
        "creationDate": "2024-10-24T14:41:03.384+0530",
        "serviceTypeCode": "100000",
        "serviceTypeName": "Business to Business",
        "serviceTypeShortName": "B2B"
    }
]
}
```

## Related APIs

- [Template management overview](/docs/template-management)
- [Quotation](/docs/quotation/quotation)
