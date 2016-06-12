import random
from collections import OrderedDict
from schematics.types import StringType
from schematics.types.compound import DictType
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


class SortedDictType(DictType):
    """ a dict type, which outputs sorted values for "to_primitive" """

    def _export(self, dict_instance, format, context):
        output = super(SortedDictType, self)._export(dict_instance, format, context)
        sorted_output = OrderedDict()
        for k in sorted(output.keys()):
            sorted_output[k] = output[k]
        return sorted_output
