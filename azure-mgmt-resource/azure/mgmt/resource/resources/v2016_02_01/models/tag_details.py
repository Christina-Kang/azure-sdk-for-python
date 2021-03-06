# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TagDetails(Model):
    """Tag details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The tag ID.
    :vartype id: str
    :param tag_name: The tag name.
    :type tag_name: str
    :param count: The tag count.
    :type count: ~azure.mgmt.resource.resources.v2016_02_01.models.TagCount
    :param values: The list of tag values.
    :type values:
     list[~azure.mgmt.resource.resources.v2016_02_01.models.TagValue]
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tag_name': {'key': 'tagName', 'type': 'str'},
        'count': {'key': 'count', 'type': 'TagCount'},
        'values': {'key': 'values', 'type': '[TagValue]'},
    }

    def __init__(self, **kwargs):
        super(TagDetails, self).__init__(**kwargs)
        self.id = None
        self.tag_name = kwargs.get('tag_name', None)
        self.count = kwargs.get('count', None)
        self.values = kwargs.get('values', None)
