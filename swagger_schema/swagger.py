from marshmallow import Schema, fields
from .lib.typeddict import TypedDict
from .external_documentation import ExternalDocumentation
from .jsonschema import JsonSchema
from .info import Info
from .path import Path
from .parameters import Parameters
from .response import Response
from .security_definitions import SecurityDefinitions
from .security_requirement import SecurityRequirement
from .tag import Tag


class Swagger(Schema):
    basePath = fields.Str()
    consumes = fields.List(fields.Str)
    definitions = TypedDict(fields.Str, fields.Nested(JsonSchema))
    externalDocs = fields.Nested(ExternalDocumentation)
    host = fields.Str()
    info = fields.Nested(Info, required=True)
    paths = TypedDict(fields.Str, fields.Nested(Path), required=True)
    parameters = fields.Nested(Parameters)
    produces = fields.List(fields.Str)
    responses = TypedDict(fields.Str, fields.Nested(Response))
    schemes = fields.List(fields.Str)
    swagger = fields.Str(required=True)
    securityDefinitions = TypedDict(fields.Str, fields.Nested(SecurityDefinitions))
    security = fields.List(fields.Nested(SecurityRequirement))
    tags = fields.List(fields.Nested(Tag))
