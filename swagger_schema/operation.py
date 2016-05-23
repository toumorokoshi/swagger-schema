from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import (
    DictType, ListType, ModelType, PolyModelType
)
from .external_documentation import ExternalDocumentation
from .types import MimeType
from .parameter import Parameters


class Operation(Model):
    tags = ListType(StringType())
    summary = StringType()
    description = StringType()
    externalDocs = ModelType(ExternalDocumentation)
    operationId = StringType()
    consumes = ListType(MimeType())
    produces = ListType(MimeType())
    parameters = Parameters
