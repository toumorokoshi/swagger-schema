from marshmallow import Schema, fields
from .items import Items


class Header(Schema):
    description = fields.Str()
    # one of
    # - string
    # - number
    # - integer
    # - boolean
    # - array
    type = fields.Str()
    # extending format for
    # the previously mentioned type.
    format = fields.Str()
    items = fields.Nested(Items)
