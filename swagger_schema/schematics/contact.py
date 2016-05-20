from schematics.models import Model
from schematics.types import StringType


class Contact(Model):
    name = StringType()
    url = StringType()
    email = StringType()
