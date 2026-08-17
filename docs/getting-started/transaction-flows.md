---
title: "Transaction flows"
sidebar_label: "Transaction flows"
description: "Bank payout and wallet payout transaction flows as described by RHUB."
---

# Transaction flows

RHUB settles a payout to one of two destinations: the beneficiary's bank account, or the
beneficiary's wallet. Which one applies determines the payout API you call —
[Payout](/docs/payout/payout) for bank transfers and
[WPT Payout](/docs/payout/wpt-payout) for wallet transfers — and, for wallet transfers, the
[WPT Wallet List](/docs/master-apis/wpt-wallet-list) master API supplies the wallet values.

The following are the transaction flows.
* Bank payout transaction flow
* Wallet payout transaction flow

## Bank Payout Transaction Flow
The bank transaction service enables the sender to send or transfer the money to the bank account of the beneficiary. Therefore the money is credited to the bank account of that beneficiary.
The sender can send the money transfer from a bank account, or cash over the counter based on the interfaces that are provided by the sending partner.
The following flow describes the remit to the bank flow.

## Wallet Payout Transaction Flow
The wallet transaction service enables the sender to send or transfer the money to the wallet of the beneficiary. Therefore the money is credited to the wallet of that beneficiary.
The following flow describes the remit to the wallet flow.

## Where these flows meet the APIs

Both settlement flows use the same integration sequence — authenticate, prepare the customer
and documents, quote, pay out, then check status. See the
[integration flow](/docs/getting-started/integration-flow) for the decision points.
