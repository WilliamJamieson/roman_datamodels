import asdf
import pytest

from roman_datamodels.pydantic._registry import TAGGED_MODELS


@pytest.mark.parametrize("model", TAGGED_MODELS.values())
def test_serialize(tmp_path, model):
    file_name = tmp_path / "test.asdf"
    asdf.AsdfFile({"test": model()}).write_to(file_name)

    with asdf.open(file_name) as af:
        assert isinstance(af.tree["test"], model)
        model.model_validate(af.tree["test"])
