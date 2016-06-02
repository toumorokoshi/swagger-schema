from schematics.models import Model
from schematics.types.compound import (
    DictType, ListType, PolyModelType, ModelType
)
from schematics.types import (
    BaseType, BooleanType, FloatType, IntType, StringType
)
from .types import (
    DataTypeFormat, RegularExpression
)


class Schema(Model):
    multipleOf = FloatType(min_value=0, serialize_when_none=False)
    # must be present if exclusiveMaximum is present.
    maximum = FloatType(serialize_when_none=False)
    exclusiveMaximum = BooleanType(serialize_when_none=False)
    # must be present if exclusiveMinimum is present.
    minimum = FloatType(serialize_when_none=False)
    exclusiveMinimum = BooleanType(serialize_when_none=False)

    # validation for strings
    maxLength = IntType(min_value=0, serialize_when_none=False)
    minLength = IntType(min_value=0, serialize_when_none=False)
    pattern = RegularExpression(serialize_when_none=False)

    # validation for arrays
    additionalItems = PolyModelType([BooleanType(), "Schema"],
                                    serialize_when_none=False)
    items = PolyModelType(["Schema", ListType(ModelType("Schema"))],
                          serialize_when_none=False)
    maxItems = IntType(min_value=0, serialize_when_none=False)
    minItems = IntType(min_value=0, serialize_when_none=False)
    uniqueItems = BooleanType(serialize_when_none=False)

    # validation for objects
    maxProperties = IntType(min_value=0, serialize_when_none=False)
    minProperties = IntType(min_value=0, serialize_when_none=False)
    additionalProperties = PolyModelType([BooleanType(), "Schema"],
                                         serialize_when_none=False)
    properties = DictType(ModelType("Schema"), serialize_when_none=False)
    patternProperties = DictType(ModelType("Schema"),
                                 serialize_when_none=False)
    dependencies = ModelType("Schema", serialize_when_none=False)
    required = ListType(StringType(), min_size=1, serialize_when_none=False)

    # any type
    enum = ListType(BaseType(), serialize_when_none=False)
    type = StringType(serialize_when_none=False)
    format = DataTypeFormat(serialize_when_none=False)
    allOf = ListType(ModelType("Schema"), serialize_when_none=False)
    anyOf = ListType(ModelType("Schema"), serialize_when_none=False)
    oneOf = ListType(ModelType("Schema"), serialize_when_none=False)
    # not = ModelType("Schema")
    definitions = ModelType("Schema", serialize_when_none=False)
    title = StringType(serialize_when_none=False)
    description = StringType(serialize_when_none=False)
    default = BaseType(serialize_when_none=False)
