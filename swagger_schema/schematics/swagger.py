from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType, ListType
from schematics.exceptions import ValidationError
from .types import MimeType

from .info import Info


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
