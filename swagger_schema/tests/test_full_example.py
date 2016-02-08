from swagger_schema import (
    Info,
    Swagger
)


def test_full_example():
    swagger = Swagger()
    result = swagger.load({
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
    import pdb; pdb.set_trace()
