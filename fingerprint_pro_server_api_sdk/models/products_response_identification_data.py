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
from fingerprint_pro_server_api_sdk.models.browser_details import BrowserDetails
from fingerprint_pro_server_api_sdk.models.deprecated_ip_location import DeprecatedIPLocation
from datetime import datetime
from fingerprint_pro_server_api_sdk.models.confidence import Confidence
from fingerprint_pro_server_api_sdk.models.seen_at import SeenAt
from fingerprint_pro_server_api_sdk.models.seen_at import SeenAt


class ProductsResponseIdentificationData(BaseModel):
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
        'last_seen_at': 'SeenAt',
        'visitor_id': 'str'
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
        'last_seen_at': 'lastSeenAt',
        'visitor_id': 'visitorId'
    }

    def __init__(self, request_id=None, browser_details=None, incognito=None, ip=None, ip_location=None, timestamp=None, time=None, url=None, tag=None, linked_id=None, confidence=None, visitor_found=None, first_seen_at=None, last_seen_at=None, visitor_id=None):  # noqa: E501
        """ProductsResponseIdentificationData - a model defined in Swagger"""  # noqa: E501
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
        self._visitor_id = None
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
        self.visitor_id = visitor_id

    @property
    def request_id(self) -> str:
        """Gets the request_id of this ProductsResponseIdentificationData.  # noqa: E501

        Unique identifier of the user's identification request.  # noqa: E501

        :return: The request_id of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id: str):
        """Sets the request_id of this ProductsResponseIdentificationData.

        Unique identifier of the user's identification request.  # noqa: E501

        :param request_id: The request_id of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def browser_details(self) -> BrowserDetails:
        """Gets the browser_details of this ProductsResponseIdentificationData.  # noqa: E501


        :return: The browser_details of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._browser_details

    @browser_details.setter
    def browser_details(self, browser_details: BrowserDetails):
        """Sets the browser_details of this ProductsResponseIdentificationData.


        :param browser_details: The browser_details of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if browser_details is None:
            raise ValueError("Invalid value for `browser_details`, must not be `None`")  # noqa: E501

        self._browser_details = browser_details

    @property
    def incognito(self) -> bool:
        """Gets the incognito of this ProductsResponseIdentificationData.  # noqa: E501

        Flag if user used incognito session.  # noqa: E501

        :return: The incognito of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._incognito

    @incognito.setter
    def incognito(self, incognito: bool):
        """Sets the incognito of this ProductsResponseIdentificationData.

        Flag if user used incognito session.  # noqa: E501

        :param incognito: The incognito of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if incognito is None:
            raise ValueError("Invalid value for `incognito`, must not be `None`")  # noqa: E501

        self._incognito = incognito

    @property
    def ip(self) -> str:
        """Gets the ip of this ProductsResponseIdentificationData.  # noqa: E501


        :return: The ip of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """Sets the ip of this ProductsResponseIdentificationData.


        :param ip: The ip of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def ip_location(self) -> DeprecatedIPLocation:
        """Gets the ip_location of this ProductsResponseIdentificationData.  # noqa: E501


        :return: The ip_location of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._ip_location

    @ip_location.setter
    def ip_location(self, ip_location: DeprecatedIPLocation):
        """Sets the ip_location of this ProductsResponseIdentificationData.


        :param ip_location: The ip_location of this ProductsResponseIdentificationData.  # noqa: E501
        """

        self._ip_location = ip_location

    @property
    def timestamp(self) -> int:
        """Gets the timestamp of this ProductsResponseIdentificationData.  # noqa: E501

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :return: The timestamp of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        """Sets the timestamp of this ProductsResponseIdentificationData.

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :param timestamp: The timestamp of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def time(self) -> datetime:
        """Gets the time of this ProductsResponseIdentificationData.  # noqa: E501

        Time expressed according to ISO 8601 in UTC format.  # noqa: E501

        :return: The time of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this ProductsResponseIdentificationData.

        Time expressed according to ISO 8601 in UTC format.  # noqa: E501

        :param time: The time of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def url(self) -> str:
        """Gets the url of this ProductsResponseIdentificationData.  # noqa: E501

        Page URL from which the identification request was sent.  # noqa: E501

        :return: The url of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this ProductsResponseIdentificationData.

        Page URL from which the identification request was sent.  # noqa: E501

        :param url: The url of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def tag(self) -> Dict[str, object]:
        """Gets the tag of this ProductsResponseIdentificationData.  # noqa: E501

        A customer-provided value or an object that was sent with identification request.  # noqa: E501

        :return: The tag of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._tag

    @tag.setter
    def tag(self, tag: Dict[str, object]):
        """Sets the tag of this ProductsResponseIdentificationData.

        A customer-provided value or an object that was sent with identification request.  # noqa: E501

        :param tag: The tag of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def linked_id(self) -> str:
        """Gets the linked_id of this ProductsResponseIdentificationData.  # noqa: E501

        A customer-provided id that was sent with identification request.  # noqa: E501

        :return: The linked_id of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._linked_id

    @linked_id.setter
    def linked_id(self, linked_id: str):
        """Sets the linked_id of this ProductsResponseIdentificationData.

        A customer-provided id that was sent with identification request.  # noqa: E501

        :param linked_id: The linked_id of this ProductsResponseIdentificationData.  # noqa: E501
        """

        self._linked_id = linked_id

    @property
    def confidence(self) -> Confidence:
        """Gets the confidence of this ProductsResponseIdentificationData.  # noqa: E501


        :return: The confidence of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence: Confidence):
        """Sets the confidence of this ProductsResponseIdentificationData.


        :param confidence: The confidence of this ProductsResponseIdentificationData.  # noqa: E501
        """

        self._confidence = confidence

    @property
    def visitor_found(self) -> bool:
        """Gets the visitor_found of this ProductsResponseIdentificationData.  # noqa: E501

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :return: The visitor_found of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._visitor_found

    @visitor_found.setter
    def visitor_found(self, visitor_found: bool):
        """Sets the visitor_found of this ProductsResponseIdentificationData.

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :param visitor_found: The visitor_found of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if visitor_found is None:
            raise ValueError("Invalid value for `visitor_found`, must not be `None`")  # noqa: E501

        self._visitor_found = visitor_found

    @property
    def first_seen_at(self) -> SeenAt:
        """Gets the first_seen_at of this ProductsResponseIdentificationData.  # noqa: E501


        :return: The first_seen_at of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._first_seen_at

    @first_seen_at.setter
    def first_seen_at(self, first_seen_at: SeenAt):
        """Sets the first_seen_at of this ProductsResponseIdentificationData.


        :param first_seen_at: The first_seen_at of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if first_seen_at is None:
            raise ValueError("Invalid value for `first_seen_at`, must not be `None`")  # noqa: E501

        self._first_seen_at = first_seen_at

    @property
    def last_seen_at(self) -> SeenAt:
        """Gets the last_seen_at of this ProductsResponseIdentificationData.  # noqa: E501


        :return: The last_seen_at of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._last_seen_at

    @last_seen_at.setter
    def last_seen_at(self, last_seen_at: SeenAt):
        """Sets the last_seen_at of this ProductsResponseIdentificationData.


        :param last_seen_at: The last_seen_at of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if last_seen_at is None:
            raise ValueError("Invalid value for `last_seen_at`, must not be `None`")  # noqa: E501

        self._last_seen_at = last_seen_at

    @property
    def visitor_id(self) -> str:
        """Gets the visitor_id of this ProductsResponseIdentificationData.  # noqa: E501

        String of 20 characters that uniquely identifies the visitor's browser.   # noqa: E501

        :return: The visitor_id of this ProductsResponseIdentificationData.  # noqa: E501
        """
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, visitor_id: str):
        """Sets the visitor_id of this ProductsResponseIdentificationData.

        String of 20 characters that uniquely identifies the visitor's browser.   # noqa: E501

        :param visitor_id: The visitor_id of this ProductsResponseIdentificationData.  # noqa: E501
        """
        if visitor_id is None:
            raise ValueError("Invalid value for `visitor_id`, must not be `None`")  # noqa: E501

        self._visitor_id = visitor_id

