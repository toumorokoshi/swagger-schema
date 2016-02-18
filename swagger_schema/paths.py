from .lib.typeddict import TypedDict
from .lib.serializer import _get_serializer, string_type
from .path import Path


class Paths(TypedDict):
    _key_serializer = _get_serializer(string_type)
    _value_serializer = _get_serializer(Path)
    # idk what to do about this.
    # <path> -> Path Item
