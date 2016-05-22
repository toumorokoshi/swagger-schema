import pytest
from swagger_schema.schematics import Items

@pytest.mark.parametrize("schema", [
    {"type": "string", "minLength": 2}
])
def test_valid_items(schema):
    Items(schema).validate()
