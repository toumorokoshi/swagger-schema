from .lib.serializer import SerializableObject
from .lib.compat import string_type
from .external_documentation import ExternalDocumentation


class Tag(SerializableObject):
    _schema = {
        "attributes": {
            "name": string_type,
            "description": string_type,
            "externalDocs": ExternalDocumentation
        },
        "required": ["name"]
    }
