---
title: "Login (Authentication) API"
sidebar_label: "Login (Authentication) API"
description: "RHUB Login (Authentication) API (source page not linked in the live documentation sidebar)."
---

# Login (Authentication) API

<span className="rhub-method rhub-method--post">POST</span>

:::warning[Publication status — REVIEW REQUIRED]

This page is reproduced from the source file `loginauthentication.md`, which **is present in the RHUB
documentation source but is commented out of the live documentation sidebar**. The
source therefore does not establish whether this contract is current, superseded or
withdrawn. Treat it as reference material and confirm with RHUB before integrating.

:::

:::info[Endpoint]

`POST`  `https://sandbox-client.remittanceshub.com:8030/ewallet/oauth/token`

:::

The Login API is used to authenticate and authorize the user.

## Request Parameter

| Parameters     | Data Type | Requirement | Description |
|----------|:-----:|:-----------:|--------|
| grant_type | String | M | URL parameter |
| scope | String | M | It is the read and write access to the endpoints |
| username | String | M | The user ID or username |
| password | String | M | The password in unreadable format |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Header Parameter
| Parameters     | Data Type  | Requirement | Description |
|----------|:------------:|:-----:|--------|
| authorization | String | M | URL parameter |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST https://sandbox-client.remittanceshub.com:8030/ewallet/oauth/token
FormData : grant_type=password&scope=read%20write&username=1000008340
password=21ED0D51B012DFB4375AB9A8ED2123B6
```

  ## Response Parameter

| Parameters     | Data Type  | Requirement | Description |
|----------|:-----:|:------------:|--------|
| access_token | String | M | Token to identify and authorize the user. |
| token_type | String | M | Type of the access token. |
| expires_in | String | M | Duration of time in seconds within which the access token expires. |
| scope | String | M |  |
| userCountryCode | String | M |  |
| userCode | String | M |  |
| firstLoginStatus | String | M |  |
| walletOwnerCode | String | M |  |
| username | String | M | The user ID or username. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
  {
"access_token": "ebf44678-d205-42ac-9dae-2bdea2fbdca5",
"token_type": "bearer",
"expires_in": 43199,
"scope": "read write",
"timeZone": "(UTC+02:00)",
"userCountryCode": "100132",
"userCode": "105432",
"firstLoginStatus": "N",
"walletOwnerCode": "1000008340",
"username": "Abdou1495",
}
```

## Related APIs

- [Unlinked source pages overview](/docs/legacy)
- [Source coverage notes](/docs/appendix/source-notes)
