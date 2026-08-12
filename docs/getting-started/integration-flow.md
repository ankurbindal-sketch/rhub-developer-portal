---
title: "Integration flow"
sidebar_label: "Integration flow"
description: "The RHUB API call sequence, as documented in the RHUB source."
---

# Integration flow

The RHUB supports the API call in the following sequence.
 1. [Login (Authentication) API](/docs/authentication/authentication)
 ➤ Required to authenticate and obtain access tokens for subsequent calls.
 2. [Quotation API](/docs/quotation/quotation)
 ➤ Used to fetch the exchange rate and charges before initiating a payout.
 3. [Bank List API](/docs/master-apis/bank-list)
 ➤ Retrieves the list of bank details and related parameters required by a specific correspondent, based on the provided receiver code.
 4. [Document Upload API](/docs/documents/document-upload)
 ➤ Enables the client to upload customer-related documents, including ID proofs and invoices.
 5. [Payout API](/docs/payout/payout)
 ➤ Initiates the fund transfer based on the selected quotation and beneficiary.
 6. [Transaction Enquiry API](/docs/transactions/transaction-enquiry)
 ➤ Used to check the status of a previously initiated payout.
 7. [Balance API](/docs/balance/balance-enquiry)
 ➤ Retrieves the current wallet or account balance.
 * [Master API](/docs/master-apis)
 ➤ These provide necessary configuration data (e.g., remittance purpose, source of funds, bank lists, occupations etc). This API is subject to specific requirements and can be invoked at any point within the sequence, depending on the use case.

However, the API call sequence is limited to the Login API, Quotation API, Payout API, and Transaction Enquiry API and the remaining APIs can be called based on the need.
