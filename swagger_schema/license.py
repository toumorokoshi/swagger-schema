from .lib.serializer import SerializableObject
from .lib.compat import string_type


class License(SerializableObject):
    _schema = {
        "attributes": {
            "name": string_type,
            "url": string_type
        },
        "required": ["name"]
    }
