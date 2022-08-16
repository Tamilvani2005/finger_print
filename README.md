<p align="center">
  <a href="https://fingerprint.com">
    <picture>
     <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/main/res/logo_light.svg" />
     <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/main/res/logo_dark.svg" />
     <img src="https://raw.githubusercontent.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/main/res/logo_dark.svg" alt="Fingerprint logo" width="312px" />
   </picture>
  </a>
</p>
<p align="center">
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/release.yml">
    <img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/release.yml/badge.svg" alt="CI badge" />
  </a>
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/test.yml">
    <img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/test.yml/badge.svg" alt="CI badge" />
  </a>
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/functional_tests.yml">
    <img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/functional_tests.yml/badge.svg" alt="CI badge" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/:license-mit-blue.svg?style=flat"/>
  </a>
  <a href="https://discord.gg/39EpE2neBg">
    <img src="https://img.shields.io/discord/852099967190433792?style=logo&label=Discord&logo=Discord&logoColor=white" alt="Discord server">
  </a>
</p>

> :warning: **Work in progress**: This is a beta version of the library

# Fingerprint Pro Server Python SDK
Fingerprint Pro Server API provides a way for validating visitors’ data issued by Fingerprint Pro.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3
- Package version: 0.0.2-beta.9
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk.git`)

Then import the package:
```python
import fingerprint_pro_server_api_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fingerprint_pro_server_api_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk import Response
from fingerprint_pro_server_api_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization and region
configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
# configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY", region="eu")

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
visitor_id = 'visitor_id_example'  # str |
#request_id = 'request_id_example'  # str | Filter events by requestId (optional)
#linked_id = 'linked_id_example'  # str | Filter events by custom identifier (optional)
limit = 10  # int | Limit scanned results (optional)
#before = 56  # int | Used to paginate results (optional)

try:
    api_response: Response = api_instance.get_visits(visitor_id, limit=2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->visitors_visitor_id_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.fpjs.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FingerprintApi* | [**get_visits**](docs/FingerprintApi.md#get_visits) | **GET** /visitors/{visitor_id} | 

## Documentation For Models

 - [BrowserDetails](docs/BrowserDetails.md)
 - [Confidence](docs/Confidence.md)
 - [IPLocation](docs/IPLocation.md)
 - [IPLocationCity](docs/IPLocationCity.md)
 - [Location](docs/Location.md)
 - [ManyRequestsResponse](docs/ManyRequestsResponse.md)
 - [Response](docs/Response.md)
 - [StSeenAt](docs/StSeenAt.md)
 - [Subdivision](docs/Subdivision.md)
 - [Visit](docs/Visit.md)
 - [WebhookVisit](docs/WebhookVisit.md)

## Documentation For Authorization


## ApiKeyHeader

- **Type**: API key
- **API key parameter name**: Auth-API-Key
- **Location**: HTTP header

## ApiKeyQuery

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Author

support@fingerprint.com
