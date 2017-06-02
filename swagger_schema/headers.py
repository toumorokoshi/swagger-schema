from schematics.types import StringType
from schematics.types.compound import DictType, ModelType
from .items import Items

class Header(Items):
    description = StringType(required=False)



Headers = DictType(ModelType(Header), serialize_when_none=False)
