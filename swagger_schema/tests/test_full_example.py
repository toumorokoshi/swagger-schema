from swagger_schema import (
    Info,
    Operation,
    Path,
    Paths,
    Swagger
)


def test_full_example():
    swagger = Swagger(
        info=Info(title="example", version="1.0"),
        paths=Paths({
            "/test": Path(
                get=Operation(
                    summary="this is a test",
                    description="this is only a test",
                    consumes=[
                        "application/json",
                        "text/x-yaml"
                    ],
                    produces=[
                        "application/json",
                        "text/x-yaml"
                    ]
                )
            )
        }),
        swagger="2.0"
    )
    import pdb; pdb.set_trace()
    result = Swagger.load({
        "swagger": "2.0",
        "info": {
            "title": "Swagger Sample App",
            "description": "This is a sample server Petstore server.",
        },
        "paths": {
            "/pets": {
                "get": {
                    "description": "Returns all pets from the system that the user has access to.",
                    "produces": ["application/json"],
                    "responses": {
                        "200": {
                            "description": "A list of pets.",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/pet"
                                }
                            }
                        }
                    }
                }
            }
        },
        "definitions": {
            "pet": {
                "type": "object",
                "descriminator": "petType",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "petType": {
                        "type": "string"
                    }
                },
                "required": ["name", "petType"]
            }
        }
    })
