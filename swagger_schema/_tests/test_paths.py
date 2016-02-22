from swagger_schema import Paths


def test_paths():
    test = {
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
    }
    paths = Paths.load(test)
    assert paths.dump() == test
