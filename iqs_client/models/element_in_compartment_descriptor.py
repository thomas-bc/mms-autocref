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


class ElementInCompartmentDescriptor(object):
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
        'compartment_uri': 'str',
        'relative_element_id': 'str'
    }

    attribute_map = {
        'compartment_uri': 'compartmentURI',
        'relative_element_id': 'relativeElementID'
    }

    def __init__(self, compartment_uri=None, relative_element_id=None):  # noqa: E501
        """ElementInCompartmentDescriptor - a model defined in OpenAPI"""  # noqa: E501

        self._compartment_uri = None
        self._relative_element_id = None
        self.discriminator = None

        self.compartment_uri = compartment_uri
        self.relative_element_id = relative_element_id

    @property
    def compartment_uri(self):
        """Gets the compartment_uri of this ElementInCompartmentDescriptor.  # noqa: E501


        :return: The compartment_uri of this ElementInCompartmentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._compartment_uri

    @compartment_uri.setter
    def compartment_uri(self, compartment_uri):
        """Sets the compartment_uri of this ElementInCompartmentDescriptor.


        :param compartment_uri: The compartment_uri of this ElementInCompartmentDescriptor.  # noqa: E501
        :type: str
        """
        if compartment_uri is None:
            raise ValueError("Invalid value for `compartment_uri`, must not be `None`")  # noqa: E501

        self._compartment_uri = compartment_uri

    @property
    def relative_element_id(self):
        """Gets the relative_element_id of this ElementInCompartmentDescriptor.  # noqa: E501


        :return: The relative_element_id of this ElementInCompartmentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._relative_element_id

    @relative_element_id.setter
    def relative_element_id(self, relative_element_id):
        """Sets the relative_element_id of this ElementInCompartmentDescriptor.


        :param relative_element_id: The relative_element_id of this ElementInCompartmentDescriptor.  # noqa: E501
        :type: str
        """
        if relative_element_id is None:
            raise ValueError("Invalid value for `relative_element_id`, must not be `None`")  # noqa: E501

        self._relative_element_id = relative_element_id

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
        if not isinstance(other, ElementInCompartmentDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
