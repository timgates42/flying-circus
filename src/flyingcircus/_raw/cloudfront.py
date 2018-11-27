"""Raw representations of every data type in the AWS CloudFront service.

See Also:
    `AWS developer guide for CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "CloudFrontOriginAccessIdentity",
    "CloudFrontOriginAccessIdentityProperties",
    "Distribution",
    "DistributionProperties",
    "StreamingDistribution",
    "StreamingDistributionProperties",
]


@attrs(**ATTRSCONFIG)
class CloudFrontOriginAccessIdentityProperties(ResourceProperties):
    CloudFrontOriginAccessIdentityConfig = attrib(default=None)


@attrs(**ATTRSCONFIG)
class CloudFrontOriginAccessIdentity(Resource):
    """A Cloud Front Origin Access Identity for CloudFront.

    See Also:
        `AWS Cloud Formation documentation for CloudFrontOriginAccessIdentity
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html>`_
    """

    RESOURCE_TYPE = "AWS::CloudFront::CloudFrontOriginAccessIdentity"

    Properties: CloudFrontOriginAccessIdentityProperties = attrib(
        factory=CloudFrontOriginAccessIdentityProperties,
        converter=create_object_converter(CloudFrontOriginAccessIdentityProperties),
    )


@attrs(**ATTRSCONFIG)
class DistributionProperties(ResourceProperties):
    DistributionConfig = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Distribution(Resource):
    """A Distribution for CloudFront.

    See Also:
        `AWS Cloud Formation documentation for Distribution
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html>`_
    """

    RESOURCE_TYPE = "AWS::CloudFront::Distribution"

    Properties: DistributionProperties = attrib(
        factory=DistributionProperties,
        converter=create_object_converter(DistributionProperties),
    )


@attrs(**ATTRSCONFIG)
class StreamingDistributionProperties(ResourceProperties):
    StreamingDistributionConfig = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class StreamingDistribution(Resource):
    """A Streaming Distribution for CloudFront.

    See Also:
        `AWS Cloud Formation documentation for StreamingDistribution
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html>`_
    """

    RESOURCE_TYPE = "AWS::CloudFront::StreamingDistribution"

    Properties: StreamingDistributionProperties = attrib(
        factory=StreamingDistributionProperties,
        converter=create_object_converter(StreamingDistributionProperties),
    )
