import copy
from .lib.serializer import SerializableObject
from .lib.compat import string_type

BASE_SCHEMA = {
    "attributes": {
        "name": string_type,
        "in": string_type,
        "description": string_type,
        "required": bool
    },
    "required": ["name", "in"]
}


class Parameter(SerializableObject):
    _schema = dict(BASE_SCHEMA)


class QueryParameter(Parameter):
    pass


class BodyParameter(Parameter):
    pass


class HeaderParameter(Parameter):
    pass


class PathParameter(Parameter):
    pass


def _extend_schema(base, extension):
    attributes = copy.copy(base["attributes"])
    attributes.update(extension.get("attributes", {}))
    required = list(set(base["required"]) + set(extension["required"]))
    return {
        "attributes": attributes,
        "required": required
    }
