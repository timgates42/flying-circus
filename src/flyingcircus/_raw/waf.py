"""Raw representations of every data type in the AWS WAF service.

See Also:
    `AWS developer guide for WAF
    <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "ByteMatchSet",
    "ByteMatchSetProperties",
    "IPSet",
    "IPSetProperties",
    "Rule",
    "RuleProperties",
    "SizeConstraintSet",
    "SizeConstraintSetProperties",
    "SqlInjectionMatchSet",
    "SqlInjectionMatchSetProperties",
    "WebACL",
    "WebACLProperties",
    "XssMatchSet",
    "XssMatchSetProperties",
]


@attrs(**ATTRSCONFIG)
class ByteMatchSetProperties(ResourceProperties):
    ByteMatchTuples = attrib(default=None)
    Name = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ByteMatchSet(Resource):
    """A Byte Match Set for WAF.

    See Also:
        `AWS Cloud Formation documentation for ByteMatchSet
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html>`_
    """

    RESOURCE_TYPE = "AWS::WAF::ByteMatchSet"

    Properties: ByteMatchSetProperties = attrib(
        factory=ByteMatchSetProperties,
        converter=create_object_converter(ByteMatchSetProperties),
    )


@attrs(**ATTRSCONFIG)
class IPSetProperties(ResourceProperties):
    IPSetDescriptors = attrib(default=None)
    Name = attrib(default=None)


@attrs(**ATTRSCONFIG)
class IPSet(Resource):
    """A Ip Set for WAF.

    See Also:
        `AWS Cloud Formation documentation for IPSet
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html>`_
    """

    RESOURCE_TYPE = "AWS::WAF::IPSet"

    Properties: IPSetProperties = attrib(
        factory=IPSetProperties, converter=create_object_converter(IPSetProperties)
    )


@attrs(**ATTRSCONFIG)
class RuleProperties(ResourceProperties):
    MetricName = attrib(default=None)
    Name = attrib(default=None)
    Predicates = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Rule(Resource):
    """A Rule for WAF.

    See Also:
        `AWS Cloud Formation documentation for Rule
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html>`_
    """

    RESOURCE_TYPE = "AWS::WAF::Rule"

    Properties: RuleProperties = attrib(
        factory=RuleProperties, converter=create_object_converter(RuleProperties)
    )


@attrs(**ATTRSCONFIG)
class SizeConstraintSetProperties(ResourceProperties):
    Name = attrib(default=None)
    SizeConstraints = attrib(default=None)


@attrs(**ATTRSCONFIG)
class SizeConstraintSet(Resource):
    """A Size Constraint Set for WAF.

    See Also:
        `AWS Cloud Formation documentation for SizeConstraintSet
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html>`_
    """

    RESOURCE_TYPE = "AWS::WAF::SizeConstraintSet"

    Properties: SizeConstraintSetProperties = attrib(
        factory=SizeConstraintSetProperties,
        converter=create_object_converter(SizeConstraintSetProperties),
    )


@attrs(**ATTRSCONFIG)
class SqlInjectionMatchSetProperties(ResourceProperties):
    Name = attrib(default=None)
    SqlInjectionMatchTuples = attrib(default=None)


@attrs(**ATTRSCONFIG)
class SqlInjectionMatchSet(Resource):
    """A Sql Injection Match Set for WAF.

    See Also:
        `AWS Cloud Formation documentation for SqlInjectionMatchSet
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html>`_
    """

    RESOURCE_TYPE = "AWS::WAF::SqlInjectionMatchSet"

    Properties: SqlInjectionMatchSetProperties = attrib(
        factory=SqlInjectionMatchSetProperties,
        converter=create_object_converter(SqlInjectionMatchSetProperties),
    )


@attrs(**ATTRSCONFIG)
class WebACLProperties(ResourceProperties):
    DefaultAction = attrib(default=None)
    MetricName = attrib(default=None)
    Name = attrib(default=None)
    Rules = attrib(default=None)


@attrs(**ATTRSCONFIG)
class WebACL(Resource):
    """A Web Acl for WAF.

    See Also:
        `AWS Cloud Formation documentation for WebACL
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html>`_
    """

    RESOURCE_TYPE = "AWS::WAF::WebACL"

    Properties: WebACLProperties = attrib(
        factory=WebACLProperties, converter=create_object_converter(WebACLProperties)
    )


@attrs(**ATTRSCONFIG)
class XssMatchSetProperties(ResourceProperties):
    Name = attrib(default=None)
    XssMatchTuples = attrib(default=None)


@attrs(**ATTRSCONFIG)
class XssMatchSet(Resource):
    """A Xss Match Set for WAF.

    See Also:
        `AWS Cloud Formation documentation for XssMatchSet
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html>`_
    """

    RESOURCE_TYPE = "AWS::WAF::XssMatchSet"

    Properties: XssMatchSetProperties = attrib(
        factory=XssMatchSetProperties,
        converter=create_object_converter(XssMatchSetProperties),
    )
