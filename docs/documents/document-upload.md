---
title: "Document Upload"
sidebar_label: "Document Upload"
description: "RHUB Document Upload API — KYC/KYB and invoice documentation for payout."
---

# Document Upload

<span className="rhub-method rhub-method--post">POST</span>

Upload the documents a payout depends on and obtain the reference the Payout request
carries. Document upload follows the [quotation](/docs/quotation/quotation) and precedes the
[payout](/docs/payout/payout).

## Two document purposes

RHUB payouts involve two distinct kinds of document. They are often confused, so it is worth
being explicit about which is which.

<div className="rhub-cards rhub-cards--two">

<div className="rhub-card rhub-card--doc">
<span className="rhub-card__kicker">KYC / KYB</span>

**Purpose** — Customer verification — KYC for individual customers, KYB for business customers.

**Applies to** — All payout transaction types

**Requirement** — Mandatory for payout

**Payout reference** — `docReferenceNumber`

</div>

<div className="rhub-card rhub-card--doc">
<span className="rhub-card__kicker">Invoice</span>

**Purpose** — Supporting document for business-related transactions.

**Applies to** — B2B, B2C, C2B

**Requirement** — Mandatory for B2B, B2C and C2B payout processing. Not applicable as an invoice requirement to C2C.

**Payout reference** — `sendClientTrxReference`

</div>

</div>

**KYC / KYB** is customer verification: KYC for individual customers, KYB for business
customers. It is required for payout on every transaction type, and the resulting reference
is passed to Payout in `docReferenceNumber`.

**Invoice** documentation supports business-related transactions. It is required for B2B,
B2C and C2B payout processing, and the invoice/transaction reference is represented in the
Payout request by `sendClientTrxReference`. It does not apply as an invoice requirement to
C2C.

The source establishes a single document upload contract, reproduced below; it does not
define a separate invoice endpoint or separate invoice-specific request fields. Where your
implementation needs that distinction at endpoint level, confirm it with RHUB.

## Contract

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/documentUpload/upload/customer'}</code>
  </div>
</div>

The Document Upload API is used to upload the ID proof documents of the specific customer of the send client.

## Request Parameter

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| walletOwnerCode | Numeric | 10 | M | To unique code of the customer whose ID proof document is to be uploaded. eg: 1000090909 |
| docReference Number | Alphanumeric | 10 - 30 | M | To unique code of the ID proof document that is to be uploaded. eg:ABCDE12345 (should contains 10 to 30 digits alpha numeric only) |
| file | application/pdf, image/jpg, image/jpeg, image/png | 5000kb max | M | The actual document which needs to be uploaded in pdf, jpg, jpeg or png format. (not more than 5000kb) |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST -
http://host/ewallet/api/v1/documentUpload/upload/customer
```

## Response Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Doc Upload** |  |  |  |  |
| code | String | M |  |  |
| walletOwnerCode | String | M | The unique code of the customer or wallet owner whose document is to be fetched. |  |
| docReferenceNumber | String | M | To unique code of the document, recieved after uploading the document. |  |
| transId | String | M |  |  |
| fileName | String | M | The file name of the ID proof document to be fetched. |  |
| byteArr | String | M | The byte array used to store the binary data. |  |
| fileLocation | String | M | The location where the ID proof document is stored. |  |
| createdOn | String | M | The date and time when the ID proof document was uploaded. The date and time conforms the following format. YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |
| status | String | M | The status of the ID proof document. |  |
| createdBy | String | M | The unique code of the agent who uploaded the ID proof document of the customer or wallet owner. |  |
| source | String | M | The source who uploaded the ID proof document of the customer or wallet owner. |  |
| docTypeCode | String | M | The unique code of the ID proof document that was uploaded. |  |
| docTypeName | String | M | The name of the ID proof document that was uploaded. |  |
| sendClientName | String | M | The name of the send client under whom the customer is registered. |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
  transactionId	"8299691"
  requestTime	"Thu Jun 20 15:29:37 IST 2024"
  responseTime	"Thu Jun 20 15:29:37 IST 2024"
  resultCode	"0"
  resultDescription	"Transaction successful"
  docUpload	Object { walletOwnerCode: "1000008998", docReferenceNumber:
   "CUSYC5A3ZH", fileName: "ID_front-960x600_CUSYC5A3ZH_20240620152937.jpg", … }
  code	""
  walletOwnerCode	"1000008998"
  docReferenceNumber	"CUSYC5A3ZH"
  transId	""
  fileName	"ID_front-960x600_CUSYC5A3ZH_20240620152937.jpg"
  byteArr	null
  fileLocation	"/opt/documentUpload/1000008998/CUSYC5A3ZH"
  createdOn	"2024-06-20T15:29:37.584+0530"
  status	"Active"
  createdBy	"105790"
  source	"CLIENT"
  docTypeCode	"100007"
  docTypeName	"Certificate of Incorporation"
  sendClientName	"marvel "
  createdByName	"marvel "
}
```

## Related APIs

- [Integration flow](/docs/getting-started/integration-flow)
- [Customer Registration](/docs/customers/customer-registration)
- [Payout](/docs/payout/payout)
- [Customer/Individual Document Type (master)](/docs/master-apis/customer-individual-document-type)
