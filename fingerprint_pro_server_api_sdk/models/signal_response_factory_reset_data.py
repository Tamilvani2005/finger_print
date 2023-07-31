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

class SignalResponseFactoryResetData(object):
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
        """SignalResponseFactoryResetData - a model defined in Swagger"""  # noqa: E501
        self._time = None
        self._timestamp = None
        self.discriminator = None
        if time is not None:
            self.time = time
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def time(self):
        """Gets the time of this SignalResponseFactoryResetData.  # noqa: E501

        Time in UTC for the Android client when recent factory reset was done.  If there is no sign of factory reset or the client isn't Android, the field will be epoch time.   # noqa: E501

        :return: The time of this SignalResponseFactoryResetData.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SignalResponseFactoryResetData.

        Time in UTC for the Android client when recent factory reset was done.  If there is no sign of factory reset or the client isn't Android, the field will be epoch time.   # noqa: E501

        :param time: The time of this SignalResponseFactoryResetData.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def timestamp(self):
        """Gets the timestamp of this SignalResponseFactoryResetData.  # noqa: E501

        Same value as it's in the `time` field but represented in timestamp format.  # noqa: E501

        :return: The timestamp of this SignalResponseFactoryResetData.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SignalResponseFactoryResetData.

        Same value as it's in the `time` field but represented in timestamp format.  # noqa: E501

        :param timestamp: The timestamp of this SignalResponseFactoryResetData.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if issubclass(SignalResponseFactoryResetData, dict):
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
        if not isinstance(other, SignalResponseFactoryResetData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignalResponseFactoryResetData):
            return True

        return self.to_dict() != other.to_dict()
