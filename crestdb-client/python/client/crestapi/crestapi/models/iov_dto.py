# coding: utf-8

"""
    CrestDB REST API

    Crest Rest Api to manage data for calibration files.

    OpenAPI spec version: 2.0
    Contact: andrea.formica@cern.ch
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IovDto(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, tag_name=None, since=None, insertion_time=None, payload_hash=None):
        """
        IovDto - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'tag_name': 'str',
            'since': 'float',
            'insertion_time': 'datetime',
            'payload_hash': 'str'
        }

        self.attribute_map = {
            'tag_name': 'tagName',
            'since': 'since',
            'insertion_time': 'insertionTime',
            'payload_hash': 'payloadHash'
        }

        self._tag_name = tag_name
        self._since = since
        self._insertion_time = insertion_time
        self._payload_hash = payload_hash

    @property
    def tag_name(self):
        """
        Gets the tag_name of this IovDto.

        :return: The tag_name of this IovDto.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """
        Sets the tag_name of this IovDto.

        :param tag_name: The tag_name of this IovDto.
        :type: str
        """

        self._tag_name = tag_name

    @property
    def since(self):
        """
        Gets the since of this IovDto.

        :return: The since of this IovDto.
        :rtype: float
        """
        return self._since

    @since.setter
    def since(self, since):
        """
        Sets the since of this IovDto.

        :param since: The since of this IovDto.
        :type: float
        """

        self._since = since

    @property
    def insertion_time(self):
        """
        Gets the insertion_time of this IovDto.

        :return: The insertion_time of this IovDto.
        :rtype: datetime
        """
        return self._insertion_time

    @insertion_time.setter
    def insertion_time(self, insertion_time):
        """
        Sets the insertion_time of this IovDto.

        :param insertion_time: The insertion_time of this IovDto.
        :type: datetime
        """

        self._insertion_time = insertion_time

    @property
    def payload_hash(self):
        """
        Gets the payload_hash of this IovDto.

        :return: The payload_hash of this IovDto.
        :rtype: str
        """
        return self._payload_hash

    @payload_hash.setter
    def payload_hash(self, payload_hash):
        """
        Sets the payload_hash of this IovDto.

        :param payload_hash: The payload_hash of this IovDto.
        :type: str
        """

        self._payload_hash = payload_hash

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, IovDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
