# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import Dict  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel
from fingerprint_pro_server_api_sdk.models.incognito_result import IncognitoResult
from fingerprint_pro_server_api_sdk.models.identification_error import IdentificationError


class SignalResponseIncognito(BaseModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'IncognitoResult',
        'error': 'IdentificationError'
    }

    attribute_map = {
        'data': 'data',
        'error': 'error'
    }

    def __init__(self, data=None, error=None):  # noqa: E501
        """SignalResponseIncognito - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._error = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if error is not None:
            self.error = error

    @property
    def data(self) -> IncognitoResult:
        """Gets the data of this SignalResponseIncognito.  # noqa: E501


        :return: The data of this SignalResponseIncognito.  # noqa: E501
        """
        return self._data

    @data.setter
    def data(self, data: IncognitoResult):
        """Sets the data of this SignalResponseIncognito.


        :param data: The data of this SignalResponseIncognito.  # noqa: E501
        """

        self._data = data

    @property
    def error(self) -> IdentificationError:
        """Gets the error of this SignalResponseIncognito.  # noqa: E501


        :return: The error of this SignalResponseIncognito.  # noqa: E501
        """
        return self._error

    @error.setter
    def error(self, error: IdentificationError):
        """Sets the error of this SignalResponseIncognito.


        :param error: The error of this SignalResponseIncognito.  # noqa: E501
        """

        self._error = error

