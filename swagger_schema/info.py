from marshmallow import Schema, fields
from .contact import Contact
from .license import License


class Info(Schema):
    title = fields.Str(required=True)
    description = fields.Str()
    termsOfService = fields.Str()
    version = fields.Str(required=True)
    contact = fields.Nested(Contact)
    license = fields.Nested(License)
