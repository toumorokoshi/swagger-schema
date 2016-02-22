from .serializer import SerializableObject


class TypedDict(dict, SerializableObject):
    """ a type key, value pair """

    _key_serializer = None
    _value_serializer = None
    _allowed_key_func = None

    def dump(self):
        out = {}
        for k, v in self.items():
            out[self._key_serializer.dump(k)] = self._value_serializer.dump(v)
        return out

    @classmethod
    def load(cls, from_dict):
        out = cls()
        for k, v in from_dict.items():
            out[cls._key_serializer.load(k)] = cls._value_serializer.load(v)
        return out

    def __setitem__(self, key, value):
        if self._allowed_key_func and not self._allowed_key_func(key):
            raise ValueError("unable to insert key {0} in {1}.".format(key, str(type(self))))
        key = self._key_serializer.load(key)
        value = self._value_serializer.load(value)
        super(TypedDict, self).__setitem__(key, value)
