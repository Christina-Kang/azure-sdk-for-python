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


class Endpoints(Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or
    table object.

    :param blob: The blob endpoint.
    :type blob: str
    :param queue: The queue endpoint.
    :type queue: str
    :param table: The table endpoint.
    :type table: str
    :param file: The file endpoint.
    :type file: str
    """

    _attribute_map = {
        'blob': {'key': 'blob', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'str'},
        'table': {'key': 'table', 'type': 'str'},
        'file': {'key': 'file', 'type': 'str'},
    }

    def __init__(self, blob=None, queue=None, table=None, file=None):
        super(Endpoints, self).__init__()
        self.blob = blob
        self.queue = queue
        self.table = table
        self.file = file
