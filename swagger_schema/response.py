from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import DictType, ModelType
from .schema import Schema


class Response(Model):
    description = StringType(required=True, serialize_when_none=False)
    schema = ModelType(Schema, serialize_when_none=False)
    # headers
    # examples


Responses = DictType(ModelType(Response), serialize_when_none=False)
