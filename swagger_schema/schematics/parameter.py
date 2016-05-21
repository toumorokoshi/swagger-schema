from schematics.models import Model
from schematics.types import StringType, BooleanType
from schematics.types.compound import ModelType
from schematics.exceptions import ValidationError


class _ParameterBase(Model):
    name = StringType(required=True)
    description = StringType()
    required = BooleanType()
    pass


class _ParameterNonbody(Model):
    type = StringType(required=True, validators=[_is_valid_datatype])
    format = StringType()
    allowEmptyValue = BooleanType()
    # items =
    pass


class QueryParameter(_ParameterBase):
    # in = query
    pass


class BodyParameter(_ParameterBase):
    # in = body
    # schema = SchemaObject


class HeaderParameter(_ParameterBase):
    # in = header
    pass


class FormDataParameter(_ParameterBase):
    # in = formData
    pass


class PathParameter(_ParameterBase):
    # in = path
    required = BooleanType(required=True)
