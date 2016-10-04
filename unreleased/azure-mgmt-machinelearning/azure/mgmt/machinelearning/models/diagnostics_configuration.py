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


class DiagnosticsConfiguration(Model):
    """Diagnostics settings for an Azure ML web service.

    :param level: Level of tracing to be used: None - disables tracing; Error
     - collects only error (stderr) traces; All - collects all traces (stdout
     and stderr). Possible values include: 'None', 'Error', 'All'
    :type level: str or :class:`DiagnosticsLevel
     <azure.mgmt.machinelearning.models.DiagnosticsLevel>`
    :param expiry: Moment of time after which diagnostics are no longer
     collected. If null, diagnostic collection is not time limited.
    :type expiry: datetime
    """ 

    _validation = {
        'level': {'required': True},
    }

    _attribute_map = {
        'level': {'key': 'level', 'type': 'str'},
        'expiry': {'key': 'expiry', 'type': 'iso-8601'},
    }

    def __init__(self, level, expiry=None):
        self.level = level
        self.expiry = expiry