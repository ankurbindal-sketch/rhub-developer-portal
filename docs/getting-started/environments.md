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
| Sandbox | `https://sandbox-client.remittanceshub.com:8130` |
| Production | `https://prod-api.remittanceshub.com:9091` |

## Resolving an endpoint

Every endpoint in this reference is documented as a path. Append the path to the base URL of
the environment you are integrating against. For
[Authentication](/docs/authentication/authentication), `POST /ewallet/oauth/token` resolves
to:

```http
POST https://sandbox-client.remittanceshub.com:8130/ewallet/oauth/token
```

```http
POST https://prod-api.remittanceshub.com:9091/ewallet/oauth/token
```

Each contract page shows both resolved URLs beneath its endpoint path, so you can copy the
one you need. Request samples on those pages use the Sandbox base URL; substitute the
Production base URL when you move over.

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

## Related

- [Authentication](/docs/authentication/authentication)
- [How to read this reference](/docs/getting-started/conventions)
- [Integration flow](/docs/getting-started/integration-flow)
- [API index](/docs/api-index)
