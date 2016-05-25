from swagger_schema.external_documentation import ExternalDocumentation


def test_external_documentation():
    result = {
        "description": "Find more info here",
        "url": "https://swagger.io"
    }
    output = ExternalDocumentation(result)
    assert output.description == "Find more info here"
    assert output.url == "https://swagger.io"
    assert output.to_primitive() == result
