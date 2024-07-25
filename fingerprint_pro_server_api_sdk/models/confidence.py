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

class Confidence(object):
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
        'score': 'float',
        'revision': 'str'
    }

    attribute_map = {
        'score': 'score',
        'revision': 'revision'
    }

    def __init__(self, score=None, revision=None):  # noqa: E501
        """Confidence - a model defined in Swagger"""  # noqa: E501
        self._score = None
        self._revision = None
        self.discriminator = None
        self.score = score
        if revision is not None:
            self.revision = revision

    @property
    def score(self):
        """Gets the score of this Confidence.  # noqa: E501

        The confidence score is a floating-point number between 0 and 1 that represents the probability of accurate identification.  # noqa: E501

        :return: The score of this Confidence.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Confidence.

        The confidence score is a floating-point number between 0 and 1 that represents the probability of accurate identification.  # noqa: E501

        :param score: The score of this Confidence.  # noqa: E501
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def revision(self):
        """Gets the revision of this Confidence.  # noqa: E501

        The revision name of the method used to calculate the Confidence score. This field is only present for customers who opted in to an alternative calculation method.  # noqa: E501

        :return: The revision of this Confidence.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Confidence.

        The revision name of the method used to calculate the Confidence score. This field is only present for customers who opted in to an alternative calculation method.  # noqa: E501

        :param revision: The revision of this Confidence.  # noqa: E501
        :type: str
        """

        self._revision = revision

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
        if issubclass(Confidence, dict):
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
        if not isinstance(other, Confidence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Confidence):
            return True

        return self.to_dict() != other.to_dict()
