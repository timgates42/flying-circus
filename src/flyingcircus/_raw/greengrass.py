"""Raw representations of every data type in the AWS Greengrass service.

See Also:
    `AWS developer guide for Greengrass
    <https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "ConnectorDefinition",
    "ConnectorDefinitionProperties",
    "ConnectorDefinitionVersion",
    "ConnectorDefinitionVersionProperties",
    "CoreDefinition",
    "CoreDefinitionProperties",
    "CoreDefinitionVersion",
    "CoreDefinitionVersionProperties",
    "DeviceDefinition",
    "DeviceDefinitionProperties",
    "DeviceDefinitionVersion",
    "DeviceDefinitionVersionProperties",
    "FunctionDefinition",
    "FunctionDefinitionProperties",
    "FunctionDefinitionVersion",
    "FunctionDefinitionVersionProperties",
    "Group",
    "GroupProperties",
    "GroupVersion",
    "GroupVersionProperties",
    "LoggerDefinition",
    "LoggerDefinitionProperties",
    "LoggerDefinitionVersion",
    "LoggerDefinitionVersionProperties",
    "ResourceDefinition",
    "ResourceDefinitionProperties",
    "ResourceDefinitionVersion",
    "ResourceDefinitionVersionProperties",
    "SubscriptionDefinition",
    "SubscriptionDefinitionProperties",
    "SubscriptionDefinitionVersion",
    "SubscriptionDefinitionVersionProperties",
]


@attrs(**ATTRSCONFIG)
class ConnectorDefinitionProperties(ResourceProperties):
    InitialVersion = attrib(default=None)
    Name = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ConnectorDefinition(Resource):
    """A Connector Definition for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for ConnectorDefinition
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::ConnectorDefinition"

    Properties: ConnectorDefinitionProperties = attrib(
        factory=ConnectorDefinitionProperties,
        converter=create_object_converter(ConnectorDefinitionProperties),
    )


@attrs(**ATTRSCONFIG)
class ConnectorDefinitionVersionProperties(ResourceProperties):
    ConnectorDefinitionId = attrib(default=None)
    Connectors = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ConnectorDefinitionVersion(Resource):
    """A Connector Definition Version for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for ConnectorDefinitionVersion
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::ConnectorDefinitionVersion"

    Properties: ConnectorDefinitionVersionProperties = attrib(
        factory=ConnectorDefinitionVersionProperties,
        converter=create_object_converter(ConnectorDefinitionVersionProperties),
    )


@attrs(**ATTRSCONFIG)
class CoreDefinitionProperties(ResourceProperties):
    InitialVersion = attrib(default=None)
    Name = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class CoreDefinition(Resource):
    """A Core Definition for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for CoreDefinition
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::CoreDefinition"

    Properties: CoreDefinitionProperties = attrib(
        factory=CoreDefinitionProperties,
        converter=create_object_converter(CoreDefinitionProperties),
    )


@attrs(**ATTRSCONFIG)
class CoreDefinitionVersionProperties(ResourceProperties):
    CoreDefinitionId = attrib(default=None)
    Cores = attrib(default=None)


@attrs(**ATTRSCONFIG)
class CoreDefinitionVersion(Resource):
    """A Core Definition Version for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for CoreDefinitionVersion
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::CoreDefinitionVersion"

    Properties: CoreDefinitionVersionProperties = attrib(
        factory=CoreDefinitionVersionProperties,
        converter=create_object_converter(CoreDefinitionVersionProperties),
    )


@attrs(**ATTRSCONFIG)
class DeviceDefinitionProperties(ResourceProperties):
    InitialVersion = attrib(default=None)
    Name = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class DeviceDefinition(Resource):
    """A Device Definition for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for DeviceDefinition
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::DeviceDefinition"

    Properties: DeviceDefinitionProperties = attrib(
        factory=DeviceDefinitionProperties,
        converter=create_object_converter(DeviceDefinitionProperties),
    )


@attrs(**ATTRSCONFIG)
class DeviceDefinitionVersionProperties(ResourceProperties):
    DeviceDefinitionId = attrib(default=None)
    Devices = attrib(default=None)


@attrs(**ATTRSCONFIG)
class DeviceDefinitionVersion(Resource):
    """A Device Definition Version for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for DeviceDefinitionVersion
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::DeviceDefinitionVersion"

    Properties: DeviceDefinitionVersionProperties = attrib(
        factory=DeviceDefinitionVersionProperties,
        converter=create_object_converter(DeviceDefinitionVersionProperties),
    )


@attrs(**ATTRSCONFIG)
class FunctionDefinitionProperties(ResourceProperties):
    InitialVersion = attrib(default=None)
    Name = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class FunctionDefinition(Resource):
    """A Function Definition for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for FunctionDefinition
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::FunctionDefinition"

    Properties: FunctionDefinitionProperties = attrib(
        factory=FunctionDefinitionProperties,
        converter=create_object_converter(FunctionDefinitionProperties),
    )


