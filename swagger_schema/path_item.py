from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import (
    PolyModelType, ListType, ModelType
)
from .operation import Operation
from .parameter import Parameter
from .reference import Reference


class PathItem(Model):

    get = ModelType(Operation)
    put = ModelType(Operation)
    post = ModelType(Operation)
    delete = ModelType(Operation)
    options = ModelType(Operation)
    head = ModelType(Operation)
    patch = ModelType(Operation)
    parameters = ListType(
        PolyModelType(Parameter, Reference)
    )
