from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType, ListType
from .external_documentation import ExternalDocumentation
from .types import MimeType


class Operation(Model):
    tags = ListType(StringType())
    summary = StringType()
    description = StringType()
    externalDocs = ModelType(ExternalDocumentation)
    operationId = StringType()
    consumes = ListType(MimeType())
    produces = ListType(MimeType())
    parameters
    pass
