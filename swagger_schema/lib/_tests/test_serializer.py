import pytest
from ..serializer import SerializableObject
from ..compat import string_type


class Example(SerializableObject):
    _schema = {
        "attributes": {
            "string": string_type,
            "integer_list": [int]
        },
        "required": ["integer_list"]
    }


def test_required_parameters_missing_raises_typeerror():
    with pytest.raises(TypeError):
        Example(string="foo")


def test_nonparameters_passes():
    Example(integer_list=[1, 2, 3])


def test_additional_parameter_raises_typeerror():
    with pytest.raises(TypeError):
        Example(string="foo", extra_arg="bar", integer_list=[1, 2, 3])


def test_happy_path():
    e = Example(string="foo", integer_list=[1, 2, 3])
    assert e.dump() == {
        "string": "foo",
        "integer_list": [1, 2, 3]
    }
