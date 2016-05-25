import pytest


@pytest.fixture
def swagger():
    return {
        "swagger": "2.0"
    }


@pytest.fixture
def contact_json():
    return {
        "name": "API Support",
        "url": "http://www.swagger.io/support",
        "email": "support@swagger.io"
    }


@pytest.fixture
def license_json():
    return {
        "name": "Apache 2.0",
        "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
    }


@pytest.fixture
def info_json(contact_json, license_json):
    return {
        "title": "Swagger Sample App",
        "description": "This is a sample server Petstore server.",
        "termsOfService": "http://swagger.io/terms/",
        "contact": contact_json,
        "license": license_json,
        "version": "1.0.1"
    }
