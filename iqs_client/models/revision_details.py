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


class RevisionDetails(object):
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
        'workspace_title': 'str',
        'resource_title': 'str',
        'branch_title': 'str'
    }

    attribute_map = {
        'workspace_title': 'workspaceTitle',
        'resource_title': 'resourceTitle',
        'branch_title': 'branchTitle'
    }

    def __init__(self, workspace_title=None, resource_title=None, branch_title=None):  # noqa: E501
        """RevisionDetails - a model defined in OpenAPI"""  # noqa: E501

        self._workspace_title = None
        self._resource_title = None
        self._branch_title = None
        self.discriminator = None

        self.workspace_title = workspace_title
        self.resource_title = resource_title
        self.branch_title = branch_title

    @property
    def workspace_title(self):
        """Gets the workspace_title of this RevisionDetails.  # noqa: E501


        :return: The workspace_title of this RevisionDetails.  # noqa: E501
        :rtype: str
        """
        return self._workspace_title

    @workspace_title.setter
    def workspace_title(self, workspace_title):
        """Sets the workspace_title of this RevisionDetails.


        :param workspace_title: The workspace_title of this RevisionDetails.  # noqa: E501
        :type: str
        """
        if workspace_title is None:
            raise ValueError("Invalid value for `workspace_title`, must not be `None`")  # noqa: E501

        self._workspace_title = workspace_title

    @property
    def resource_title(self):
        """Gets the resource_title of this RevisionDetails.  # noqa: E501


        :return: The resource_title of this RevisionDetails.  # noqa: E501
        :rtype: str
        """
        return self._resource_title

    @resource_title.setter
    def resource_title(self, resource_title):
        """Sets the resource_title of this RevisionDetails.


        :param resource_title: The resource_title of this RevisionDetails.  # noqa: E501
        :type: str
        """
        if resource_title is None:
            raise ValueError("Invalid value for `resource_title`, must not be `None`")  # noqa: E501

        self._resource_title = resource_title

    @property
    def branch_title(self):
        """Gets the branch_title of this RevisionDetails.  # noqa: E501


        :return: The branch_title of this RevisionDetails.  # noqa: E501
        :rtype: str
        """
        return self._branch_title

    @branch_title.setter
    def branch_title(self, branch_title):
        """Sets the branch_title of this RevisionDetails.


        :param branch_title: The branch_title of this RevisionDetails.  # noqa: E501
        :type: str
        """
        if branch_title is None:
            raise ValueError("Invalid value for `branch_title`, must not be `None`")  # noqa: E501

        self._branch_title = branch_title

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
        if not isinstance(other, RevisionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other