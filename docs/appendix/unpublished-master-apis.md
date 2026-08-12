---
title: "Unpublished master APIs"
sidebar_label: "Unpublished master APIs"
description: "Master API sections that are commented out in the RHUB source."
unlisted: true
---

# Unpublished master APIs

:::warning[REVIEW REQUIRED — not published by the source]

Each section below is present in `master.md` **inside an HTML comment**, which means it is not rendered by the live RHUB documentation. The contracts are reproduced here verbatim so that no source content is lost, but the source does not establish whether they are current, forthcoming or withdrawn. Confirm with RHUB before using them.

:::

## Legal Status Code

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/customerLegalStatus/getByCustomerTypeCode/{code}'}</code>
  </div>
</div>

The Legal Status code Api of Business.

#### Request Parameter

| Parameters | Data Type | Requirement | Description            |
|------------|:-------------:|:------------:|------------------------|
| code | String | M | 100002 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/customerLegalStatus/getByCustomerTypeCode/100002
```

#### Response Parameter of Nature of Business

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **customerLegalStatusList** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the record, which will be passed where required. |  |
| customerTypeCode | String | M | Business customer type code. |  |
| name | String | M | The nature of the business run by the customer. |  |
| status | String | M | The status of the customer. |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details of Nature of Business

```json
{
"transactionId": "9217696",
"requestTime": "Tue Jan 28 16:15:34 IST 2025",
"responseTime": "Tue Jan 28 16:15:34 IST 2025",
"resultCode": "0",
"resultDescription": "Transaction successful",
"customerLegalStatusList": [
    {
        "id": 6,
        "code": "RHB001",
        "customerTypeCode": "100002",
        "name": "Partnership",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 13,
        "code": "RHB002",
        "customerTypeCode": "100002",
        "name": "Corporation",
        "status": "Active",
        "creationDate": "2025-03-19T17:23:54.415+0530"
    },
    {
        "id": 7,
        "code": "RHB003",
        "customerTypeCode": "100002",
        "name": "Proprietorship",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 8,
        "code": "RHB004",
        "customerTypeCode": "100002",
        "name": "Govt. Entity",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 9,
        "code": "RHB005",
        "customerTypeCode": "100002",
        "name": "Private ltd",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 11,
        "code": "RHB006",
        "customerTypeCode": "100002",
        "name": "WLL",
        "status": "Active",
        "creationDate": "2025-03-19T17:23:54.415+0530"
    },
    {
        "id": 12,
        "code": "RHB007",
        "customerTypeCode": "100002",
        "name": "BSC",
        "status": "Active",
        "creationDate": "2025-03-19T17:23:54.415+0530"
    }
]
}
```

## Payment Mode

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/api/v1/getPaymentMode/paymentmode'}</code>
  </div>
</div>

The Payment Mode API is used to fetch the mode of payment.

#### Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/api/v1/getPaymentMode/paymentmode
```

#### Response Parameter

| Parameters        |        Data Type | Requirement | Description                                                                 |
|-------------------|:-------------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | The unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Result** |  |  |  |
| Result - data | String | M |  |
| Result - value | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details

```json
{
"requestTime": "Wed May 17 12:45:00 IST 2023",
"responseTime": "Wed May 17 12:45:25 IST 2023",
"resultCode": "0",
"resultDescription": "Transaction Successful",
"result": [
 {
        "data": "Cash/Wallet",
        "value": "Cash"
    },
    {
        "data": "Bank Transfer",
        "value": "Bank"
    },
    {
        "data": "Cheque",
        "value": "Cheque"
    },
    {
        "data": "POS Pmts",
        "value": "POS"
    }
 ]
}
```

## Branch List

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/payoutbranchlist/{countryCode}/{bankCode}/{recieverCode}'}</code>
  </div>
</div>

The Branch API is used to fetch the list of the payout banks.

#### Request Parameter

