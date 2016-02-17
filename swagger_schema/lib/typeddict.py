from .serializer import _get_serializer, SerializableObject


class TypedDict(SerializableObject):
    """ a type key, value pair """

    _key_type =

    def __init__(self, key_type, value_type):
        self._dict = {}
        self._key_type = key_type
        self._key_serializer = _get_serializer(key_type)
        self._value_type = value_type
        self._value_serializer = _get_serializer(value_type)

    def dump(self):
        return dict(self._dict)

    @classmethod
    def load(self, from_dict):
        out = TypedDict(self._key_type, self._value_type)
        for k, v in from_dict.items():
            out[k] = v
        return out

    def __setitem__(self, key, value):
        key = self._key_serializer.load(key)
        value = self._value_serializer.load(value)
        self._dict[key] = value

    def __getitem__(self, key):
        return self._dict.__getitem__(key)

    def __delitem__(self, key):
        return self._dict.__delitem__(key)

    def __contains__(self, item):
        return self._dict.__contains__(item)
