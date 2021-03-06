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


class PayloadDto(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, hash=None, version=None, object_type=None, data=None, streamer_info=None, insertion_time=None):
        """
        PayloadDto - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'hash': 'str',
            'version': 'str',
            'object_type': 'str',
            'data': 'str',
            'streamer_info': 'str',
            'insertion_time': 'datetime'
        }

        self.attribute_map = {
            'hash': 'hash',
            'version': 'version',
            'object_type': 'objectType',
            'data': 'data',
            'streamer_info': 'streamerInfo',
            'insertion_time': 'insertionTime'
        }

        self._hash = hash
        self._version = version
        self._object_type = object_type
        self._data = data
        self._streamer_info = streamer_info
        self._insertion_time = insertion_time

    @property
    def hash(self):
        """
        Gets the hash of this PayloadDto.

        :return: The hash of this PayloadDto.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this PayloadDto.

        :param hash: The hash of this PayloadDto.
        :type: str
        """

        self._hash = hash

    @property
    def version(self):
        """
        Gets the version of this PayloadDto.

        :return: The version of this PayloadDto.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PayloadDto.

        :param version: The version of this PayloadDto.
        :type: str
        """

        self._version = version

    @property
    def object_type(self):
        """
        Gets the object_type of this PayloadDto.

        :return: The object_type of this PayloadDto.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this PayloadDto.

        :param object_type: The object_type of this PayloadDto.
        :type: str
        """

        self._object_type = object_type

    @property
    def data(self):
        """
        Gets the data of this PayloadDto.

        :return: The data of this PayloadDto.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this PayloadDto.

        :param data: The data of this PayloadDto.
        :type: str
        """

        self._data = data

    @property
    def streamer_info(self):
        """
        Gets the streamer_info of this PayloadDto.

        :return: The streamer_info of this PayloadDto.
        :rtype: str
        """
        return self._streamer_info

    @streamer_info.setter
    def streamer_info(self, streamer_info):
        """
        Sets the streamer_info of this PayloadDto.

        :param streamer_info: The streamer_info of this PayloadDto.
        :type: str
        """

        self._streamer_info = streamer_info

    @property
    def insertion_time(self):
        """
        Gets the insertion_time of this PayloadDto.

        :return: The insertion_time of this PayloadDto.
        :rtype: datetime
        """
        return self._insertion_time

    @insertion_time.setter
    def insertion_time(self, insertion_time):
        """
        Sets the insertion_time of this PayloadDto.

        :param insertion_time: The insertion_time of this PayloadDto.
        :type: datetime
        """

        self._insertion_time = insertion_time

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
        if not isinstance(other, PayloadDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