| Parameters     | Input Type | Length | Requirement | Description      |
|----------------|:-------------:|:------------:|:------------:|:--------------:|
| countryCode | Alpha | 03 | M | The 3-digit country code. eg: BEL |
| bankCode | Alphanumeric | 01 - 20 | M | The code recieved from Bank List Api. |
| recieverCode | Numeric | 10 | M | The 10 digit code of the correspondent. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/payoutbranchlist/BEL/UTIB/1000008396
```

#### Response Parameter

| Parameters        |       Data Type | Requirement | Description                                                                 |
|-------------------|:-------------:|:------------:|-------------------------------------------------------------------------------|
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | The unique code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Result** |  |  |  |
| Result - data | String | M |  |
| Result - value | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details

```json
{
"transactionId": "7559853",
"requestTime": "Thu Aug 03 12:16:21 IST 2023",
"responseTime": "Thu Aug 03 12:16:21 IST 2023",
"resultCode": "0",
"resultDescription": "Transaction Successful",
"branchList": [
{
"code": "\\599\\",
"name": "\\AZAMINO BRANCH\\"
},
{
"code": "\\710\\",
"name": "\\IWAKI BRANCH\\"
},
{
"code": "\\759\\",
"name": "\\SAITAMASHINTOSHIN\\"
},
{
"code": "\\589\\",
"name": "\\SENGENDAI BRANCH\\"
},
{
"code": "\\738\\",
"name": "\\TAMAPURA-ZA BRANCH\\"
},
{
"code": "\\697\\",
"name": "\\TSUKUBA BRANCH\\"
},
{
"code": "\\262\\",
"name": "\\HIBARIGAOKA BRANCH\\"
},
{
"code": "\\626\\",
"name": "\\FUJIMINO BRANCH\\"
},
{
"code": "\\985\\",
"name": "\\MIZUHOSHIYOUKEN BRANCH\\"
},
{
"code": "\\305\\",
"name": "\\WARABI BRANCH\\"
},
{
"code": "\\692\\",
"name": "\\AKEBI BRANCH\\"
},
{
"code": "\\560\\",
"name": "\\INTA-NETSUTO BRANCH\\"
},
{
"code": "\\988\\",
"name": "\\KAGOME BRANCH\\"
},
{
"code": "\\609\\",
"name": "\\KINMOKUSEI BRANCH\\"
},
{
"code": "\\640\\",
"name": "\\KUNUGI BRANCH\\"
},
{
"code": "\\555\\",
"name": "\\SAZANKA BRANCH\\"
},
{
"code": "\\553\\",
"name": "\\SATSUKI BRANCH\\"
},
]
}
```

## Customer Type

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/customerType/{parameter}'}</code>
  </div>
</div>

The Customer Type API is used to fetch all types of the customer.

#### Request Parameter of all Customers

| Parameters | Data Type | Requirement | Description                      |
|------------|:------------:|:------------:|----------------------------------|
| all | String | O | To fetch all types of customers. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details of all Customers

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http://host/api/v1/customerType/all
```

#### Response Parameter of all Customers

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Customer Type List** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the record, which will be passed where required. |  |
| name | String | M | Type of the customer. |  |
| short_name | String | M | The initials of the type of the customer. |  |
| status | String | M | The status of the customer. |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details of all Customers

```json
{
"transactionId": "8301002",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"customerTypeList": [
{
"id": 1,
"code": "100001",
"name": "Individual",
"short_name": "I",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
},
{
"id": 2,
"code": "100002",
"name": "Business",
"short_name": "B",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
}
]
}
```

## Resident Status

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/residenceStatus/customerTypeCode/{customerTypeCode}'}</code>
  </div>
</div>

The Resident Status API is used to fetch all types of the resident status.

#### Request Parameter of all Resident Status

| Parameters | Data Type | Requirement | Description                                |
|------------|:--------------:|:------------:|--------------------------------------------|
| customerTypeCode | String | M | Individual customer : 100001, Business customer : 100002 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details of all Resident Status

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http://host/ewallet/api/v1/residenceStatus/customerTypeCode/100001
```

#### Response Parameter of all Resident Status

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction, for successful transaction it will be "0" |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Residence Status List** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the record, which will be passed where required. |  |
| name | String | M | The name of the resident status. |  |
| status | String | M | The status of the customer. |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details of Individual Cus. Resident Status

```json
{"transactionId": "8301012 ",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"residenceStatusList": [
{
"id": 1,
"code": "100001",
"name": "National",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
},
{
"id": 2,
"code": "100002",
"name": "Resident",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
}
{
"id": 3,
"code": "100001",
"name": "Visitor",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
},
]
}
```

#### Response Details of Business Cus. Resident Status

```json
{"transactionId": "8301012 ",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"residenceStatusList": [
  {
        "id": 4,
        "code": "100006",
        "name": "Foreign Company",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 5,
        "code": "100007",
        "name": "Local Company ",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    }
]
}
```

## Purpose of Opening Business

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/purposeOfOpeningBusiness/getByCustomerTypeCode/{customerTypeCode}'}</code>
  </div>
</div>

The Purpose of Opening Business API is used to fetch the purpose of opening the business by the customer.

#### Request Parameter of the Purpose of Opening Business

| Parameters       | Data Type | Requirement | Description                          |
|------------------|:----------:|:----------:|--------------------------------------|
| customerTypeCode | String | M | The unique code of the customer type, for Business customer : 100002 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details of the Purpose of Opening Business

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET -
http://host/ewallet/api/v1/purposeOfOpeningBusiness/getByCustomerTypeCode/100002
```

