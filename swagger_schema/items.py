from schematics.models import Model, FieldDescriptor
from schematics.types import (
    BaseType, BooleanType, IntType, FloatType, StringType
)
from schematics.types.compound import (
    ListType, ModelType
)
from .types import DiscreteStringType, DataTypeFormat


class Items(Model):
    type = DataTypeFormat()
    format = StringType(required=False)
    collectionFormat = DiscreteStringType(
        valid_strings=["csv", "ssv", "tsv", "pipes"]
    )
    default = BaseType(required=False)
    maximum = FloatType(required=False)
    exclusiveMaximum = BooleanType(required=False)
    minimum = FloatType(required=False)
    exclusiveMinimum = BooleanType(required=False)
    maxLength = IntType(required=False)
    minLength = IntType(required=False)
    pattern = StringType(required=False)
    maxItems = IntType(required=False)
    minItems = IntType(required=False)
    uniqueItems = BooleanType(required=False)
    enum = ListType(BaseType(), required=False)
    multipleOf = FloatType(required=False)
    items = ModelType("Items")
