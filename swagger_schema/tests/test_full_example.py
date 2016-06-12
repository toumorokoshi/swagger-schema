from __future__ import unicode_literals
from swagger_schema import (
    Info,
    Operation,
    PathItem,
    Response,
    Schema,
    Swagger,
    QueryParameter
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
                    "parameters": [
                        QueryParameter({
                            "name": "foo",
                            "description": "a foo parameter.",
                            "required": False,
                            "type": "string"
                        })
                    ],
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
                }),
            }),
            "/z": PathItem({
                "get": Operation({
                    "summary": "this is a test",
                    "consumes": ["application/json"],
                    "produces": ["application/json"],
                    "responses": {
                        "200": Response({
                            "description": "a list of pets",
                            "schema": Schema({
                                "type": "string",
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
            "/z": {
                "get": {
                    "summary": "this is a test",
                    "consumes": ["application/json"],
                    "produces": ["application/json"],
                    "responses": {
                        "200": {
                            "description": "a list of pets",
                            "schema": {
                                "type": "string",
                            }
                        }
                    }
                }
            },
            "/test": {
                "get": {
                    "summary": "this is a test",
                    "consumes": ["application/json"],
                    "produces": ["application/json"],
                    "parameters": [
                        {
                            "in": "query",
                            "name": "foo",
                            "description": "a foo parameter.",
                            "required": False,
                            "type": "string"
                        }
                    ],
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
    assert swagger.to_primitive() == full
    result = Swagger(full)
    output = result.to_primitive()
    assert output == full
    # assert the sorted order is correct.
    assert list(output["paths"].keys()) == ["/test", "/z"]
