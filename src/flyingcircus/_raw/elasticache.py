"""Raw representations of every data type in the AWS ElastiCache service.

See Also:
    `AWS developer guide for ElastiCache
    <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/index.html>`_

This file is automatically generated, and should not be directly edited.
"""

from typing import Any
from typing import Dict

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "CacheCluster",
    "CacheClusterProperties",
    "ParameterGroup",
    "ParameterGroupProperties",
    "ReplicationGroup",
    "ReplicationGroupProperties",
    "SecurityGroup",
    "SecurityGroupProperties",
    "SecurityGroupIngress",
    "SecurityGroupIngressProperties",
    "SubnetGroup",
    "SubnetGroupProperties",
]


@attrs(**ATTRSCONFIG)
class CacheClusterProperties(ResourceProperties):
    AutoMinorVersionUpgrade = attrib(default=None)
    AZMode = attrib(default=None)
    CacheNodeType = attrib(default=None)
    CacheParameterGroupName = attrib(default=None)
    CacheSecurityGroupNames = attrib(default=None)
    CacheSubnetGroupName = attrib(default=None)
    ClusterName = attrib(default=None)
    Engine = attrib(default=None)
    EngineVersion = attrib(default=None)
    NotificationTopicArn = attrib(default=None)
    NumCacheNodes = attrib(default=None)
    Port = attrib(default=None)
    PreferredAvailabilityZone = attrib(default=None)
    PreferredAvailabilityZones = attrib(default=None)
    PreferredMaintenanceWindow = attrib(default=None)
    SnapshotArns = attrib(default=None)
    SnapshotName = attrib(default=None)
    SnapshotRetentionLimit = attrib(default=None)
    SnapshotWindow = attrib(default=None)
    Tags = attrib(default=None)
    VpcSecurityGroupIds = attrib(default=None)


@attrs(**ATTRSCONFIG)
class CacheCluster(Resource):
    """A Cache Cluster for ElastiCache.

    See Also:
        `AWS Cloud Formation documentation for CacheCluster
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html>`_
    """

    RESOURCE_TYPE = "AWS::ElastiCache::CacheCluster"

    Properties: CacheClusterProperties = attrib(
        factory=CacheClusterProperties,
        converter=create_object_converter(CacheClusterProperties),
    )


@attrs(**ATTRSCONFIG)
class ParameterGroupProperties(ResourceProperties):
    CacheParameterGroupFamily = attrib(default=None)
    Description = attrib(default=None)
    Properties = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ParameterGroup(Resource):
    """A Parameter Group for ElastiCache.

    See Also:
        `AWS Cloud Formation documentation for ParameterGroup
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html>`_
    """

    RESOURCE_TYPE = "AWS::ElastiCache::ParameterGroup"

    Properties: ParameterGroupProperties = attrib(
        factory=ParameterGroupProperties,
        converter=create_object_converter(ParameterGroupProperties),
    )


@attrs(**ATTRSCONFIG)
class ReplicationGroupProperties(ResourceProperties):
    AtRestEncryptionEnabled = attrib(default=None)
    AuthToken = attrib(default=None)
    AutomaticFailoverEnabled = attrib(default=None)
    AutoMinorVersionUpgrade = attrib(default=None)
    CacheNodeType = attrib(default=None)
    CacheParameterGroupName = attrib(default=None)
    CacheSecurityGroupNames = attrib(default=None)
    CacheSubnetGroupName = attrib(default=None)
    Engine = attrib(default=None)
    EngineVersion = attrib(default=None)
    NodeGroupConfiguration = attrib(default=None)
    NotificationTopicArn = attrib(default=None)
    NumCacheClusters = attrib(default=None)
    NumNodeGroups = attrib(default=None)
    Port = attrib(default=None)
    PreferredCacheClusterAZs = attrib(default=None)
    PreferredMaintenanceWindow = attrib(default=None)
    PrimaryClusterId = attrib(default=None)
    ReplicasPerNodeGroup = attrib(default=None)
    ReplicationGroupDescription = attrib(default=None)
    ReplicationGroupId = attrib(default=None)
    SecurityGroupIds = attrib(default=None)
    SnapshotArns = attrib(default=None)
    SnapshotName = attrib(default=None)
    SnapshotRetentionLimit = attrib(default=None)
    SnapshottingClusterId = attrib(default=None)
    SnapshotWindow = attrib(default=None)
    Tags = attrib(default=None)
    TransitEncryptionEnabled = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ReplicationGroup(Resource):
    """A Replication Group for ElastiCache.

    See Also:
        `AWS Cloud Formation documentation for ReplicationGroup
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html>`_
    """

    RESOURCE_TYPE = "AWS::ElastiCache::ReplicationGroup"

    Properties: ReplicationGroupProperties = attrib(
        factory=ReplicationGroupProperties,
        converter=create_object_converter(ReplicationGroupProperties),
    )

    # NB: UpdatePolicy may be set for ReplicationGroup
    # (unlike most Resource types)
    UpdatePolicy: Dict[str, Any] = attrib(factory=dict)


@attrs(**ATTRSCONFIG)
class SecurityGroupProperties(ResourceProperties):
    Description = attrib(default=None)


@attrs(**ATTRSCONFIG)
class SecurityGroup(Resource):
    """A Security Group for ElastiCache.

    See Also:
        `AWS Cloud Formation documentation for SecurityGroup
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html>`_
    """

    RESOURCE_TYPE = "AWS::ElastiCache::SecurityGroup"

    Properties: SecurityGroupProperties = attrib(
        factory=SecurityGroupProperties,
        converter=create_object_converter(SecurityGroupProperties),
    )


@attrs(**ATTRSCONFIG)
class SecurityGroupIngressProperties(ResourceProperties):
    CacheSecurityGroupName = attrib(default=None)
    EC2SecurityGroupName = attrib(default=None)
    EC2SecurityGroupOwnerId = attrib(default=None)


@attrs(**ATTRSCONFIG)
class SecurityGroupIngress(Resource):
    """A Security Group Ingress for ElastiCache.

    See Also:
        `AWS Cloud Formation documentation for SecurityGroupIngress
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html>`_
    """

    RESOURCE_TYPE = "AWS::ElastiCache::SecurityGroupIngress"

    Properties: SecurityGroupIngressProperties = attrib(
        factory=SecurityGroupIngressProperties,
        converter=create_object_converter(SecurityGroupIngressProperties),
    )


@attrs(**ATTRSCONFIG)
class SubnetGroupProperties(ResourceProperties):
    CacheSubnetGroupName = attrib(default=None)
    Description = attrib(default=None)
    SubnetIds = attrib(default=None)


@attrs(**ATTRSCONFIG)
class SubnetGroup(Resource):
    """A Subnet Group for ElastiCache.

    See Also:
        `AWS Cloud Formation documentation for SubnetGroup
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html>`_
    """

    RESOURCE_TYPE = "AWS::ElastiCache::SubnetGroup"

    Properties: SubnetGroupProperties = attrib(
        factory=SubnetGroupProperties,
        converter=create_object_converter(SubnetGroupProperties),
    )