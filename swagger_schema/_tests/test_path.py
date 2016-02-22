from swagger_schema import Path


def test_path():
    test = {
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
    path = Path.load(test)
    assert path.dump() == test
