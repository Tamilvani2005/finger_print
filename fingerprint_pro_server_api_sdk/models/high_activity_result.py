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


class HighActivityResult(BaseModel):
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
        'result': 'bool',
        'daily_requests': 'float'
    }

    attribute_map = {
        'result': 'result',
        'daily_requests': 'dailyRequests'
    }

    def __init__(self, result=None, daily_requests=None):  # noqa: E501
        """HighActivityResult - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._daily_requests = None
        self.discriminator = None
        self.result = result
        if daily_requests is not None:
            self.daily_requests = daily_requests

    @property
    def result(self):
        """Gets the result of this HighActivityResult.  # noqa: E501

        Flag indicating whether the request came from a high activity visitor.  # noqa: E501

        :return: The result of this HighActivityResult.  # noqa: E501
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this HighActivityResult.

        Flag indicating whether the request came from a high activity visitor.  # noqa: E501

        :param result: The result of this HighActivityResult.  # noqa: E501
        :type: bool
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def daily_requests(self):
        """Gets the daily_requests of this HighActivityResult.  # noqa: E501

        Number of requests from the same visitor in the previous day.  # noqa: E501

        :return: The daily_requests of this HighActivityResult.  # noqa: E501
        :rtype: float
        """
        return self._daily_requests

    @daily_requests.setter
    def daily_requests(self, daily_requests):
        """Sets the daily_requests of this HighActivityResult.

        Number of requests from the same visitor in the previous day.  # noqa: E501

        :param daily_requests: The daily_requests of this HighActivityResult.  # noqa: E501
        :type: float
        """

        self._daily_requests = daily_requests

