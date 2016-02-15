from .compat import string_type


class SerializerNotFound(Exception):
    pass


class SerializableObject(object):
    """
    helps serialize objects to and
    from the desired type.
    """

    def __init__(self, **kwargs):
        self._serializer = self._create_serializer()
        for k, v in self._serializer.items():
            if k not in kwargs:
                raise TypeError("type {0} requires an argument {1}".format(
                    type(self), k
                ))
            setattr(self, k, v.load(kwargs[k]))
            del kwargs[k]
        if len(kwargs):
            raise TypeError("type {0} does not accept arguments {1}".format(
                type(self), kwargs.keys()
            ))

    def dump(self):
        out_dict = {}
        for k, serializer in self._serializer.items():
            val = getattr(self, k)
            out_dict[k] = serializer.dump(val)
        return out_dict

    @classmethod
    def load(cls, from_dict):
        return cls(**from_dict)

    @classmethod
    def _create_serializer(cls):
        serializer = {}
        for name, typ in cls._schema.items():
            serializer[name] = _get_serializer(typ)
        return serializer


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
    elif issubclass(typ, SerializableObject):
        return SerializerObjectSerializer(typ)
    else:
        for basetype in BASETYPE_SERIALIZERS:
            if issubclass(basetype, typ):
                return BASETYPE_SERIALIZERS[basetype]
    raise SerializerNotFound()


class StringSerializer(object):
    @staticmethod
    def dump(value):
        return str(value)

    @staticmethod
    def load(raw_value):
        return str(raw_value)


class IntSerializer(object):
    @staticmethod
    def dump(value):
        return int(value)

    @staticmethod
    def load(raw_value):
        return int(raw_value)


class FloatSerializer(object):
    @staticmethod
    def dump(value):
        return float(value)

    @staticmethod
    def load(raw_value):
        return float(raw_value)


class BoolSerializer(object):
    @staticmethod
    def dump(value):
        return bool(value)

    @staticmethod
    def load(raw_value):
        return bool(raw_value)


class ListSerializer(object):

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
