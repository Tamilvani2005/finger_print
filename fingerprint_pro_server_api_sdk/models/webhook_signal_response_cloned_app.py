# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WebhookSignalResponseClonedApp(object):
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
        'result': 'bool'
    }

    attribute_map = {
        'result': 'result'
    }

    def __init__(self, result=None):  # noqa: E501
        """WebhookSignalResponseClonedApp - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self.discriminator = None
        if result is not None:
            self.result = result

    @property
    def result(self):
        """Gets the result of this WebhookSignalResponseClonedApp.  # noqa: E501

        Android specific cloned application detection. There are 2 values: • `true` - Presence of app cloners work detected (e.g. fully cloned application found or launch of it inside of a not main working profile detected). • `false` - No signs of cloned application detected or the client is not Android.   # noqa: E501

        :return: The result of this WebhookSignalResponseClonedApp.  # noqa: E501
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this WebhookSignalResponseClonedApp.

        Android specific cloned application detection. There are 2 values: • `true` - Presence of app cloners work detected (e.g. fully cloned application found or launch of it inside of a not main working profile detected). • `false` - No signs of cloned application detected or the client is not Android.   # noqa: E501

        :param result: The result of this WebhookSignalResponseClonedApp.  # noqa: E501
        :type: bool
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebhookSignalResponseClonedApp, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebhookSignalResponseClonedApp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookSignalResponseClonedApp):
            return True

        return self.to_dict() != other.to_dict()
