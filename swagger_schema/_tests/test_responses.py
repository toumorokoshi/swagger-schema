from swagger_schema import Responses


def test_responses():
    test = {
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
    responses = Responses.load(test)
    assert responses.dump() == test
