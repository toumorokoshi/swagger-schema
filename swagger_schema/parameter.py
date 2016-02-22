import copy
from .lib.serializer import SerializableObject
from .lib.compat import string_type
from .items import Items

BASE_SCHEMA = {
    "attributes": {
        "name": string_type,
        "in": string_type,
        "description": string_type,
        "required": bool
    },
    "required": ["name", "in"]
}


def _extend_schema(base, extension):
    attributes = copy.copy(base["attributes"])
    attributes.update(extension.get("attributes", {}))
    required = list(set(base["required"]) | set(extension["required"]))
    return {
        "attributes": attributes,
        "required": required
    }


class Parameter(SerializableObject):
    _schema = dict(BASE_SCHEMA)


class QueryParameter(Parameter):
    _in = "query"
    pass


class BodyParameter(Parameter):
    _in = "body"


class NonBodyParameter(Parameter):
    _schema = _extend_schema(BASE_SCHEMA, {
        "attributes": {
            # string, number, integer, boolean, array,
            # file
            "type": string_type,
            "format": string_type,
            "allowEmptyValue": bool,
            "items": Items,
            "collectionFormat": string_type,
            # "default": Any,
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
            # "enum": list(any)
            "multipleOf": float
        },
        "required": []
    })


class HeaderParameter(NonBodyParameter):
    _in = "header"


class PathParameter(NonBodyParameter):
    _in = "path"


class FormDataParameter(NonBodyParameter):
    _in = "formData"
