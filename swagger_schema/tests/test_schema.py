import pytest
from swagger_schema import Schema


@pytest.mark.parametrize("data", [
    {"type": "foo"},
    {"type": "array", "items": {"type": "string"}}
])
def test_schema(data):
    assert Schema(data).to_primitive() == data
