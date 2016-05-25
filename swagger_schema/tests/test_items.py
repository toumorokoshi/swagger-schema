import pytest
from swagger_schema import Items


@pytest.mark.parametrize("schema", [
    {"type": "string", "minLength": 2},
    {"type": "array", "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 63
    }}
])
def test_valid_items(schema):
    Items(schema).validate()
