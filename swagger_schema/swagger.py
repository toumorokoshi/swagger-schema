from .lib.serializer import SerializableObject
from .lib.compat import string_type
from .lib.typeddict import TypedDict
from .external_documentation import ExternalDocumentation
from .info import Info
from .paths import Paths
from .path import Path
from .parameters import Parameters
from .security_requirement import SecurityRequirement
from .tag import Tag


class Swagger(SerializableObject):
    _schema = {
        "attributes": {
            "basePath": string_type,
            "consumes":  [string_type],
            # "definitions": TypedDict <string_type, JsonSchema>
            "externalDocs": ExternalDocumentation,
            "host": string_type,
            "info": Info,
            "paths": Paths,
            # "parameters": TypedDict
            # "responses": TypeDict
            "schemes": [string_type],
            "swagger": string_type,
            # "securityDefinitions"
            "security": SecurityRequirement,
            "tags": [Tag]
        },
        "required": ["info", "paths", "swagger"]
    }


# class _Swagger(Schema):
#   pass
#basePath = fields.Str()
#consumes = fields.List(fields.Str)
#definitions = TypedDict(fields.Str, fields.Nested(JsonSchema))
#externalDocs = fields.Nested(ExternalDocumentation)
#host = fields.Str()
#info = fields.Nested(Info, required=True)
#paths = TypedDict(fields.Str, fields.Nested(Path), required=True)
#parameters = fields.Nested(Parameters)
#produces = fields.List(fields.Str)
#responses = TypedDict(fields.Str, fields.Nested(Response))
#schemes = fields.List(fields.Str)
#swagger = fields.Str(required=True)
#securityDefinitions = TypedDict(fields.Str, fields.Nested(SecurityDefinitions))
#security = fields.List(fields.Nested(SecurityRequirement))
#tags = fields.List(fields.Nested(Tag))
