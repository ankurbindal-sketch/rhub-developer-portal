---
title: "Authentication"
sidebar_label: "Authentication"
slug: "/authentication/authentication"
description: "RHUB Login (Authentication) API — obtain an access token."
---

# Authentication

<span className="rhub-method rhub-method--post">POST</span>

Authenticate and obtain the access token that every other RHUB API call requires.

:::info[Using the access token]

Send the token on subsequent API calls in the `Authorization` header:

```http
Authorization: Bearer <access_token>
```

The response also returns `token_type`, `expires_in` and `scope`.

:::

:::note[`scope` is a response field]

Clients do not need to send `scope` on the token request. The historical request example
below includes `scope=read%20write`; it is reproduced unchanged, but it is not a required
request parameter. `scope` is returned in the response.

:::

## Contract

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--post">POST</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/oauth/token'}</code>
  </div>
</div>

The Login API is used to authenticate and authorize the user.

## Request Parameter

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| grant_type | Alphanumeric | 08 | M | password |
| username | Alphanumeric | 10 | M | The user ID or username. |
| password | Alphanumeric (Encrypted) | 0 - 128 | M | Password in unreadable/hashed format |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Header Parameter

| Parameters | Input Type | Length | Requirement | Description |
|---|---|---|---|---|
| channel | Alpha | 03 | M | WEB |
| source | Alpha | 05 | M | AGENT |
| Accept-Language | Alpha | 02 | M | en |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Request Details

```http
POST /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
POST http://host/ewallet/oauth/token
FormData : grant_type=password&scope=read%20write&username=1000008340
password : 21ED0D51*****FB437*****8ED2123B6
```

## Response Parameter

| Parameters     | Data Type  | Requirement | Description |
|----------|:-----:|:------------:|--------|
| access_token | String | M | Token to identify and authorize the user. |
| token_type | String | M | Type of the access token. |
| expires_in | String | M | Duration of time in seconds within which the access token expires. |
| scope | String | M |  |
| clientCode | String | M |  |
| locale | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

## Response Details

```json
{
"access_token": "15*****f-54fe-43d9-***7-b7dc****1b9",
"token_type": "bearer",
"expires_in": 21150,
"scope": "read write trust",
"clientCode": "1000008483",
"locale": "en"
}
```

## Related APIs

- [Quotation](/docs/quotation/quotation)
- [Payout](/docs/payout/payout)
- [Integration flow](/docs/getting-started/integration-flow)
