"""Raw representations of every data type in the AWS Kinesis service.

See Also:
    `AWS developer guide for Kinesis
    <https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = ["Stream", "StreamProperties", "StreamConsumer", "StreamConsumerProperties"]


@attrs(**ATTRSCONFIG)
class StreamProperties(ResourceProperties):
    Name = attrib(default=None)
    RetentionPeriodHours = attrib(default=None)
    ShardCount = attrib(default=None)
    StreamEncryption = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Stream(Resource):
    """A Stream for Kinesis.

    See Also:
        `AWS Cloud Formation documentation for Stream
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html>`_
    """

    RESOURCE_TYPE = "AWS::Kinesis::Stream"

    Properties: StreamProperties = attrib(
        factory=StreamProperties, converter=create_object_converter(StreamProperties)
    )


@attrs(**ATTRSCONFIG)
class StreamConsumerProperties(ResourceProperties):
    ConsumerName = attrib(default=None)
    StreamARN = attrib(default=None)


@attrs(**ATTRSCONFIG)
class StreamConsumer(Resource):
    """A Stream Consumer for Kinesis.

    See Also:
        `AWS Cloud Formation documentation for StreamConsumer
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html>`_
    """

    RESOURCE_TYPE = "AWS::Kinesis::StreamConsumer"

    Properties: StreamConsumerProperties = attrib(
        factory=StreamConsumerProperties,
        converter=create_object_converter(StreamConsumerProperties),
    )
