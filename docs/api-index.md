---
title: "API index"
sidebar_label: "API index"
hide_table_of_contents: true
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

## Virtual Account APIs

Virtual Account onboarding endpoints. Customer registration uses the same endpoint as the rest of the platform, in a VA onboarding context with a VA-specific request; see the linked page for that variant.

<div className="rhub-apitable">

| API | Method | Purpose | Integration stage | Endpoint | Page |
|---|---|---|---|---|---|
| VA Currencies | `GET` | Returns the settlement currencies enabled for Virtual Accounts under a send client. | VA onboarding | `http://host/ewallet/api/v1/currency/virtualAccountCurrency/{sendClientCode}` | [Open](/docs/virtual-accounts/va-currencies) |
| VA Document Type List | `GET` | Returns the document checklist for a VA customer type. | VA onboarding | `http://host/ewallet/api/v1/virtualAccount/customerDocumentType/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/virtual-accounts/document-requirements) |
| Upload VA Document | `POST` | Uploads a single VA document against its document type. | VA onboarding | `http://host/ewallet/api/v1/documentUpload/upload/virtualCustomer` | [Open](/docs/virtual-accounts/upload-documents) |
| Get Uploaded VA Documents | `GET` | Returns the VA documents already uploaded for a wallet owner. | VA onboarding | `http://host/ewallet/api/v1/documentUpload/virtualDocument/{walletOwnerCode}` | [Open](/docs/virtual-accounts/get-documents) |
| VA Customer Registration (individual) | `POST` | Registers an individual VA customer. Shared endpoint, VA-specific request. | VA onboarding | `http://host/ewallet/api/v1/customer-registration` | [Open](/docs/virtual-accounts/individual/create) |
| VA Customer Registration (business) | `POST` | Registers a business VA customer. Shared endpoint, VA-specific request. | VA onboarding | `http://host/ewallet/api/v1/customer-registration` | [Open](/docs/virtual-accounts/business/create) |
| Retrieve VA Customer | `GET` | Returns a registered VA customer record. | VA onboarding | `http://host/ewallet/api/v1/customer-registration/{code}` | [Open](/docs/virtual-accounts/individual/retrieve) |
| Edit VA Customer | `PUT` | Updates the editable fields of a registered VA customer. | VA onboarding | `http://host/ewallet/api/v1/customer-registration/{code}` | [Open](/docs/virtual-accounts/individual/edit) |
| VA Request Status | `GET` | Returns the state of submitted VA account requests. | VA post-registration | `http://host/ewallet/api/v1/collectionBank/individual/virtualAccount/customer/all` | [Open](/docs/virtual-accounts/va-request-status) |

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

### Lookups used for Virtual Account onboarding

These lookups supply the coded values the [Virtual Account](/docs/virtual-accounts) registration payloads expect. Full response shapes and list keys are on [VA reference data](/docs/virtual-accounts/va-reference-data).

<div className="rhub-apitable">

| API | Method | Purpose | Integration stage | Endpoint | Page |
|---|---|---|---|---|---|
| Business Transaction Volume | `GET` | Returns the business transaction-volume bands for a customer type. Used for VA onboarding. | Payout preparation / reference | `http://host/ewallet/api/v1/businessTxnVolume/getByCustomerTypeCode/{customerTypeCode}` | [Open](/docs/virtual-accounts/va-reference-data) |
| Purpose of Opening Business | `GET` | Returns the business-relationship purposes for business customers. Used for VA onboarding. | Payout preparation / reference | `http://host/ewallet/api/v1/purposeOfOpeningBusiness/getByCustomerTypeCode/100002` | [Open](/docs/virtual-accounts/va-reference-data) |
| Residence Status | `GET` | Returns the residence-status values for individual customers. Used for VA onboarding. | Payout preparation / reference | `http://host/ewallet/api/v1/residenceStatus/customerTypeCode/100001` | [Open](/docs/virtual-accounts/va-reference-data) |
| ID Type | `GET` | Returns the identity-document types for business customers. Used for VA onboarding. | Payout preparation / reference | `http://host/ewallet/api/v1/idType/getByCustomerTypeCode/100002` | [Open](/docs/virtual-accounts/va-reference-data) |
| Customer Type | `GET` | Returns the customer types, for example individual and business. Used for VA onboarding. | Payout preparation / reference | `http://host/ewallet/api/v1/customerType/all` | [Open](/docs/virtual-accounts/va-reference-data) |

</div>

:::note

Endpoint strings are reproduced exactly as RHUB writes them, including the literal `http://host` placeholder where RHUB uses it.

:::

## Related

- [Integration flow](/docs/getting-started/integration-flow)
- [How to read this reference](/docs/getting-started/conventions)
- [Errors and response codes](/docs/errors)
