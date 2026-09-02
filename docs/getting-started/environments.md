---
title: "API environments"
sidebar_label: "API environments"
description: "RHUB Sandbox and Production API base URLs and how authentication applies to both."
---

# API environments

RHUB exposes two API environments. Both use the same request and response contracts; only
the base URL and your credentials differ.

| Environment | Base URL |
|---|---|
| Sandbox | `https://sandbox-api.remittanceshub.com` |
| Production | `https://api.remittanceshub.com` |

Prefix the documented paths with the base URL of the environment you are integrating
against. For example, `POST /ewallet/oauth/token` against Sandbox is
`https://sandbox-api.remittanceshub.com/ewallet/oauth/token`.

## Authentication

Both environments use the same mechanism: obtain an access token from the
[Authentication API](/docs/authentication/authentication) and send it on every subsequent
call.

```http
Authorization: Bearer <access_token>
```

## Credentials and client configuration

Environment-specific credentials and client configuration — including your client code —
are supplied through RHUB onboarding. Sandbox credentials are not valid in Production.

:::note[Endpoint paths in this reference]

Some contract pages write their path as `http://host/ewallet/api/v1/...`, where `host`
stands for the base URL of your environment. Substitute the Sandbox or Production base URL
above. The paths themselves are reproduced exactly as RHUB documents them.

:::

## Related

- [Authentication](/docs/authentication/authentication)
- [How to read this reference](/docs/getting-started/conventions)
- [Integration flow](/docs/getting-started/integration-flow)
