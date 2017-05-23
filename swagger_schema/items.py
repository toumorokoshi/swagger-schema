from schematics.models import Model, FieldDescriptor
from schematics.types import (
    BaseType, BooleanType, IntType, FloatType, StringType
)
from schematics.types.compound import (
    ListType, ModelType
)
from .types import DiscreteStringType, DataTypeFormat


class Items(Model):
    type = DataTypeFormat(required=True)
    format = StringType(
        required=False,
        serialize_when_none=False)
    collectionFormat = DiscreteStringType(
        valid_strings=["csv", "ssv", "tsv", "pipes"],
        serialize_when_none=False
    )
    default = BaseType(
        required=False,
        serialize_when_none=False)
    maximum = FloatType(
        required=False,
        serialize_when_none=False)
    exclusiveMaximum = BooleanType(
        required=False,
        serialize_when_none=False)
    minimum = FloatType(
        required=False,
        serialize_when_none=False)
    exclusiveMinimum = BooleanType(
        required=False,
        serialize_when_none=False)
    maxLength = IntType(
        required=False,
        serialize_when_none=False)
    minLength = IntType(
        required=False,
        serialize_when_none=False)
    pattern = StringType(
        required=False,
        serialize_when_none=False)
    maxItems = IntType(
        required=False,
        serialize_when_none=False)
    minItems = IntType(
        required=False,
        serialize_when_none=False)
    uniqueItems = BooleanType(
        required=False,
        serialize_when_none=False)
    enum = ListType(BaseType(),
                    required=False,
                    serialize_when_none=False)
    multipleOf = FloatType(required=False,
                           serialize_when_none=False)
    items_ = ModelType("Items",
                       required=False,
                       serialized_name="items",
                       deserialize_from=["items"],
                       serialize_when_none=False)
