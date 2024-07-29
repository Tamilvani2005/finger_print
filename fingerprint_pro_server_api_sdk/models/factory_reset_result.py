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
from datetime import datetime


class FactoryResetResult(BaseModel):
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
        'time': 'datetime',
        'timestamp': 'int'
    }

    attribute_map = {
        'time': 'time',
        'timestamp': 'timestamp'
    }

    def __init__(self, time=None, timestamp=None):  # noqa: E501
        """FactoryResetResult - a model defined in Swagger"""  # noqa: E501
        self._time = None
        self._timestamp = None
        self.discriminator = None
        self.time = time
        self.timestamp = timestamp

    @property
    def time(self) -> datetime:
        """Gets the time of this FactoryResetResult.  # noqa: E501

        Time in UTC when the most recent factory reset of the Android or iOS device was done.  If there is no sign of factory reset or the client is not a mobile device, the field will contain the epoch time (1 January 1970) in UTC.   # noqa: E501

        :return: The time of this FactoryResetResult.  # noqa: E501
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this FactoryResetResult.

        Time in UTC when the most recent factory reset of the Android or iOS device was done.  If there is no sign of factory reset or the client is not a mobile device, the field will contain the epoch time (1 January 1970) in UTC.   # noqa: E501

        :param time: The time of this FactoryResetResult.  # noqa: E501
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def timestamp(self) -> int:
        """Gets the timestamp of this FactoryResetResult.  # noqa: E501

        Same value as it's in the `time` field but represented in timestamp format.  # noqa: E501

        :return: The timestamp of this FactoryResetResult.  # noqa: E501
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        """Sets the timestamp of this FactoryResetResult.

        Same value as it's in the `time` field but represented in timestamp format.  # noqa: E501

        :param timestamp: The timestamp of this FactoryResetResult.  # noqa: E501
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

