from .external_documentation import ExternalDocumentation
from .lib.serializer import SerializableObject
from .lib.compat import string_type
from .responses import Responses


class Operation(SerializableObject):
    _schema = {
        "attributes": {
            "tags": [string_type],
            "summary": string_type,
            "description": string_type,
            "operationId": string_type,
            "consumes": [string_type],
            "produces": [string_type],
            "schemes": [string_type],
            "deprecated": bool,
            "externalDocs": ExternalDocumentation,
            "responses": Responses
            # security = [security requirement object]
            # parameters = [parameter object | reference object]
        },
        "required": ["responses"]
    }
