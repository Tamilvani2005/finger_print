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

class BrowserDetails(object):
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
        'browser_name': 'str',
        'browser_major_version': 'str',
        'browser_full_version': 'str',
        'os': 'str',
        'os_version': 'str',
        'device': 'str',
        'user_agent': 'str',
        'bot_probability': 'int'
    }

    attribute_map = {
        'browser_name': 'browserName',
        'browser_major_version': 'browserMajorVersion',
        'browser_full_version': 'browserFullVersion',
        'os': 'os',
        'os_version': 'osVersion',
        'device': 'device',
        'user_agent': 'userAgent',
        'bot_probability': 'botProbability'
    }

    def __init__(self, browser_name=None, browser_major_version=None, browser_full_version=None, os=None, os_version=None, device=None, user_agent=None, bot_probability=None):  # noqa: E501
        """BrowserDetails - a model defined in Swagger"""  # noqa: E501
        self._browser_name = None
        self._browser_major_version = None
        self._browser_full_version = None
        self._os = None
        self._os_version = None
        self._device = None
        self._user_agent = None
        self._bot_probability = None
        self.discriminator = None
        self.browser_name = browser_name
        self.browser_major_version = browser_major_version
        self.browser_full_version = browser_full_version
        self.os = os
        self.os_version = os_version
        self.device = device
        self.user_agent = user_agent
        if bot_probability is not None:
            self.bot_probability = bot_probability

    @property
    def browser_name(self):
        """Gets the browser_name of this BrowserDetails.  # noqa: E501


        :return: The browser_name of this BrowserDetails.  # noqa: E501
        :rtype: str
        """
        return self._browser_name

    @browser_name.setter
    def browser_name(self, browser_name):
        """Sets the browser_name of this BrowserDetails.


        :param browser_name: The browser_name of this BrowserDetails.  # noqa: E501
        :type: str
        """
        if browser_name is None:
            raise ValueError("Invalid value for `browser_name`, must not be `None`")  # noqa: E501

        self._browser_name = browser_name

    @property
    def browser_major_version(self):
        """Gets the browser_major_version of this BrowserDetails.  # noqa: E501


        :return: The browser_major_version of this BrowserDetails.  # noqa: E501
        :rtype: str
        """
        return self._browser_major_version

    @browser_major_version.setter
    def browser_major_version(self, browser_major_version):
        """Sets the browser_major_version of this BrowserDetails.


        :param browser_major_version: The browser_major_version of this BrowserDetails.  # noqa: E501
        :type: str
        """
        if browser_major_version is None:
            raise ValueError("Invalid value for `browser_major_version`, must not be `None`")  # noqa: E501

        self._browser_major_version = browser_major_version

    @property
    def browser_full_version(self):
        """Gets the browser_full_version of this BrowserDetails.  # noqa: E501


        :return: The browser_full_version of this BrowserDetails.  # noqa: E501
        :rtype: str
        """
        return self._browser_full_version

    @browser_full_version.setter
    def browser_full_version(self, browser_full_version):
        """Sets the browser_full_version of this BrowserDetails.


        :param browser_full_version: The browser_full_version of this BrowserDetails.  # noqa: E501
        :type: str
        """
        if browser_full_version is None:
            raise ValueError("Invalid value for `browser_full_version`, must not be `None`")  # noqa: E501

        self._browser_full_version = browser_full_version

    @property
    def os(self):
        """Gets the os of this BrowserDetails.  # noqa: E501


        :return: The os of this BrowserDetails.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this BrowserDetails.


        :param os: The os of this BrowserDetails.  # noqa: E501
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def os_version(self):
        """Gets the os_version of this BrowserDetails.  # noqa: E501


        :return: The os_version of this BrowserDetails.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this BrowserDetails.


        :param os_version: The os_version of this BrowserDetails.  # noqa: E501
        :type: str
        """
        if os_version is None:
            raise ValueError("Invalid value for `os_version`, must not be `None`")  # noqa: E501

        self._os_version = os_version

    @property
    def device(self):
        """Gets the device of this BrowserDetails.  # noqa: E501


        :return: The device of this BrowserDetails.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this BrowserDetails.


        :param device: The device of this BrowserDetails.  # noqa: E501
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def user_agent(self):
        """Gets the user_agent of this BrowserDetails.  # noqa: E501


        :return: The user_agent of this BrowserDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this BrowserDetails.


        :param user_agent: The user_agent of this BrowserDetails.  # noqa: E501
        :type: str
        """
        if user_agent is None:
            raise ValueError("Invalid value for `user_agent`, must not be `None`")  # noqa: E501

        self._user_agent = user_agent

    @property
    def bot_probability(self):
        """Gets the bot_probability of this BrowserDetails.  # noqa: E501


        :return: The bot_probability of this BrowserDetails.  # noqa: E501
        :rtype: int
        """
        return self._bot_probability

    @bot_probability.setter
    def bot_probability(self, bot_probability):
        """Sets the bot_probability of this BrowserDetails.


        :param bot_probability: The bot_probability of this BrowserDetails.  # noqa: E501
        :type: int
        """

        self._bot_probability = bot_probability

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
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
        if issubclass(BrowserDetails, dict):
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
        if not isinstance(other, BrowserDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BrowserDetails):
            return True

        return self.to_dict() != other.to_dict()
