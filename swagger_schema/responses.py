from .lib.typeddict import TypedDict
from .lib.serializer import _get_serializer
from .lib.compat import string_type
from .response import Response


class Responses(TypedDict):

    _key_serializer = _get_serializer(string_type)
    _value_serializer = _get_serializer(Response)

    @staticmethod
    def _allowed_key_func(k):
        if k == "default":
            return True
        k = int(k)
        if k > 100 and k < 1000:
            return True
