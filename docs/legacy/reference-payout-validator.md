---
title: "Reference API (Payout Validator)"
sidebar_label: "Reference API (Payout Validator)"
description: "RHUB Reference API (Payout Validator) (source page not linked in the live documentation sidebar)."
---

# Reference API (Payout Validator)

<span className="rhub-method rhub-method--get">GET</span>

*Source of truth: `payoutValidator.md` — from the RHUB documentation export of 2026-08-12 (`https://docs.remittanceshub.com/`).*

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `payoutValidator.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`GET`  `http://host/api/v1/payoutValidator/{partnerCode}/{serviceTypeCode}/{currency}/{userTypeCode}/{modeOfPayment}`

:::

The Reference API is used to fetch the validator for the receiver.

## Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| partnerCode | String | M | Respective Client Code. eg: 1000001000 |
| serviceTypeCode | String | M | The following are the service types: • B2B • C2C • B2C • C2B • WPT |
| currency | String | M | ISO3 Code e.g. INR |
| userTypeCode | String | M | Sender Code: 100000, Beneficiary code: 100001 |
| modeOfPayment | String | O | This is the requested would be: Bank CASH Wallet |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/payoutValidator/1000008855/B2B/INR/100001
```

## Response Parameter

| Parameters                     | Data Type  | Requirement | Description                                                                   |
|--------------------------------|:-----------:|:------------:|-------------------------------------------------------------------------------|
| transactionId | String | M |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime |  |  | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | The code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Payout Validator Response List** |  |  |  |
| id | String | M |  |
| partnerCode | String | M |  |
| serviceTypeCode | String | M |  |
| fieldName | String | M | Name of the business |
| currency | String | M | Payout currency |
| fieldLabel | String | M | Name of the business |
| minLength | String | M | Minimum length |
| maxLength | String | M | Maxium length |
| isMandatory | String | M | Requirement status |
| userTypeCode | String | M |  |
*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"transactionId": "8155703",
"requestTime": "Fri Feb 09 10:50:08 IST 2024",
"responseTime": "Fri Feb 09 10:50:08 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"payoutValidatorResponseList": [

{
"id": 1636,
"partnerCode": "1000008855",
"serviceTypeCode": "B2B",
"fieldName": "BusinessName",
"currency": "INR",
"fieldLabel": "Business Name",
"minLength": 1,
"maxLength": 50,
"isMandatory": true,
"userTypeCode": "100001"

},

{
"id": 1637,
"partnerCode": "1000008855",
"serviceTypeCode": "B2B",
"fieldName": "Industry",
"currency": "INR",
"fieldLabel": "Industry",
"minLength": 1,
"maxLength": 50,
"isMandatory": true,
"userTypeCode": "100001"

},

}
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
