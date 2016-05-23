from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import (
    DictType, ModelType, ListType
)
from schematics.exceptions import ValidationError
from .external_documentation import ExternalDocumentation
from .path_item import PathItem
from .schema import Schema
from .parameter import Parameters
from .info import Info
from .response import Responses
from .tag import Tag


def _is_20(value):
    """ swagger's swagger field must be 2.0 """
    if value != "2.0":
        raise ValidationError("must be the value 2.0")


def _starts_with_leading_slash(value):
    if not value.startswith("/"):
        raise ValidationError("must start with leading slash")


VALID_PROTOCOLS = ["http", "https", "ws", "wss"]


def _is_supported_protocol(value):
    if value not in VALID_PROTOCOLS:
        raise ValidationError("{0} is not a supported protocol (one of {1})".format(
            value, VALID_PROTOCOLS
        ))


class Swagger(Model):
    swagger = StringType(validators=[_is_20])
    info = ModelType(Info)
    host = StringType()
    basePath = StringType(validators=[_starts_with_leading_slash])
    schemes = ListType(StringType(validators=[_is_supported_protocol]))
    consumes = ListType(StringType())
    produces = ListType(StringType())
    paths = DictType(ModelType(PathItem))
    definitions = DictType(ModelType(Schema))
    parameters = Parameters
    responses = Responses
    # security definitions
    # security_requirement
    tags = ListType(ModelType(Tag))
    externalDocs = ModelType(ExternalDocumentation)
