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


class ParsingDiagnostics(object):
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
        'errors': 'list[ParsingDiagnostic]',
        'warnings': 'list[ParsingDiagnostic]'
    }

    attribute_map = {
        'errors': 'errors',
        'warnings': 'warnings'
    }

    def __init__(self, errors=None, warnings=None):  # noqa: E501
        """ParsingDiagnostics - a model defined in OpenAPI"""  # noqa: E501

        self._errors = None
        self._warnings = None
        self.discriminator = None

        self.errors = errors
        if warnings is not None:
            self.warnings = warnings

    @property
    def errors(self):
        """Gets the errors of this ParsingDiagnostics.  # noqa: E501


        :return: The errors of this ParsingDiagnostics.  # noqa: E501
        :rtype: list[ParsingDiagnostic]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ParsingDiagnostics.


        :param errors: The errors of this ParsingDiagnostics.  # noqa: E501
        :type: list[ParsingDiagnostic]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def warnings(self):
        """Gets the warnings of this ParsingDiagnostics.  # noqa: E501


        :return: The warnings of this ParsingDiagnostics.  # noqa: E501
        :rtype: list[ParsingDiagnostic]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this ParsingDiagnostics.


        :param warnings: The warnings of this ParsingDiagnostics.  # noqa: E501
        :type: list[ParsingDiagnostic]
        """

        self._warnings = warnings

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
        if not isinstance(other, ParsingDiagnostics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
