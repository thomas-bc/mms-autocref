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


class RevisionDescriptorWithURI(object):
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
        'revision_number': 'int',
        'branch_id': 'str',
        'resource_id': 'str',
        'workspace_id': 'str',
        'compartment_uri': 'str',
        'author': 'str'
    }

    attribute_map = {
        'revision_number': 'revisionNumber',
        'branch_id': 'branchId',
        'resource_id': 'resourceId',
        'workspace_id': 'workspaceId',
        'compartment_uri': 'compartmentURI',
        'author': 'author'
    }

    def __init__(self, revision_number=None, branch_id=None, resource_id=None, workspace_id=None, compartment_uri=None, author=None):  # noqa: E501
        """RevisionDescriptorWithURI - a model defined in OpenAPI"""  # noqa: E501

        self._revision_number = None
        self._branch_id = None
        self._resource_id = None
        self._workspace_id = None
        self._compartment_uri = None
        self._author = None
        self.discriminator = None

        self.revision_number = revision_number
        self.branch_id = branch_id
        self.resource_id = resource_id
        self.workspace_id = workspace_id
        self.compartment_uri = compartment_uri
        if author is not None:
            self.author = author

    @property
    def revision_number(self):
        """Gets the revision_number of this RevisionDescriptorWithURI.  # noqa: E501


        :return: The revision_number of this RevisionDescriptorWithURI.  # noqa: E501
        :rtype: int
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this RevisionDescriptorWithURI.


        :param revision_number: The revision_number of this RevisionDescriptorWithURI.  # noqa: E501
        :type: int
        """
        if revision_number is None:
            raise ValueError("Invalid value for `revision_number`, must not be `None`")  # noqa: E501

        self._revision_number = revision_number

    @property
    def branch_id(self):
        """Gets the branch_id of this RevisionDescriptorWithURI.  # noqa: E501


        :return: The branch_id of this RevisionDescriptorWithURI.  # noqa: E501
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this RevisionDescriptorWithURI.


        :param branch_id: The branch_id of this RevisionDescriptorWithURI.  # noqa: E501
        :type: str
        """
        if branch_id is None:
            raise ValueError("Invalid value for `branch_id`, must not be `None`")  # noqa: E501

        self._branch_id = branch_id

    @property
    def resource_id(self):
        """Gets the resource_id of this RevisionDescriptorWithURI.  # noqa: E501


        :return: The resource_id of this RevisionDescriptorWithURI.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this RevisionDescriptorWithURI.


        :param resource_id: The resource_id of this RevisionDescriptorWithURI.  # noqa: E501
        :type: str
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501

        self._resource_id = resource_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this RevisionDescriptorWithURI.  # noqa: E501


        :return: The workspace_id of this RevisionDescriptorWithURI.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this RevisionDescriptorWithURI.


        :param workspace_id: The workspace_id of this RevisionDescriptorWithURI.  # noqa: E501
        :type: str
        """
        if workspace_id is None:
            raise ValueError("Invalid value for `workspace_id`, must not be `None`")  # noqa: E501

        self._workspace_id = workspace_id

    @property
    def compartment_uri(self):
        """Gets the compartment_uri of this RevisionDescriptorWithURI.  # noqa: E501


        :return: The compartment_uri of this RevisionDescriptorWithURI.  # noqa: E501
        :rtype: str
        """
        return self._compartment_uri

    @compartment_uri.setter
    def compartment_uri(self, compartment_uri):
        """Sets the compartment_uri of this RevisionDescriptorWithURI.


        :param compartment_uri: The compartment_uri of this RevisionDescriptorWithURI.  # noqa: E501
        :type: str
        """
        if compartment_uri is None:
            raise ValueError("Invalid value for `compartment_uri`, must not be `None`")  # noqa: E501

        self._compartment_uri = compartment_uri

    @property
    def author(self):
        """Gets the author of this RevisionDescriptorWithURI.  # noqa: E501


        :return: The author of this RevisionDescriptorWithURI.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this RevisionDescriptorWithURI.


        :param author: The author of this RevisionDescriptorWithURI.  # noqa: E501
        :type: str
        """

        self._author = author

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
        if not isinstance(other, RevisionDescriptorWithURI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other