#### Response Parameter of the Purpose of Opening Business

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Purpose of Opening Business** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of business purpose, which needs to be passed while customer registration process. |  |
| customerTypeCode | String | M | The unique code of the following. • Individual • Business |  |
| name | String | M | The purpose of opening the business by the customer. |  |
| status | String | M | The status of the record. note: Only records with status "Active" needs to be used |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details of the Purpose of Opening the Business

```json
{
"transactionId": "8301037",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"purposeOfOpeningBusinessList": [
 {
        "id": 3,
        "code": "100003",
        "customerTypeCode": "100002",
        "name": "International Remittance",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 4,
        "code": "100004",
        "customerTypeCode": "100002",
        "name": "Others",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    }
]
}
```

## Transaction Volume

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/businessTxnVolume/getByCustomerTypeCode/{customerTypeCode}'}</code>
  </div>
</div>

The Customer Sub Type API is used to fetch the transaction volume of the customer.

#### Request Parameter of Transaction Volume

| Parameters       | Data Type | Requirement | Description                          |
|------------------|:------:|:------------:|--------------------------------------|
| customerTypeCode | String | M | Individual:100001, Business:100002 |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details of Transaction Volume

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http://host/ewallet/api/v1/businessTxnVolume/getByCustomerTypeCode/100001
```

#### Response Parameter of Transaction Volume

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **BusinessTxnVolumeList** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the record, which will be passed where required. |  |
| customerTypeCode | String | M | The unique code of the following. • Individual • Business |  |
| name | String | M | The transaction volume of the business run by the customer. |  |
| status | String | M | The status of the customer. |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details of Individual Cus. Transaction Volume

```json
{
"transactionId": "8301045",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"businessTxnVolumeList": [
  {
        "id": 1,
        "code": "100001",
        "customerTypeCode": "100001",
        "name": "Less Than 10,000",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 2,
        "code": "100002",
        "customerTypeCode": "100001",
        "name": "Between 10,000 and 1,000,000",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 3,
        "code": "100003",
        "customerTypeCode": "100001",
        "name": "Greater Than 1,000,000",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    }
]
}
```

#### Response Details of Business Cus. Transaction Volume

```json
{
"transactionId": "8301045",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"businessTxnVolumeList": [
   {
        "id": 4,
        "code": "100004",
        "customerTypeCode": "100002",
        "name": "Less Than 10,000",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 5,
        "code": "100005",
        "customerTypeCode": "100002",
        "name": "Between 10,000 and 1,000,000",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    },
    {
        "id": 6,
        "code": "100006",
        "customerTypeCode": "100002",
        "name": "Greater Than 1,000,000",
        "status": "Active",
        "creationDate": "2024-04-15T00:00:00.000+0530"
    }
]
}
```

## ID Type

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__label">Of all customers</div>
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/api/v1/idType/{parameter}'}</code>
  </div>
  <div className="rhub-endpoint__label">Of a single customer</div>
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/api/v1/idType/getByCustomerTypeCode/{parameter}'}</code>
  </div>
</div>

The ID Type API is used to fetch the ID type of the customer.

#### Request Parameter of all ID Types

| Parameters | Data Type | Requirement | Description           |
|------------|:------------------:|:------------:|-----------------------|
| all | String | M | To fetch all ID types |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details of all ID Types

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http://host/api/v1/idType/all
```

#### Response Parameter of all ID Types

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **ID Type List** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the record, which will be passed where required. |  |
| customerTypeCode | String | M | The unique code of the following. • Individual • Business |  |
| name | String | M | The name of the ID type. |  |
| status | String | M | The status of the customer. |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details of all ID Types

