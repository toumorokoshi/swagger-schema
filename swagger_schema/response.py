from marshmallow import Schema, fields
from .jsonschema import JsonSchema


class Response(Schema):
    descriptions = fields.Str(required=True)
    schema = fields.Nested(JsonSchema)
    pass
