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

class IpInfoResultV6(object):
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
        'address': 'str',
        'geolocation': 'IPLocation',
        'asn': 'ASN',
        'datacenter': 'DataCenterInfo',
        'data_center': 'DataCenter'
    }

    attribute_map = {
        'address': 'address',
        'geolocation': 'geolocation',
        'asn': 'asn',
        'datacenter': 'datacenter',
        'data_center': 'dataCenter'
    }

    def __init__(self, address=None, geolocation=None, asn=None, datacenter=None, data_center=None):  # noqa: E501
        """IpInfoResultV6 - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._geolocation = None
        self._asn = None
        self._datacenter = None
        self._data_center = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if geolocation is not None:
            self.geolocation = geolocation
        if asn is not None:
            self.asn = asn
        if datacenter is not None:
            self.datacenter = datacenter
        if data_center is not None:
            self.data_center = data_center

    @property
    def address(self):
        """Gets the address of this IpInfoResultV6.  # noqa: E501


        :return: The address of this IpInfoResultV6.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IpInfoResultV6.


        :param address: The address of this IpInfoResultV6.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def geolocation(self):
        """Gets the geolocation of this IpInfoResultV6.  # noqa: E501


        :return: The geolocation of this IpInfoResultV6.  # noqa: E501
        :rtype: IPLocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """Sets the geolocation of this IpInfoResultV6.


        :param geolocation: The geolocation of this IpInfoResultV6.  # noqa: E501
        :type: IPLocation
        """

        self._geolocation = geolocation

    @property
    def asn(self):
        """Gets the asn of this IpInfoResultV6.  # noqa: E501


        :return: The asn of this IpInfoResultV6.  # noqa: E501
        :rtype: ASN
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this IpInfoResultV6.


        :param asn: The asn of this IpInfoResultV6.  # noqa: E501
        :type: ASN
        """

        self._asn = asn

    @property
    def datacenter(self):
        """Gets the datacenter of this IpInfoResultV6.  # noqa: E501


        :return: The datacenter of this IpInfoResultV6.  # noqa: E501
        :rtype: DataCenterInfo
        """
        return self._datacenter

    @datacenter.setter
    def datacenter(self, datacenter):
        """Sets the datacenter of this IpInfoResultV6.


        :param datacenter: The datacenter of this IpInfoResultV6.  # noqa: E501
        :type: DataCenterInfo
        """

        self._datacenter = datacenter

    @property
    def data_center(self):
        """Gets the data_center of this IpInfoResultV6.  # noqa: E501


        :return: The data_center of this IpInfoResultV6.  # noqa: E501
        :rtype: DataCenter
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """Sets the data_center of this IpInfoResultV6.


        :param data_center: The data_center of this IpInfoResultV6.  # noqa: E501
        :type: DataCenter
        """

        self._data_center = data_center

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
        if issubclass(IpInfoResultV6, dict):
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
        if not isinstance(other, IpInfoResultV6):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpInfoResultV6):
            return True

        return self.to_dict() != other.to_dict()
