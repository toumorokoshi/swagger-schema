from .lib.serializer import SerializableObject
from .operation import Operation


class Path(SerializableObject):
    _schema = {
        "attributes": {
            "get": Operation,
            "put": Operation,
            "post": Operation,
            "delete": Operation,
            "options": Operation,
            "head": Operation,
            "patch": Operation
            # parameters: [Parameter object | reference object]
        },
        "required": []
    }
