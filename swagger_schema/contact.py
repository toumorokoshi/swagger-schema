from marshmallow import Schema, fields


class Contact(Schema):
    name = fields.Str()
    url = fields.Str()
    email = fields.Str()
