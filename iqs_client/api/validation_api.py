# coding: utf-8

"""
    IncQuery Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.12.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from iqs_client.api_client import ApiClient


class ValidationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def validate_model_compartment(self, model_compartment, **kwargs):  # noqa: E501
        """Validate rules that are defined by queries contained by loaded compartment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_model_compartment(model_compartment, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelCompartment model_compartment: Model compartment descriptor.  (required)
        :return: GenericValidationResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_model_compartment_with_http_info(model_compartment, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_model_compartment_with_http_info(model_compartment, **kwargs)  # noqa: E501
            return data

    def validate_model_compartment_with_http_info(self, model_compartment, **kwargs):  # noqa: E501
        """Validate rules that are defined by queries contained by loaded compartment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_model_compartment_with_http_info(model_compartment, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelCompartment model_compartment: Model compartment descriptor.  (required)
        :return: GenericValidationResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['model_compartment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_model_compartment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_compartment' is set
        if ('model_compartment' not in local_var_params or
                local_var_params['model_compartment'] is None):
            raise ValueError("Missing the required parameter `model_compartment` when calling `validate_model_compartment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model_compartment' in local_var_params:
            body_params = local_var_params['model_compartment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/validation.validateModelCompartment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GenericValidationResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
