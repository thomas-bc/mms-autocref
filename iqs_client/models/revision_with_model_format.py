# coding: utf-8

"""
    IncQuery Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RevisionWithModelFormat(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'revision_descriptor': 'RevisionDescriptor',
        'format': 'ModelRepresentationFormat'
    }

    attribute_map = {
        'revision_descriptor': 'revisionDescriptor',
        'format': 'format'
    }

    def __init__(self, revision_descriptor=None, format=None):  # noqa: E501
        """RevisionWithModelFormat - a model defined in OpenAPI"""  # noqa: E501

        self._revision_descriptor = None
        self._format = None
        self.discriminator = None

        self.revision_descriptor = revision_descriptor
        self.format = format

    @property
    def revision_descriptor(self):
        """Gets the revision_descriptor of this RevisionWithModelFormat.  # noqa: E501


        :return: The revision_descriptor of this RevisionWithModelFormat.  # noqa: E501
        :rtype: RevisionDescriptor
        """
        return self._revision_descriptor

    @revision_descriptor.setter
    def revision_descriptor(self, revision_descriptor):
        """Sets the revision_descriptor of this RevisionWithModelFormat.


        :param revision_descriptor: The revision_descriptor of this RevisionWithModelFormat.  # noqa: E501
        :type: RevisionDescriptor
        """
        if revision_descriptor is None:
            raise ValueError("Invalid value for `revision_descriptor`, must not be `None`")  # noqa: E501

        self._revision_descriptor = revision_descriptor

    @property
    def format(self):
        """Gets the format of this RevisionWithModelFormat.  # noqa: E501


        :return: The format of this RevisionWithModelFormat.  # noqa: E501
        :rtype: ModelRepresentationFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this RevisionWithModelFormat.


        :param format: The format of this RevisionWithModelFormat.  # noqa: E501
        :type: ModelRepresentationFormat
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501

        self._format = format

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RevisionWithModelFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
