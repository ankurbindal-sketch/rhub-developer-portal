---
title: "Currency validations (LOCAL rail)"
sidebar_label: "Currency validations"
description: "Currency- and correspondent-specific conditional field requirements for RHUB payouts."
---

# Currency validations (LOCAL rail)

:::info[How to use these tables]

These tables state, per currency and rail, which [Payout](/docs/payout/payout) fields the
correspondent requires. They qualify **Conditional** fields only — the source is explicit
that fields marked Mandatory in the Payout API must always be supplied regardless of
correspondent. The source's own wording is reproduced below.

:::

:::note

** Field Requirement Clarification

:::
<br />
:::info[Field requirement clarification (from source)]

- Fields marked as Mandatory in the Payout Api must always be provided, irrespective of whether the correspondent requires them or not. These fields are enforced at the application level and are non-negotiable.
- Fields marked as Conditional are subject to correspondent-specific requirements. Such fields are mandatory only when explicitly required by the selected correspondent, as described in the corresponding conditions section below.
- Users are required to validate and comply with correspondent rules only for fields marked as Conditional in the Payout Api. Mandatory fields defined in this documentation(Payout Api) take precedence and must be supplied in all cases.

:::

:::note

Note: “YES” indicates that the field is mandatory, while “NO” indicates that it is optional.

:::

### Sender Customer

