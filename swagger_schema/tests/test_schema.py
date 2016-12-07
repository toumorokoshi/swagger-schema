import pytest
from swagger_schema import Schema


@pytest.mark.parametrize("name, data", [
    ("basic_object", {"type": "foo"}),
    ("array", {"type": "array", "items": {"type": "string"}}),
    ("complex", {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "petType": {"type": "string"}
        },
        "required": ["name", "petType"]
    }),
    ("additional_props", {
        "type": "object",
        "additionalProperties": {"type": "number"}
    }),
])
def test_schema(name, data):
    assert Schema(data).to_primitive() == data


def test_type_required():
    with pytest.raises(Exception):
        Schema({}).validate()
