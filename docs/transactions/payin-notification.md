---
title: "Payin Notification"
sidebar_label: "Payin Notification"
description: "RHUB Payin Notification API — retrieve partner wallet transaction records for a date range and customer."
---

# Payin Notification

<span className="rhub-method rhub-method--get">GET</span>

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

The Payin Notification API retrieves partner wallet transaction records for a specified date range and customer. The response provides detailed transaction information including transaction identifiers, wallet details, amounts, currencies, transaction type, balances, fees, status, payment mode, purpose of payment, token and other transaction attributes.

:::note[A query endpoint, not a push notification]

This is a `GET` statement query: you call it to retrieve transaction records. RHUB has not documented any webhook, callback or push behaviour for it.

:::

## Query Parameters

| Parameter | Example | Description |
|---|---|---|
| `sortBy` | creationDate | Field used to sort the transaction records. |
| `limit` | 500 | Maximum number of records requested. |
| `sort` | desc | Sort direction. |
| `fromDate` | 2026-08-01 | Start date for the transaction search. |
| `toDate` | 2026-09-01 | End date for the transaction search. |
| `walletCode` | &#123;walletCode&#125; | Wallet code used for the statement query. |
| `selectedCategory` | 100008 | Transaction category. |
| `transactionId` | null | Transaction ID filter. |
| `sendClientCustomerCode` | &#123;customerId&#125; | Customer identifier used to filter transactions. |
| `transactionType` | 100002 | Transaction type. |
| `transactionSubType` | 100002 | Transaction subtype. |

A complete request appends the query string to the endpoint path. The template below carries the placeholders exactly as RHUB supplies them:

```http
GET /ewallet/api/v1/miniStatement/partnerStatement?sortBy=creationDate&limit=500&sort=desc&fromDate={formDate}&toDate={toDate}&walletCode={walletCode}&selectedCategory=100008&transactionId=null&sendClientCustomerCode={customerId}&transactionType=100002&transactionSubType=100002
```

With the documented example values:

```http
GET /ewallet/api/v1/miniStatement/partnerStatement?sortBy=creationDate&limit=500&sort=desc&fromDate=2026-08-01&toDate=2026-09-01&walletCode={walletCode}&selectedCategory=100008&transactionId=null&sendClientCustomerCode={customerId}&transactionType=100002&transactionSubType=100002
```

:::note[Placeholder spelling]

The parameter is `fromDate`; the placeholder RHUB supplies for it is written `&#123;formDate&#125;`. Both are reproduced exactly as given.

:::

## Response

Example values are synthetic. The structure, field names, nesting and data types are as returned.

```json
{
  "transactionId": "null",
  "requestTime": "Tue Oct 06 15:57:44 IST 2026",
  "responseTime": "Tue Oct 06 15:57:44 IST 2026",
  "resultCode": "0",
  "resultDescription": "Transaction successful",
  "pageable": {
    "limit": 500,
    "totalRecords": 9,
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
        "fromWalletOwnerName": "EXAMPLE1234",
        "toWalletOwnerName": "John Doe",
        "toWalletOwnerMsisdn": "9876543210",
        "fromAmount": 90.0,
        "fromWalletCode": "1000000010",
        "fromWalletName": "Main Wallet",
        "toWalletCode": "1000000020",
        "toWalletName": "Main Wallet",
        "fromCurrencyCode": "100003",
        "toCurrencyCode": "100003",
        "fromCurrencyName": "USD-USA",
        "toCurrencyName": "USD-USA",
        "fromCurrencySymbol": "$",
        "toCurrencySymbol": "$",
        "transactionTypeCode": "100002",
        "transactionTypeName": "Received from send client",
        "creationDate": "2026-08-31 19:21:54",
        "fee": 10.0,
        "status": "SUCCESS",
        "srcPostBalance": -4910.0,
        "srcPreviousBalance": -5000.0,
        "destPreviousBalance": 10000.0,
        "destPostBalance": 10080.0,
        "transactionAmount": 100.0,
        "fromWalletTypeCode": "100008",
        "toWalletTypeCode": "100008",
        "debitAmount": 0.0,
        "creditAmount": 80.0,
        "postBalance": 10080.0,
        "payoutFee": 10.0,
        "rate": 0.0,
        "rateAfterMargin": 0.0,
        "remarkToClient": "Example client remark",
        "paymentMode": "NA",
        "toRemittanceUserType": "100000",
        "purposeOfPaymentCode": "PREP",
        "purposeOfPaymentName": "Pre-Fund",
        "featureCode": "100054",
        "token": "TKN1234567",
        "toAmount": 80.0
      }
    ]
  }
}
```

