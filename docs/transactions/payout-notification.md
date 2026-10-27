---
title: "Payout Notification"
sidebar_label: "Payout Notification"
description: "RHUB payout statement for a wallet and date range."
---

# Payout Notification

<span className="rhub-method rhub-method--get">GET</span>

Retrieve a collection of payout-related transaction records matching the supported statement filters and date range. This is a query endpoint: it returns records on request and sends no notification or callback.

:::note[Statement or enquiry?]

Use this endpoint for a set of records across a wallet and date range. For the details and state of one transaction you already have an id for, use [Transaction Enquiry](/docs/transactions/transaction-enquiry).

:::

## Payout Statement

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/miniStatement/partnerStatement'}</code>
  </div>
  <div className="rhub-endpoint__envs">
    <span className="rhub-endpoint__env"><span className="rhub-endpoint__envname">Sandbox</span><code>https://sandbox-client.remittanceshub.com:8130/ewallet/api/v1/miniStatement/partnerStatement</code></span>
    <span className="rhub-endpoint__env"><span className="rhub-endpoint__envname">Production</span><code>https://prod-api.remittanceshub.com:9091/ewallet/api/v1/miniStatement/partnerStatement</code></span>
  </div>
</div>

Returns partner wallet transaction records for the requested date range, wallet and filters, in JSON.

:::info[Authentication]

This API uses the same access token as the rest of the platform. Obtain it from
the [Authentication API](/docs/authentication/authentication) and send it on every call:

```http
Authorization: Bearer <access_token>
```

:::

### Query Parameters

| Parameter | Example | Description |
|---|---|---|
| `sortBy` | creationDate | Field used to sort the transaction records. |
| `limit` | 500 | Maximum number of records requested. |
| `sort` | desc | Sort direction. |
| `fromDate` | 2026-08-01 | Start date for the transaction search. |
| `toDate` | 2026-09-01 | End date for the transaction search. |
| `walletCode` | 1000000010 | Wallet code used for the statement query. |
| `selectedCategory` | 100008 | Transaction category. |
| `transactionId` | 200001 | Transaction ID filter. |
| `sendClientCustomerCode` | 100000000000005B | Customer identifier used to filter transactions. |
| `transactionType` | all | Transaction type. |
| `transactionSubType` | *(empty)* | Transaction subtype. |

A complete request appends the query string to the endpoint path:

```http
GET /ewallet/api/v1/miniStatement/partnerStatement?sortBy=creationDate&limit=500&sort=desc&fromDate=2026-08-01&toDate=2026-09-01&walletCode=1000000010&selectedCategory=100008&transactionId=200001&sendClientCustomerCode=100000000000005B&transactionType=all&transactionSubType=
```

### Transaction type filters

RHUB supplies these transaction type values:

| Label | Value |
|---|---|
| Payout | `101442` |
| Incoming | `100001` |
| Incoming VA | `100002` |
| All | `all` |

and these filter combinations, reproduced as given:

| Filter | Query |
|---|---|
| Incoming | `transactionType=100002&transactionSubType=100001` |
| Incoming VA | `transactionType=100002&transactionSubType=100002` |
| All transactions | `transactionType=all&transactionSubType=` |
| Payout | `transactionType=101442` |

:::note[Result limit]

The statement query limit is `500`. The response reports how many records matched in `pageable.totalRecords`. Records beyond the 500-record limit are available through the dashboard/portal. RHUB has not documented an offset, cursor or page parameter for this endpoint, so none is listed here.

:::

### Response

Example values are synthetic. The structure, field names, nesting and value types are as returned.

```json
{
  "transactionId": "null",
  "requestTime": "Fri Oct 23 16:46:15 IST 2026",
  "responseTime": "Fri Oct 23 16:46:15 IST 2026",
  "resultCode": "0",
  "resultDescription": "Transaction successful",
  "pageable": {
    "limit": 500,
    "totalRecords": 1,
    "sort": "desc",
    "sortBy": "creationDate"
  },
  "miniStatement": {
    "walletTransactionList": [
      {
        "id": 100001,
        "code": "1000100001",
        "transactionId": "200001",
        "fromWalletOwnerCode": "1000000001",
        "toWalletOwnerCode": "1000000002",
        "fromWalletOwnerName": "Example-Send-Client",
        "toWalletOwnerName": "RHUB",
        "fromWalletOwnerMsisdn": "987654321",
        "toWalletOwnerMsisdn": "9876543210",
        "fromAmount": 10.51,
        "fromWalletCode": "1000000010",
        "fromWalletName": "Main Wallet",
        "toWalletCode": "1000000020",
        "toWalletName": "Main Wallet",
        "fromCurrencyCode": "100003",
        "toCurrencyCode": "100069",
        "fromCurrencyName": "USD-USA",
        "toCurrencyName": "USD-USA",
        "fromCurrencySymbol": "$",
        "toCurrencySymbol": "$",
        "transactionTypeCode": "101442",
        "transactionTypeName": "Payout",
        "creationDate": "2026-08-10 18:04:09",
        "fee": 0.0,
        "status": "SUCCESS",
        "srcPostBalance": 1.234566749E7,
        "srcPreviousBalance": 1.23456780E7,
        "destPreviousBalance": -1.2345678E8,
        "destPostBalance": -1.2345676949E8,
        "transactionAmount": 10.51,
        "fromWalletTypeCode": "100008",
        "toWalletTypeCode": "100008",
        "debitAmount": 10.51,
        "creditAmount": 0.0,
        "convertedFeeAmount": 0.0,
        "convertedMarginAmount": 0.0,
        "payinCurrencyName": "USD-USA",
        "postBalance": 1.234566749E7,
        "payoutFee": 0.0,
        "paymentMode": "Cash",
        "fromRemittanceUserType": "100000",
        "sendClientFeeReverse": false,
        "payoutClientFeeReverse": false,
        "token": null,
        "toAmount": 10.51
      }
    ]
  }
}
```

### Response structure

| Element | Contents |
|---|---|
| Top level | `transactionId`, `requestTime`, `responseTime`, `resultCode` and `resultDescription` — request/response metadata and the result. |
| `pageable` | Statement result metadata: `limit`, `totalRecords`, `sort`, `sortBy`. |
| `miniStatement.walletTransactionList` | An array of transaction records. Each record carries identifiers, wallet owners, wallet information, currencies, transaction amounts, fees, status, timestamps, balances, payment mode and related transaction attributes, as shown above. |

Field-level descriptions RHUB has published for the same record shape are on [Payin Notification](/docs/virtual-accounts/payin-notification). Fields that appear only in this response are left undescribed rather than guessed.

## Related APIs

- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
- [Payin Notification](/docs/virtual-accounts/payin-notification)
- [Payout](/docs/payout/payout)
