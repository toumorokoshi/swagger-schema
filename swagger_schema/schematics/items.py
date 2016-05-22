from schematics.models import Model
from schematics.types import (
    BaseType, BooleanType, IntType, NumberType, StringType
)
from schematics.types.compound import (
    ListType, ModelType
)
from .types import DiscreteStringType, DataType


class Items(Model):
    type = DataType()
    format = StringType()
    items = ModelType("Items")
    collectionFormat = DiscreteStringType(
        valid_strings=["csv", "ssv", "tsv", "pipes"]
    )
    default = BaseType()
    maximum = NumberType()
    exclusiveMaximum = BooleanType()
    minimum = NumberType()
    exclusiveMinimum = BooleanType()
    maxLength = IntType()
    minLength = IntType()
    pattern = StringType()
    maxItems = IntType()
    minItems = IntType()
    uniqueItems = BooleanType()
    enum = ListType(BaseType())
    multipleOf = NumberType()