## Response Parameters

Types and examples are taken from the response above. RHUB has not supplied field descriptions, requirement flags or lengths for this API, so none are stated here.

### Top level

| Field | Type | Example |
|---|---|---|
| `transactionId` | String | "null" |
| `requestTime` | String | Tue Oct 06 15:57:44 IST 2026 |
| `responseTime` | String | Tue Oct 06 15:57:44 IST 2026 |
| `resultCode` | String | 0 |
| `resultDescription` | String | Transaction successful |

### pageable

| Field | Type | Example |
|---|---|---|
| `limit` | Number | 500 |
| `totalRecords` | Number | 9 |
| `sort` | String | desc |
| `sortBy` | String | creationDate |

### miniStatement.walletTransactionList[]

| Field | Type | Example |
|---|---|---|
| `id` | Number | 100001 |
| `code` | String | 1000100001 |
| `transactionId` | String | 200001 |
| `fromWalletOwnerCode` | String | 1000000001 |
| `toWalletOwnerCode` | String | 1000000002 |
| `fromWalletOwnerName` | String | EXAMPLE1234 |
| `toWalletOwnerName` | String | John Doe |
| `toWalletOwnerMsisdn` | String | 9876543210 |
| `fromAmount` | Number | 90.0 |
| `fromWalletCode` | String | 1000000010 |
| `fromWalletName` | String | Main Wallet |
| `toWalletCode` | String | 1000000020 |
| `toWalletName` | String | Main Wallet |
| `fromCurrencyCode` | String | 100003 |
| `toCurrencyCode` | String | 100003 |
| `fromCurrencyName` | String | USD-USA |
| `toCurrencyName` | String | USD-USA |
| `fromCurrencySymbol` | String | $ |
| `toCurrencySymbol` | String | $ |
| `transactionTypeCode` | String | 100002 |
| `transactionTypeName` | String | Received from send client |
| `creationDate` | String | 2026-08-31 19:21:54 |
| `fee` | Number | 10.0 |
| `status` | String | SUCCESS |
| `srcPostBalance` | Number | -4910.0 |
| `srcPreviousBalance` | Number | -5000.0 |
| `destPreviousBalance` | Number | 10000.0 |
| `destPostBalance` | Number | 10080.0 |
| `transactionAmount` | Number | 100.0 |
| `fromWalletTypeCode` | String | 100008 |
| `toWalletTypeCode` | String | 100008 |
| `debitAmount` | Number | 0.0 |
| `creditAmount` | Number | 80.0 |
| `postBalance` | Number | 10080.0 |
| `payoutFee` | Number | 10.0 |
| `rate` | Number | 0.0 |
| `rateAfterMargin` | Number | 0.0 |
| `remarkToClient` | String | Example client remark |
| `paymentMode` | String | NA |
| `toRemittanceUserType` | String | 100000 |
| `purposeOfPaymentCode` | String | PREP |
| `purposeOfPaymentName` | String | Pre-Fund |
| `featureCode` | String | 100054 |
| `token` | String | TKN1234567 |
| `toAmount` | Number | 80.0 |

## Related APIs

- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
- [Balance Enquiry](/docs/balance/balance-enquiry)
- [Integration flow](/docs/getting-started/integration-flow)
