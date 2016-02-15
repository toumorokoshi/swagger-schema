from .lib.serializer import SerializableObject
from .lib.compat import string_type


class ExternalDocumentation(SerializableObject):
    _schema = {
        "attributes": {
            "description": string_type,
            "url": string_type
        },
        "required": ["url"]
    }
