from schematics.models import Model
from schematics.types import StringType, BooleanType
from schematics.types.serializable import serializable
from schematics.types.compound import (
    DictType, PolyModelType, ModelType
)
from .items import Items
from .schema import Schema


class _ParameterBase(Model):
    name = StringType(required=True)
    description = StringType()
    required = BooleanType()

    @serializable(serialized_name="in")
    def _in(self):
        self._IN


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
    schema = ModelType(Schema)


def _match_data_to_parameter(data):
    """ find the appropriate parameter for a parameter field """
    in_value = data["in"]
    for cls in [QueryParameter, HeaderParameter, FormDataParameter,
                PathParameter, BodyParameter]:
        if in_value == cls._IN:
            return cls
    return None


Parameters = DictType(
    PolyModelType([
        QueryParameter, HeaderParameter,
        FormDataParameter, PathParameter,
        BodyParameter
    ]),
    serialize_when_none=False
)
