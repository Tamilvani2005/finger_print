<p align="center">
  <a href="https://fingerprint.com">
    <picture>
     <source media="(prefers-color-scheme: dark)" srcset="https://fingerprintjs.github.io/home/resources/logo_light.svg" />
     <source media="(prefers-color-scheme: light)" srcset="https://fingerprintjs.github.io/home/resources/logo_dark.svg" />
     <img src="https://fingerprintjs.github.io/home/resources/logo_dark.svg" alt="Fingerprint logo" width="312px" />
   </picture>
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/fingerprint-pro-server-api-sdk/"><img alt="PyPI" src="https://img.shields.io/pypi/v/fingerprint-pro-server-api-sdk"></a>
  <a href="https://fingerprintjs.github.io/fingerprint-pro-server-api-python-sdk/"><img src="https://fingerprintjs.github.io/fingerprint-pro-server-api-python-sdk/badges.svg" alt="coverage"></a>
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/release.yml"><img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/release.yml/badge.svg" alt="CI badge" /></a>
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/test.yml"><img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/test.yml/badge.svg" alt="CI badge" /></a>
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/functional_tests.yml"><img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/functional_tests.yml/badge.svg" alt="CI badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/:license-mit-blue.svg?style=flat"/></a>
  <a href="https://discord.gg/39EpE2neBg"><img src="https://img.shields.io/discord/852099967190433792?style=logo&label=Discord&logo=Discord&logoColor=white" alt="Discord server"></a>
</p>

# Fingerprint Pro Server Python SDK

[Fingerprint](https://fingerprint.com) is a device intelligence platform offering 99.5% accurate visitor identification.
The Fingerprint Server Python SDK is an easy way to interact with the Fingerprint [Server API](https://dev.fingerprint.com/reference/pro-server-api) from your Python application. You can retrieve visitor history or individual identification events.


This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3
- Package version: 6.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements

The following Python versions are supported:

- Python >= 3.8

## Installation & Usage
### pip install

You can install the package directly from the Github

```sh
pip install git+https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk.git
```

Or from the PyPI

```sh
pip install fingerprint_pro_server_api_sdk
```

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
import fingerprint_pro_server_api_sdk

# Configure API key authorization and region
configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
# configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY", region="eu")

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
```

## Examples

Fetching visits using visitorId:
```python
import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk import Response
from fingerprint_pro_server_api_sdk.rest import ApiException, KnownApiException

configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)

visitor_id = 'visitor_id_example'  # str |
#request_id = 'request_id_example'  # str | Filter events by requestId (optional)
#linked_id = 'linked_id_example'  # str | Filter events by custom identifier (optional)
limit = 10  # int | Limit scanned results (optional)
#before = 56  # int | Used to paginate results (optional)

try:
    api_response: Response = api_instance.get_visits(visitor_id, limit=2)
    print(api_response)
except KnownApiException as e:
    structured_error = e.structured_error
    print("Error: %s\n" % structured_error.error)
except ApiException as e:
    print("Exception when calling DefaultApi->visitors_visitor_id_get: %s\n" % e)
```

Fetching events for requestId:
```python
import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk import EventResponse
from fingerprint_pro_server_api_sdk.rest import ApiException, KnownApiException

configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)

request_id = 'request_id_example'  # str

try:
    events_response: EventResponse = api_instance.get_event(request_id)

except KnownApiException as e:
    structured_error = e.structured_error
    print("Error code: %s. Error message: %s\n" % (structured_error.error.code, structured_error.error.message))
except ApiException as e:
    print("Exception when calling DefaultApi->get_event: %s\n" % e)
```

## Sealed results

This SDK provides utility methods for decoding [sealed results](https://dev.fingerprint.com/docs/sealed-client-results).
```python
import base64
import os

from dotenv import load_dotenv

from fingerprint_pro_server_api_sdk import EventResponse
from fingerprint_pro_server_api_sdk.sealed import unseal_events_response, DecryptionKey, DecryptionAlgorithm

load_dotenv()

sealed_result = base64.b64decode(os.environ["BASE64_SEALED_RESULT"])
key = base64.b64decode(os.environ["BASE64_KEY"])

try:
    events_response: EventResponse = unseal_events_response(sealed_result, [DecryptionKey(key, DecryptionAlgorithm['Aes256Gcm'])])
    print("\n\n\nEvent response: \n", events_response.products)
except Exception as e:
    print("Exception when calling unsealing events response: %s\n" % e)
    exit(1)

print("Unseal successful!")

