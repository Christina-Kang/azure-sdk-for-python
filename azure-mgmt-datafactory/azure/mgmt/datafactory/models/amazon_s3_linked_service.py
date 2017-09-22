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

from .linked_service import LinkedService


class AmazonS3LinkedService(LinkedService):
    """Linked service for Amazon S3.

    :param connect_via: The integration runtime reference.
    :type connect_via: :class:`IntegrationRuntimeReference
     <azure.mgmt.datafactory.models.IntegrationRuntimeReference>`
    :param description: Linked service description.
    :type description: str
    :param type: Polymorphic Discriminator
    :type type: str
    :param access_key_id: The access key identifier of the Amazon S3 Identity
     and Access Management (IAM) user. Type: string (or Expression with
     resultType string).
    :type access_key_id: object
    :param secret_access_key: The secret access key of the Amazon S3 Identity
     and Access Management (IAM) user.
    :type secret_access_key: :class:`SecureString
     <azure.mgmt.datafactory.models.SecureString>`
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'access_key_id': {'key': 'typeProperties.accessKeyId', 'type': 'object'},
        'secret_access_key': {'key': 'typeProperties.secretAccessKey', 'type': 'SecureString'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, connect_via=None, description=None, access_key_id=None, secret_access_key=None, encrypted_credential=None):
        super(AmazonS3LinkedService, self).__init__(connect_via=connect_via, description=description)
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.encrypted_credential = encrypted_credential
        self.type = 'AmazonS3'