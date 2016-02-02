from marshmallow import Schema, fields


class License(Schema):
    name = fields.Str(required=True)
    url = fields.Str()
