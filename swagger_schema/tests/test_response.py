from swagger_schema import Header, Headers, Response


def test_response():
    response = {
        "description": "foo",
        "schema": {
            "type": "boolean"
        },
        "headers": {
            "location": {
                "description": "foo",
                "type": "string"
            }
        }
    }
    response_obj = Response(response)
    response_obj.validate()
    assert response_obj.to_primitive() == response
