from schematics.models import Model
from schematics.types import BaseType, StringType, BooleanType
from schematics.types.serializable import serializable
from schematics.types.compound import ModelType
from .items import Items
from .types import DiscreteStringType, DataType


class _ParameterBase(Model):
    name = StringType(required=True)
    description = StringType()
    required = BooleanType()

    @serializable(serialized_name="in")
    def _in(self):
        self._IN


class _ParameterNonbody(Model):
    type = DataType(required=True)
    format = StringType()
    allowEmptyValue = BooleanType()
    items = ModelType(Items)
    collectionFormat = DiscreteStringType(
        valid_strings=["csv", "ssv", "tsv", "pipes"]
    )
    default = BaseType()


class QueryParameter(Items, _ParameterBase):
    _IN = "query"


class HeaderParameter(Items, _ParameterBase):
    _IN = "header"


class FormDataParameter(Items, _ParameterBase):
    _IN = "formData"


class PathParameter(Items, _ParameterBase):
    _IN = "path"
    required = BooleanType(required=True)


class BodyParameter(_ParameterBase):
    _IN = "path"
    # schema = SchemaObject
