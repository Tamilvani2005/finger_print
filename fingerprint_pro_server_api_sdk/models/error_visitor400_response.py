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


class ErrorVisitor400Response(BaseModel):
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
        'error': 'ErrorVisitor400ResponseError'
    }

    attribute_map = {
        'error': 'error'
    }

    def __init__(self, error=None):  # noqa: E501
        """ErrorVisitor400Response - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self.discriminator = None
        if error is not None:
            self.error = error

    @property
    def error(self):
        """Gets the error of this ErrorVisitor400Response.  # noqa: E501


        :return: The error of this ErrorVisitor400Response.  # noqa: E501
        :rtype: ErrorVisitor400ResponseError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ErrorVisitor400Response.


        :param error: The error of this ErrorVisitor400Response.  # noqa: E501
        :type: ErrorVisitor400ResponseError
        """

        self._error = error

