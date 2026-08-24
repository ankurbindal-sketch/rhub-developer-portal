---
title: "Balance Enquiry"
sidebar_label: "Balance Enquiry"
description: "RHUB Balance Enquiry API — retrieve the current wallet or account balance."
---

# Balance Enquiry

<span className="rhub-method rhub-method--get">GET</span>

Retrieve the current balance. Balance is the final API in the [documented integration sequence](/docs/getting-started/integration-flow); call it when you need the current balance rather than after every transaction.

## Contract

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/wallet/walletOwner/{walletOwnerCode}'}</code>
  </div>
</div>

The Balance API is used to fetch the current balance in the ledger of the partner. The balance can be fetched for the entire ledger of a specific currency.

## Request Parameter

| Parameters | Input Type  | Length  | Requirement | Description                               |
|------------|:------------:|:------------:|:------------:|-------------------------------------------|
| walletOwnerCode | Numeric | 10 | M | The 10 digit code of Wallet owner. eg: 1000009090 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http:host/ewallet/api/v1/wallet/walletOwner/1000008444
```

## Response Parameter

| Parameters        | Data Type | Requirement | Description                                                                   |
|-------------------|:-------------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | Unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| walletOwnerCode | String | M | The 10 digit wallet owner code of client. |
| walletOwnerName | String | M | The wallet owner name. |
| walletOwnerMsisdn | String | M | The contact number of wallet owner. |
| currencyCode | String | M | The stored code of the currency. |
| currencyName | String | M | The name of the currency. |
| currencySymbol | String | M | The symbol of the currency. |
| walletTypeCode | String | M | Type of wallet's code. |
| walletTypeName | String | M | Type of wallet. |
| minValue | String | M | Minimum value |
| maxValue | String | M | Maximum value |
| value | String | M | Balance of currency |
| minTransValue | String | M | Max tansaction limit value. |
| maxTransValue | String | M | Min tansaction limit value. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"transactionId": "8474053",
"requestTime": "Wed Dec 10 16:31:05 IST 2025",
"responseTime": "Wed Dec 10 16:31:07 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"walletList": [
  {
      "id": 68620,
      "code": "1000068800",
      "walletOwnerCode": "1000008398",
      "walletOwnerName": "John",
      "walletOwnerMsisdn": "+265768568432",
      "currencyCode": "100004",
      "currencyName": "EUR",
      "currencySymbol": "€",
      "walletTypeCode": "100009",
      "walletTypeName": "Comission Wallet",
      "minValue": 0.0,
      "maxValue": 0.0,
      "value": 0.0,
      "minTransValue": 0.0,
      "maxTransValue": 0.0,
      "allocatedValue": 0.0,
      "alertValue": 0.0,
      "notifyMisdns": 0,
      "balance": 0.0,
      "status": "Active",
      "state": "Approved",
      "walletOwnerCategoryCode": "100000",
      "validityDays": 0,
      "operatorName": "Example Trading Ltd",
      "creditLimitValue": 0.0,
      "hideCurrency": false,
      "thresholdAmount": 0.0
  },
  {
      "id": 68623,
      "code": "1000068803",
      "walletOwnerCode": "1000008398",
      "walletOwnerName": "John",
      "walletOwnerMsisdn": "+265768568432",
      "currencyCode": "100004",
      "currencyName": "EUR",
      "currencySymbol": "€",
      "walletTypeCode": "100008",
      "walletTypeName": "Main Wallet",
      "minValue": 0.0,
      "maxValue": 2000000.0,
      "value": 122141.27,
      "minTransValue": 100.0,
      "maxTransValue": 100000.0,
      "allocatedValue": 0.0,
      "alertValue": 10000.0,
      "notifyMisdns": 0,
      "balance": 0.0,
      "status": "Active",
      "state": "Approved",
      "walletOwnerCategoryCode": "100000",
      "validityDays": 0,
      "operatorName": "Example Trading Ltd",
      "creditLimitValue": 0.0,
      "hideCurrency": false,
      "thresholdAmount": 0.0
  },
  {
      "id": 68619,
      "code": "1000068799",
      "walletOwnerCode": "1000008398",
      "walletOwnerName": "John",
      "walletOwnerMsisdn": "+265768568432",
      "currencyCode": "100003",
      "currencyName": "USD-USA",
      "currencySymbol": "$",
      "walletTypeCode": "100009",
      "walletTypeName": "Comission Wallet",
      "minValue": 0.0,
      "maxValue": 0.0,
      "value": 0.0,
      "minTransValue": 0.0,
      "maxTransValue": 0.0,
      "allocatedValue": 0.0,
      "alertValue": 0.0,
      "notifyMisdns": 0,
      "balance": 0.0,
      "status": "Active",
      "state": "Approved",
      "walletOwnerCategoryCode": "100000",
      "validityDays": 0,
      "operatorName": "Example Trading Ltd",
      "creditLimitValue": 0.0,
      "hideCurrency": false,
      "thresholdAmount": 0.0
  },
  {
      "id": 68622,
      "code": "1000068802",
      "walletOwnerCode": "1000008398",
      "walletOwnerName": "John",
      "walletOwnerMsisdn": "+265768568432",
      "currencyCode": "100003",
      "currencyName": "USD-USA",
      "currencySymbol": "$",
      "walletTypeCode": "100008",
      "walletTypeName": "Main Wallet",
      "minValue": 0.0,
      "maxValue": 2000000.0,
      "value": 1149998.8,
      "minTransValue": 100.0,
      "maxTransValue": 100000.0,
      "allocatedValue": 0.0,
      "alertValue": 10000.0,
      "notifyMisdns": 0,
      "balance": 0.0,
      "status": "Active",
      "state": "Approved",
      "walletOwnerCategoryCode": "100000",
      "validityDays": 0,
      "overDraftExpiryDate": "2023-11-20T00:00:00.000+0530",
      "operatorName": "Example Trading Ltd",
      "creditLimitValue": 0.0,
      "hideCurrency": false,
      "thresholdAmount": 0.0
  },
  {
      "id": 68621,
      "code": "1000068801",
      "walletOwnerCode": "1000008398",
      "walletOwnerName": "John",
      "walletOwnerMsisdn": "+265768568432",
      "currencyCode": "100131",
      "currencyName": "ZAR",
      "currencySymbol": "R",
      "walletTypeCode": "100009",
      "walletTypeName": "Comission Wallet",
      "minValue": 0.0,
      "maxValue": 0.0,
      "value": 0.0,
      "minTransValue": 0.0,
      "maxTransValue": 0.0,
      "allocatedValue": 0.0,
      "alertValue": 0.0,
      "notifyMisdns": 0,
      "balance": 0.0,
      "status": "Active",
      "state": "Approved",
      "walletOwnerCategoryCode": "100000",
      "validityDays": 0,
      "operatorName": "Example Trading Ltd",
      "creditLimitValue": 0.0,
      "hideCurrency": false,
      "thresholdAmount": 0.0
  },
  {
      "id": 68624,
      "code": "1000068804",
      "walletOwnerCode": "1000008398",
      "walletOwnerName": "John",
      "walletOwnerMsisdn": "+265768568432",
      "currencyCode": "100131",
      "currencyName": "ZAR",
      "currencySymbol": "R",
      "walletTypeCode": "100008",
      "walletTypeName": "Main Wallet",
      "minValue": 0.0,
      "maxValue": 2000000.0,
      "value": 988934.08,
      "minTransValue": 100.0,
      "maxTransValue": 100000.0,
      "allocatedValue": 0.0,
      "alertValue": 10000.0,
      "notifyMisdns": 0,
      "balance": 0.0,
      "status": "Active",
      "state": "Approved",
      "walletOwnerCategoryCode": "100000",
      "validityDays": 0,
      "operatorName": "Example Trading Ltd",
      "creditLimitValue": 0.0,
      "hideCurrency": false,
      "thresholdAmount": 0.0
  }
  ]
}
```

## Related APIs

- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
- [Integration flow](/docs/getting-started/integration-flow)
