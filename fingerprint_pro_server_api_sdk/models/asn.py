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


class ASN(BaseModel):
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
        'asn': 'str',
        'network': 'str',
        'name': 'str'
    }

    attribute_map = {
        'asn': 'asn',
        'network': 'network',
        'name': 'name'
    }

    def __init__(self, asn=None, network=None, name=None):  # noqa: E501
        """ASN - a model defined in Swagger"""  # noqa: E501
        self._asn = None
        self._network = None
        self._name = None
        self.discriminator = None
        self.asn = asn
        self.network = network
        if name is not None:
            self.name = name

    @property
    def asn(self):
        """Gets the asn of this ASN.  # noqa: E501


        :return: The asn of this ASN.  # noqa: E501
        :rtype: str
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this ASN.


        :param asn: The asn of this ASN.  # noqa: E501
        :type: str
        """
        if asn is None:
            raise ValueError("Invalid value for `asn`, must not be `None`")  # noqa: E501

        self._asn = asn

    @property
    def network(self):
        """Gets the network of this ASN.  # noqa: E501


        :return: The network of this ASN.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this ASN.


        :param network: The network of this ASN.  # noqa: E501
        :type: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def name(self):
        """Gets the name of this ASN.  # noqa: E501


        :return: The name of this ASN.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ASN.


        :param name: The name of this ASN.  # noqa: E501
        :type: str
        """

        self._name = name

