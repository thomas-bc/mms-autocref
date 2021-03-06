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


class ImpactAnalysisResourceStatistics(object):
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
        'results_filtered': 'bool',
        'number_of_resources': 'int',
        'number_of_filtered_resources': 'int'
    }

    attribute_map = {
        'results_filtered': 'resultsFiltered',
        'number_of_resources': 'numberOfResources',
        'number_of_filtered_resources': 'numberOfFilteredResources'
    }

    def __init__(self, results_filtered=None, number_of_resources=None, number_of_filtered_resources=None):  # noqa: E501
        """ImpactAnalysisResourceStatistics - a model defined in OpenAPI"""  # noqa: E501

        self._results_filtered = None
        self._number_of_resources = None
        self._number_of_filtered_resources = None
        self.discriminator = None

        self.results_filtered = results_filtered
        self.number_of_resources = number_of_resources
        self.number_of_filtered_resources = number_of_filtered_resources

    @property
    def results_filtered(self):
        """Gets the results_filtered of this ImpactAnalysisResourceStatistics.  # noqa: E501


        :return: The results_filtered of this ImpactAnalysisResourceStatistics.  # noqa: E501
        :rtype: bool
        """
        return self._results_filtered

    @results_filtered.setter
    def results_filtered(self, results_filtered):
        """Sets the results_filtered of this ImpactAnalysisResourceStatistics.


        :param results_filtered: The results_filtered of this ImpactAnalysisResourceStatistics.  # noqa: E501
        :type: bool
        """
        if results_filtered is None:
            raise ValueError("Invalid value for `results_filtered`, must not be `None`")  # noqa: E501

        self._results_filtered = results_filtered

    @property
    def number_of_resources(self):
        """Gets the number_of_resources of this ImpactAnalysisResourceStatistics.  # noqa: E501


        :return: The number_of_resources of this ImpactAnalysisResourceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._number_of_resources

    @number_of_resources.setter
    def number_of_resources(self, number_of_resources):
        """Sets the number_of_resources of this ImpactAnalysisResourceStatistics.


        :param number_of_resources: The number_of_resources of this ImpactAnalysisResourceStatistics.  # noqa: E501
        :type: int
        """
        if number_of_resources is None:
            raise ValueError("Invalid value for `number_of_resources`, must not be `None`")  # noqa: E501

        self._number_of_resources = number_of_resources

    @property
    def number_of_filtered_resources(self):
        """Gets the number_of_filtered_resources of this ImpactAnalysisResourceStatistics.  # noqa: E501


        :return: The number_of_filtered_resources of this ImpactAnalysisResourceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._number_of_filtered_resources

    @number_of_filtered_resources.setter
    def number_of_filtered_resources(self, number_of_filtered_resources):
        """Sets the number_of_filtered_resources of this ImpactAnalysisResourceStatistics.


        :param number_of_filtered_resources: The number_of_filtered_resources of this ImpactAnalysisResourceStatistics.  # noqa: E501
        :type: int
        """
        if number_of_filtered_resources is None:
            raise ValueError("Invalid value for `number_of_filtered_resources`, must not be `None`")  # noqa: E501

        self._number_of_filtered_resources = number_of_filtered_resources

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
        if not isinstance(other, ImpactAnalysisResourceStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
