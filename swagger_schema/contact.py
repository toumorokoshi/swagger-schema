from .lib.serializer import SerializableObject
from .lib.compat import string_type


class Contact(SerializableObject):
    _schema = {
        "attributes": {
            "name": string_type,
            "url": string_type,
            "email": string_type
        },
        "required": []
    }
