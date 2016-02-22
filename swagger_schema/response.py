from .lib.serializer import SerializableObject
from .lib.compat import string_type
from .schema import JsonSchemaObject


class Response(SerializableObject):
    _schema = {
        "attributes": {
            "description": string_type,
            "schema": JsonSchemaObject
            # headers
            # example object
        },
        "required": ["description"]
    }
