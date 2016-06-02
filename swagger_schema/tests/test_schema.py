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
    })
])
def test_schema(name, data):
    assert Schema(data).to_primitive() == data
