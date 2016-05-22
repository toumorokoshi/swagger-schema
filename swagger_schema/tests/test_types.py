import pytest
from swagger_schema.schematics.types import DataType
from schematics.exceptions import ValidationError


@pytest.mark.parametrize("typ", [
    "string", "number", "integer",
    "boolean", "array"
])
def test_valid_datatypes(typ):
    validator = DataType()
    result = validator.to_native(typ)
    assert result == typ


def test_invalid_datatypes():
    validator = DataType()
    with pytest.raises(ValidationError):
        validator.validate("ooga")
