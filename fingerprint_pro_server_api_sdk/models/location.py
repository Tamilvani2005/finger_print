# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import Dict, List, Optional  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel


class Location(BaseModel):
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
        'code': 'str',
        'name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, code=None, name=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._name = None
        self.discriminator = None
        self.code = code
        self.name = name

    @property
    def code(self) -> str:
        """Gets the code of this Location.  # noqa: E501


        :return: The code of this Location.  # noqa: E501
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this Location.


        :param code: The code of this Location.  # noqa: E501
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def name(self) -> str:
        """Gets the name of this Location.  # noqa: E501


        :return: The name of this Location.  # noqa: E501
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Location.


        :param name: The name of this Location.  # noqa: E501
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

