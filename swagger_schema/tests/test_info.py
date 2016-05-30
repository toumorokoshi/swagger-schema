import pytest
from schematics.exceptions import BaseError
from swagger_schema import Contact, License, Info


def test_info(contact_json, license_json, info_json):
    output = Info(info_json)
    assert output.title == info_json["title"]
    assert output.description == info_json["description"]
    assert output.termsOfService == info_json["termsOfService"]
    assert output.contact == Contact(info_json["contact"])
    assert output.license == License(info_json["license"])
    assert output.version == info_json["version"]


def test_info_version_required(info_json):
    del info_json["version"]
    with pytest.raises(BaseError):
        Info(info_json).validate()


def test_info_title_required(info_json):
    del info_json["title"]
    with pytest.raises(BaseError):
        Info(info_json).validate()
