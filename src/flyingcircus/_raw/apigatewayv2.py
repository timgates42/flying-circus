"""Raw representations of every data type in the AWS ApiGatewayV2 service.

See Also:
    `AWS developer guide for ApiGatewayV2
    <https://docs.aws.amazon.com/apigateway/latest/developerguide/index.html>`_

This file is automatically generated, and should not be directly edited.
"""

from attr import attrib
from attr import attrs

from ..core import ATTRSCONFIG
from ..core import Resource
from ..core import ResourceProperties
from ..core import create_object_converter

__all__ = [
    "Api",
    "ApiProperties",
    "ApiMapping",
    "ApiMappingProperties",
    "Authorizer",
    "AuthorizerProperties",
    "Deployment",
    "DeploymentProperties",
    "DomainName",
    "DomainNameProperties",
    "Integration",
    "IntegrationProperties",
    "IntegrationResponse",
    "IntegrationResponseProperties",
    "Model",
    "ModelProperties",
    "Route",
    "RouteProperties",
    "RouteResponse",
    "RouteResponseProperties",
    "Stage",
    "StageProperties",
]


@attrs(**ATTRSCONFIG)
class ApiProperties(ResourceProperties):
    ApiKeySelectionExpression = attrib(default=None)
    BasePath = attrib(default=None)
    Body = attrib(default=None)
    BodyS3Location = attrib(default=None)
    CorsConfiguration = attrib(default=None)
    CredentialsArn = attrib(default=None)
    Description = attrib(default=None)
    DisableSchemaValidation = attrib(default=None)
    FailOnWarnings = attrib(default=None)
    Name = attrib(default=None)
    ProtocolType = attrib(default=None)
    RouteKey = attrib(default=None)
    RouteSelectionExpression = attrib(default=None)
    Tags = attrib(default=None)
    Target = attrib(default=None)
    Version = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Api(Resource):
    """A Api for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for Api
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::Api"

    Properties: ApiProperties = attrib(
        factory=ApiProperties, converter=create_object_converter(ApiProperties)
    )


@attrs(**ATTRSCONFIG)
class ApiMappingProperties(ResourceProperties):
    ApiId = attrib(default=None)
    ApiMappingKey = attrib(default=None)
    DomainName = attrib(default=None)
    Stage = attrib(default=None)


@attrs(**ATTRSCONFIG)
class ApiMapping(Resource):
    """A Api Mapping for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for ApiMapping
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::ApiMapping"

    Properties: ApiMappingProperties = attrib(
        factory=ApiMappingProperties,
        converter=create_object_converter(ApiMappingProperties),
    )


@attrs(**ATTRSCONFIG)
class AuthorizerProperties(ResourceProperties):
    ApiId = attrib(default=None)
    AuthorizerCredentialsArn = attrib(default=None)
    AuthorizerResultTtlInSeconds = attrib(default=None)
    AuthorizerType = attrib(default=None)
    AuthorizerUri = attrib(default=None)
    IdentitySource = attrib(default=None)
    IdentityValidationExpression = attrib(default=None)
    JwtConfiguration = attrib(default=None)
    Name = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Authorizer(Resource):
    """A Authorizer for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for Authorizer
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::Authorizer"

    Properties: AuthorizerProperties = attrib(
        factory=AuthorizerProperties,
        converter=create_object_converter(AuthorizerProperties),
    )


@attrs(**ATTRSCONFIG)
class DeploymentProperties(ResourceProperties):
    ApiId = attrib(default=None)
    Description = attrib(default=None)
    StageName = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Deployment(Resource):
    """A Deployment for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for Deployment
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::Deployment"

    Properties: DeploymentProperties = attrib(
        factory=DeploymentProperties,
        converter=create_object_converter(DeploymentProperties),
    )


