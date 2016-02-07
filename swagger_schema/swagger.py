from marshmallow import Schema, fields
from .lib.typeddict import TypedDict
from .definitions import Definitions
from .external_documentation import ExternalDocumentation
from .info import Info
from .path import Path
from .paths import Paths
from .parameters import Parameters
from .response import Response
from .schema import Schema
from .security_definitions import SecurityDefinitions
from .security_requirement import SecurityRequirement
from .tag import Tag


class Swagger(Schema):
    basePath = fields.Str()
    consumes = fields.List(fields.Str)
    definitions = TypedDict(fields.Str, fields.Nested(Schema))
    externalDocs = fields.Nested(ExternalDocumentation)
    host = fields.Str()
    info = fields.Nested(Info)
    paths = TypedDict(fields.Str, fields.Nested(Path), required=True)
    parameters = fields.Nested(Parameters)
    produces = fields.List(fields.Str)
    responses = TypedDict(fields.Str, fields.Nested(Response))
    schemes = fields.List(fields.Str)
    swagger = fields.Str(required=True)
    securityDefinitions = fields.Nested(SecurityDefinitions)
    security = fields.List(fields.Nested(SecurityRequirement))
    tags = fields.List(fields.Nested(Tag))
