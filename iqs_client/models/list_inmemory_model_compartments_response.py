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


class ListInmemoryModelCompartmentsResponse(object):
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
        'inmemory_model_compartments': 'list[ModelCompartment]'
    }

    attribute_map = {
        'inmemory_model_compartments': 'inmemoryModelCompartments'
    }

    def __init__(self, inmemory_model_compartments=None):  # noqa: E501
        """ListInmemoryModelCompartmentsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._inmemory_model_compartments = None
        self.discriminator = None

        self.inmemory_model_compartments = inmemory_model_compartments

    @property
    def inmemory_model_compartments(self):
        """Gets the inmemory_model_compartments of this ListInmemoryModelCompartmentsResponse.  # noqa: E501

        List of model compartments   # noqa: E501

        :return: The inmemory_model_compartments of this ListInmemoryModelCompartmentsResponse.  # noqa: E501
        :rtype: list[ModelCompartment]
        """
        return self._inmemory_model_compartments

    @inmemory_model_compartments.setter
    def inmemory_model_compartments(self, inmemory_model_compartments):
        """Sets the inmemory_model_compartments of this ListInmemoryModelCompartmentsResponse.

        List of model compartments   # noqa: E501

        :param inmemory_model_compartments: The inmemory_model_compartments of this ListInmemoryModelCompartmentsResponse.  # noqa: E501
        :type: list[ModelCompartment]
        """
        if inmemory_model_compartments is None:
            raise ValueError("Invalid value for `inmemory_model_compartments`, must not be `None`")  # noqa: E501

        self._inmemory_model_compartments = inmemory_model_compartments

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
        if not isinstance(other, ListInmemoryModelCompartmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
