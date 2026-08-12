---
title: "Account Type"
sidebar_label: "Account Type"
description: "RHUB Account Type master API."
---

# Account Type

<span className="rhub-method rhub-method--get">GET</span>

[Go To Payout](/docs/payout/payout#transactioninfo-req-param)

:::info[Endpoint]

`GET`  `http://host/ewallet/api/v1/accountType/all`

:::

The Account Type API is used to fetch the type of the account.

## Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/accountType/all
```

## Response Parameter

| Parameters        |       Data Type | Requirement | Description                                                                 |
|-------------------|:----------------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | Unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **accountTypeList** |  |  |  |
| code | String | M | Code representing the account type to be used for the payout. eg: 100000,100001 |
| type | String | M | Value representing the account type. eg: Current, Saving |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"transactionId": "10992372",
"requestTime": "Wed May 17 12:45:00 IST 2023",
"responseTime": "Wed May 17 12:45:25 IST 2023",
"resultCode": "0",
"resultDescription": "Transaction Successful",
"accountTypeList": [
    {
        "id": 2,
        "code": "100001",
        "typeFr": "Business account",
        "type": "Current",
        "status": "Active",
        "creationDate": "2020-08-25T11:43:31.960+0530"
    },
    {
        "id": 1,
        "code": "100000",
        "typeFr": "Client money account",
        "type": "Saving",
        "status": "Active",
        "creationDate": "2020-08-25T11:43:11.555+0530"
    }
]
}
```

## Related APIs

- [All master APIs](/docs/master-apis)
- [Payout](/docs/payout/payout)
- [Customer Registration](/docs/customers/customer-registration)
