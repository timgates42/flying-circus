"""Raw representations of every data type in the AWS ManagedBlockchain service.

See Also:
    `AWS developer guide for ManagedBlockchain
    <https://docs.aws.amazon.com/managed-blockchain/latest/managementguide>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = ["Member", "MemberProperties", "Node", "NodeProperties"]


@attrs(**ATTRSCONFIG)
class MemberProperties(ResourceProperties):
    InvitationId = attrib(default=None)
    MemberConfiguration = attrib(default=None)
    NetworkConfiguration = attrib(default=None)
    NetworkId = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Member(Resource):
    """A Member for ManagedBlockchain.

    See Also:
        `AWS Cloud Formation documentation for Member
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html>`_
    """

    RESOURCE_TYPE = "AWS::ManagedBlockchain::Member"

    Properties: MemberProperties = attrib(
        factory=MemberProperties, converter=create_object_converter(MemberProperties)
    )


@attrs(**ATTRSCONFIG)
class NodeProperties(ResourceProperties):
    MemberId = attrib(default=None)
    NetworkId = attrib(default=None)
    NodeConfiguration = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Node(Resource):
    """A Node for ManagedBlockchain.

    See Also:
        `AWS Cloud Formation documentation for Node
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html>`_
    """

    RESOURCE_TYPE = "AWS::ManagedBlockchain::Node"

    Properties: NodeProperties = attrib(
        factory=NodeProperties, converter=create_object_converter(NodeProperties)
    )
