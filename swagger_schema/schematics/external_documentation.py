from schematics.models import Model
from schematics.types import StringType


class ExternalDocumentation(Model):
    description = StringType()
    url = StringType(required=True)
