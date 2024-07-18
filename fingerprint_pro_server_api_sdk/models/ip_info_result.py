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

class IpInfoResult(object):
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
    def v4(self):
        """Gets the v4 of this IpInfoResult.  # noqa: E501


        :return: The v4 of this IpInfoResult.  # noqa: E501
        :rtype: IpInfoResultV4
        """
        return self._v4

    @v4.setter
    def v4(self, v4):
        """Sets the v4 of this IpInfoResult.


        :param v4: The v4 of this IpInfoResult.  # noqa: E501
        :type: IpInfoResultV4
        """

        self._v4 = v4

    @property
    def v6(self):
        """Gets the v6 of this IpInfoResult.  # noqa: E501


        :return: The v6 of this IpInfoResult.  # noqa: E501
        :rtype: IpInfoResultV6
        """
        return self._v6

    @v6.setter
    def v6(self, v6):
        """Sets the v6 of this IpInfoResult.


        :param v6: The v6 of this IpInfoResult.  # noqa: E501
        :type: IpInfoResultV6
        """

        self._v6 = v6

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
            elif value is None:
                continue
            else:
                result[attr] = value
        if issubclass(IpInfoResult, dict):
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
        if not isinstance(other, IpInfoResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpInfoResult):
            return True

        return self.to_dict() != other.to_dict()
