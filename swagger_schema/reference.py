from schematics.models import Model
from schematics.types import StringType


class Reference(Model):
    ref = StringType(required=True, serialized_name="$ref",
                     deserialize_from="$ref")
