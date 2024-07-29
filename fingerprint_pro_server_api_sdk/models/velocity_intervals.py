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
from fingerprint_pro_server_api_sdk.models.velocity_interval_result import VelocityIntervalResult


class VelocityIntervals(BaseModel):
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
        'intervals': 'VelocityIntervalResult'
    }

    attribute_map = {
        'intervals': 'intervals'
    }

    def __init__(self, intervals=None):  # noqa: E501
        """VelocityIntervals - a model defined in Swagger"""  # noqa: E501
        self._intervals = None
        self.discriminator = None
        if intervals is not None:
            self.intervals = intervals

    @property
    def intervals(self) -> VelocityIntervalResult:
        """Gets the intervals of this VelocityIntervals.  # noqa: E501


        :return: The intervals of this VelocityIntervals.  # noqa: E501
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals: VelocityIntervalResult):
        """Sets the intervals of this VelocityIntervals.


        :param intervals: The intervals of this VelocityIntervals.  # noqa: E501
        """

        self._intervals = intervals

