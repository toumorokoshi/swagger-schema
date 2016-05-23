from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType

from .contact import Contact
from .license import License


class Info(Model):
    title = StringType(required=True)
    description = StringType()
    termsOfService = StringType()
    contact = ModelType(Contact)
    license = ModelType(License)
    version = StringType(required=True)
