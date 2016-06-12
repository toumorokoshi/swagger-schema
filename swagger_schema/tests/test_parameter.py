from swagger_schema import QueryParameter


def test_query_parameter():
    param = QueryParameter({
        "name": "foo",
        "description": "bar",
        "required": False,
        "type": "string"
    })

    assert param.to_primitive() == {
        "name": "foo",
        "description": "bar",
        "required": False,
        "in": "query",
        "type": "string"
    }
