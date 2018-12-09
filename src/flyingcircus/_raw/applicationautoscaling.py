"""Raw representations of every data type in the AWS ApplicationAutoScaling service.

See Also:
    `AWS developer guide for ApplicationAutoScaling
    <https://docs.aws.amazon.com/autoscaling/application/APIReference/Welcome.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "ScalableTarget",
    "ScalableTargetProperties",
    "ScalingPolicy",
    "ScalingPolicyProperties",
]


@attrs(**ATTRSCONFIG)
class ScalableTargetProperties(ResourceProperties):
    MaxCapacity = attrib(default=None)
    MinCapacity = attrib(default=None)
    ResourceId = attrib(default=None)
    RoleARN = attrib(default=None)
    ScalableDimension = attrib(default=None)
    ScheduledActions = attrib(default=None)
    ServiceNamespace = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ScalableTarget(Resource):
    """A Scalable Target for ApplicationAutoScaling.

    See Also:
        `AWS Cloud Formation documentation for ScalableTarget
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html>`_
    """

    RESOURCE_TYPE = "AWS::ApplicationAutoScaling::ScalableTarget"

    Properties: ScalableTargetProperties = attrib(
        factory=ScalableTargetProperties,
        converter=create_object_converter(ScalableTargetProperties),
    )


@attrs(**ATTRSCONFIG)
class ScalingPolicyProperties(ResourceProperties):
    PolicyName = attrib(default=None)
    PolicyType = attrib(default=None)
    ResourceId = attrib(default=None)
    ScalableDimension = attrib(default=None)
    ScalingTargetId = attrib(default=None)
    ServiceNamespace = attrib(default=None)
    StepScalingPolicyConfiguration = attrib(default=None)
    TargetTrackingScalingPolicyConfiguration = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ScalingPolicy(Resource):
    """A Scaling Policy for ApplicationAutoScaling.

    See Also:
        `AWS Cloud Formation documentation for ScalingPolicy
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`_
    """

    RESOURCE_TYPE = "AWS::ApplicationAutoScaling::ScalingPolicy"

    Properties: ScalingPolicyProperties = attrib(
        factory=ScalingPolicyProperties,
        converter=create_object_converter(ScalingPolicyProperties),
    )
