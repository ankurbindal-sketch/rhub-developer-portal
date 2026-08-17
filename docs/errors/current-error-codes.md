---
title: "Current API error codes"
sidebar_label: "Current API error codes"
description: "Current RHUB API error-handling reference: resultCode classes and resultDescription values, supplied by the RHUB team."
---

# Current API error codes

:::info[Authoritative and current]

These are the error codes the RHUB API returns today, supplied by the **RHUB team** on **2026-08-12**. Handle failures on the `resultCode` and `resultDescription` pair below; use [transaction status codes](/docs/errors/transaction-status-codes) to follow a transaction through processing.

:::

## How resultCode and resultDescription relate

The resultCode represents a category/class of error rather than a unique identifier for every individual validation condition.

The same resultCode may therefore appear against multiple resultDescription values.

Examples:

- **400** — broadly represents request validation failures.
- **5000 and 5001** — represent business-rule/field validation failures.
- **1000** — represents a system/technical failure.

The resultDescription carries the specific, actionable reason for the failure and should be used for precise error handling and messaging shown to end users.

resultCode should be used for coarse-grained handling, such as distinguishing request-format/validation issues from business-rule rejection or system-level failure.

:::caution[Do not key on resultCode alone]

resultCode must not be treated as a unique key for a specific validation condition.
Handle `resultCode` coarsely and branch on `resultDescription` for the specific condition.

:::

## Error code reference

All 65 entries as supplied. Rows that share a `resultCode` are listed separately and are **not** merged, because one code covers many distinct conditions.

| S. No. | Result Code | Result Description |
|---|---|---|
| 1 | 400 | payin amount should not be Empty |
| 2 | 400 | payout amount should not be Empty |
| 3 | 5001 | payin amount is not matching with amount used while creating quotation. Please check |
| 4 | 400 | transactioninfoRequest.requestDate.NotNull |
| 5 | 1027 | Currency Not Found |
| 6 | 1000 | technical.failure |
| 7 | 400 | request date should not be Blank |
| 8 | 5001 | sendClientTxnReference is mandatory. |
| 9 | 5001 | sendClientTxnReference document must be uploaded before payout process. |
| 10 | 5001 | document reference must be uploaded before payout process. |
| 11 | 5000 | descriptionText field is missing! Length should be between 1 and 25 |
| 12 | 5000 | Special characters not allowed In descriptionText |
| 13 | 5000 | PaymentMode must be 'Cash' or 'Bank' or 'UPI' |
| 14 | 1197 | invalid.request |
| 15 | 5001 | destinationCountryCode should be same as what we used while creating quotation. Please check! |
| 16 | 5001 | Invalid sourceCountry! |
| 17 | 400 | Invalid JSON format |
| 18 | 5001 | isAutoRegistered is mandatory. |
| 19 | 5001 | declaration is mandatory. |
| 20 | 5001 | Document reference number is mandatory. |
| 21 | 400 | settlement currency should not be Blank |
| 22 | 400 | fx rate value should not be null |
| 23 | 400 | senderMargin value should not be null |
| 24 | 5000 | Business Name field is missing! Length should be between 1 and 70 |
| 25 | 5000 | Industry field is missing! Length should be between 1 and 10 |
| 26 | 5001 | Invalid Sender Business Type. |
| 27 | 5001 | Invalid Receiver Business Type. |
| 28 | 5000 | Special characters not allowed In Sender BusinessRegistrationNumber |
| 29 | 5001 | Sender Invalid Business Registration Issued At. |
| 30 | 5001 | Receiver Invalid Business Registration Issued At. |
| 31 | 5001 | Sender Invalid Business Registration Type. |
| 32 | 5001 | Receiver Invalid Business Registration Type. |
| 33 | 5001 | Please enter minimum 7 digit Contact Number for Sender |
| 34 | 5001 | Please enter minimum 7 digit Contact Number for Receiver |
| 35 | 5000 | State field should not contain leading or trailing whitespace! |
| 36 | 5000 | City field should not contain leading or trailing whitespace! |
| 37 | 5001 | Sender Invalid Business Country Code. |
| 38 | 5001 | Receiver Invalid Business Country Code. |
| 39 | 1384 | authentication failed username or password is incorrect or Beneficiary name does not match |
| 40 | 5000 | Special characters not allowed In Receiver IFSC Code |
| 41 | 400 | quote id should not be blank |
| 42 | 400 | compliance remittance Purpose Should Not Be empty |
| 43 | 5001 | RemittancePurpose is not valid. Please check! |
| 44 | 5001 | SourceOfFund is not valid. Please check! |
| 45 | 5001 | Relationship is not valid. Please check! |
| 46 | 5001 | Please note that the Sender CustomerCode is mandatory. Kindly ensure that the sender is registered before initiating any payment transactions! |
| 47 | 5003 | destinationCountryCode could not be null or empty! |
| 48 | 5003 | Please enter a valid receiverCurrencyCode and destinationCountryCode! |
| 49 | 1368 | Some parameters are missing in quotation request |
| 50 | 400 | fxRateQuotation sendCurrencyCode Should Not Be Null |
| 51 | 1071 | Wallet Owner Not Found |
| 52 | 1382 | payout quotation failed. |
| 53 | *Not provided* | Wallet Not Found |
| 54 | 1364 | master business type not found |
| 55 | 1056 | Transaction Not Found |
| 56 | 4117 | Beneficiary not found |
| 57 | 4001 | Invalid docReferenceNumber. Please upload document first |
| 58 | 4107 | Residence status type not found |
| 59 | 4001 | Individual customer registration Invalid Id Type Code |
| 60 | 4001 | Individual customer registration Invalid Occupation Code |
| 61 | 5001 | Customer already registered with customer ID - 100000896013888I |
| 62 | 4001 | TradeName is mandatory! |
| 63 | 4001 | Business Customer Registration Invalid Nature Of Business. |
| 64 | 4001 | Business Customer Registration Invalid Country Code. |
| 65 | 4001 | Business Customer Registration Invalid Legal Status Code. |

