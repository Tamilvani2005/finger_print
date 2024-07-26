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


class ErrorUpdateEvent400ResponseError(BaseModel):
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
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, code=None, message=None):  # noqa: E501
        """ErrorUpdateEvent400ResponseError - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self.discriminator = None
        self.code = code
        self.message = message

    @property
    def code(self):
        """Gets the code of this ErrorUpdateEvent400ResponseError.  # noqa: E501

        Error code: * `RequestCannotBeParsed` - the JSON content of the request contains some errors that prevented us from parsing it (wrong type/surpassed limits) * `Failed` - the event is more than 10 days old and cannot be updated   # noqa: E501

        :return: The code of this ErrorUpdateEvent400ResponseError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorUpdateEvent400ResponseError.

        Error code: * `RequestCannotBeParsed` - the JSON content of the request contains some errors that prevented us from parsing it (wrong type/surpassed limits) * `Failed` - the event is more than 10 days old and cannot be updated   # noqa: E501

        :param code: The code of this ErrorUpdateEvent400ResponseError.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = ["RequestCannotBeParsed", "Failed"]  # noqa: E501
        if (code not in allowed_values):
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self):
        """Gets the message of this ErrorUpdateEvent400ResponseError.  # noqa: E501

        Details about the underlying issue with the input payload  # noqa: E501

        :return: The message of this ErrorUpdateEvent400ResponseError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorUpdateEvent400ResponseError.

        Details about the underlying issue with the input payload  # noqa: E501

        :param message: The message of this ErrorUpdateEvent400ResponseError.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

