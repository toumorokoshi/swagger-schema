from .lib.serializer import SerializableObject
from .lib.compat import string_type


class Response(SerializableObject):
    _schema = {
        "attributes": {
            "description": string_type,
            # "schema"
            # headers
            # example object
        },
        "required": ["description"]
    }