```json
{
"transactionId": "8304103",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"idTypeList": [
{
"id": 1,
"code": "100001",
"customerTypeCode": "100001",
"name": "Pan",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
},
{
"id": 2,
"code": "100002",
"customerTypeCode": "100001",
"name": "Passport",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
},
{
"id": 3,
"code": "100003",
"customerTypeCode": "100001",
"name": "Adhar",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
},
]
}
```

#### Request Parameter of the Individual and Business ID Types

| Parameters       | Data Type | Requirement | Description                          |
|------------------|:------:|:------------:|--------------------------------------|
| customerTypeCode | String | M | The unique code of the customer type. (Individual : 100001, Business : 100002) |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details of ID Type of a Single Customer

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET - http://host/api/v1/idType/getByCustomerTypeCode/{customerTypeCode}
```

#### Response Parameter of the Individual and Business ID Types

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **ID Type List** |  |  |  |  |
| id | String | M | The serial number of the record. |  |
| code | String | M | The unique code of the record, which will be passed where required. |  |
| customerTypeCode | String | M | The unique code of the following. • Individual • Business |  |
| name | String | M | The name of the ID type. |  |
| status | String | M | The status of the customer. |  |
| creationDate | String | M | The creation date of the customer in the YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details of the Individual ID Type

```json
{
"transactionId": "8304122",
"requestTime": "Wed Apr 17 21:06:35 IST 2024",
"responseTime": "Wed Apr 17 21:06:36 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"idTypeList": [
{
"id": 1,
"code": "100001",
"customerTypeCode": "100001",
"name": "Pan",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
},
{
"id": 2,
"code": "100002",
"customerTypeCode": "100001",
"name": "Passport",
"status": "Active",
"creationDate": "2024-04-08T00:00:00.000+0530"
},
]
}
```

#### Response Details of the Business ID Type

```json
{
"transactionId": "8304719",
"requestTime": "Fri Apr 19 12:58:51 IST 2024",
"responseTime": "Fri Apr 19 12:58:52 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"idTypeList": [
{
"id": 6,
"code": "100006",
"customerTypeCode": "100002",
"name": "Pan",
"status": "Active",
"creationDate": "2024-04-18T00:00:00.000+0530"
},
{
"id": 7,
"code": "100007",
"customerTypeCode": "100002",
"name": "Passport",
"status": "Active",
"creationDate": "2024-04-18T00:00:00.000+0530"
},
]
}
```

## Customer Document Fetch

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/ewallet/api/v1/documentUpload/{senderCode}/{docReferenceNumber}'}</code>
  </div>
</div>

The Document Fetch API is used to fetch the details ID proof documents of the specific customer of the send client.

#### Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| senderCode | String | M | To unique code of the send partner. |
| docReference Number | String | M | To unique code of the ID proof document that is to be fetched. |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET -
http://host/ewallet/api/v1/documentUpload/1000008867?docReferenceNumber=CUS2C83P1A
```

#### Response Parameter

| Parameters | Data Type | Requirement | Description |  |
|---|---|---|---|---|
| transactionId | String | M |  |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| responseTime | String | M | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |  |
| resultCode | String | M | Unique code of the status of the transaction. |  |
| resultDescription | String | M | Description of the status of the transaction. |  |
| **Doc Upload List** |  |  |  |  |
| code | String | M |  |  |
| recieverCode | String | M | The unique code of the customer or wallet owner whose document is to be fetched. |  |
| docReferenceNumber | String | M | The unique code of the ID proof document to be fetched. |  |
| transId | String | M |  |  |
| fileName | String | M | The file name of the ID proof document to be fetched. |  |
| byteArr | String | M | The byte array used to store the binary data. |  |
| fileLocation | String | M | The location where the ID proof document is stored. |  |
| createdOn | String | M | The date and time when the ID proof document was uploaded. The date and time conforms the following format. YYYY-MM-DD &lt;Delimiter> HH:MM:SS.MS TIMEZONE |  |
| status | String | M | The status of the ID proof document. |  |
| createdBy | String | M | The unique code of the agent who uploaded the ID proof document of the customer or wallet owner. |  |
| source | String | M | The source who uploaded the ID proof document of the customer or wallet owner. |  |
| docTypeCode | String | M | The unique code of the ID proof document that was uploaded. |  |
| docTypeName | String | M | The name of the ID proof document that was uploaded. |  |
| sendClientName | String | M | The name of the send client under whom the customer is registered. |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details

