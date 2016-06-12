from schematics.models import Model
from schematics.types import StringType, BooleanType
from schematics.types.serializable import serializable
from schematics.types.compound import (
    ListType, PolyModelType, ModelType
)
from .items import Items
from .schema import Schema


class _ParameterBase(Model):
    name = StringType(required=True)
    description = StringType(serialize_when_none=False)
    required = BooleanType(serialize_when_none=False)


class QueryParameter(Items, _ParameterBase):
    IN = "query"
    _in = StringType(default=IN,
                     serialized_name="in")


class HeaderParameter(Items, _ParameterBase):
    IN = "header"
    _in = StringType(default=IN,
                     serialized_name="in")


class FormDataParameter(Items, _ParameterBase):
    IN = "formData"
    _in = StringType(default=IN,
                     serialized_name="in")


class PathParameter(Items, _ParameterBase):
    IN = "path"
    _in = StringType(default=IN,
                     serialized_name="in")
    required = BooleanType(required=True)


class BodyParameter(_ParameterBase):
    IN = "body"
    _in = StringType(default=IN,
                     serialized_name="in")
    schema = ModelType(Schema, required=True)


def _match_data_to_parameter(cls, data):
    """ find the appropriate parameter for a parameter field """
    in_value = data["in"]
    for cls in [QueryParameter, HeaderParameter, FormDataParameter,
                PathParameter, BodyParameter]:
        if in_value == cls.IN:
            return cls
    return None


Parameters = ListType(
    PolyModelType([
        QueryParameter, HeaderParameter,
        FormDataParameter, PathParameter,
        BodyParameter
    ], claim_function=_match_data_to_parameter),
    serialize_when_none=False
)
