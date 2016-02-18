from .lib.typeddict import TypedDict
from .lib.serializer import _get_serializer
from .lib.compat import string_type


class SecurityRequirement(TypedDict):
    _key_serializer = _get_serializer(string_type)
    _value_serializer = _get_serializer([string_type])
