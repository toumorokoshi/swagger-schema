from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import DictType, ModelType
from .schema import Schema


class Response(Model):
    description = StringType(required=True)
    schema = ModelType(Schema)
    # headers
    # examples


Responses = DictType(Response)
