from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import (
    DictType, ListType, ModelType, PolyModelType
)
from .external_documentation import ExternalDocumentation
from .types import MimeType
from .parameter import Parameters
from .response import Response
from .reference import Reference


class Operation(Model):
    tags = ListType(StringType(), serialize_when_none=False)
    summary = StringType(serialize_when_none=False)
    description = StringType(serialize_when_none=False)
    externalDocs = ModelType(ExternalDocumentation, serialize_when_none=False)
    operationId = StringType(serialize_when_none=False)
    consumes = ListType(MimeType(), serialize_when_none=False)
    produces = ListType(MimeType(), serialize_when_none=False)
    parameters = Parameters
    responses = DictType(
        PolyModelType([Response, Reference]),
        required=True
    )
