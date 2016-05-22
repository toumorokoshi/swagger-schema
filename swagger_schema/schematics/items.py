from schematics.models import Model, FieldDescriptor
from schematics.types import (
    BaseType, BooleanType, IntType, FloatType, StringType
)
from schematics.types.compound import (
    ListType, ModelType
)
from .types import DiscreteStringType, DataType


class Items(Model):
    type = DataType()
    format = StringType()
    collectionFormat = DiscreteStringType(
        valid_strings=["csv", "ssv", "tsv", "pipes"]
    )
    default = BaseType()
    maximum = FloatType()
    exclusiveMaximum = BooleanType()
    minimum = FloatType()
    exclusiveMinimum = BooleanType()
    maxLength = IntType()
    minLength = IntType()
    pattern = StringType()
    maxItems = IntType()
    minItems = IntType()
    uniqueItems = BooleanType()
    enum = ListType(BaseType())
    multipleOf = FloatType()

# a workaround for self-referential types.
# replace when a blessed way to self-reference is provided.
Items._fields["items"] = ModelType(Items)
setattr(Items, "items", FieldDescriptor("items"))
