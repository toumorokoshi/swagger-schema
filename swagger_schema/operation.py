from marshmallow import Schema, fields
from .external_documentation import ExternalDocumentation


class Operation(Schema):
    tags = fields.Str()  # many
    summary = fields.Str()
    description = fields.Str()
    operationId = fields.Str()
    consumes = fields.Str()  # many
    produces = fields.Str()  # many
    schemes = fields.Str()  # many
    deprecated = fields.Bool()
    externalDocs = fields.Nested(ExternalDocumentation)
    # security = [security requirement object]
    # responses = responses object required
    # parameters = [parameter object | reference object]
    pass
