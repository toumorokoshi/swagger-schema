from .lib.serializer import SerializableObject
from .lib.compat import string_type
from .external_documentation import ExternalDocumentation
from .info import Info
from .paths import Paths
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
            "parameters": Parameters,
            # "responses": TypeDict
            "schemes": [string_type],
            "swagger": string_type,
            # "securityDefinitions"
            "security": SecurityRequirement,
            "tags": [Tag]
        },
        "required": ["info", "paths", "swagger"]
    }
