from .lib.serializer import SerializableObject
from .lib.compat import string_type


class Items(SerializableObject):
    _schema = {
        "type": string_type,
        "format": string_type,
        # "items":
        # valid options: csv, ssv, tsv, pipes
        "collectionFormat": string_type,
        # "default":
        "maximum": float,
        "exclusiveMaximum": bool,
        "minimum": float,
        "exclusiveMinimum": bool,
        "maxLength": int,
        "minLength": int,
        "pattern": string_type,
        "maxItems": int,
        "minItems": int,
        "uniqueItems": bool,
        # "enum": [Any]
        "multipleOf": int
    }
