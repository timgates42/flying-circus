"""Raw representations of every data type in the AWS Amplify service.

See Also:
    `AWS developer guide for Amplify
    <https://docs.aws.amazon.com/amplify/latest/userguide/getting-started.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "App",
    "AppProperties",
    "Branch",
    "BranchProperties",
    "Domain",
    "DomainProperties",
]


@attrs(**ATTRSCONFIG)
class AppProperties(ResourceProperties):
    AccessToken = attrib(default=None)
    BasicAuthConfig = attrib(default=None)
    BuildSpec = attrib(default=None)
    CustomRules = attrib(default=None)
    Description = attrib(default=None)
    EnvironmentVariables = attrib(default=None)
    IAMServiceRole = attrib(default=None)
    Name = attrib(default=None)
    OauthToken = attrib(default=None)
    Repository = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class App(Resource):
    """A App for Amplify.

    See Also:
        `AWS Cloud Formation documentation for App
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html>`_
    """

    RESOURCE_TYPE = "AWS::Amplify::App"

    Properties: AppProperties = attrib(
        factory=AppProperties, converter=create_object_converter(AppProperties)
    )


@attrs(**ATTRSCONFIG)
class BranchProperties(ResourceProperties):
    AppId = attrib(default=None)
    BasicAuthConfig = attrib(default=None)
    BranchName = attrib(default=None)
    BuildSpec = attrib(default=None)
    Description = attrib(default=None)
    EnvironmentVariables = attrib(default=None)
    Stage = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Branch(Resource):
    """A Branch for Amplify.

    See Also:
        `AWS Cloud Formation documentation for Branch
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html>`_
    """

    RESOURCE_TYPE = "AWS::Amplify::Branch"

    Properties: BranchProperties = attrib(
        factory=BranchProperties, converter=create_object_converter(BranchProperties)
    )


@attrs(**ATTRSCONFIG)
class DomainProperties(ResourceProperties):
    AppId = attrib(default=None)
    DomainName = attrib(default=None)
    SubDomainSettings = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Domain(Resource):
    """A Domain for Amplify.

    See Also:
        `AWS Cloud Formation documentation for Domain
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html>`_
    """

    RESOURCE_TYPE = "AWS::Amplify::Domain"

    Properties: DomainProperties = attrib(
        factory=DomainProperties, converter=create_object_converter(DomainProperties)
    )
