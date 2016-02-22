from swagger_schema import (
    Info,
    Operation,
    Path,
    Paths,
    Responses,
    Response,
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
                    ],
                    responses=Responses({
                        200: Response(
                            description="ok"
                        )
                    })
                )
            )
        }),
        swagger="2.0"
    )
    result = Swagger.load({
        "swagger": "2.0",
        "info": {
            "title": "Swagger Sample App",
            "version": "1.0",
        },
        "paths": {
            "/pets": {
                "get": {
                    "description": "Returns all pets from the system that the user has access to.",
                    "produces": ["application/json"],
                    "responses": {
                        "200": {
                            "description": "A list of pets.",
                            "schema":  {
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
                    }
                }
            }
        },
    })
    print(result.dump())
