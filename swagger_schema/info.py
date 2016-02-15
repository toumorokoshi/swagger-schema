from .lib.serializer import SerializableObject
from .lib.compat import string_type
from .contact import Contact
from .license import License


class Info(SerializableObject):
    _schema = {
        "attributes": {
            "title": string_type,
            "description": string_type,
            "termsOfService": string_type,
            "version": string_type,
            "contact": Contact,
            "license": License,
        },
        "required": ["title", "version"]
    }
