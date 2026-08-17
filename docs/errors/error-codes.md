---
title: "Error codes"
sidebar_label: "HTTP and application error codes"
description: "RHUB HTTP status codes and application error codes."
unlisted: true
---

# Error codes

## HTTP Error Codes
HTTP Status Codes

| Status Code | Category | Description |
|---|---|---|
| 100 | Informational | Continue – Request received, continue processing. |
| 101 | Informational | Switching Protocols – Server switching protocols. |
| 200 | Success | OK – Request successful. |
| 201 | Success | Created – Resource created successfully. |
| 204 | Success | No Content – Success with no response body. |
| 301 | Redirection | Moved Permanently – Resource moved to new URL. |
| 302 | Redirection | Found – Temporary redirection. |
| 400 | Client Error | Bad Request – Invalid request format. |
| 401 | Client Error | Unauthorized – Authentication required. |
| 403 | Client Error | Forbidden – Access denied. |
| 404 | Client Error | Not Found – Resource does not exist. |
| 429 | Client Error | Too Many Requests – Rate limit exceeded. |
| 500 | Server Error | Internal Server Error – Generic failure. |
| 502 | Server Error | Bad Gateway – Invalid upstream response. |
| 503 | Server Error | Service Unavailable – Server temporarily unavailable. |
| 504 | Server Error | Gateway Timeout – Upstream timeout. |

<br />

