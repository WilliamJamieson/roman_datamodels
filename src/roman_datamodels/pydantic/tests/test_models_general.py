import json

import pytest
from pydantic import ConfigDict, ValidationError

from roman_datamodels.pydantic._registry import URI_MODELS


class Mock:
    """
    Class which should fail any Roman field validation

    This is specifically not a MagicMock, because that can pass some of the validation
    checks.
    """

    pass


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


@pytest.mark.parametrize("cls", URI_MODELS.values())
def test_model_paused_validation_revalidate(cls):
    """Test that the model's paused validation works."""
    model = cls()

    for field_name in cls.model_fields:
        print(field_name)
        with pytest.raises(ValidationError):
            has_been_set = False
            with model.pause_validation():
                setattr(model, field_name, mock := Mock())
                assert getattr(model, field_name) is mock
                has_been_set = True

            # Ensure that the validation error happens on the exit of the context manager
            assert has_been_set


@pytest.mark.parametrize("cls", URI_MODELS.values())
def test_model_paused_validation_no_revalidate(cls):
    """Test that the model's paused validation works."""
    model = cls()

    for field_name in cls.model_fields:
        with model.pause_validation(revalidate_on_exit=False):
            setattr(model, field_name, mock := Mock())
            assert getattr(model, field_name) is mock


@pytest.mark.parametrize("cls", URI_MODELS.values())
def test_model_dict_access(cls):
    """Test that the model's dict access works, ie using model["field_name"]"""
    model = cls()

    for field_name in cls.model_fields:
        assert model[field_name] is getattr(model, field_name)


@pytest.mark.parametrize("cls", URI_MODELS.values())
def test_model_dict_set(cls):
    """Test the model's dict set works, ie using model["field_name"] = value"""
    model = cls()

    # Just to avoid validation issues
    with model.pause_validation(revalidate_on_exit=False):
        for field_name in cls.model_fields:
            mock = Mock()
            model[field_name] = mock
            assert getattr(model, field_name) is mock


@pytest.mark.parametrize("cls", URI_MODELS.values())
def test_model_set_arbitrary_field(cls):
    """Test that we can set arbitrary fields on the model. ie ones not defined in the model"""
    model = cls()

    # `foo` is not a field of the model
    assert "foo" not in model.model_fields

    # Set/check the extra field
    model.foo = "bar"
    assert model.foo == "bar"

    # Check that the extra field is not defined as an explicit field of the model
    assert "foo" not in model.model_fields

    # Do the same via dict access
    assert "baz" not in model.model_fields
    model["baz"] = "qux"
    assert model.baz == "qux"
    assert "baz" not in model.model_fields
