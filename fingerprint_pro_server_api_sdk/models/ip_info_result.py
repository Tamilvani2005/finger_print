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
from fingerprint_pro_server_api_sdk.models.ip_info_result_v4 import IpInfoResultV4
from fingerprint_pro_server_api_sdk.models.ip_info_result_v6 import IpInfoResultV6


class IpInfoResult(BaseModel):
    """
    Details about the request IP address. Has separate fields for v4 and v6 IP address versions.

    NOTE: This class is auto generated by the swagger code generator program.

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
        'v4': 'IpInfoResultV4',
        'v6': 'IpInfoResultV6'
    }

    attribute_map = {
        'v4': 'v4',
        'v6': 'v6'
    }

    def __init__(self, v4=None, v6=None):  # noqa: E501
        """IpInfoResult - a model defined in Swagger"""  # noqa: E501
        self._v4 = None
        self._v6 = None
        self.discriminator = None
        if v4 is not None:
            self.v4 = v4
        if v6 is not None:
            self.v6 = v6

    @property
    def v4(self) -> IpInfoResultV4:
        """Gets the v4 of this IpInfoResult.  # noqa: E501


        :return: The v4 of this IpInfoResult.  # noqa: E501
        """
        return self._v4

    @v4.setter
    def v4(self, v4: IpInfoResultV4):
        """Sets the v4 of this IpInfoResult.


        :param v4: The v4 of this IpInfoResult.  # noqa: E501
        """

        self._v4 = v4

    @property
    def v6(self) -> IpInfoResultV6:
        """Gets the v6 of this IpInfoResult.  # noqa: E501


        :return: The v6 of this IpInfoResult.  # noqa: E501
        """
        return self._v6

    @v6.setter
    def v6(self, v6: IpInfoResultV6):
        """Sets the v6 of this IpInfoResult.


        :param v6: The v6 of this IpInfoResult.  # noqa: E501
        """

        self._v6 = v6

