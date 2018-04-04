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

from .certificate_item import CertificateItem


class DeletedCertificateItem(CertificateItem):
    """The deleted certificate item containing metadata about the deleted
    certificate.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Certificate identifier.
    :type id: str
    :param attributes: The certificate management attributes.
    :type attributes: ~azure.keyvault.models.CertificateAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    :param x509_thumbprint: Thumbprint of the certificate.
    :type x509_thumbprint: bytes
    :param recovery_id: The url of the recovery object, used to identify and
     recover the deleted certificate.
    :type recovery_id: str
    :ivar scheduled_purge_date: The time when the certificate is scheduled to
     be purged, in UTC
    :vartype scheduled_purge_date: datetime
    :ivar deleted_date: The time when the certificate was deleted, in UTC
    :vartype deleted_date: datetime
    """

    _validation = {
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'x509_thumbprint': {'key': 'x5t', 'type': 'base64'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(self, *, id: str=None, attributes=None, tags=None, x509_thumbprint: bytes=None, recovery_id: str=None, **kwargs) -> None:
        super(DeletedCertificateItem, self).__init__(id=id, attributes=attributes, tags=tags, x509_thumbprint=x509_thumbprint, **kwargs)
        self.recovery_id = recovery_id
        self.scheduled_purge_date = None
        self.deleted_date = None