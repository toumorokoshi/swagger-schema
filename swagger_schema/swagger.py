from marshmallow import Schema, fields
from .info import Info
from .external_documentation import ExternalDocumentation


class Swagger(Schema):
    swagger = fields.Str(required=True)
    host = fields.Str()
    basePath = fields.Str()
    info = fields.Nested(Info)
    schemes = fields.Str()  # many
    consumes = fields.Str()  # many
    produces = fields.Str()  # many
    externalDocs = fields.Nested(ExternalDocumentation)
    # paths = path object (required)
    # definitions = definitons object
    # parameters = parameters definition object
    # responses = responses definitions object
    # securityDefinitions = security definition object
    # security = security requirement object
    # tags = [Tag object]
