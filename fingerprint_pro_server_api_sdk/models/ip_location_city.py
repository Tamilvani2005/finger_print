# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel


class IPLocationCity(BaseModel):
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
        'name': 'str'
    }

    attribute_map = {
        'name': 'name'
    }

    def __init__(self, name=None):  # noqa: E501
        """IPLocationCity - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self.discriminator = None
        if name is not None:
            self.name = name

    @property
    def name(self):
        """Gets the name of this IPLocationCity.  # noqa: E501


        :return: The name of this IPLocationCity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IPLocationCity.


        :param name: The name of this IPLocationCity.  # noqa: E501
        :type: str
        """

        self._name = name

