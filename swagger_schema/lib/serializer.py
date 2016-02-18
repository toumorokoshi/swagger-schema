from .compat import string_type


class SerializerNotFound(Exception):
    pass


class SerializableObject(object):
    """
    helps serialize objects to and
    from the desired type.
    """

    def __init__(self, **kwargs):
        self._serializer, self._required_values \
            = self._create_serializer()
        for k, v in self._serializer.items():
            if k in kwargs:
                setattr(self, k, v.load(kwargs[k]))
                del kwargs[k]
            elif k in self._required_values:
                raise TypeError("type {0} requires an argument {1}".format(
                    type(self), k
                ))
        if len(kwargs):
            raise TypeError("type {0} does not accept arguments {1}".format(
                type(self), kwargs.keys()
            ))

    def dump(self):
        out_dict = {}
        for k, serializer in self._serializer.items():
            if hasattr(self, k):
                val = getattr(self, k)
                out_dict[k] = serializer.dump(val)
        return out_dict

    @classmethod
    def load(cls, from_dict):
        return cls(**from_dict)

    @classmethod
    def _create_serializer(cls):
        serializer = {}
        for name, typ in cls._schema["attributes"].items():
            serializer[name] = _get_serializer(typ)
        return (
            serializer,
            cls._schema.get("required", cls._schema["attributes"].keys())
        )


class SerializerObjectSerializer(object):

    def __init__(self, typ):
        self._typ = typ

    @staticmethod
    def dump(value):
        return value.dump()

    def load(self, raw_value):
        if isinstance(raw_value, self._typ):
            return raw_value
        return self._typ(**raw_value)


def _get_serializer(typ):
    if isinstance(typ, list):
        return ListSerializer(typ[0])
    elif issubclass(typ, Serializer):
        return typ
    elif issubclass(typ, SerializableObject):
        return SerializerObjectSerializer(typ)
    else:
        for basetype in BASETYPE_SERIALIZERS:
            if issubclass(basetype, typ):
                return BASETYPE_SERIALIZERS[basetype]
    raise SerializerNotFound()


class Serializer(object):
    """ """

    def dump(self, value):
        pass

    def load(value):
        pass


class StringSerializer(Serializer):
    @staticmethod
    def dump(value):
        return str(value)

    @staticmethod
    def load(raw_value):
        return str(raw_value)


class IntSerializer(Serializer):
    @staticmethod
    def dump(value):
        return int(value)

    @staticmethod
    def load(raw_value):
        return int(raw_value)


class FloatSerializer(Serializer):
    @staticmethod
    def dump(value):
        return float(value)

    @staticmethod
    def load(raw_value):
        return float(raw_value)


class BoolSerializer(Serializer):
    @staticmethod
    def dump(value):
        return bool(value)

    @staticmethod
    def load(raw_value):
        return bool(raw_value)


class ListSerializer(Serializer):

    def __init__(self, subtype):
        self._subtype = subtype
        self._subtype_serializer = _get_serializer(subtype)

    def dump(self, values):
        return [
            self._subtype_serializer.dump(v) for v in values
        ]

    def load(self, raw_values):
        return [
            self._subtype_serializer.load(v) for v in raw_values
        ]

BASETYPE_SERIALIZERS = {
    string_type: StringSerializer,
    int: IntSerializer,
    float: FloatSerializer,
    bool: BoolSerializer
}
