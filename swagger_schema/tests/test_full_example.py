from swagger_schema import (
    Info,
    Operation,
    PathItem,
    Response,
    Swagger
)


def test_full_example():
    swagger = Swagger({
        "info": Info({
            "title": "example",
            "version": "1.0"
        }),
        "paths": {
            "/test": PathItem({
                "get": Operation({
                    "summary": "this is a test",
                    "consumes": ["application/json"],
                    "produces": ["application/json"],
                    "responses": {
                        "200": Response({
                            "description": "a list of pets"
                        })
                    }
                })
            })
        },
        "swagger": "2.0"
    })
    full = {
        "swagger": "2.0",
        "info": {
            "title": "Swagger Sample App",
            "version": "1.0",
        },
        "paths": {
            "/pets": {
                "get": {
                    "summary": "this is a test",
                    "consumes": ["application/json"],
                    "produces": ["application/json"],
                    "responses": {
                        "200": {
                            "description": "A list of pets.",
                        }
                    }
                }
            }
        },
    }
    result = Swagger(full)
    assert result.to_primitive() == full

#                            "schema":  {
#                                "type": "object",
#                                "descriminator": "petType",
#                                "properties": {
#                                    "name": {
#                                        "type": "string"
#                                    },
#                                    "petType": {
#                                        "type": "string"
#                                    }
#                                },
#                                "required": ["name", "petType"]
#                            }
