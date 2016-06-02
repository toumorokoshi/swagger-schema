from __future__ import unicode_literals
from swagger_schema import (
    Info,
    Operation,
    PathItem,
    Response,
    Schema,
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
                            "description": "a list of pets",
                            "schema": Schema({
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    },
                                    "petType": {
                                        "type": "string"
                                    }
                                },
                                "required": ["name", "petType"]
                            })
                        })
                    }
                })
            })
        }
    })
    full = {
        "swagger": "2.0",
        "info": {
            "title": "example",
            "version": "1.0"
        },
        "paths": {
            "/test": {
                "get": {
                    "summary": "this is a test",
                    "consumes": ["application/json"],
                    "produces": ["application/json"],
                    "responses": {
                        "200": {
                            "description": "a list of pets",
                            "schema": {
                                "type": "object",
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
        }
    }
    result = Swagger(full)
    output = result.to_primitive()
    assert output == full
    assert swagger.to_primitive() == full
