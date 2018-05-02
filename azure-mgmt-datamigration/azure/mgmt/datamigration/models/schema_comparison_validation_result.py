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


class SchemaComparisonValidationResult(Model):
    """Results for schema comparison between the source and target.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar schema_differences: List of schema differences between the source
     and target databases
    :vartype schema_differences:
     ~azure.mgmt.datamigration.models.SchemaComparisonValidationResultType
    :ivar validation_errors: List of errors that happened while performing
     schema compare validation
    :vartype validation_errors:
     ~azure.mgmt.datamigration.models.ValidationError
    :param source_database_object_count: Count of source database objects
    :type source_database_object_count: dict[str, long]
    :param target_database_object_count: Count of target database objects
    :type target_database_object_count: dict[str, long]
    """

    _validation = {
        'schema_differences': {'readonly': True},
        'validation_errors': {'readonly': True},
    }

    _attribute_map = {
        'schema_differences': {'key': 'schemaDifferences', 'type': 'SchemaComparisonValidationResultType'},
        'validation_errors': {'key': 'validationErrors', 'type': 'ValidationError'},
        'source_database_object_count': {'key': 'sourceDatabaseObjectCount', 'type': '{long}'},
        'target_database_object_count': {'key': 'targetDatabaseObjectCount', 'type': '{long}'},
    }

    def __init__(self, **kwargs):
        super(SchemaComparisonValidationResult, self).__init__(**kwargs)
        self.schema_differences = None
        self.validation_errors = None
        self.source_database_object_count = kwargs.get('source_database_object_count', None)
        self.target_database_object_count = kwargs.get('target_database_object_count', None)
