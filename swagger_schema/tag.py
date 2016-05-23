from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType
from .external_documentation import ExternalDocumentation


class Tag(Model):
    name = StringType(required=True)
    description = StringType()
    externalDocs = ModelType(ExternalDocumentation)
