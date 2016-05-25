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

    get = ModelType(Operation, serialize_when_none=False)
    put = ModelType(Operation, serialize_when_none=False)
    post = ModelType(Operation, serialize_when_none=False)
    delete = ModelType(Operation, serialize_when_none=False)
    options = ModelType(Operation, serialize_when_none=False)
    head = ModelType(Operation, serialize_when_none=False)
    patch = ModelType(Operation, serialize_when_none=False)
    parameters = ListType(
        PolyModelType([QueryParameter, HeaderParameter,
                      FormDataParameter, PathParameter,
                       BodyParameter, Reference]),
        serialize_when_none=False
    )
