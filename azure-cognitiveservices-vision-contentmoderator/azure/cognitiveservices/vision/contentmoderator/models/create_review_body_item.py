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


class CreateReviewBodyItem(Model):
    """Schema items of the body.

    :param type: Type of the content. Possible values include: 'Image', 'Text'
    :type type: str or
     ~azure.cognitiveservices.vision.contentmoderator.models.enum
    :param content: Content to review.
    :type content: str
    :param content_id: Content Identifier.
    :type content_id: str
    :param callback_endpoint: Optional CallbackEndpoint.
    :type callback_endpoint: str
    :param metadata: Optional metadata details.
    :type metadata:
     list[~azure.cognitiveservices.vision.contentmoderator.models.CreateReviewBodyItemMetadataItem]
    """

    _validation = {
        'type': {'required': True},
        'content': {'required': True},
        'content_id': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'Type', 'type': 'str'},
        'content': {'key': 'Content', 'type': 'str'},
        'content_id': {'key': 'ContentId', 'type': 'str'},
        'callback_endpoint': {'key': 'CallbackEndpoint', 'type': 'str'},
        'metadata': {'key': 'Metadata', 'type': '[CreateReviewBodyItemMetadataItem]'},
    }

    def __init__(self, type, content, content_id, callback_endpoint=None, metadata=None):
        super(CreateReviewBodyItem, self).__init__()
        self.type = type
        self.content = content
        self.content_id = content_id
        self.callback_endpoint = callback_endpoint
        self.metadata = metadata
