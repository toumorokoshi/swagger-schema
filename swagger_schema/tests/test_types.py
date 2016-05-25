import pytest
from swagger_schema.types import DataTypeFormat
from schematics.exceptions import ValidationError


@pytest.mark.parametrize("typ", [
    "string", "number", "integer",
    "boolean", "array"
])
def test_valid_datatypes(typ):
    validator = DataTypeFormat()
    result = validator.to_native(typ)
    assert result == typ


def test_invalid_datatypes():
    validator = DataTypeFormat()
    with pytest.raises(ValidationError):
        validator.validate("ooga")
