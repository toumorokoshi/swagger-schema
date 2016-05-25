from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType

from .contact import Contact
from .license import License


class Info(Model):
    title = StringType(required=True)
    description = StringType(serialize_when_none=False)
    termsOfService = StringType(serialize_when_none=False)
    contact = ModelType(Contact, serialize_when_none=False)
    license = ModelType(License, serialize_when_none=False)
    version = StringType(required=True)