```json
{
"transactionId": "8337502",
"requestTime": "Wed May 01 15:57:02 IST 2024",
"responseTime": "Wed May 01 15:57:02 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"docUploadList": [
{
"code": "100227",
"recieverCode": "1000008867",
"docReferenceNumber": "CUS2C83P1A",
"transId": "undefined",
"fileName": "file-example_PDF_500_kB_CUS2C83P1A_20240501155702.pdf",
"byteArr": null,
"fileLocation": "/opt/documentUpload/1000008867/CUS2C83P1A",
"createdOn": "2024-05-01T15:57:02.276+0530",
"status": "Active",
"createdBy": "105889",
"source": "AGENT",
"docTypeCode": "100001",
"docTypeName": "Drivers License",
"sendClientName": "Rahul Send Client"
}
]
}
```

## Payout Validator

`GET` — status: **REVIEW REQUIRED (commented out in source)**

<div className="rhub-endpoint">
  <div className="rhub-endpoint__row">
    <span className="rhub-method rhub-method--get">GET</span>
    <code className="rhub-endpoint__url">{'http://host/api/v1/payoutValidator/{recieverCode}/{serviceTypeCode}/{currency}/{userTypeCode}/{modeOfPayment}'}</code>
  </div>
</div>

The Pay Validator API is used to fetch the validator for the receiver.

#### Request Parameter

| Parameters | Data Type | Requirement | Description |
|---|---|---|---|
| recieverCode | String | M | Respective payout Client Code. eg: 1000001000 |
| serviceTypeCode | String | M | The following are the service types: • B2B • C2C • B2C • C2B • WPT |
| currency | String | M | 3-digit Currency Code e.g. INR |
| userTypeCode | String | M | Sender Code: 100000, Beneficiary code: 100001 |
| modeOfPayment | String | O | This is the requested would be: Bank, Cash, Wallet |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Request Details

```http
GET /services HTTP/1.0
HOST: XXX.XXX.XXX.XXX:Port
Content-Type: application/json; charset=utf-8
GET http://host/ewallet/api/v1/payoutValidator/1000008855/B2B/INR/100001
```

#### Response Parameter

| Parameters                     | Data Type  | Requirement | Description                                                                   |
|--------------------------------|:-----------:|:------------:|-------------------------------------------------------------------------------|
| transactionId | String | M |  |
| requestTime | String | M | This is the requested date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| responseTime |  |  | This is the response date and time in the Day Mmm DD HH:MM:SS TIMEZONE YYYY. |
| resultCode | String | M | The code of the status of the transaction. |
| resultDescription | String | M | Description of the status of the transaction. |
| **Payout Validator Response List** |  |  |  |
| id | String | M |  |
| partnerCode | String | M |  |
| serviceTypeCode | String | M |  |
| fieldName | String | M | Name of the business |
| currency | String | M | Payout currency |
| fieldLabel | String | M | Name of the business |
| minLength | String | M | Minimum length |
| maxLength | String | M | Maxium length |
| isMandatory | String | M | Requirement status |
| userTypeCode | String | M | Sender Code: 100000, Beneficiary code: 100001 |
| paymentMode | String | M | Mode of payment (cash, cheque, bank) |
| status | String | M |  |
| state | String | M |  |
| creationDate | String | M |  |

*Requirement legend: M = Mandatory · O = Optional · C = Conditional*

#### Response Details

```json
{
"transactionId": "8155703",
"requestTime": "Fri Feb 09 10:50:08 IST 2024",
"responseTime": "Fri Feb 09 10:50:08 IST 2024",
"resultCode": "0",
"resultDescription": "Transaction successful",
"payoutValidatorResponseList": [

{
"id": 1636,
"partnerCode": "1000008855",
"serviceTypeCode": "B2B",
"fieldName": "BusinessName",
"currency": "INR",
"fieldLabel": "Business Name",
"minLength": 1,
"maxLength": 50,
"isMandatory": true,
"userTypeCode": "100001",
"paymentMode": "Bank",
"status": "Approved",
"state": "Approved",
"creationDate": "2024-03-24T00:00:00.000+0530"

},

{
"id": 1637,
"partnerCode": "1000008855",
"serviceTypeCode": "B2B",
"fieldName": "Industry",
"currency": "INR",
"fieldLabel": "Industry",
"minLength": 1,
"maxLength": 50,
"isMandatory": true,
"userTypeCode": "100001",
"paymentMode": "Bank",
"status": "Approved",
"state": "Approved",
"creationDate": "2024-03-24T00:00:00.000+0530"

},
]
}
```
