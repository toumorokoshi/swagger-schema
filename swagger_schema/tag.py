from marshmallow import Schema, fields
from .external_documentation import ExternalDocumentation


class Tag(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
    externalDocs = fields.Nested(ExternalDocumentation)