exit(0)
```
To learn more, refer to example located in [sealed_results_example.py](sealed_results_example.py).

## Documentation for API Endpoints

All URIs are relative to *https://api.fpjs.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FingerprintApi* | [**get_event**](docs/FingerprintApi.md#get_event) | **GET** /events/{request_id} | Get event by requestId
*FingerprintApi* | [**get_visits**](docs/FingerprintApi.md#get_visits) | **GET** /visitors/{visitor_id} | Get visits by visitorId

## Documentation For Models

 - [ASN](docs/ASN.md)
 - [BotdDetectionResult](docs/BotdDetectionResult.md)
 - [BotdResult](docs/BotdResult.md)
 - [BrowserDetails](docs/BrowserDetails.md)
 - [ClonedAppResult](docs/ClonedAppResult.md)
 - [Confidence](docs/Confidence.md)
 - [DataCenter](docs/DataCenter.md)
 - [DeprecatedIPLocation](docs/DeprecatedIPLocation.md)
 - [DeprecatedIPLocationCity](docs/DeprecatedIPLocationCity.md)
 - [EmulatorResult](docs/EmulatorResult.md)
 - [ErrorEvent403Response](docs/ErrorEvent403Response.md)
 - [ErrorEvent403ResponseError](docs/ErrorEvent403ResponseError.md)
 - [ErrorEvent404Response](docs/ErrorEvent404Response.md)
 - [ErrorEvent404ResponseError](docs/ErrorEvent404ResponseError.md)
 - [ErrorVisits403](docs/ErrorVisits403.md)
 - [EventResponse](docs/EventResponse.md)
 - [FactoryResetResult](docs/FactoryResetResult.md)
 - [FridaResult](docs/FridaResult.md)
 - [HighActivityResult](docs/HighActivityResult.md)
 - [IPLocation](docs/IPLocation.md)
 - [IPLocationCity](docs/IPLocationCity.md)
 - [IdentificationError](docs/IdentificationError.md)
 - [IncognitoResult](docs/IncognitoResult.md)
 - [IpBlockListResult](docs/IpBlockListResult.md)
 - [IpBlockListResultDetails](docs/IpBlockListResultDetails.md)
 - [IpInfoResult](docs/IpInfoResult.md)
 - [IpInfoResultV4](docs/IpInfoResultV4.md)
 - [IpInfoResultV6](docs/IpInfoResultV6.md)
 - [JailbrokenResult](docs/JailbrokenResult.md)
 - [Location](docs/Location.md)
 - [LocationSpoofingResult](docs/LocationSpoofingResult.md)
 - [ManyRequestsResponse](docs/ManyRequestsResponse.md)
 - [PrivacySettingsResult](docs/PrivacySettingsResult.md)
 - [ProductError](docs/ProductError.md)
 - [ProductsResponse](docs/ProductsResponse.md)
 - [ProductsResponseBotd](docs/ProductsResponseBotd.md)
 - [ProductsResponseIdentification](docs/ProductsResponseIdentification.md)
 - [ProductsResponseIdentificationData](docs/ProductsResponseIdentificationData.md)
 - [ProxyResult](docs/ProxyResult.md)
 - [RawDeviceAttributesResult](docs/RawDeviceAttributesResult.md)
 - [Response](docs/Response.md)
 - [ResponseVisits](docs/ResponseVisits.md)
 - [RootAppsResult](docs/RootAppsResult.md)
 - [SeenAt](docs/SeenAt.md)
 - [SignalResponseClonedApp](docs/SignalResponseClonedApp.md)
 - [SignalResponseEmulator](docs/SignalResponseEmulator.md)
 - [SignalResponseFactoryReset](docs/SignalResponseFactoryReset.md)
 - [SignalResponseFrida](docs/SignalResponseFrida.md)
 - [SignalResponseHighActivity](docs/SignalResponseHighActivity.md)
 - [SignalResponseIncognito](docs/SignalResponseIncognito.md)
 - [SignalResponseIpBlocklist](docs/SignalResponseIpBlocklist.md)
 - [SignalResponseIpInfo](docs/SignalResponseIpInfo.md)
 - [SignalResponseJailbroken](docs/SignalResponseJailbroken.md)
 - [SignalResponseLocationSpoofing](docs/SignalResponseLocationSpoofing.md)
 - [SignalResponsePrivacySettings](docs/SignalResponsePrivacySettings.md)
 - [SignalResponseProxy](docs/SignalResponseProxy.md)
 - [SignalResponseRawDeviceAttributes](docs/SignalResponseRawDeviceAttributes.md)
 - [SignalResponseRootApps](docs/SignalResponseRootApps.md)
 - [SignalResponseSuspectScore](docs/SignalResponseSuspectScore.md)
 - [SignalResponseTampering](docs/SignalResponseTampering.md)
 - [SignalResponseTor](docs/SignalResponseTor.md)
 - [SignalResponseVirtualMachine](docs/SignalResponseVirtualMachine.md)
 - [SignalResponseVpn](docs/SignalResponseVpn.md)
 - [Subdivision](docs/Subdivision.md)
 - [SuspectScoreResult](docs/SuspectScoreResult.md)
 - [TamperingResult](docs/TamperingResult.md)
 - [TorResult](docs/TorResult.md)
 - [VirtualMachineResult](docs/VirtualMachineResult.md)
 - [Visit](docs/Visit.md)
 - [VpnResult](docs/VpnResult.md)
 - [VpnResultMethods](docs/VpnResultMethods.md)
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


## Documentation for sealed results

- [SealedResults](docs/SealedResults.md)
- [DecryptionKey](docs/DecryptionKey.md)

## Support

To report problems, ask questions or provide feedback, please use [Issues](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/issues).
If you need private support, you can email us at [oss-support@fingerprint.com](mailto:oss-support@fingerprint.com).

## License

This project is licensed under the [MIT License](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/blob/main/LICENSE).