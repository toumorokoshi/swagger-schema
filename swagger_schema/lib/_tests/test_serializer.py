import pytest
from swagger_schema.lib.serializer import SerializableObject
from swagger_schema.lib.compat import string_type


class Example(SerializableObject):
    _schema = {
        "string": string_type,
        "integer_list": [int]
    }


def test_required_parameters_missing_raises_typeerror():
    with pytest.raises(TypeError):
        Example(string="foo")


def test_additional_parameter_raises_typeerror():
    with pytest.raises(TypeError):
        Example(string="foo", extra_arg="bar", integer_list=[1, 2, 3])


def test_happy_path():
    e = Example(string="foo", integer_list=[1, 2, 3])
    assert e.dump() == {
        "string": "foo",
        "integer_list": [1, 2, 3]
    }
