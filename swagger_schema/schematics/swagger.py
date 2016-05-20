from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType
from schematics.exceptions import ValidationError


def is_20(value):
    """ swagger's swagger field must be 2.0 """
    if value != "2.0":
        raise ValidationError("must be the value 2.0")


class Swagger(Model):
    swagger = StringType(validators=[is_20])
    info =