@attrs(**ATTRSCONFIG)
class FunctionDefinitionVersionProperties(ResourceProperties):
    DefaultConfig = attrib(default=None)
    FunctionDefinitionId = attrib(default=None)
    Functions = attrib(default=None)


@attrs(**ATTRSCONFIG)
class FunctionDefinitionVersion(Resource):
    """A Function Definition Version for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for FunctionDefinitionVersion
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::FunctionDefinitionVersion"

    Properties: FunctionDefinitionVersionProperties = attrib(
        factory=FunctionDefinitionVersionProperties,
        converter=create_object_converter(FunctionDefinitionVersionProperties),
    )


@attrs(**ATTRSCONFIG)
class GroupProperties(ResourceProperties):
    InitialVersion = attrib(default=None)
    Name = attrib(default=None)
    RoleArn = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Group(Resource):
    """A Group for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for Group
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::Group"

    Properties: GroupProperties = attrib(
        factory=GroupProperties, converter=create_object_converter(GroupProperties)
    )


@attrs(**ATTRSCONFIG)
class GroupVersionProperties(ResourceProperties):
    ConnectorDefinitionVersionArn = attrib(default=None)
    CoreDefinitionVersionArn = attrib(default=None)
    DeviceDefinitionVersionArn = attrib(default=None)
    FunctionDefinitionVersionArn = attrib(default=None)
    GroupId = attrib(default=None)
    LoggerDefinitionVersionArn = attrib(default=None)
    ResourceDefinitionVersionArn = attrib(default=None)
    SubscriptionDefinitionVersionArn = attrib(default=None)


@attrs(**ATTRSCONFIG)
class GroupVersion(Resource):
    """A Group Version for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for GroupVersion
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::GroupVersion"

    Properties: GroupVersionProperties = attrib(
        factory=GroupVersionProperties,
        converter=create_object_converter(GroupVersionProperties),
    )


@attrs(**ATTRSCONFIG)
class LoggerDefinitionProperties(ResourceProperties):
    InitialVersion = attrib(default=None)
    Name = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class LoggerDefinition(Resource):
    """A Logger Definition for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for LoggerDefinition
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::LoggerDefinition"

    Properties: LoggerDefinitionProperties = attrib(
        factory=LoggerDefinitionProperties,
        converter=create_object_converter(LoggerDefinitionProperties),
    )


@attrs(**ATTRSCONFIG)
class LoggerDefinitionVersionProperties(ResourceProperties):
    LoggerDefinitionId = attrib(default=None)
    Loggers = attrib(default=None)


@attrs(**ATTRSCONFIG)
class LoggerDefinitionVersion(Resource):
    """A Logger Definition Version for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for LoggerDefinitionVersion
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::LoggerDefinitionVersion"

    Properties: LoggerDefinitionVersionProperties = attrib(
        factory=LoggerDefinitionVersionProperties,
        converter=create_object_converter(LoggerDefinitionVersionProperties),
    )


@attrs(**ATTRSCONFIG)
class ResourceDefinitionProperties(ResourceProperties):
    InitialVersion = attrib(default=None)
    Name = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ResourceDefinition(Resource):
    """A Resource Definition for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for ResourceDefinition
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::ResourceDefinition"

    Properties: ResourceDefinitionProperties = attrib(
        factory=ResourceDefinitionProperties,
        converter=create_object_converter(ResourceDefinitionProperties),
    )


@attrs(**ATTRSCONFIG)
class ResourceDefinitionVersionProperties(ResourceProperties):
    ResourceDefinitionId = attrib(default=None)
    Resources = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ResourceDefinitionVersion(Resource):
    """A Resource Definition Version for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for ResourceDefinitionVersion
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::ResourceDefinitionVersion"

    Properties: ResourceDefinitionVersionProperties = attrib(
        factory=ResourceDefinitionVersionProperties,
        converter=create_object_converter(ResourceDefinitionVersionProperties),
    )


@attrs(**ATTRSCONFIG)
class SubscriptionDefinitionProperties(ResourceProperties):
    InitialVersion = attrib(default=None)
    Name = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class SubscriptionDefinition(Resource):
    """A Subscription Definition for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for SubscriptionDefinition
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::SubscriptionDefinition"

    Properties: SubscriptionDefinitionProperties = attrib(
        factory=SubscriptionDefinitionProperties,
        converter=create_object_converter(SubscriptionDefinitionProperties),
    )


@attrs(**ATTRSCONFIG)
class SubscriptionDefinitionVersionProperties(ResourceProperties):
    SubscriptionDefinitionId = attrib(default=None)
    Subscriptions = attrib(default=None)


@attrs(**ATTRSCONFIG)
class SubscriptionDefinitionVersion(Resource):
    """A Subscription Definition Version for Greengrass.

    See Also:
        `AWS Cloud Formation documentation for SubscriptionDefinitionVersion
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html>`_
    """

    RESOURCE_TYPE = "AWS::Greengrass::SubscriptionDefinitionVersion"

    Properties: SubscriptionDefinitionVersionProperties = attrib(
        factory=SubscriptionDefinitionVersionProperties,
        converter=create_object_converter(SubscriptionDefinitionVersionProperties),
    )
