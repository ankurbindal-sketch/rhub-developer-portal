---
title: "VA approval process"
sidebar_label: "VA approval process"
description: "What happens after a VA registration request is submitted, and the RHUB Admin/Operations step."
---

# VA approval process

:::warning[RHUB Admin / Operations]

VA approval is carried out by RHUB Admin/Operations. This page explains what happens to a
request after you submit it. Client integrations do not call this operation, and it is not
listed in the [API index](/docs/api-index).

:::

## What happens after you register a VA customer

1. Your registration request is submitted through
   [Individual](/docs/virtual-accounts/individual/create) or
   [Business](/docs/virtual-accounts/business/create) VA customer registration.
2. RHUB Admin/Operations reviews and processes the request.
3. The collection bank relationship is established, as applicable to the customer and
   settlement currency.
4. The request progresses to its resulting status, which you can follow with
   [VA request status](/docs/virtual-accounts/va-request-status).

On completion the request is linked to a collection bank account and activated. Re-query
[VA request status](/docs/virtual-accounts/va-request-status) to see the updated state and
the resulting account details.

## Request states you will see

| state | stateName | Meaning |
|---|---|---|
| `U` | Created | Customer registered; no collection bank account linked yet. |
| `A` | Approved | Linked to a collection bank account via [VA approval process](/docs/virtual-accounts/va-approval-process) — the Virtual Account is live. |

## The operation RHUB performs

Recorded for transparency. This is an internal RHUB Admin/Operations call, performed by RHUB
rather than by your integration.

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--put">PUT</span>
    <code className="rhub-endpoint__url">{'/ewallet/api/v1/collectionBank/virtualAccountCustomer/approve'}</code>
  </div>
</div>

## Related

- [VA request status](/docs/virtual-accounts/va-request-status)
- [VA integration flow](/docs/virtual-accounts/integration-flow)
- [Virtual Accounts overview](/docs/virtual-accounts)
