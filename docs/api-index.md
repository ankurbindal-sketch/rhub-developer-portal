---
title: "API reference index"
sidebar_label: "API index"
description: "Complete index of RHUB APIs documented in this portal."
---

# API reference index

Every API contract published by the RHUB source, in one table.

| API | Method | Endpoint (as written in source) | Page |
|---|---|---|---|
| Authentication | `POST` | `http://host/ewallet/oauth/token` | [Open](/docs/authentication/authentication) |
| Customer Registration | `POST` | `http://host/ewallet/api/v1/customer-registration` | [Open](/docs/customers/customer-registration) |
| Quotation | `POST` | `http://host/ewallet/api/v1/fxratequotation/api` | [Open](/docs/quotation/quotation) |
| Payout | `POST` | `http://host/ewallet/api/v1/payoutProcess/api` | [Open](/docs/payout/payout) |
| WPT Payout | `POST` | `http://host/ewallet/api/v1/payoutProcess/api` | [Open](/docs/payout/wpt-payout) |
| Transaction Enquiry | `GET` | `http://host/ewallet/api/v1/transactionInfo/api?types=all&status=all&transId={value}` | [Open](/docs/transactions/transaction-enquiry) |
| Balance Enquiry | `GET` | `http://host/ewallet/api/v1/wallet/walletOwner/{walletOwnerCode}` | [Open](/docs/balance/balance-enquiry) |
| Document Upload | `POST` | `http://host/ewallet/api/v1/documentUpload/upload/customer` | [Open](/docs/documents/document-upload) |
| Remittance Purpose | `GET` | `http://host/ewallet/api/v1/purposeOfRemittance/RHUB/{transactionType}/{countryCode}` | [Open](/docs/master-apis/remittance-purpose) |
| Source of Fund | `GET` | `http://host/ewallet/api/v1/getSourceOfFund/RHUB/{transactionType}/{countryCode}` | [Open](/docs/master-apis/source-of-fund) |
| Relationship | `GET` | `http://host/ewallet/api/v1/getRelationship/RHUB/{transactionType}` | [Open](/docs/master-apis/relationship) |
| Document ID Type | `GET` | `http://host/ewallet/api/v1/getDocumentIdType/RHUB/{transactionType}` | [Open](/docs/master-apis/document-id-type) |
| Occupation | `GET` | `http://host/ewallet/api/v1/getOccupation/RHUB/{transactionType}` | [Open](/docs/master-apis/occupation) |
| Business Type | `GET` | `http://host/ewallet/api/v1/masterBusinessTypes/RHUB/{transactionType}` | [Open](/docs/master-apis/business-type) |
| Business Registration Type | `GET` | `http://host/ewallet/api/v1/masterBusinessRegistrationTypes/RHUB/{transactionType}` | [Open](/docs/master-apis/business-registration-type) |
| Account Type | `GET` | `http://host/ewallet/api/v1/accountType/all` | [Open](/docs/master-apis/account-type) |
| WPT Wallet List | `GET` | `http://host/ewallet/api/v1/walletList/{countryCode}/{currencyCode}/{receiverCode}/WPT` | [Open](/docs/master-apis/wpt-wallet-list) |
| Bank List | `GET` | `http://host/ewallet/api/v1/payoutbanklist/{country}/{currency}/{recieverCode}` | [Open](/docs/master-apis/bank-list) |
| Customer Legal Status | `GET` | `http://host/ewallet/api/v1/customerLegalStatus/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/master-apis/customer-legal-status) |
| Nature of Business | `GET` | `http://host/ewallet/api/v1/natureOfBusiness/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/master-apis/nature-of-business) |
| Customer Occupation Type | `GET` | `http://host/ewallet/api/v1/customerOccupationType/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/master-apis/customer-occupation-type) |
| Customer/Individual Document Type | `GET` | `http://host/ewallet/api/v1/customerDocumentType/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/master-apis/customer-individual-document-type) |
| WPT — Customer Registration | `POST` | `http://host/ewallet/api/v1/customer-registration` | [Open](/docs/wpt/customer-registration) |
| WPT — Quotation | `POST` | `http://host/ewallet/api/v1/fxratequotation/api` | [Open](/docs/wpt/quotation) |
| WPT — Payout | `POST` | `http://host/ewallet/api/v1/payoutProcess/api` | [Open](/docs/wpt/payout) |
| Service Fee | `GET` | `http://host/ewallet/api/v1/senderClientfeeTemplate/getWalletOwner/{senderCode}` | [Open](/docs/template-management/service-fee) |
| Update Service Fee | `POST` | `http://host/ewallet/api/v1/senderClientfeeTemplate` | [Open](/docs/template-management/update-service-fee) |
| Transaction List | `GET` | `http://host/ewallet/api/v1/sendclienttransactionlimittemplate/walletowner/{senderCode}` | [Open](/docs/template-management/transaction-list) |
| Update Transaction Limit | `POST` | `http://host/ewallet/api/v1/sendclienttransactionlimittemplate` | [Open](/docs/template-management/update-transaction-limit) |
| Forex Margin | `GET` | `http://host/ewallet/api/v1/sendClientMarginTemplate/getWalletOwner/{senderCode}` | [Open](/docs/template-management/forex-margin) |
| Update Forex Margin | `POST` | `http://host/ewallet/api/v1/sendClientMarginTemplate` | [Open](/docs/template-management/update-forex-margin) |

:::note

Endpoint strings are reproduced exactly as the source writes them, including the literal `http://host` placeholder where the source uses it.

:::
