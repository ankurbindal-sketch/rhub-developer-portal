---
title: "API index"
sidebar_label: "API index"
description: "Index of the public RHUB APIs, with purpose, integration stage and endpoint."
---

# API index

Every API in the public reference, with the stage of an integration at which it is typically used. Purposes are RHUB's own descriptions.

## Transaction APIs

<div className="rhub-apitable">

| API | Method | Purpose | Integration stage | Endpoint | Page |
|---|---|---|---|---|---|
| Authentication | `POST` | The Login API is used to authenticate and authorize the user. | Start | `http://host/ewallet/oauth/token` | [Open](/docs/authentication/authentication) |
| Quotation | `POST` | The Quotation API is used to fetch the forex rate between the payin and payout currencies. | Pricing / pre-registration | `http://host/ewallet/api/v1/fxratequotation/api` | [Open](/docs/quotation/quotation) |
| Document Upload | `POST` | The Document Upload API is used to upload the ID proof documents of the specific customer of the send client. | Payout preparation | `http://host/ewallet/api/v1/documentUpload/upload/customer` | [Open](/docs/documents/document-upload) |
| Customer Registration | `POST` | The Customer-Registration API is used to register or create the customer in the system. | Conditional customer setup | `http://host/ewallet/api/v1/customer-registration` | [Open](/docs/customers/customer-registration) |
| Payout | `POST` | The Payout API is used to perform all types of transactions (B2B,C2C,C2B,B2C). | Transaction | `http://host/ewallet/api/v1/payoutProcess/api` | [Open](/docs/payout/payout) |
| WPT Payout | `POST` | This Payout API is used to perform all types of Wallet transactions (C2C). | Transaction | `http://host/ewallet/api/v1/payoutProcess/api` | [Open](/docs/payout/wpt-payout) |
| Transaction Enquiry | `GET` | The Transaction Enquiry API is used to fetch the statement for the specified period. | Post-payout | `http://host/ewallet/api/v1/transactionInfo/api?types=all&status=all&transId={value}` | [Open](/docs/transactions/transaction-enquiry) |
| Balance Enquiry | `GET` | The Balance API is used to fetch the current balance in the ledger of the partner. | Final / supporting | `http://host/ewallet/api/v1/wallet/walletOwner/{walletOwnerCode}` | [Open](/docs/balance/balance-enquiry) |

</div>

## Master / reference APIs

Master APIs supply the coded values other requests expect. They are need-based: call the ones your route and use case require, in whatever order suits your implementation. They are not a sequence.

<div className="rhub-apitable">

| API | Method | Purpose | Integration stage | Endpoint | Page |
|---|---|---|---|---|---|
| Remittance Purpose | `GET` | The Remittance Purpose API is used to fetch the purpose to send the remittance. | Payout preparation / reference | `http://host/ewallet/api/v1/purposeOfRemittance/RHUB/{transactionType}/{countryCode}` | [Open](/docs/master-apis/remittance-purpose) |
| Source of Fund | `GET` | The Source of Fund API is used to fetch the source of the fund. | Payout preparation / reference | `http://host/ewallet/api/v1/getSourceOfFund/RHUB/{transactionType}/{countryCode}` | [Open](/docs/master-apis/source-of-fund) |
| Relationship | `GET` | The Relationship API is used to fetch the relation of the beneficiary with the sender. | Payout preparation / reference | `http://host/ewallet/api/v1/getRelationship/RHUB/{transactionType}` | [Open](/docs/master-apis/relationship) |
| Document ID Type | `GET` | The Document ID Type API is used to fetch the list of all document types. | Payout preparation / reference | `http://host/ewallet/api/v1/getDocumentIdType/RHUB/{transactionType}` | [Open](/docs/master-apis/document-id-type) |
| Occupation | `GET` | The Occupation API is used to fetch the occupation. | Payout preparation / reference | `http://host/ewallet/api/v1/getOccupation/RHUB/{transactionType}` | [Open](/docs/master-apis/occupation) |
| Business Type | `GET` | The Business API is used to fetch the Business type of customer. | Payout preparation / reference | `http://host/ewallet/api/v1/masterBusinessTypes/RHUB/{transactionType}` | [Open](/docs/master-apis/business-type) |
| Business Registration Type | `GET` | The Business registration type API is used to fetch the registration type of business customers. | Payout preparation / reference | `http://host/ewallet/api/v1/masterBusinessRegistrationTypes/RHUB/{transactionType}` | [Open](/docs/master-apis/business-registration-type) |
| Account Type | `GET` | The Account Type API is used to fetch the type of the account. | Payout preparation / reference | `http://host/ewallet/api/v1/accountType/all` | [Open](/docs/master-apis/account-type) |
| WPT Wallet List | `GET` | The Wallet list API is used to fetch the list of WPT providers. | Payout preparation / reference | `http://host/ewallet/api/v1/walletList/{countryCode}/{currencyCode}/{receiverCode}/WPT` | [Open](/docs/master-apis/wpt-wallet-list) |
| Bank List | `GET` | The Bank List API is used to fetch the list of the bank. | Payout preparation / reference | `http://host/ewallet/api/v1/payoutbanklist/{country}/{currency}/{recieverCode}` | [Open](/docs/master-apis/bank-list) |
| Customer Legal Status | `GET` | The Customer Type API is used to fetch the legal status of the customer. | Payout preparation / reference | `http://host/ewallet/api/v1/customerLegalStatus/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/master-apis/customer-legal-status) |
| Nature of Business | `GET` | The Nature of Business API is used to fetch the nature of the business run by the customer. | Payout preparation / reference | `http://host/ewallet/api/v1/natureOfBusiness/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/master-apis/nature-of-business) |
| Customer Occupation Type | `GET` | The Customer Occupation Type API is used to fetch the occupation of the customer. | Payout preparation / reference | `http://host/ewallet/api/v1/customerOccupationType/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/master-apis/customer-occupation-type) |
| Customer/Individual Document Type | `GET` | The Customer Document Type API is used to fetch the ID proof documents of the customer. | Payout preparation / reference | `http://host/ewallet/api/v1/customerDocumentType/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/master-apis/customer-individual-document-type) |

</div>

:::note

Endpoint strings are reproduced exactly as RHUB writes them, including the literal `http://host` placeholder where RHUB uses it.

:::

## Related

- [Integration flow](/docs/getting-started/integration-flow)
- [How to read this reference](/docs/getting-started/conventions)
- [Errors and response codes](/docs/errors)
