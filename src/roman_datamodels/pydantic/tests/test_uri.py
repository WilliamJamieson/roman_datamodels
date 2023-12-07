import pytest

from roman_datamodels.pydantic._uri import asdf_tag_uri, asdf_uri, base_uri, version


@pytest.mark.parametrize("uri", asdf_uri)
def test_asdf_uris(uri):
    """Test the asdf reference uris"""
    assert isinstance(uri, asdf_uri)
    assert isinstance(uri, str)

    assert uri.startswith(base_uri.SCHEMA.value)
    assert uri.endswith(f"-{version.VERSION.value}")


@pytest.mark.parametrize("uri", asdf_tag_uri)
def test_asdf_tag_uris(uri):
    """Test the asdf tag uris"""
    assert isinstance(uri, asdf_tag_uri)
    assert isinstance(uri, str)

    assert uri.startswith(base_uri.TAG.value)
    assert uri.endswith(f"-{version.VERSION.value}")
