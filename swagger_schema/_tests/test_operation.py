from swagger_schema import Operation


def test_operation():
    test = {
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
    operation = Operation.load(test)
    assert operation.dump() == test
