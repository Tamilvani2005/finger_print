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


class EventUpdateRequest(BaseModel):
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
        'linked_id': 'str',
        'tag': 'object',
        'suspect': 'bool'
    }

    attribute_map = {
        'linked_id': 'linkedId',
        'tag': 'tag',
        'suspect': 'suspect'
    }

    def __init__(self, linked_id=None, tag=None, suspect=None):  # noqa: E501
        """EventUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._linked_id = None
        self._tag = None
        self._suspect = None
        self.discriminator = None
        if linked_id is not None:
            self.linked_id = linked_id
        if tag is not None:
            self.tag = tag
        if suspect is not None:
            self.suspect = suspect

    @property
    def linked_id(self) -> str:
        """Gets the linked_id of this EventUpdateRequest.  # noqa: E501

        LinkedID value to assign to the existing event  # noqa: E501

        :return: The linked_id of this EventUpdateRequest.  # noqa: E501
        """
        return self._linked_id

    @linked_id.setter
    def linked_id(self, linked_id: str):
        """Sets the linked_id of this EventUpdateRequest.

        LinkedID value to assign to the existing event  # noqa: E501

        :param linked_id: The linked_id of this EventUpdateRequest.  # noqa: E501
        """

        self._linked_id = linked_id

    @property
    def tag(self) -> object:
        """Gets the tag of this EventUpdateRequest.  # noqa: E501

        Full `tag` value to be set to the existing event. Replaces any existing `tag` payload completely.  # noqa: E501

        :return: The tag of this EventUpdateRequest.  # noqa: E501
        """
        return self._tag

    @tag.setter
    def tag(self, tag: object):
        """Sets the tag of this EventUpdateRequest.

        Full `tag` value to be set to the existing event. Replaces any existing `tag` payload completely.  # noqa: E501

        :param tag: The tag of this EventUpdateRequest.  # noqa: E501
        """

        self._tag = tag

    @property
    def suspect(self) -> bool:
        """Gets the suspect of this EventUpdateRequest.  # noqa: E501

        Suspect flag indicating observed suspicious or fraudulent event  # noqa: E501

        :return: The suspect of this EventUpdateRequest.  # noqa: E501
        """
        return self._suspect

    @suspect.setter
    def suspect(self, suspect: bool):
        """Sets the suspect of this EventUpdateRequest.

        Suspect flag indicating observed suspicious or fraudulent event  # noqa: E501

        :param suspect: The suspect of this EventUpdateRequest.  # noqa: E501
        """

        self._suspect = suspect

