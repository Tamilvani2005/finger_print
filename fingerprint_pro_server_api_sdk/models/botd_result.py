# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. This API can be used for data exports, decision-making, and data analysis scenarios.  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BotdResult(object):
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
        'ip': 'str',
        'time': 'datetime',
        'url': 'str',
        'bot': 'BotdDetectionResult'
    }

    attribute_map = {
        'ip': 'ip',
        'time': 'time',
        'url': 'url',
        'bot': 'bot'
    }

    def __init__(self, ip=None, time=None, url=None, bot=None):  # noqa: E501
        """BotdResult - a model defined in Swagger"""  # noqa: E501
        self._ip = None
        self._time = None
        self._url = None
        self._bot = None
        self.discriminator = None
        self.ip = ip
        self.time = time
        self.url = url
        self.bot = bot

    @property
    def ip(self):
        """Gets the ip of this BotdResult.  # noqa: E501

        IP address of the requesting browser or bot.  # noqa: E501

        :return: The ip of this BotdResult.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this BotdResult.

        IP address of the requesting browser or bot.  # noqa: E501

        :param ip: The ip of this BotdResult.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def time(self):
        """Gets the time of this BotdResult.  # noqa: E501

        Time in UTC when the request from the JS agent was made. We recommend to treat requests that are older than 2 minutes as malicious. Otherwise, request replay attacks are possible  # noqa: E501

        :return: The time of this BotdResult.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this BotdResult.

        Time in UTC when the request from the JS agent was made. We recommend to treat requests that are older than 2 minutes as malicious. Otherwise, request replay attacks are possible  # noqa: E501

        :param time: The time of this BotdResult.  # noqa: E501
        :type: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def url(self):
        """Gets the url of this BotdResult.  # noqa: E501

        Page URL from which identification request was sent.  # noqa: E501

        :return: The url of this BotdResult.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BotdResult.

        Page URL from which identification request was sent.  # noqa: E501

        :param url: The url of this BotdResult.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def bot(self):
        """Gets the bot of this BotdResult.  # noqa: E501


        :return: The bot of this BotdResult.  # noqa: E501
        :rtype: BotdDetectionResult
        """
        return self._bot

    @bot.setter
    def bot(self, bot):
        """Sets the bot of this BotdResult.


        :param bot: The bot of this BotdResult.  # noqa: E501
        :type: BotdDetectionResult
        """
        if bot is None:
            raise ValueError("Invalid value for `bot`, must not be `None`")  # noqa: E501

        self._bot = bot

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
        if issubclass(BotdResult, dict):
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
        if not isinstance(other, BotdResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BotdResult):
            return True

        return self.to_dict() != other.to_dict()
