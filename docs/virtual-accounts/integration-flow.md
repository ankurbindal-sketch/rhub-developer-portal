---
title: "VA integration flow"
sidebar_label: "Integration flow"
description: "The Virtual Account onboarding sequence, from authentication to approval."
---

# VA integration flow

The sequence below is the order RHUB supports for Virtual Account onboarding. Steps 1 to 6
are client actions; the final step is carried out by RHUB Admin/Operations.

<div className="rhub-journey">

<div className="rhub-journey__step">
<span className="rhub-journey__index">01</span>
<span className="rhub-journey__kind">Client · shared API</span>

**[Authentication](/docs/authentication/authentication)**

Obtain the access token used on every VA call.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">02</span>
<span className="rhub-journey__kind">Client</span>

**[Check VA-supported currencies](/docs/virtual-accounts/va-currencies)**

Confirm the settlement currency you need is enabled for Virtual Accounts.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">03</span>
<span className="rhub-journey__kind">Client</span>

**[Fetch VA document requirements](/docs/virtual-accounts/document-requirements)**

Retrieve the document checklist for the customer type you are onboarding.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">04</span>
<span className="rhub-journey__kind">Client</span>

**[Upload the required VA documents](/docs/virtual-accounts/upload-documents)**

Upload each document with its document type. One client-generated
`docReferenceNumber` groups the set.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">05</span>
<span className="rhub-journey__kind">Client</span>

**Register the VA customer**

[Individual](/docs/virtual-accounts/individual/create) or
[Business](/docs/virtual-accounts/business/create).

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">06</span>
<span className="rhub-journey__kind">Client · optional</span>

**Retrieve or edit the customer, and the uploaded documents**

[Retrieve individual](/docs/virtual-accounts/individual/retrieve) ·
[Edit individual](/docs/virtual-accounts/individual/edit) ·
[Retrieve business](/docs/virtual-accounts/business/retrieve) ·
[Edit business](/docs/virtual-accounts/business/edit) ·
[Get uploaded documents](/docs/virtual-accounts/get-documents)

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">07</span>
<span className="rhub-journey__kind">Client</span>

**[Check the VA request status](/docs/virtual-accounts/va-request-status)**

Follow the request through to its resulting state.

</div>

<div className="rhub-journey__step">
<span className="rhub-journey__index">08</span>
<span className="rhub-journey__kind">RHUB Admin / Operations</span>

**[Approval and collection-bank setup](/docs/virtual-accounts/va-approval-process)**

RHUB reviews the request and establishes the collection bank relationship. Clients do not
call this operation.

</div>

</div>

### Recommended Order of API Calls

| # | Step | API | Why This Step? |
|---|---|---|---|
| 1 | **Check Currencies** | Get VA Currency API | Confirm which currencies are VA-settlement enabled (`vaSettlementFlag: true`) before onboarding. |
| 2 | **Fetch Document Checklist** | VA Document Type List API | Get the mandatory/optional document list for the customer type (Individual vs Business). |
| 3 | **Upload Documents** | Upload VA Document API | Upload each document from the checklist. Each call returns a `docReferenceNumber`. |
| 4 | **Verify Uploads (optional)** | Get Uploaded VA Documents API | List what's been uploaded so far for a wallet owner, useful for a progress checklist UI. |
| 5 | **Register the Customer** | Create Individual / Business Customer API | Submit the full registration payload, referencing the `docReferenceNumber` from Step 3. |
| 6 | **Fetch the Receipt (optional)** | Customer Receipt API | Re-fetch the registration to confirm what was saved and its screening/approval state. |
| 7 | **Edit if Needed** | Edit Individual / Business Customer API | Update the customer record — same payload shape as Create, keyed by `customerCode`. |
| 8 | **Track VA Request** | VA Account Request Status API | Ops-side: view the queue of pending/approved VA account requests. |
| 9 | **Approve & Link Bank** | VA Customer Account Approve API | Ops-side: link the customer to a collection bank account and activate the Virtual Account. |
