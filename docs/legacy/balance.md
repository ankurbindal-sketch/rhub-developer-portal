---
title: "Balance API"
sidebar_label: "Balance API"
description: "RHUB Balance API (source page not linked in the live documentation sidebar)."
unlisted: true
---

# Balance API

<span className="rhub-method rhub-method--get">GET</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `balance.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/api/v1/balance/{parameter}'}</code>
  </div>
</div>

The Balance API is used to fetch the current balance in the ledger of the partner. The balance can be fetched for the entire ledger of a specific currency.

## Request Parameter of all Currency

| Parameters | Data Type  | Requirement | Description                               |
|------------|:------------:|:------------:|-------------------------------------------|
| all | String | O | To fetch the balance of all the currency. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details of all Currency

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http://host/api/v1/balance/all
```

## Response Parameter of all Currency

| Parameters        | Data Type | Requirement | Description                                                                   |
|-------------------|:-------------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | Unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| currency | String | M | The ISO currency code of the currency. |
| currentBalance | String | M | The current balance of the specific currency. |
| status | String | M | The status of the currency. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details of all Currency

```json
{

"requestTime": "Wed May 17 12:45:00 IST 2023",

"responseTime": "Wed May 17 12:45:25 IST 2023",

"resultCode": "0",

"resultDescription": "Transaction Successful",

"balanceDetails": {

{

"currency": "USD",

"currentBalance": "1000.000000",

"status": "available"

},

{

"currency": "NGN",

"currentBalance": "3000000.000000",

"status": "available"

},

}

}
```

## Request Parameter for a Single Currency

| Parameters   | Data Type | Requirement | Description                            |
|--------------|:-----------:|:------------:|-------------------------------------|
| currencyCode | String | O | The ISO currency code of the currency. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details for a Single Currency

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/api/v1/balance/USD
```

## Response Parameter for a Single Currency

| Parameters        | Data Type | Requirement | Description                                                                   |
|-------------------|:-------------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | The unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| currency | String | M | The ISO currency code of the currency. |
| currentBalance | String | M | The current balance of the specific currency. |
| status | String | M | The status of the currency. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details for a Single Currency

```json
{

"requestTime": "Wed May 17 12:45:00 IST 2023",

"responseTime": "Wed May 17 12:45:25 IST 2023",

"resultCode": "0",

"resultDescription": "Transaction Successful",

"balanceDetails": {

"currency": "USD",

"currentBalance": "1000.000000",

"status": "available"

}

}
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
