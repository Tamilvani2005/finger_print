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

class Visit(object):
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
        'request_id': 'str',
        'browser_details': 'BrowserDetails',
        'incognito': 'bool',
        'ip': 'str',
        'ip_location': 'DeprecatedIPLocation',
        'timestamp': 'int',
        'time': 'datetime',
        'url': 'str',
        'tag': 'dict(str, object)',
        'linked_id': 'str',
        'confidence': 'Confidence',
        'visitor_found': 'bool',
        'first_seen_at': 'SeenAt',
        'last_seen_at': 'SeenAt'
    }

    attribute_map = {
        'request_id': 'requestId',
        'browser_details': 'browserDetails',
        'incognito': 'incognito',
        'ip': 'ip',
        'ip_location': 'ipLocation',
        'timestamp': 'timestamp',
        'time': 'time',
        'url': 'url',
        'tag': 'tag',
        'linked_id': 'linkedId',
        'confidence': 'confidence',
        'visitor_found': 'visitorFound',
        'first_seen_at': 'firstSeenAt',
        'last_seen_at': 'lastSeenAt'
    }

    def __init__(self, request_id=None, browser_details=None, incognito=None, ip=None, ip_location=None, timestamp=None, time=None, url=None, tag=None, linked_id=None, confidence=None, visitor_found=None, first_seen_at=None, last_seen_at=None):  # noqa: E501
        """Visit - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._browser_details = None
        self._incognito = None
        self._ip = None
        self._ip_location = None
        self._timestamp = None
        self._time = None
        self._url = None
        self._tag = None
        self._linked_id = None
        self._confidence = None
        self._visitor_found = None
        self._first_seen_at = None
        self._last_seen_at = None
        self.discriminator = None
        self.request_id = request_id
        self.browser_details = browser_details
        self.incognito = incognito
        self.ip = ip
        if ip_location is not None:
            self.ip_location = ip_location
        self.timestamp = timestamp
        self.time = time
        self.url = url
        self.tag = tag
        if linked_id is not None:
            self.linked_id = linked_id
        if confidence is not None:
            self.confidence = confidence
        self.visitor_found = visitor_found
        self.first_seen_at = first_seen_at
        self.last_seen_at = last_seen_at

    @property
    def request_id(self):
        """Gets the request_id of this Visit.  # noqa: E501

        Unique identifier of the user's identification request.  # noqa: E501

        :return: The request_id of this Visit.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this Visit.

        Unique identifier of the user's identification request.  # noqa: E501

        :param request_id: The request_id of this Visit.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def browser_details(self):
        """Gets the browser_details of this Visit.  # noqa: E501


        :return: The browser_details of this Visit.  # noqa: E501
        :rtype: BrowserDetails
        """
        return self._browser_details

    @browser_details.setter
    def browser_details(self, browser_details):
        """Sets the browser_details of this Visit.


        :param browser_details: The browser_details of this Visit.  # noqa: E501
        :type: BrowserDetails
        """
        if browser_details is None:
            raise ValueError("Invalid value for `browser_details`, must not be `None`")  # noqa: E501

        self._browser_details = browser_details

    @property
    def incognito(self):
        """Gets the incognito of this Visit.  # noqa: E501

        Flag if user used incognito session.  # noqa: E501

        :return: The incognito of this Visit.  # noqa: E501
        :rtype: bool
        """
        return self._incognito

    @incognito.setter
    def incognito(self, incognito):
        """Sets the incognito of this Visit.

        Flag if user used incognito session.  # noqa: E501

        :param incognito: The incognito of this Visit.  # noqa: E501
        :type: bool
        """
        if incognito is None:
            raise ValueError("Invalid value for `incognito`, must not be `None`")  # noqa: E501

        self._incognito = incognito

    @property
    def ip(self):
        """Gets the ip of this Visit.  # noqa: E501


        :return: The ip of this Visit.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Visit.


        :param ip: The ip of this Visit.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def ip_location(self):
        """Gets the ip_location of this Visit.  # noqa: E501


        :return: The ip_location of this Visit.  # noqa: E501
        :rtype: DeprecatedIPLocation
        """
        return self._ip_location

    @ip_location.setter
    def ip_location(self, ip_location):
        """Sets the ip_location of this Visit.


        :param ip_location: The ip_location of this Visit.  # noqa: E501
        :type: DeprecatedIPLocation
        """

        self._ip_location = ip_location

    @property
    def timestamp(self):
        """Gets the timestamp of this Visit.  # noqa: E501

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :return: The timestamp of this Visit.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Visit.

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :param timestamp: The timestamp of this Visit.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def time(self):
        """Gets the time of this Visit.  # noqa: E501

        Time expressed according to ISO 8601 in UTC format.  # noqa: E501

        :return: The time of this Visit.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Visit.

        Time expressed according to ISO 8601 in UTC format.  # noqa: E501

        :param time: The time of this Visit.  # noqa: E501
        :type: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def url(self):
        """Gets the url of this Visit.  # noqa: E501

        Page URL from which the identification request was sent.  # noqa: E501

        :return: The url of this Visit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Visit.

        Page URL from which the identification request was sent.  # noqa: E501

        :param url: The url of this Visit.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def tag(self):
        """Gets the tag of this Visit.  # noqa: E501

        A customer-provided value or an object that was sent with identification request.  # noqa: E501

        :return: The tag of this Visit.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Visit.

        A customer-provided value or an object that was sent with identification request.  # noqa: E501

        :param tag: The tag of this Visit.  # noqa: E501
        :type: dict(str, object)
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def linked_id(self):
        """Gets the linked_id of this Visit.  # noqa: E501

        A customer-provided id that was sent with identification request.  # noqa: E501

        :return: The linked_id of this Visit.  # noqa: E501
        :rtype: str
        """
        return self._linked_id

    @linked_id.setter
    def linked_id(self, linked_id):
        """Sets the linked_id of this Visit.

        A customer-provided id that was sent with identification request.  # noqa: E501

        :param linked_id: The linked_id of this Visit.  # noqa: E501
        :type: str
        """

        self._linked_id = linked_id

    @property
    def confidence(self):
        """Gets the confidence of this Visit.  # noqa: E501


        :return: The confidence of this Visit.  # noqa: E501
        :rtype: Confidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Visit.


        :param confidence: The confidence of this Visit.  # noqa: E501
        :type: Confidence
        """

        self._confidence = confidence

    @property
    def visitor_found(self):
        """Gets the visitor_found of this Visit.  # noqa: E501

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :return: The visitor_found of this Visit.  # noqa: E501
        :rtype: bool
        """
        return self._visitor_found

    @visitor_found.setter
    def visitor_found(self, visitor_found):
        """Sets the visitor_found of this Visit.

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :param visitor_found: The visitor_found of this Visit.  # noqa: E501
        :type: bool
        """
        if visitor_found is None:
            raise ValueError("Invalid value for `visitor_found`, must not be `None`")  # noqa: E501

        self._visitor_found = visitor_found

    @property
    def first_seen_at(self):
        """Gets the first_seen_at of this Visit.  # noqa: E501


        :return: The first_seen_at of this Visit.  # noqa: E501
        :rtype: SeenAt
        """
        return self._first_seen_at

    @first_seen_at.setter
    def first_seen_at(self, first_seen_at):
        """Sets the first_seen_at of this Visit.


        :param first_seen_at: The first_seen_at of this Visit.  # noqa: E501
        :type: SeenAt
        """
        if first_seen_at is None:
            raise ValueError("Invalid value for `first_seen_at`, must not be `None`")  # noqa: E501

        self._first_seen_at = first_seen_at

    @property
    def last_seen_at(self):
        """Gets the last_seen_at of this Visit.  # noqa: E501


        :return: The last_seen_at of this Visit.  # noqa: E501
        :rtype: SeenAt
        """
        return self._last_seen_at

    @last_seen_at.setter
    def last_seen_at(self, last_seen_at):
        """Sets the last_seen_at of this Visit.


        :param last_seen_at: The last_seen_at of this Visit.  # noqa: E501
        :type: SeenAt
        """
        if last_seen_at is None:
            raise ValueError("Invalid value for `last_seen_at`, must not be `None`")  # noqa: E501

        self._last_seen_at = last_seen_at

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
        if issubclass(Visit, dict):
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
        if not isinstance(other, Visit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Visit):
            return True

        return self.to_dict() != other.to_dict()