[Go To Payout(Sender details)](/docs/payout/payout#sender-req-param)

**Sender (Individual)**

*Source column groups: Kyc detail fields (4 columns)*

| Currency | RAIL | senderIdType | senderIssueDate | senderIdExpiration | senderIdCountry |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AED | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| MYR | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| LKR | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| NGN | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| ARS | LOCAL | YES with value RHD003(Passport) | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| KES | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| NPR | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| KRW | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| INR | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| VND | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| MXN | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| COP | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| PHP | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| TRY | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| BRL | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| PKR | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| IDR | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| ZAR | LOCAL | YES | YES | YES | YES |  |  |  |  |  |  |  |  |  |  |  |  |
| HKD | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |
| SGD | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |
| EUR, EUR-INSTANT | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |
| JPY | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |
| GBP, GBP-INSTANT, GBP-STANDARD | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |
| CAD | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |
| AUD | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |
| USD-USA | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |
| THB | LOCAL | YES | NO | NO | NO |  |  |  |  |  |  |  |  |  |  |  |  |

### Receiver Customer

[Go To Payout(Receiver details)](/docs/payout/payout#receiver-req-param)

**Beneficary (Individual)**

*Source column groups: Bank detail fields (8 columns); Additional Kyc detail fields (7 columns)*

| Currency | RAIL | receiverBankName | receiverBankCode | receiverAccountNumber | receiverSwiftCode | receiverAccountHolderName | receiverAccountType | receiverBankCountry | receiverBankAddress | receiverMsisdn | receiverIdType | receiverIdNumber | receiverDOB | receiverPinCode | receiverIdExpiration |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AED | LOCAL | YES | YES | YES | YES it represents the Swift Code | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| MYR | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| LKR | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| NGN | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| ARS | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES with value RHD010(Tax ID No) | YES (for UAT use: 27386132859) | NO | YES | YES |  |
| KES | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| NPR | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| KRW* | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| INR | LOCAL | YES | YES | YES | YES it represents the IFSC Code | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| VND* | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| MXN | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| COP | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| PHP | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| TRY | LOCAL | YES | NO | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| BRL | LOCAL | YES | YES | YES | NO | YES | YES | YES it represents the Bank Sub Code | NO | YES | YES with value RHD010(CPF/Tax ID No) | YES with min-max length 11 | NO | YES | YES |  |
| PKR | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| IDR* | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| ZAR | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| HKD | LOCAL | YES | NO | YES | NO | YES | NO | YES | NO | YES | YES | YES | NO | YES | NO |  |
| SGD | LOCAL | YES | YES | YES | NO | YES | NO | NO | NO | YES | YES | YES | NO | YES | NO |  |
| EUR, EUR-INSTANT | LOCAL | YES | NO | YES | NO | YES | NO | YES | NO | YES | NO | NO | NO | YES | NO |  |
| JPY* | LOCAL | YES | YES | YES | NO | YES | NO | YES | NO | YES | YES | YES | NO | YES | YES |  |
| GBP, GBP-INSTANT, GBP-STANDARD | LOCAL | YES | NO | YES | NO | YES | NO | YES | NO | YES | NO | NO | NO | YES | NO |  |
| CAD | LOCAL | YES | NO | YES | NO | YES | NO | YES | NO | YES | YES | YES | NO | YES | YES |  |
| AUD | LOCAL | YES | YES | YES | YES it represents the BSB Code | YES | NO | NO | NO | YES | YES | YES | NO | YES | YES |  |
| USD-USA | LOCAL | YES | NO | YES | YES it represents the Routing No | YES | NO | YES | NO | YES | NO | NO | NO | YES | NO |  |
| THB | LOCAL | YES | NO | YES | NO | YES | NO | YES | NO | YES | NO | NO | NO | YES | NO |  |

*Decimal values are not allowed in the payout amount for these currencies.

### Sender Business

[Go To Payout(Sender details)](/docs/payout/payout#sender-req-param)

**Sender (Business)**

*Source column groups: Kyc detail fields (3 columns)*

| Currency | RAIL | businessRegistrationIssueDate | businessIdValidThru | businessPinCode |
|---|---|---|---|---|
| AED | LOCAL | YES | YES | YES |
| MYR | LOCAL | YES | YES | YES |
| LKR | LOCAL | YES | YES | YES |
| NGN | LOCAL | YES | YES | YES |
| ARS | LOCAL | YES | YES | YES |
| KES | LOCAL | YES | YES | YES |
| NPR | LOCAL | YES | YES | YES |
| KRW | LOCAL | YES | YES | YES |
| INR | LOCAL | YES | YES | YES |
| VND | LOCAL | YES | YES | YES |
| MXN | LOCAL | YES | YES | YES |
| COP | LOCAL | YES | YES | YES |
| PHP | LOCAL | YES | YES | YES |
| TRY | LOCAL | YES | YES | YES |
| BRL | LOCAL | YES | YES | YES |
| PKR | LOCAL | YES | YES | YES |
| IDR | LOCAL | YES | YES | YES |
| ZAR | LOCAL | YES | YES | YES |
| HKD | LOCAL | NO | NO | YES |
| SGD | LOCAL | NO | NO | YES |
| EUR, EUR-INSTANT | LOCAL | NO | NO | YES |
| JPY | LOCAL | NO | NO | YES |
| GBP, GBP-INSTANT, GBP-STANDARD | LOCAL | NO | NO | YES |
| CAD | LOCAL | NO | NO | YES |
| AUD | LOCAL | NO | NO | YES |
| USD-USA | LOCAL | NO | NO | YES |
| THB | LOCAL | NO | NO | YES |

### Receiver Business

[Go To Payout(Receiver details)](/docs/payout/payout#receiver-req-param)

**Beneficary (Business)**

*Source column groups: Bank detail fields (4 columns); Additional Kyc detail fields (5 columns)*

| Currency | RAIL | businessBankCode | businessSwiftCode | businessAccountType | businessBankCountry | businessPrimaryContactNumber | businessRegistrationIssueDate | businessRegistrationNumber | businessPinCode | businessIdValidThru |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AED | LOCAL | YES | YES it represents the Swift Code | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| MYR | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| LKR | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| NGN | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| ARS | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| KES | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| NPR | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| KRW* | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| INR | LOCAL | YES | YES it represents the IFSC Code | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| VND* | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| MXN | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| COP | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| PHP | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| TRY | LOCAL | NO | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| BRL | LOCAL | YES | NO | YES | YES it represents the Bank Sub Code | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| PKR | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| IDR* | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| ZAR | LOCAL | YES | NO | NO | NO | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| HKD | LOCAL | NO | NO | NO | YES | YES | NO | NO | YES | NO |  |  |  |  |  |  |
| SGD | LOCAL | YES | NO | NO | NO | YES | NO | NO | YES | NO |  |  |  |  |  |  |
| EUR, EUR-INSTANT | LOCAL | NO | NO | NO | YES | YES | NO | NO | YES | NO |  |  |  |  |  |  |
| JPY* | LOCAL | YES | NO | NO | YES | YES | YES | YES | YES | YES |  |  |  |  |  |  |
| GBP, GBP-INSTANT, GBP-STANDARD | LOCAL | NO | NO | NO | YES | YES | NO | NO | YES | NO |  |  |  |  |  |  |
| CAD | LOCAL | NO | YES it represents the Transit Code | NO | YES | YES | NO | NO | YES | NO |  |  |  |  |  |  |
| AUD | LOCAL | NO | YES it represents the BSB Code | NO | YES | YES | NO | NO | YES | NO |  |  |  |  |  |  |
| USD-USA | LOCAL | NO | YES it represents the Routing No | NO | YES | YES | NO | NO | YES | NO |  |  |  |  |  |  |
| THB | LOCAL | NO | NO | NO | YES | YES | NO | NO | YES | NO |  |  |  |  |  |  |

*Decimal values are not allowed in the payout amount for these currencies.

<br />

## Related

- [Payout](/docs/payout/payout)
- [Country validations (SWIFT rail)](/docs/validation/country-validations)
- [WPT Payout](/docs/payout/wpt-payout)
