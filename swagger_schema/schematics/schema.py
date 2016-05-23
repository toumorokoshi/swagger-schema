from schematics.models import Model
from schematics.types.compound import ListType
from schematics.types import (
    BaseType, BooleanType, FloatType, IntType, StringType
)
from .types import (
    DataTypeFormat
)


class Schema(Model):
    format = DataTypeFormat()
    title = StringType()
    default = BaseType()
    multipleOf = FloatType()
    maximum = FloatType()
    exclusiveMaximum = BooleanType()
    minimum = FloatType()
    exclusiveMinimum = BooleanType()
    maxLength = IntType()
    minLength = IntType()
    uniqueItems = BooleanType()
    enum = ListType(BaseType())
