"""Raw representations of every data type in the AWS DocDB service.

See Also:
    `AWS developer guide for DocDB
    <https://docs.aws.amazon.com/documentdb/latest/developerguide/index.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "DBCluster",
    "DBClusterProperties",
    "DBClusterParameterGroup",
    "DBClusterParameterGroupProperties",
    "DBInstance",
    "DBInstanceProperties",
    "DBSubnetGroup",
    "DBSubnetGroupProperties",
]


@attrs(**ATTRSCONFIG)
class DBClusterProperties(ResourceProperties):
    AvailabilityZones = attrib(default=None)
    BackupRetentionPeriod = attrib(default=None)
    DBClusterIdentifier = attrib(default=None)
    DBClusterParameterGroupName = attrib(default=None)
    DBSubnetGroupName = attrib(default=None)
    EngineVersion = attrib(default=None)
    KmsKeyId = attrib(default=None)
    MasterUsername = attrib(default=None)
    MasterUserPassword = attrib(default=None)
    Port = attrib(default=None)
    PreferredBackupWindow = attrib(default=None)
    PreferredMaintenanceWindow = attrib(default=None)
    SnapshotIdentifier = attrib(default=None)
    StorageEncrypted = attrib(default=None)
    Tags = attrib(default=None)
    VpcSecurityGroupIds = attrib(default=None)


@attrs(**ATTRSCONFIG)
class DBCluster(Resource):
    """A Db Cluster for DocDB.

    See Also:
        `AWS Cloud Formation documentation for DBCluster
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html>`_
    """

    RESOURCE_TYPE = "AWS::DocDB::DBCluster"

    Properties: DBClusterProperties = attrib(
        factory=DBClusterProperties,
        converter=create_object_converter(DBClusterProperties),
    )


@attrs(**ATTRSCONFIG)
class DBClusterParameterGroupProperties(ResourceProperties):
    Description = attrib(default=None)
    Family = attrib(default=None)
    Name = attrib(default=None)
    Parameters = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class DBClusterParameterGroup(Resource):
    """A Db Cluster Parameter Group for DocDB.

    See Also:
        `AWS Cloud Formation documentation for DBClusterParameterGroup
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html>`_
    """

    RESOURCE_TYPE = "AWS::DocDB::DBClusterParameterGroup"

    Properties: DBClusterParameterGroupProperties = attrib(
        factory=DBClusterParameterGroupProperties,
        converter=create_object_converter(DBClusterParameterGroupProperties),
    )


@attrs(**ATTRSCONFIG)
class DBInstanceProperties(ResourceProperties):
    AutoMinorVersionUpgrade = attrib(default=None)
    AvailabilityZone = attrib(default=None)
    DBClusterIdentifier = attrib(default=None)
    DBInstanceClass = attrib(default=None)
    DBInstanceIdentifier = attrib(default=None)
    PreferredMaintenanceWindow = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class DBInstance(Resource):
    """A Db Instance for DocDB.

    See Also:
        `AWS Cloud Formation documentation for DBInstance
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html>`_
    """

    RESOURCE_TYPE = "AWS::DocDB::DBInstance"

    Properties: DBInstanceProperties = attrib(
        factory=DBInstanceProperties,
        converter=create_object_converter(DBInstanceProperties),
    )


@attrs(**ATTRSCONFIG)
class DBSubnetGroupProperties(ResourceProperties):
    DBSubnetGroupDescription = attrib(default=None)
    DBSubnetGroupName = attrib(default=None)
    SubnetIds = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class DBSubnetGroup(Resource):
    """A Db Subnet Group for DocDB.

    See Also:
        `AWS Cloud Formation documentation for DBSubnetGroup
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html>`_
    """

    RESOURCE_TYPE = "AWS::DocDB::DBSubnetGroup"

    Properties: DBSubnetGroupProperties = attrib(
        factory=DBSubnetGroupProperties,
        converter=create_object_converter(DBSubnetGroupProperties),
    )
