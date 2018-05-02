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

from .migrate_sql_server_sql_db_task_output import MigrateSqlServerSqlDbTaskOutput


class MigrateSqlServerSqlDbTaskOutputDatabaseLevel(MigrateSqlServerSqlDbTaskOutput):
    """Database level result for Sql Server to Azure Sql DB migration.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar database_name: Name of the item
    :vartype database_name: str
    :ivar started_on: Migration start time
    :vartype started_on: datetime
    :ivar ended_on: Migration end time
    :vartype ended_on: datetime
    :ivar state: Current state of migration. Possible values include: 'None',
     'InProgress', 'Failed', 'Warning', 'Completed', 'Skipped', 'Stopped'
    :vartype state: str or ~azure.mgmt.datamigration.models.MigrationState
    :ivar stage: Migration stage that this database is in. Possible values
     include: 'None', 'Initialize', 'Backup', 'FileCopy', 'Restore',
     'Completed'
    :vartype stage: str or
     ~azure.mgmt.datamigration.models.DatabaseMigrationStage
    :ivar status_message: Status message
    :vartype status_message: str
    :ivar message: Migration progress message
    :vartype message: str
    :ivar number_of_objects: Number of objects
    :vartype number_of_objects: long
    :ivar number_of_objects_completed: Number of successfully completed
     objects
    :vartype number_of_objects_completed: long
    :ivar error_count: Number of database/object errors.
    :vartype error_count: long
    :ivar error_prefix: Wildcard string prefix to use for querying all errors
     of the item
    :vartype error_prefix: str
    :ivar result_prefix: Wildcard string prefix to use for querying all
     sub-tem results of the item
    :vartype result_prefix: str
    :ivar exceptions_and_warnings: Migration exceptions and warnings.
    :vartype exceptions_and_warnings:
     list[~azure.mgmt.datamigration.models.ReportableException]
    :ivar object_summary: Summary of object results in the migration
    :vartype object_summary: dict[str,
     ~azure.mgmt.datamigration.models.DataItemMigrationSummaryResult]
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'database_name': {'readonly': True},
        'started_on': {'readonly': True},
        'ended_on': {'readonly': True},
        'state': {'readonly': True},
        'stage': {'readonly': True},
        'status_message': {'readonly': True},
        'message': {'readonly': True},
        'number_of_objects': {'readonly': True},
        'number_of_objects_completed': {'readonly': True},
        'error_count': {'readonly': True},
        'error_prefix': {'readonly': True},
        'result_prefix': {'readonly': True},
        'exceptions_and_warnings': {'readonly': True},
        'object_summary': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'ended_on': {'key': 'endedOn', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'stage': {'key': 'stage', 'type': 'str'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'number_of_objects': {'key': 'numberOfObjects', 'type': 'long'},
        'number_of_objects_completed': {'key': 'numberOfObjectsCompleted', 'type': 'long'},
        'error_count': {'key': 'errorCount', 'type': 'long'},
        'error_prefix': {'key': 'errorPrefix', 'type': 'str'},
        'result_prefix': {'key': 'resultPrefix', 'type': 'str'},
        'exceptions_and_warnings': {'key': 'exceptionsAndWarnings', 'type': '[ReportableException]'},
        'object_summary': {'key': 'objectSummary', 'type': '{DataItemMigrationSummaryResult}'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrateSqlServerSqlDbTaskOutputDatabaseLevel, self).__init__(**kwargs)
        self.database_name = None
        self.started_on = None
        self.ended_on = None
        self.state = None
        self.stage = None
        self.status_message = None
        self.message = None
        self.number_of_objects = None
        self.number_of_objects_completed = None
        self.error_count = None
        self.error_prefix = None
        self.result_prefix = None
        self.exceptions_and_warnings = None
        self.object_summary = None
        self.result_type = 'DatabaseLevelOutput'
