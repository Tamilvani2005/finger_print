# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import Dict, List  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel


class VpnResultMethods(BaseModel):
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
        'timezone_mismatch': 'bool',
        'public_vpn': 'bool',
        'auxiliary_mobile': 'bool',
        'os_mismatch': 'bool'
    }

    attribute_map = {
        'timezone_mismatch': 'timezoneMismatch',
        'public_vpn': 'publicVPN',
        'auxiliary_mobile': 'auxiliaryMobile',
        'os_mismatch': 'osMismatch'
    }

    def __init__(self, timezone_mismatch=None, public_vpn=None, auxiliary_mobile=None, os_mismatch=None):  # noqa: E501
        """VpnResultMethods - a model defined in Swagger"""  # noqa: E501
        self._timezone_mismatch = None
        self._public_vpn = None
        self._auxiliary_mobile = None
        self._os_mismatch = None
        self.discriminator = None
        self.timezone_mismatch = timezone_mismatch
        self.public_vpn = public_vpn
        self.auxiliary_mobile = auxiliary_mobile
        self.os_mismatch = os_mismatch

    @property
    def timezone_mismatch(self) -> bool:
        """Gets the timezone_mismatch of this VpnResultMethods.  # noqa: E501

        The browser timezone doesn't match the timezone inferred from the request IP address.  # noqa: E501

        :return: The timezone_mismatch of this VpnResultMethods.  # noqa: E501
        """
        return self._timezone_mismatch

    @timezone_mismatch.setter
    def timezone_mismatch(self, timezone_mismatch: bool):
        """Sets the timezone_mismatch of this VpnResultMethods.

        The browser timezone doesn't match the timezone inferred from the request IP address.  # noqa: E501

        :param timezone_mismatch: The timezone_mismatch of this VpnResultMethods.  # noqa: E501
        """
        if timezone_mismatch is None:
            raise ValueError("Invalid value for `timezone_mismatch`, must not be `None`")  # noqa: E501

        self._timezone_mismatch = timezone_mismatch

    @property
    def public_vpn(self) -> bool:
        """Gets the public_vpn of this VpnResultMethods.  # noqa: E501

        Request IP address is owned and used by a public VPN service provider.  # noqa: E501

        :return: The public_vpn of this VpnResultMethods.  # noqa: E501
        """
        return self._public_vpn

    @public_vpn.setter
    def public_vpn(self, public_vpn: bool):
        """Sets the public_vpn of this VpnResultMethods.

        Request IP address is owned and used by a public VPN service provider.  # noqa: E501

        :param public_vpn: The public_vpn of this VpnResultMethods.  # noqa: E501
        """
        if public_vpn is None:
            raise ValueError("Invalid value for `public_vpn`, must not be `None`")  # noqa: E501

        self._public_vpn = public_vpn

    @property
    def auxiliary_mobile(self) -> bool:
        """Gets the auxiliary_mobile of this VpnResultMethods.  # noqa: E501

        This method applies to mobile devices only. Indicates the result of additional methods used to detect a VPN in mobile devices.  # noqa: E501

        :return: The auxiliary_mobile of this VpnResultMethods.  # noqa: E501
        """
        return self._auxiliary_mobile

    @auxiliary_mobile.setter
    def auxiliary_mobile(self, auxiliary_mobile: bool):
        """Sets the auxiliary_mobile of this VpnResultMethods.

        This method applies to mobile devices only. Indicates the result of additional methods used to detect a VPN in mobile devices.  # noqa: E501

        :param auxiliary_mobile: The auxiliary_mobile of this VpnResultMethods.  # noqa: E501
        """
        if auxiliary_mobile is None:
            raise ValueError("Invalid value for `auxiliary_mobile`, must not be `None`")  # noqa: E501

        self._auxiliary_mobile = auxiliary_mobile

    @property
    def os_mismatch(self) -> bool:
        """Gets the os_mismatch of this VpnResultMethods.  # noqa: E501

        The browser runs on a different operating system than the operating system inferred from the  request network signature.  # noqa: E501

        :return: The os_mismatch of this VpnResultMethods.  # noqa: E501
        """
        return self._os_mismatch

    @os_mismatch.setter
    def os_mismatch(self, os_mismatch: bool):
        """Sets the os_mismatch of this VpnResultMethods.

        The browser runs on a different operating system than the operating system inferred from the  request network signature.  # noqa: E501

        :param os_mismatch: The os_mismatch of this VpnResultMethods.  # noqa: E501
        """
        if os_mismatch is None:
            raise ValueError("Invalid value for `os_mismatch`, must not be `None`")  # noqa: E501

        self._os_mismatch = os_mismatch

