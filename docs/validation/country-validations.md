---
title: "Country validations (SWIFT rail)"
sidebar_label: "Country validations"
description: "Country-specific SWIFT field requirements for RHUB payouts."
---

# Country validations (SWIFT rail)

:::info[How to use these tables]

These tables state, per country group, which bank-related [Payout](/docs/payout/payout)
fields are mandatory when a transaction is processed through the SWIFT network. As with the
currency tables, they qualify **Conditional** fields; fields marked Mandatory in the Payout
API must always be supplied. The source's own wording is reproduced below.

:::

[Go To Payout(Receiver details)](/docs/payout/payout#receiver-req-param)

:::note

** Field Requirement Clarification

:::
<br />
:::info[Field requirement clarification (from source)]

- Fields marked as Mandatory in the Payout Api must always be provided, irrespective of whether the correspondent requires them or not. These fields are enforced at the application level and are non-negotiable.
- Fields marked as Conditional are subject to correspondent-specific requirements. Such fields are mandatory only when explicitly required by the selected correspondent, as described in the corresponding conditions section below.
- Users are required to validate and comply with correspondent rules only for fields marked as Conditional in the Payout Api. Mandatory fields defined in this documentation(Payout Api) take precedence and must be supplied in all cases.

:::

**SWIFT Transaction Requirements** <br /><br />
**AR – Argentina, BB – Barbados, BM – Bermuda, BN – Brunei, BS – Bahamas, CO – Colombia, DZ – Algeria,** <br />
**EC – Ecuador, FJ – Fiji, HN – Honduras, JM – Jamaica, JP – Japan, KE – Kenya, KR – South Korea,** <br />
**KY – Cayman Islands, MO – Macao, MW – Malawi, NG – Nigeria, NI – Nicaragua, NP – Nepal, NZ – New Zealand,** <br />
**PE – Peru, SZ – Eswatini, TH – Thailand, UG – Uganda, ZA – South Africa**

For the countries listed above, when transactions are processed through the SWIFT network, the following bank-related fields are mandatory for successful transaction processing:

- businessBankName, receiverBankName - used to capture Bank name details
- businessAccountNumber, receiverAccountNumber - used to capture **Bank Account Number details**
- businessSwiftCode, receiverSwiftCode - used to capture Swift Code details
- businessAccountHolderName, receiverAccountHolderName – used to capture beneficiary name details

In the table below, the column headers represent the applicable API field requirements for both business and customer contexts.

:::note

Note: “YES” indicates that the field is mandatory and accepts the value/information specified above. If a different value/information is accepted, it is explicitly mentioned in the table. “NO” indicates that it is optional.

:::

| Country | RAIL | businessBankName, receiverBankName | businessAccountNumber, receiverAccountNumber | businessSwiftCode, receiverSwiftCode | businessAccountHolderName, receiverAccountHolderName |
|---|---|---|---|---|---|
| AR | SWIFT | Yes | Yes | Yes | Yes |
| BB | SWIFT | Yes | Yes | Yes | Yes |
| BM | SWIFT | Yes | Yes | Yes | Yes |
| BN | SWIFT | Yes | Yes | Yes | Yes |
| BS | SWIFT | Yes | Yes | Yes | Yes |
| CO | SWIFT | Yes | Yes | Yes | Yes |
| DZ | SWIFT | Yes | Yes | Yes | Yes |
| EC | SWIFT | Yes | Yes | Yes | Yes |
| FJ | SWIFT | Yes | Yes | Yes | Yes |
| HN | SWIFT | Yes | Yes | Yes | Yes |
| JM | SWIFT | Yes | Yes | Yes | Yes |
| JP | SWIFT | Yes | Yes | Yes | Yes |
| KE | SWIFT | Yes | Yes | Yes | Yes |
| KR | SWIFT | Yes | Yes | Yes | Yes |
| KY | SWIFT | Yes | Yes | Yes | Yes |
| MO | SWIFT | Yes | Yes | Yes | Yes |
| MW | SWIFT | Yes | Yes | Yes | Yes |
| NG | SWIFT | Yes | Yes | Yes | Yes |
| NI | SWIFT | Yes | Yes | Yes | Yes |
| NP | SWIFT | Yes | Yes | Yes | Yes |
| NZ | SWIFT | Yes | Yes | Yes | Yes |
| PE | SWIFT | Yes | Yes | Yes | Yes |
| SZ | SWIFT | Yes | Yes | Yes | Yes |
| TH | SWIFT | Yes | Yes | Yes | Yes |
| UG | SWIFT | Yes | Yes | Yes | Yes |
| ZA | SWIFT | Yes | Yes | Yes | Yes |

---

**SWIFT Transaction Requirements** <br /><br />
**AE – United Arab Emirates, AL – Albania, AT – Austria, BE – Belgium, BG – Bulgaria, BH – Bahrain, CH – Switzerland,** <br />
**CR – Costa Rica, CY – Cyprus, CZ – Czech Republic, DE – Germany, DK – Denmark, EE – Estonia, ES – Spain,** <br />
**FI – Finland, FR – France, GR – Greece, GT – Guatemala, HR – Croatia, HU – Hungary, IE – Ireland, IL – Israel,** <br />
**IT – Italy, JO – Jordan, KW – Kuwait, KZ – Kazakhstan, LB – Lebanon, LI – Liechtenstein, LT – Lithuania,** <br />
**LU – Luxembourg, LV – Latvia, MC – Monaco, MT – Malta, MU – Mauritius, MZ – Mozambique, NL – Netherlands,** <br />
**NO – Norway, OM – Oman, PK – Pakistan, PL – Poland, PT – Portugal, QA – Qatar, RO – Romania, RS – Serbia,** <br />
**SA – Saudi Arabia, SE – Sweden, SI – Slovenia, SK – Slovakia, TN – Tunisia, TR – Turkey, UA – Ukraine**

For the countries listed above, when transactions are processed through the SWIFT network, the following bank-related fields are mandatory for successful transaction processing:

- businessBankName, receiverBankName – used to capture bank name details
- businessAccountNumber, receiverAccountNumber – used to capture **IBAN details**
- businessSwiftCode, receiverSwiftCode – used to capture SWIFT code details
- businessAccountHolderName, receiverAccountHolderName – used to capture beneficiary name details

In the table below, the column headers represent the applicable API field requirements for both business and customer contexts.

:::note

Note: “YES” indicates that the field is mandatory and accepts the value/information specified above. If a different value/information is accepted, it is explicitly mentioned in the table. “NO” indicates that it is optional.

:::

| Country | RAIL | businessBankName, receiverBankName | businessAccountNumber, receiverAccountNumber | businessSwiftCode, receiverSwiftCode | businessAccountHolderName, receiverAccountHolderName |
|---|---|---|---|---|---|
| AE | SWIFT | Yes | Yes | Yes | Yes |
| AL | SWIFT | Yes | Yes | Yes | Yes |
| AT | SWIFT | Yes | Yes | Yes | Yes |
| BE | SWIFT | Yes | Yes | Yes | Yes |
| BG | SWIFT | Yes | Yes | Yes | Yes |
| BH | SWIFT | Yes | Yes | Yes | Yes |
| CH | SWIFT | Yes | Yes | Yes | Yes |
| CR | SWIFT | Yes | Yes | Yes | Yes |
| CY | SWIFT | Yes | Yes | Yes | Yes |
| CZ | SWIFT | Yes | Yes | Yes | Yes |
| DE | SWIFT | Yes | Yes | Yes | Yes |
| DK | SWIFT | Yes | Yes | Yes | Yes |
| EE | SWIFT | Yes | Yes | Yes | Yes |
| ES | SWIFT | Yes | Yes | Yes | Yes |
| FI | SWIFT | Yes | Yes | Yes | Yes |
| FR | SWIFT | Yes | Yes | Yes | Yes |
| GR | SWIFT | Yes | Yes | Yes | Yes |
| GT | SWIFT | Yes | Yes | Yes | Yes |
| HR | SWIFT | Yes | Yes | Yes | Yes |
| HU | SWIFT | Yes | Yes | Yes | Yes |
| IE | SWIFT | Yes | Yes | Yes | Yes |
| IL | SWIFT | Yes | Yes | Yes | Yes |
| IT | SWIFT | Yes | Yes | Yes | Yes |
| JO | SWIFT | Yes | Yes | Yes | Yes |
| KW | SWIFT | Yes | Yes | Yes | Yes |
| KZ | SWIFT | Yes | Yes | Yes | Yes |
| LB | SWIFT | Yes | Yes | Yes | Yes |
| LI | SWIFT | Yes | Yes | Yes | Yes |
| LT | SWIFT | Yes | Yes | Yes | Yes |
| LU | SWIFT | Yes | Yes | Yes | Yes |
| LV | SWIFT | Yes | Yes | Yes | Yes |
| MC | SWIFT | Yes | Yes | Yes | Yes |
| MT | SWIFT | Yes | Yes | Yes | Yes |
| MU | SWIFT | Yes | Yes | Yes | Yes |
| MZ | SWIFT | Yes | Yes | Yes | Yes |
| NL | SWIFT | Yes | Yes | Yes | Yes |
| NO | SWIFT | Yes | Yes | Yes | Yes |
| OM | SWIFT | Yes | Yes | Yes | Yes |
| PK | SWIFT | Yes | Yes | Yes | Yes |
| PL | SWIFT | Yes | Yes | Yes | Yes |
| PT | SWIFT | Yes | Yes | Yes | Yes |
| QA | SWIFT | Yes | Yes | Yes | Yes |
| RO | SWIFT | Yes | Yes | Yes | Yes |
| RS | SWIFT | Yes | Yes | Yes | Yes |
| SA | SWIFT | Yes | Yes | Yes | Yes |
| SE | SWIFT | Yes | Yes | Yes | Yes |
| SI | SWIFT | Yes | Yes | Yes | Yes |
| SK | SWIFT | Yes | Yes | Yes | Yes |
| TN | SWIFT | Yes | Yes | Yes | Yes |
| TR | SWIFT | Yes | Yes | Yes | Yes |
| UA | SWIFT | Yes | Yes | Yes | Yes |

---

**SWIFT Transaction Requirements** <br /><br />
**GB – United Kingdom, MY – Malaysia, ZM – Zambia**

For the countries listed above, when transactions are processed through the SWIFT network, the following bank-related fields are mandatory for successful transaction processing:

- businessBankName, receiverBankName – used to capture bank name details
- businessAccountNumber, receiverAccountNumber – used to capture bank account number details
- businessSwiftCode, receiverSwiftCode – used to capture SWIFT code details
- businessBankCode, receiverBankCode – used to capture bank sort code details
- businessAccountHolderName, receiverAccountHolderName – used to capture beneficiary name details

In the table below, the column headers represent the applicable API field requirements for both business and customer contexts.

:::note

Note: “YES” indicates that the field is mandatory and accepts the value/information specified above. If a different value/information is accepted, it is explicitly mentioned in the table. “NO” indicates that it is optional.

:::

| Country | RAIL | businessBankName, receiverBankName | businessAccountNumber, receiverAccountNumber | businessSwiftCode, receiverSwiftCode | businessBankCode, receiverBankCode | businessAccountHolderName, receiverAccountHolderName |
|---|---|---|---|---|---|---|
| GB | SWIFT | Yes | Yes | Yes | Yes | Yes |
| MY | SWIFT | Yes | Yes | Yes | Yes | Yes |
| ZM | SWIFT | Yes | Yes | Yes | Yes | Yes |

---

**SWIFT Transaction Requirements** <br /><br />
**LK – Sri Lanka, MA – Morocco, TT – Trinidad and Tobago**

For the countries listed above, when transactions are processed through the SWIFT network, the following bank-related fields are mandatory for successful transaction processing:

- businessBankName, receiverBankName – used to capture bank name details
- businessAccountNumber, receiverAccountNumber – used to capture bank account number details
- businessSwiftCode, receiverSwiftCode – used to capture SWIFT code details
- businessBankCode, receiverBankCode – used to capture bank code details
- businessBankCountry, receiverBankCountry – used to capture branch code details
- businessAccountHolderName, receiverAccountHolderName – used to capture beneficiary name details

In the table below, the column headers represent the applicable API field requirements for both business and customer contexts.

:::note

Note: “YES” indicates that the field is mandatory and accepts the value/information specified above. If a different value/information is accepted, it is explicitly mentioned in the table. “NO” indicates that it is optional.

:::

| Country | RAIL | businessBankName, receiverBankName | businessAccountNumber, receiverAccountNumber | businessSwiftCode, receiverSwiftCode | businessBankCode, receiverBankCode | businessBankCountry, receiverBankCountry | businessAccountHolderName, receiverAccountHolderName |
|---|---|---|---|---|---|---|---|
| LK | SWIFT | Yes | Yes | Yes | Yes | Yes | Yes |
| MA | SWIFT | Yes | Yes | Yes | Yes | Yes | Yes |
| TT | SWIFT | Yes | Yes | Yes | Yes | Yes | Yes |

---

**SWIFT Transaction Requirements** <br /><br />
**CN – China, HK – Hong Kong, TW – Taiwan**

For the countries listed above, when transactions are processed through the SWIFT network, the following bank-related fields are mandatory for successful transaction processing:

- businessAccountHolderName, receiverAccountHolderName – used to capture beneficiary name details
- businessBankName, receiverBankName – used to capture bank name details
- businessAccountNumber, receiverAccountNumber – used to capture bank account number details
- businessSwiftCode, receiverSwiftCode – used to capture SWIFT code details

In the table below, the column headers represent the applicable API field requirements for both business and customer contexts.

:::note

Note: “YES” indicates that the field is mandatory and accepts the value/information specified above. If a different value/information is accepted, it is explicitly mentioned in the table. “NO” indicates that it is optional.

:::

| Country | RAIL | businessAccountHolderName, receiverAccountHolderName | businessBankName, receiverBankName | businessAccountNumber, receiverAccountNumber | businessSwiftCode, receiverSwiftCode |
|---|---|---|---|---|---|
| CN | SWIFT | Yes | Yes | Yes | Yes |
| HK | SWIFT | Yes | Yes | Yes | Yes |
| TW | SWIFT | Yes | Yes | Yes | Yes |

---

**SWIFT Transaction Requirements** <br /><br />
**AM – Armenia, BD – Bangladesh**

For the countries listed above, when transactions are processed through the SWIFT network, the following bank-related fields are mandatory for successful transaction processing:

- businessBankName, receiverBankName – used to capture bank name details
- businessAccountNumber, receiverAccountNumber – used to capture bank account number details
- businessSwiftCode, receiverSwiftCode – used to capture SWIFT code details
- businessBankCode, receiverBankCode – used to capture bank code details
- businessAccountHolderName, receiverAccountHolderName – used to capture beneficiary name details

In the table below, the column headers represent the applicable API field requirements for both business and customer contexts.

:::note

Note: “YES” indicates that the field is mandatory and accepts the value/information specified above. If a different value/information is accepted, it is explicitly mentioned in the table. “NO” indicates that it is optional.

:::

| Country | RAIL | businessBankName, receiverBankName | businessAccountNumber, receiverAccountNumber | businessSwiftCode, receiverSwiftCode | businessBankCode, receiverBankCode | businessAccountHolderName, receiverAccountHolderName |
|---|---|---|---|---|---|---|
| AM | SWIFT | Yes | Yes | Yes | Yes | Yes |
| BD | SWIFT | Yes | Yes | Yes | Yes | Yes |

---

**SWIFT Transaction Requirements** <br /><br />
**DO – Dominican Republic, UY – Uruguay**

For the countries listed above, when transactions are processed through the SWIFT network, the following bank-related fields are mandatory for successful transaction processing:

- businessBankName, receiverBankName – used to capture bank name details
- businessAccountNumber, receiverAccountNumber – used to capture bank account number details
- businessSwiftCode, receiverSwiftCode – used to capture SWIFT code details
- businessAccountType, receiverAccountType – used to capture account type details
- businessAccountHolderName, receiverAccountHolderName – used to capture beneficiary name details

In the table below, the column headers represent the applicable API field requirements for both business and customer contexts.

:::note

Note: “YES” indicates that the field is mandatory and accepts the value/information specified above. If a different value/information is accepted, it is explicitly mentioned in the table. “NO” indicates that it is optional.

:::

| Country | RAIL | businessBankName, receiverBankName | businessAccountNumber, receiverAccountNumber | businessSwiftCode, receiverSwiftCode | businessAccountType, receiverAccountType | businessAccountHolderName, receiverAccountHolderName |
|---|---|---|---|---|---|---|
| DO | SWIFT | Yes | Yes | Yes | Yes | Yes |
| UY | SWIFT | Yes | Yes | Yes | Yes | Yes |

---

**SWIFT Transaction Requirements** <br /><br />
**AU – Australia, BR – Brazil, CA – Canada, CL – Chile, EG – Egypt, ID – Indonesia, IN – India,** <br />
**IS – Iceland, MX – Mexico, PH – Philippines, SG – Singapore, US – United States**

For the countries listed above, when transactions are processed through the SWIFT network, the following bank-related fields are mandatory for successful transaction processing:

- businessBankName, receiverBankName – used for Bank name details
- businessAccountNumber, receiverAccountNumber – used for Bank Account Number details
- businessSwiftCode, receiverSwiftCode – used for Swift Code details
- businessBankCountry, receiverBankCountry – used to capture branch code details
- businessBankCode, receiverBankCode – used to capture bank code/ IFSC/ BSB NO/ Routing no details based on country
- businessAccountType, receiverAccountType – used to capture account type details
- businessAccountHolderName, receiverAccountHolderName – used to capture beneficiary name details

In the table below, the column headers represent the applicable API field requirements for both business and customer contexts.

:::note

Note: “YES” indicates that the field is mandatory and accepts the value/information specified above. If a different value/information is accepted, it is explicitly mentioned in the table. “NO” indicates that it is optional.

:::

| Country | RAIL | businessBankName, receiverBankName | businessAccountNumber, receiverAccountNumber | businessSwiftCode, receiverSwiftCode | businessBankCountry, receiverBankCountry | businessBankCode, receiverBankCode | businessAccountType, receiverAccountType | businessAccountHolderName, receiverAccountHolderName |
|---|---|---|---|---|---|---|---|---|
| AU | SWIFT | Yes | Yes | Yes | No | Yes used for bsb no | No | Yes |
| BR | SWIFT | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| CA | SWIFT | Yes | Yes | Yes | No | Yes used for transitCode | No | Yes |
| CL | SWIFT | Yes | Yes | Yes | No | No | No | Yes |
| EG | SWIFT | Yes | Yes | Yes | No | No | No | Yes |
| ID | SWIFT | Yes | Yes | Yes | Yes | Yes | No | Yes |
| IN | SWIFT | Yes | Yes | Yes | No | Yes used for IFSC code | No | Yes |
| IS | SWIFT | Yes | Yes | Yes | No | No | No | Yes |
| MX | SWIFT | Yes | Yes (used for CLABE / Mexican bank account number) | Yes | No | No | No | Yes |
| PH | SWIFT | Yes | Yes | Yes | No | Yes used for routing no | Yes | Yes |
| SG | SWIFT | Yes | Yes | Yes | Yes | Yes | No | Yes |
| US | SWIFT | Yes | Yes | Yes | No | Yes used for routing no | No | Yes |

<br />

## Related

- [Payout](/docs/payout/payout)
- [Currency validations (LOCAL rail)](/docs/validation/currency-validations)
