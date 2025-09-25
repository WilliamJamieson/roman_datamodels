import pytest

from roman_datamodels.stnode._stnode import MANIFESTS


@pytest.fixture(scope="session", params=MANIFESTS)
def manifest(request):
    return request.param
