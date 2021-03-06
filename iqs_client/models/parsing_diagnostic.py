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


class ParsingDiagnostic(object):
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
        'length': 'int',
        'line_number': 'int',
        'offset': 'int',
        'column': 'int',
        'code': 'str',
        'message': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'length': 'length',
        'line_number': 'lineNumber',
        'offset': 'offset',
        'column': 'column',
        'code': 'code',
        'message': 'message',
        'severity': 'severity'
    }

    def __init__(self, length=None, line_number=None, offset=None, column=None, code=None, message=None, severity=None):  # noqa: E501
        """ParsingDiagnostic - a model defined in OpenAPI"""  # noqa: E501

        self._length = None
        self._line_number = None
        self._offset = None
        self._column = None
        self._code = None
        self._message = None
        self._severity = None
        self.discriminator = None

        self.length = length
        self.line_number = line_number
        self.offset = offset
        self.column = column
        self.code = code
        self.message = message
        self.severity = severity

    @property
    def length(self):
        """Gets the length of this ParsingDiagnostic.  # noqa: E501


        :return: The length of this ParsingDiagnostic.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this ParsingDiagnostic.


        :param length: The length of this ParsingDiagnostic.  # noqa: E501
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def line_number(self):
        """Gets the line_number of this ParsingDiagnostic.  # noqa: E501


        :return: The line_number of this ParsingDiagnostic.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this ParsingDiagnostic.


        :param line_number: The line_number of this ParsingDiagnostic.  # noqa: E501
        :type: int
        """
        if line_number is None:
            raise ValueError("Invalid value for `line_number`, must not be `None`")  # noqa: E501

        self._line_number = line_number

    @property
    def offset(self):
        """Gets the offset of this ParsingDiagnostic.  # noqa: E501


        :return: The offset of this ParsingDiagnostic.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ParsingDiagnostic.


        :param offset: The offset of this ParsingDiagnostic.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def column(self):
        """Gets the column of this ParsingDiagnostic.  # noqa: E501


        :return: The column of this ParsingDiagnostic.  # noqa: E501
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this ParsingDiagnostic.


        :param column: The column of this ParsingDiagnostic.  # noqa: E501
        :type: int
        """
        if column is None:
            raise ValueError("Invalid value for `column`, must not be `None`")  # noqa: E501

        self._column = column

    @property
    def code(self):
        """Gets the code of this ParsingDiagnostic.  # noqa: E501


        :return: The code of this ParsingDiagnostic.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ParsingDiagnostic.


        :param code: The code of this ParsingDiagnostic.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this ParsingDiagnostic.  # noqa: E501


        :return: The message of this ParsingDiagnostic.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ParsingDiagnostic.


        :param message: The message of this ParsingDiagnostic.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def severity(self):
        """Gets the severity of this ParsingDiagnostic.  # noqa: E501


        :return: The severity of this ParsingDiagnostic.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ParsingDiagnostic.


        :param severity: The severity of this ParsingDiagnostic.  # noqa: E501
        :type: str
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501
        allowed_values = ["ERROR", "WARNING"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

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
        if not isinstance(other, ParsingDiagnostic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
