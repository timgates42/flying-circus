"""Raw representations of every data type in the AWS CloudWatch service.

See Also:
    `AWS developer guide for CloudWatch
    <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "Alarm",
    "Dashboard",
]


@attrs(**ATTRSCONFIG)
class Alarm(Resource):
    """A Alarm for CloudWatch.

    See Also:
        `AWS Cloud Formation documentation for Alarm
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`_
    """

    RESOURCE_TYPE = "AWS::CloudWatch::Alarm"

    @attrs(**ATTRSCONFIG)
    class PropertiesType(ResourceProperties):
        ActionsEnabled = attrib(default=None)
        AlarmActions = attrib(default=None)
        AlarmDescription = attrib(default=None)
        AlarmName = attrib(default=None)
        ComparisonOperator = attrib(default=None)
        DatapointsToAlarm = attrib(default=None)
        Dimensions = attrib(default=None)
        EvaluateLowSampleCountPercentile = attrib(default=None)
        EvaluationPeriods = attrib(default=None)
        ExtendedStatistic = attrib(default=None)
        InsufficientDataActions = attrib(default=None)
        MetricName = attrib(default=None)
        Namespace = attrib(default=None)
        OKActions = attrib(default=None)
        Period = attrib(default=None)
        Statistic = attrib(default=None)
        Threshold = attrib(default=None)
        TreatMissingData = attrib(default=None)
        Unit = attrib(default=None)

    Properties: PropertiesType = attrib(factory=PropertiesType, converter=create_object_converter(PropertiesType))


@attrs(**ATTRSCONFIG)
class Dashboard(Resource):
    """A Dashboard for CloudWatch.

    See Also:
        `AWS Cloud Formation documentation for Dashboard
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html>`_
    """

    RESOURCE_TYPE = "AWS::CloudWatch::Dashboard"

    @attrs(**ATTRSCONFIG)
    class PropertiesType(ResourceProperties):
        DashboardBody = attrib(default=None)
        DashboardName = attrib(default=None)

    Properties: PropertiesType = attrib(factory=PropertiesType, converter=create_object_converter(PropertiesType))