@attrs(**ATTRSCONFIG)
class DomainNameProperties(ResourceProperties):
    DomainName = attrib(default=None)
    DomainNameConfigurations = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class DomainName(Resource):
    """A Domain Name for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for DomainName
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::DomainName"

    Properties: DomainNameProperties = attrib(
        factory=DomainNameProperties,
        converter=create_object_converter(DomainNameProperties),
    )


@attrs(**ATTRSCONFIG)
class IntegrationProperties(ResourceProperties):
    ApiId = attrib(default=None)
    ConnectionType = attrib(default=None)
    ContentHandlingStrategy = attrib(default=None)
    CredentialsArn = attrib(default=None)
    Description = attrib(default=None)
    IntegrationMethod = attrib(default=None)
    IntegrationType = attrib(default=None)
    IntegrationUri = attrib(default=None)
    PassthroughBehavior = attrib(default=None)
    PayloadFormatVersion = attrib(default=None)
    RequestParameters = attrib(default=None)
    RequestTemplates = attrib(default=None)
    TemplateSelectionExpression = attrib(default=None)
    TimeoutInMillis = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Integration(Resource):
    """A Integration for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for Integration
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::Integration"

    Properties: IntegrationProperties = attrib(
        factory=IntegrationProperties,
        converter=create_object_converter(IntegrationProperties),
    )


@attrs(**ATTRSCONFIG)
class IntegrationResponseProperties(ResourceProperties):
    ApiId = attrib(default=None)
    ContentHandlingStrategy = attrib(default=None)
    IntegrationId = attrib(default=None)
    IntegrationResponseKey = attrib(default=None)
    ResponseParameters = attrib(default=None)
    ResponseTemplates = attrib(default=None)
    TemplateSelectionExpression = attrib(default=None)


@attrs(**ATTRSCONFIG)
class IntegrationResponse(Resource):
    """A Integration Response for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for IntegrationResponse
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::IntegrationResponse"

    Properties: IntegrationResponseProperties = attrib(
        factory=IntegrationResponseProperties,
        converter=create_object_converter(IntegrationResponseProperties),
    )


@attrs(**ATTRSCONFIG)
class ModelProperties(ResourceProperties):
    ApiId = attrib(default=None)
    ContentType = attrib(default=None)
    Description = attrib(default=None)
    Name = attrib(default=None)
    Schema = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Model(Resource):
    """A Model for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for Model
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::Model"

    Properties: ModelProperties = attrib(
        factory=ModelProperties, converter=create_object_converter(ModelProperties)
    )


@attrs(**ATTRSCONFIG)
class RouteProperties(ResourceProperties):
    ApiId = attrib(default=None)
    ApiKeyRequired = attrib(default=None)
    AuthorizationScopes = attrib(default=None)
    AuthorizationType = attrib(default=None)
    AuthorizerId = attrib(default=None)
    ModelSelectionExpression = attrib(default=None)
    OperationName = attrib(default=None)
    RequestModels = attrib(default=None)
    RequestParameters = attrib(default=None)
    RouteKey = attrib(default=None)
    RouteResponseSelectionExpression = attrib(default=None)
    Target = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Route(Resource):
    """A Route for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for Route
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::Route"

    Properties: RouteProperties = attrib(
        factory=RouteProperties, converter=create_object_converter(RouteProperties)
    )


@attrs(**ATTRSCONFIG)
class RouteResponseProperties(ResourceProperties):
    ApiId = attrib(default=None)
    ModelSelectionExpression = attrib(default=None)
    ResponseModels = attrib(default=None)
    ResponseParameters = attrib(default=None)
    RouteId = attrib(default=None)
    RouteResponseKey = attrib(default=None)


@attrs(**ATTRSCONFIG)
class RouteResponse(Resource):
    """A Route Response for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for RouteResponse
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::RouteResponse"

    Properties: RouteResponseProperties = attrib(
        factory=RouteResponseProperties,
        converter=create_object_converter(RouteResponseProperties),
    )


@attrs(**ATTRSCONFIG)
class StageProperties(ResourceProperties):
    AccessLogSettings = attrib(default=None)
    ApiId = attrib(default=None)
    AutoDeploy = attrib(default=None)
    ClientCertificateId = attrib(default=None)
    DefaultRouteSettings = attrib(default=None)
    DeploymentId = attrib(default=None)
    Description = attrib(default=None)
    RouteSettings = attrib(default=None)
    StageName = attrib(default=None)
    StageVariables = attrib(default=None)
    Tags = attrib(default=None)


@attrs(**ATTRSCONFIG)
class Stage(Resource):
    """A Stage for ApiGatewayV2.

    See Also:
        `AWS Cloud Formation documentation for Stage
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html>`_
    """

    RESOURCE_TYPE = "AWS::ApiGatewayV2::Stage"

    Properties: StageProperties = attrib(
        factory=StageProperties, converter=create_object_converter(StageProperties)
    )
