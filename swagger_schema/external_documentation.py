from marshmallow import Schema, fields


class ExternalDocumentation(Schema):
    description = fields.Str()
    url = fields.Str(required=True)
