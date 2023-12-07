import json

import pytest
from pydantic import ConfigDict

from roman_datamodels.pydantic._registry import URI_MODELS


@pytest.mark.parametrize(("uri", "cls"), URI_MODELS.items())
def test_uri_id_in_json_schema(uri, cls):
    """Test that the URI is in the JSON schema."""
    assert cls.model_json_schema()["id"] == uri


@pytest.mark.parametrize("cls", URI_MODELS.values())
def test_datamodels_defaults_validate(cls):
    """Test that the default values validate."""

    class TestModel(cls):
        model_config = ConfigDict(
            # This forces the model to validate the default values when its instantiated
            # Normally, this is off for performance reasons.
            validate_default=True,
        )

    # Create model to see that it validates
    TestModel()


@pytest.mark.parametrize("cls", URI_MODELS.values())
def test_dump_model_json(cls):
    """Test that the model's json schema output can be dumped to JSON."""
    json.dumps(cls.model_json_schema())
