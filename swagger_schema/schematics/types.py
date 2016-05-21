from schematics.types import StringType
from schematics.exceptions import ValidationError


class MimeType(StringType):
    pass


VALID_DATATYPES = [
    "string", "number", "integer", "boolean",
    "array", "file"
]


def _is_valid_datatype(value):
    if value not in VALID_DATATYPES:
        raise ValidationError("{0} is not a valid dataype (one of {1})".format(
            value, VALID_DATATYPES
        ))


class DataType(StringType):
    pass
