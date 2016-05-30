import pytest
from swagger_schema.license import License
from schematics.exceptions import BaseError


def test_license():
    result = {
        "name": "Apache 2.0",
        "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
    }
    output = License(result)
    assert output.name == "Apache 2.0"
    assert output.url == "http://www.apache.org/licenses/LICENSE-2.0.html"
    assert output.to_primitive() == result


def test_license_no_name():
    """ name is required """
    with pytest.raises(BaseError):
        l = License({"url": "http://www.apache.org/licenses/LICENSE-2.0.html"})
        l.validate()