## Application Error Codes
| Result Code | Result Description | Details |
|---|---|---|
| 0 | transaction.successful | Transaction completed successfully. |
| 00 | transaction.successful | Transaction completed successfully. |
| 000 | user.is.active | User account is active and operational. |
| 100 | in.progress | Transaction is currently being processed. |
| 1000 | technical.failure | A system or technical error occurred. |
| 1001 | processor.not.found | Requested processor configuration not found. |
| 1002 | schema.not.found | Required schema definition is missing. |
| 1003 | connection.not.found | Unable to locate required connection. |
| 1005 | host.not.found | Target host/server could not be reached. |
| 1006 | invalid.service.provider | Service provider information is invalid. |
| 1007 | adapter.not.available | Requested adapter service is unavailable. |
| 1008 | rrn.not.found | Retrieval Reference Number not found. |
| 1014 | switch.connection.time.out | Connection to switch timed out. |
| 1015 | record.not.found | Requested record does not exist. |
| 1091 | mobile.number.not.found | Mobile number not registered in system. |
| 1092 | invalid.mobile.number | Provided mobile number format is invalid. |
| 1098 | database.connection.error | Database connectivity issue occurred. |
| 1141 | encryption.error | Error occurred during encryption process. |
| 1142 | invalid.message.type | Message type provided is invalid. |
| 1143 | invalid.xml.format | XML format is malformed or invalid. |
| 1144 | invalid.activation.code | Activation code entered is incorrect. |
| 1145 | invalid.pin | Entered PIN is incorrect. |
| 1146 | inactive.device | Device is inactive and cannot process requests. |
| 1147 | inactive.merchant | Merchant account is inactive. |
| 1148 | device.not.exist | Specified device does not exist. |
| 1149 | merchant.not.exist | Merchant record not found. |
| 1150 | no.of.activation.attempts.exceeded | Maximum activation attempts exceeded. |
| 1151 | no.of.pin.attempts.exceeded | Maximum PIN attempts exceeded. |
| 1152 | already.active.device | Device is already activated. |
| 1153 | invalid.secured.pin | Secured PIN validation failed. |
| 1154 | invalid.terminal.id | Terminal ID provided is invalid. |
| 1155 | invalid.serial.id | Serial ID is invalid. |
| 1156 | invalid.amount | Transaction amount is invalid. |
| 1157 | VOID.request.time.exceeded | Void request exceeded allowed time. |
| 1158 | refund.request.time.exceeded | Refund request exceeded allowed time. |
| 1170 | transaction.limit.amount.exceed | Transaction exceeds allowed amount limit. |
| 1171 | transaction.limit.number.exceed | Transaction exceeds allowed count limit. |
| 1172 | transaction.limit.total.amount.exceed | Total transaction amount limit exceeded. |
| 1173 | transaction.limit.odd.hours | Transaction not allowed during restricted hours. |
| 1201 | iso.packing.error | Error occurred while packing ISO message. |
| 1202 | iso.unpacking.error | Error occurred while unpacking ISO message. |
| 1203 | transaction.is.reversed | Transaction has been reversed. |
| 1204 | transaction.is.not.reversed | Transaction reversal not completed. |
| 1207 | switch.error | Switch system returned an error. |
| 1208 | your.PIN.have.been.expired | User PIN has expired. |
| 1215 | you.exceeded.otp.request.max.attempt | Maximum OTP request attempts exceeded. |
| 1216 | invalid.otp | Entered OTP is invalid. |
| 1220 | insufficient.balance | Account has insufficient balance. |
| 1223 | otp.has.expired | OTP has expired and is no longer valid. |
| 1248 | Loyality Points Less Then Min. Required | Loyalty points below minimum required threshold. |
| 1249 | Loyality Points Greater Then Max. Allowed | Loyalty points exceed maximum allowed limit. |
| 1251 | Unauthorised Device Or IP Address. | Access attempt from unauthorized device or IP. |
| 1311 | You 5 times Login attempt wrong password. Your UserId is blocked, Contact to Customer Care | User blocked after multiple failed login attempts. |
| 4126 | Password is Incorrect | Incorrect password entered. |
| 1389 | third.party.server.down | Third-party server is currently unavailable. |
| Result Code | Result Description | Details |
|---|---|---|
| 0 | transaction.successful | The request was processed successfully. |
| 00 | transaction.success | General success status for the transaction. |
| 000 | user.is.active | The user account is currently active and valid. |
| 100 | in.progress | Transaction is initiated and awaiting completion. |
| 1000 | technical.failure | A general system or internal server error occurred. |
| 1001 | processor.not.found | The specific payment processor is not configured. |
| 1002 | schema.not.found | The database or API schema definition is missing. |
| 1003 | connection.not.found | Unable to establish a connection to the requested service. |
| 10004 | invalid.license.API | The API license key is invalid or has expired. |
| 1005 | host.not.found | The destination server host could not be located. |
| 1014 | switch.connection.time.out | The connection to the network switch timed out. |
| 1098 | database.connection.error | Critical failure in connecting to the database. |
| 1141 | encryption.error | Failure during data encryption or decryption. |
| 1207 | switch.error | A generic error returned by the processing switch. |
| 1389 | third.party.server.down | The external third-party provider is unreachable. |
| 1015 | record.not.found | The requested data record does not exist. |
| 1016 | account.type.not.found | The specified account category was not found. |
| 1023 | channel.not.found | The requested transaction channel is not defined. |
| 1026 | country.not.found | The specified country code is not supported. |
| 1034 | exchange.rate.not.found | No currency exchange rate found for this pair. |
| 1037 | fee.template.not.found | The required fee calculation template is missing. |
| 1051 | service.provider.not.found | The selected service provider is not registered. |
| 1059 | user.not.found | The system could not find the specified user. |
| 1077 | wallet.not.found | The specific user wallet account does not exist. |
| 1082 | customer.not.found | The customer profile could not be retrieved. |
| 1087 | user.is.blocked | User access is restricted due to too many failed attempts. |
| 1088 | user.is.suspended | The user account has been temporarily suspended. |
| 1090 | user.is.inactive | The user account is disabled or not yet activated. |
| 1146 | inactive.device | The device used for the transaction is not active. |
| 1147 | inactive.merchant | The merchant account is currently disabled. |
| 1106 | walletOwner.already.exist | A profile for this wallet owner already exists. |
| 1107 | template.already.exist | A configuration template with this name already exists. |
| 1111 | user.already.exist | The username or ID is already registered. |
| 1120 | wallet.already.exist | A wallet for this user is already initialized. |
| 1136 | tax.configuration.already.exist | Tax settings for this category are already defined. |
| 1145 | invalid.pin | The personal identification number (PIN) is incorrect. |
| 1156 | invalid.amount | The transaction amount is invalid or zero. |
| 1170 | transaction.limit.amount.exceed | Transaction exceeds the maximum allowed amount. |
| 1171 | transaction.limit.number.exceed | User has reached the max number of daily transactions. |
| 1213 | transaction.amount.too.low | Amount is less than the minimum allowed value. |
| 1216 | invalid.otp | The One-Time Password provided is incorrect. |
| 1220 | insufficient.balance | Wallet balance is too low for this transaction. |
| 1223 | otp.has.expired | The OTP is no longer valid; a new one is required. |
| 1203 | transaction.is.reversed | The transaction has already been reversed. |
| 1208 | your.PIN.have.been.expired | The user's PIN must be changed before proceeding. |
| 1251 | Unauthorised Device Or IP Address | Request originated from an untrusted source. |
| 1311 | Login attempts exceeded | Account locked after 5 failed password attempts. |
| 4126 | Password is Incorrect | The password provided does not match our records. |

## Related

- [Current API error codes](/docs/errors/current-error-codes)
- [Transaction status codes](/docs/errors/transaction-status-codes)
- [Payout](/docs/payout/payout)
