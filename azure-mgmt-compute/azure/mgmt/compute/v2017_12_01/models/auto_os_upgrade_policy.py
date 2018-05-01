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


class AutoOSUpgradePolicy(Model):
    """The configuration parameters used for performing automatic OS upgrade.

    :param disable_auto_rollback: whether OS image rollback feature should be
     disabled.
    :type disable_auto_rollback: bool
    """

    _attribute_map = {
        'disable_auto_rollback': {'key': 'disableAutoRollback', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(AutoOSUpgradePolicy, self).__init__(**kwargs)
        self.disable_auto_rollback = kwargs.get('disable_auto_rollback', None)