### Entry 53 — no result code supplied

:::note[No result code for this entry]

**Result Code: Not provided**

**Result Description:** Wallet Not Found

This is current API behaviour: the entry has no `resultCode`. Handle it on the `resultDescription`. No code has been inferred or assigned.

:::

## Result codes at a glance

The 65 entries use **16 distinct result codes**, plus one entry with no code.

| Result Code | Entries | Conditions covered |
|---|---|---|
| 400 | 11 | multiple distinct conditions |
| 1000 | 1 | one condition in this list |
| 1027 | 1 | one condition in this list |
| 1056 | 1 | one condition in this list |
| 1071 | 1 | one condition in this list |
| 1197 | 1 | one condition in this list |
| 1364 | 1 | one condition in this list |
| 1368 | 1 | one condition in this list |
| 1382 | 1 | one condition in this list |
| 1384 | 1 | one condition in this list |
| 4001 | 7 | multiple distinct conditions |
| 4107 | 1 | one condition in this list |
| 4117 | 1 | one condition in this list |
| 5000 | 9 | multiple distinct conditions |
| 5001 | 24 | multiple distinct conditions |
| 5003 | 2 | multiple distinct conditions |
| *Not provided* | 1 | one condition in this list |

:::info[HTTP status codes and result codes are separate]

An HTTP status describes the transport-level outcome of a request. A `resultCode` describes the RHUB application or business error category, and `resultDescription` carries the specific reason. The same numeral can appear in both without the two meaning the same thing.

:::

:::note[No remediation guidance]

RHUB supplies code values and descriptions only, so no remediation steps, retry policy or backoff behaviour is documented here.

:::

## Related

- [Errors and response codes overview](/docs/errors)
- [Transaction status codes](/docs/errors/transaction-status-codes)
- [Payout](/docs/payout/payout)
- [Transaction Enquiry](/docs/transactions/transaction-enquiry)
