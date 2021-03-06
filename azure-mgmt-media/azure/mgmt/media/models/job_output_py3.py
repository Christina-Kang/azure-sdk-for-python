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


class JobOutput(Model):
    """Describes all the properties of a JobOutput.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: JobOutputAsset

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar error: If the JobOutput is in the Error state, it contains the
     details of the error.
    :vartype error: ~azure.mgmt.media.models.JobError
    :ivar state: Describes the state of the JobOutput. Possible values
     include: 'Canceled', 'Canceling', 'Error', 'Finished', 'Processing',
     'Queued', 'Scheduled'
    :vartype state: str or ~azure.mgmt.media.models.JobState
    :ivar progress: If the JobOutput is in a Processing state, this contains
     the job completion percentage.  The value is an estimate and not intended
     to be used to predict job completion times. To determine if the JobOutput
     is complete, use the State property.
    :vartype progress: int
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    """

    _validation = {
        'error': {'readonly': True},
        'state': {'readonly': True},
        'progress': {'readonly': True},
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'JobError'},
        'state': {'key': 'state', 'type': 'JobState'},
        'progress': {'key': 'progress', 'type': 'int'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
    }

    _subtype_map = {
        'odatatype': {'#Microsoft.Media.JobOutputAsset': 'JobOutputAsset'}
    }

    def __init__(self, **kwargs) -> None:
        super(JobOutput, self).__init__(**kwargs)
        self.error = None
        self.state = None
        self.progress = None
        self.odatatype = None
