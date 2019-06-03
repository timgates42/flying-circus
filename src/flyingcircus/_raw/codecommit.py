"""Raw representations of every data type in the AWS CodeCommit service.

See Also:
    `AWS developer guide for CodeCommit
    <https://docs.aws.amazon.com/codecommit/latest/userguide/index.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = ["Repository", "RepositoryProperties"]


@attrs(**ATTRSCONFIG)
class RepositoryProperties(ResourceProperties):
    Code = attrib(default=None)
    RepositoryDescription = attrib(default=None)
    RepositoryName = attrib(default=None)
    Triggers = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Repository(Resource):
    """A Repository for CodeCommit.

    See Also:
        `AWS Cloud Formation documentation for Repository
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html>`_
    """

    RESOURCE_TYPE = "AWS::CodeCommit::Repository"

    Properties: RepositoryProperties = attrib(
        factory=RepositoryProperties,
        converter=create_object_converter(RepositoryProperties),
    )
