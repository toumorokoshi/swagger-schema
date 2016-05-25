from swagger_schema.contact import Contact


def test_contact():
    result = {
        "name": "API Support",
        "url": "http://www.swagger.io/support",
        "email": "support@swagger.io"
    }
    output = Contact(result)
    assert output.name == "API Support"
    assert output.url == "http://www.swagger.io/support"
    assert output.email == "support@swagger.io"
    assert output.to_primitive() == result
