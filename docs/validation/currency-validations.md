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
:::info[Field requirement clarification]

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

<div className="rhub-reqs">

<details className="rhub-req">
<summary><span className="rhub-req__code">AED</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">MYR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">LKR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">NGN</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">ARS</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES with value RHD003(Passport) |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">KES</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">NPR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">KRW</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">INR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">VND</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">MXN</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">COP</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">PHP</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">TRY</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">BRL</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">PKR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">IDR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">ZAR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | YES |
| senderIdExpiration | YES |
| senderIdCountry | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">HKD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">SGD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">EUR, EUR-INSTANT</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">JPY</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">GBP, GBP-INSTANT, GBP-STANDARD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">CAD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">AUD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">USD-USA</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">THB</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| senderIdType | YES |
| senderIssueDate | NO |
| senderIdExpiration | NO |
| senderIdCountry | NO |

</details>

</div>

### Receiver Customer

[Go To Payout(Receiver details)](/docs/payout/payout#receiver-req-param)

**Beneficary (Individual)**

*Source column groups: Bank detail fields (8 columns); Additional Kyc detail fields (7 columns)*

<div className="rhub-reqs">

<details className="rhub-req">
<summary><span className="rhub-req__code">AED</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | YES it represents the Swift Code |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">MYR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">LKR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">NGN</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">ARS</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES with value RHD010(Tax ID No) |
| receiverIdNumber | YES (for UAT use: 27386132859) |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">KES</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">NPR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">KRW*</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">INR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | YES it represents the IFSC Code |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">VND*</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">MXN</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">COP</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">PHP</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">TRY</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | NO |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">BRL</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | YES |
| receiverBankCountry | YES it represents the Bank Sub Code |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES with value RHD010(CPF/Tax ID No) |
| receiverIdNumber | YES with min-max length 11 |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">PKR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">IDR*</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">ZAR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">HKD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | NO |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | YES |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">SGD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">EUR, EUR-INSTANT</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | NO |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | YES |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | NO |
| receiverIdNumber | NO |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">JPY*</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | YES |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">GBP, GBP-INSTANT, GBP-STANDARD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | NO |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | YES |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | NO |
| receiverIdNumber | NO |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">CAD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | NO |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | YES |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">AUD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | YES |
| receiverAccountNumber | YES |
| receiverSwiftCode | YES it represents the BSB Code |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | NO |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | YES |
| receiverIdNumber | YES |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">USD-USA</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | NO |
| receiverAccountNumber | YES |
| receiverSwiftCode | YES it represents the Routing No |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | YES |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | NO |
| receiverIdNumber | NO |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">THB</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| receiverBankName | YES |
| receiverBankCode | NO |
| receiverAccountNumber | YES |
| receiverSwiftCode | NO |
| receiverAccountHolderName | YES |
| receiverAccountType | NO |
| receiverBankCountry | YES |
| receiverBankAddress | NO |
| receiverMsisdn | YES |
| receiverIdType | NO |
| receiverIdNumber | NO |
| receiverDOB | NO |
| receiverPinCode | YES |
| receiverIdExpiration | NO |

</details>

</div>

*Decimal values are not allowed in the payout amount for these currencies.

### Sender Business

[Go To Payout(Sender details)](/docs/payout/payout#sender-req-param)

**Sender (Business)**

*Source column groups: Kyc detail fields (3 columns)*

<div className="rhub-reqs">

<details className="rhub-req">
<summary><span className="rhub-req__code">AED</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">MYR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">LKR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">NGN</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">ARS</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">KES</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">NPR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">KRW</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">INR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">VND</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">MXN</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">COP</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">PHP</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">TRY</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">BRL</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">PKR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">IDR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">ZAR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | YES |
| businessIdValidThru | YES |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">HKD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">SGD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">EUR, EUR-INSTANT</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">JPY</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">GBP, GBP-INSTANT, GBP-STANDARD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">CAD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">AUD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">USD-USA</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">THB</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessRegistrationIssueDate | NO |
| businessIdValidThru | NO |
| businessPinCode | YES |

</details>

</div>

### Receiver Business

[Go To Payout(Receiver details)](/docs/payout/payout#receiver-req-param)

**Beneficary (Business)**

*Source column groups: Bank detail fields (4 columns); Additional Kyc detail fields (5 columns)*

<div className="rhub-reqs">

<details className="rhub-req">
<summary><span className="rhub-req__code">AED</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | YES it represents the Swift Code |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">MYR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">LKR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">NGN</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">ARS</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">KES</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">NPR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">KRW*</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">INR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | YES it represents the IFSC Code |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">VND*</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">MXN</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">COP</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">PHP</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">TRY</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | NO |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">BRL</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | YES |
| businessBankCountry | YES it represents the Bank Sub Code |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">PKR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">IDR*</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">ZAR</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">HKD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | NO |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | YES |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | NO |
| businessRegistrationNumber | NO |
| businessPinCode | YES |
| businessIdValidThru | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">SGD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | NO |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | NO |
| businessRegistrationNumber | NO |
| businessPinCode | YES |
| businessIdValidThru | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">EUR, EUR-INSTANT</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | NO |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | YES |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | NO |
| businessRegistrationNumber | NO |
| businessPinCode | YES |
| businessIdValidThru | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">JPY*</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | YES |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | YES |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | YES |
| businessRegistrationNumber | YES |
| businessPinCode | YES |
| businessIdValidThru | YES |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">GBP, GBP-INSTANT, GBP-STANDARD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | NO |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | YES |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | NO |
| businessRegistrationNumber | NO |
| businessPinCode | YES |
| businessIdValidThru | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">CAD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | NO |
| businessSwiftCode | YES it represents the Transit Code |
| businessAccountType | NO |
| businessBankCountry | YES |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | NO |
| businessRegistrationNumber | NO |
| businessPinCode | YES |
| businessIdValidThru | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">AUD</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | NO |
| businessSwiftCode | YES it represents the BSB Code |
| businessAccountType | NO |
| businessBankCountry | YES |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | NO |
| businessRegistrationNumber | NO |
| businessPinCode | YES |
| businessIdValidThru | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">USD-USA</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | NO |
| businessSwiftCode | YES it represents the Routing No |
| businessAccountType | NO |
| businessBankCountry | YES |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | NO |
| businessRegistrationNumber | NO |
| businessPinCode | YES |
| businessIdValidThru | NO |

</details>

<details className="rhub-req">
<summary><span className="rhub-req__code">THB</span><span className="rhub-req__rail">LOCAL</span><span className="rhub-req__cta">View requirements</span></summary>

| Field | Requirement |
|---|---|
| businessBankCode | NO |
| businessSwiftCode | NO |
| businessAccountType | NO |
| businessBankCountry | YES |
| businessPrimaryContactNumber | YES |
| businessRegistrationIssueDate | NO |
| businessRegistrationNumber | NO |
| businessPinCode | YES |
| businessIdValidThru | NO |

</details>

</div>

*Decimal values are not allowed in the payout amount for these currencies.

<br />

## Related

- [Payout](/docs/payout/payout)
- [Country validations (SWIFT rail)](/docs/validation/country-validations)
- [WPT Payout](/docs/payout/wpt-payout)
