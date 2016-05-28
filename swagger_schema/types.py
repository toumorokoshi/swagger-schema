import random
from schematics.types import StringType
from schematics.exceptions import StopValidation


class MimeType(StringType):
    pass


class RegularExpression(StringType):
    pass


class DiscreteStringType(StringType):
    """ a string type where only a specific set is valid. """

    def __init__(self, valid_strings=None, **kwargs):
        super(DiscreteStringType, self).__init__(**kwargs)
        self.valid_strings = valid_strings or []

    def _mock(self, context):
        return random.choice(self.valid_strings)

    def validate_data(self, value):
        if value not in self.valid_strings:
            raise StopValidation("not one of {0})".format(
                self.valid_strings
            ))


class DataTypeFormat(StringType):

    VALID_DATATYPES = [
        "string", "number", "integer",
        "boolean", "array"
    ]

    def __init__(self, additional_valid_types=None, **kwargs):
        super(DataTypeFormat, self).__init__(**kwargs)
        self.valid_datatypes = self.VALID_DATATYPES + (
            additional_valid_types or []
        )

    def _mock(self, context):
        return random.choice(self.valid_datatypes)

    def validate_data(self, value):
        if value not in self.valid_datatypes:
            raise StopValidation("not a valid dataype (one of {0})".format(
                self.valid_datatypes
            ))
