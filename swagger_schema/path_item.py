from schematics.models import Model
from schematics.types.compound import (
    PolyModelType, ListType, ModelType
)
from .operation import Operation
from .reference import Reference
from .parameter import (
    QueryParameter, HeaderParameter,
    FormDataParameter, PathParameter,
    BodyParameter
)


class PathItem(Model):

    get = ModelType(Operation)
    put = ModelType(Operation)
    post = ModelType(Operation)
    delete = ModelType(Operation)
    options = ModelType(Operation)
    head = ModelType(Operation)
    patch = ModelType(Operation)
    parameters = ListType(
        PolyModelType([QueryParameter, HeaderParameter,
                      FormDataParameter, PathParameter,
                       BodyParameter, Reference])
    )
