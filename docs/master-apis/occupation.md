---
title: "Occupation"
sidebar_label: "Occupation"
description: "RHUB Occupation master API."
---

# Occupation

<span className="rhub-method rhub-method--get">GET</span>

[Go To Payout](/docs/payout/payout#transactioninfo-req-param)
[Go To WPT](/docs/payout/wpt-payout#transactioninfo-req-param)

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/getOccupation/RHUB/{transactionType}'}</code>
  </div>
</div>

The Occupation API is used to fetch the occupation.

## Request Parameter

| Parameters | Input Type | Length  | Requirement | Description            |
|------------|:-------------:|:------------:|:------------:|------------------------|
| transactionType | Alphanumeric | 03 | M | The harmonized Transaction Type. Fixed default value B2C, B2B, C2C, C2B. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/getOccupation/RHUB/C2C
```

## Response Parameter

| Parameters        |        Data Type | Requirement | Description                                                                 |
|-------------------|:------------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day mm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | Unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Result** |  |  |  |
| Result - data | String | M |  |
| Result - value | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"requestTime": "Tue Jan 28 16:35:55 IST 2025",
"responseTime": "Tue Jan 28 16:35:55 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"result": [
    {
        "data": "RHO062",
        "value": "Technician"
    },
    {
        "data": "RHO061",
        "value": "Teacher"
    },
    {
        "data": "RHO060",
        "value": "Tailor"
    },
    {
        "data": "RHO059",
        "value": "Surveyor"
    },
    {
        "data": "RHO058",
        "value": "Supervisor"
    },
    {
        "data": "RHO057",
        "value": "Software developer"
    },
    {
        "data": "RHO056",
        "value": "Social workers"
    },
    {
        "data": "RHO055",
        "value": "Security Officer"
    },
    {
        "data": "RHO054",
        "value": "Secretary"
    },
    {
        "data": "RHO053",
        "value": "Scientist"
    },
    {
        "data": "RHO052",
        "value": "Salesman"
    },
    {
        "data": "RHO051",
        "value": "Retired"
    },
    {
        "data": "RHO050",
        "value": "Researcher / Scientist"
    },
    {
        "data": "RHO049",
        "value": "Receptionist"
    },
    {
        "data": "RHO048",
        "value": "Waiter/Waitress"
    },
    {
        "data": "RHO047",
        "value": "Travel agent"
    },
    {
        "data": "RHO046",
        "value": "Real estate agent"
    },
    {
        "data": "RHO045",
        "value": "Police Officer"
    },
    {
        "data": "RHO044",
        "value": "Plumber"
    },
    {
        "data": "RHO043",
        "value": "Pilot"
    },
    {
        "data": "RHO042",
        "value": "Physician"
    },
    {
        "data": "RHO041",
        "value": "Pharmacist"
    },
    {
        "data": "RHO040",
        "value": "Officer"
    },
    {
        "data": "RHO039",
        "value": "Office Boy / Peon"
    },
    {
        "data": "RHO038",
        "value": "Nurses"
    },
    {
        "data": "RHO037",
        "value": "Musician"
    },
    {
        "data": "RHO036",
        "value": "Mechanic"
    },
    {
        "data": "RHO035",
        "value": "Manager"
    },
    {
        "data": "RHO034",
        "value": "Librarian"
    },
    {
        "data": "RHO033",
        "value": "Lawyer"
    },
    {
        "data": "RHO032",
        "value": "Labourer"
    },
    {
        "data": "RHO031",
        "value": "Judge"
    },
    {
        "data": "RHO030",
        "value": "Journalist"
    },
    {
        "data": "RHO029",
        "value": "HOUSEKEEPING"
    },
    {
        "data": "RHO028",
        "value": "House Maid"
    },
    {
        "data": "RHO027",
        "value": "Government worker"
    },
    {
        "data": "RHO026",
        "value": "Gardener"
    },
    {
        "data": "RHO025",
        "value": "Fisherman"
    },
    {
        "data": "RHO024",
        "value": "Factory worker"
    },
    {
        "data": "RHO023",
        "value": "Engineer"
    },
    {
        "data": "RHO022",
        "value": "Electrician"
    },
    {
        "data": "RHO021",
        "value": "Driver"
    },
    {
        "data": "RHO020",
        "value": "Doctor"
    },
    {
        "data": "RHO019",
        "value": "Designer"
    },
    {
        "data": "RHO018",
        "value": "Dentist"
    },
    {
        "data": "RHO017",
        "value": "Customer Service Executive"
    },
    {
        "data": "RHO016",
        "value": "Cook"
    },
    {
        "data": "RHO015",
        "value": "Consultant"
    },
    {
        "data": "RHO014",
        "value": "Clerk"
    },
    {
        "data": "RHO013",
        "value": "Chef"
    },
    {
        "data": "RHO012",
        "value": "Chartered Accountant"
    },
    {
        "data": "RHO011",
        "value": "Cashier"
    },
    {
        "data": "RHO010",
        "value": "Carpenter"
    },
    {
        "data": "RHO009",
        "value": "Butcher"
    },
    {
        "data": "RHO008",
        "value": "Broker"
    },
    {
        "data": "RHO007",
        "value": "BPO"
    },
    {
        "data": "RHO006",
        "value": "Auditor"
    },
    {
        "data": "RHO005",
        "value": "Assistant"
    },
    {
        "data": "RHO004",
        "value": "Artist"
    },
    {
        "data": "RHO003",
        "value": "Architect"
    },
    {
        "data": "RHO002",
        "value": "Actor / Actress"
    },
    {
        "data": "RHO001",
        "value": "Accountant"
    }
]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
