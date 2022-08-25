# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API provides a way for validating visitors’ data issued by Fingerprint Pro.  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StSeenAt(object):
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
        '_global': 'datetime',
        'subscription': 'datetime'
    }

    attribute_map = {
        '_global': 'global',
        'subscription': 'subscription'
    }

    def __init__(self, _global=None, subscription=None):  # noqa: E501
        """StSeenAt - a model defined in Swagger"""  # noqa: E501
        self.__global = None
        self._subscription = None
        self.discriminator = None
        self._global = _global
        self.subscription = subscription

    @property
    def _global(self):
        """Gets the _global of this StSeenAt.  # noqa: E501


        :return: The _global of this StSeenAt.  # noqa: E501
        :rtype: datetime
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this StSeenAt.


        :param _global: The _global of this StSeenAt.  # noqa: E501
        :type: datetime
        """

        self.__global = _global

    @property
    def subscription(self):
        """Gets the subscription of this StSeenAt.  # noqa: E501


        :return: The subscription of this StSeenAt.  # noqa: E501
        :rtype: datetime
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this StSeenAt.


        :param subscription: The subscription of this StSeenAt.  # noqa: E501
        :type: datetime
        """

        self._subscription = subscription

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
        if issubclass(StSeenAt, dict):
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
        if not isinstance(other, StSeenAt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StSeenAt):
            return True

        return self.to_dict() != other.to_dict()
