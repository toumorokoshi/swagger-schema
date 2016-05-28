from schematics.models import Model
from schematics.types.compound import ListType, PolyModelType
from schematics.types import (
    BaseType, BooleanType, FloatType, IntType, StringType
)
from .types import (
    DataTypeFormat, RegularExpression
)


class Schema(Model):
    multipleOf = FloatType(min_value=0)
    maximum = FloatType()
    exclusiveMaximum = BooleanType()
    minimum = FloatType()
    exclusiveMinimum = BooleanType()
    pattern = RegularExpression()
    maxLength = IntType(min_value=0)
    minLength = IntType(min_value=0)
    maxItems = IntType()
    # for arrays

    type = StringType()
    format = DataTypeFormat()
    title = StringType()
    default = BaseType()
    uniqueItems = BooleanType()
    enum = ListType(BaseType())

# for arrays
additionalItems = PolyModelType([BooleanType(), Schema])
items = PolyModelType([BooleanType(), Schema])
