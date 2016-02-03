from marshmallow import Schema, fields


class Parameter(Schema):
    name = fields.Str(required=True)
    # possible values are:
    # query, header, path, formData, or body
    in = fields.Str(required=True)
    description = fields.Str()
    required = fields.Bool()


class BodyParameter(Parameter):
    # schema == Schema object
    pass


class NonBodyParameter(Parameter):
    type = fields.Str()
    format = fields.Str()
    allowEmptyValue = fields.Bool()
    collectionFormat = fields.Str()
    maximum = fields.Int()  # actually a number
    exclusiveMaximum = fields.Bool()
    minimum = fields.Int()  # actually a number
    exclusiveMinimum = fields.Bool()
    maxLength = fields.Int()
    minLength = fields.Int()
    pattern = fields.Str()
    maxItems = fields.Int()
    minItems = fields.Int()
    uniqueItems = fields.Boolean()
    multipleOf = fields.Int()  # actually a number
    # enum = ?
    #   items = Items object
    #   possible values are csv, ssv, tsv, pipes, multi
    #   default value =
