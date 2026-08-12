---
id: "master-index"
title: "Master / reference APIs"
sidebar_label: "Overview"
slug: "/master-apis"
description: "Inventory of the RHUB master / reference APIs."
---

# Master / reference APIs

The master APIs supply the configuration and reference data required by the transactional APIs. The source states that these APIs provide necessary configuration data (for example remittance purpose, source of funds, bank lists and occupations), and that they are subject to specific requirements and can be invoked at any point within the sequence, depending on the use case.

## Published master APIs

These 14 master APIs are documented and published in the RHUB source.

| Master API | Method | Endpoint | Reference |
|---|---|---|---|
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

:::note[Master APIs RHUB does not publish]

The RHUB source file also carries ten further master sections that RHUB has not published: Legal Status Code, Payment Mode, Branch List, Customer Type, Resident Status, Purpose of Opening Business, Transaction Volume, ID Type, Customer Document Fetch and Payout Validator. They are not documented here because RHUB does not publish them — confirm with RHUB before relying on any of them.

:::
