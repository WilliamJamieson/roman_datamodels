import asdf
import pytest

from roman_datamodels.pydantic._core import BaseRomanDataModel
from roman_datamodels.pydantic._registry import TAGGED_MODELS


@pytest.mark.parametrize("model", TAGGED_MODELS.values())
def test_serialize(tmp_path, model):
    file_name = tmp_path / "test.asdf"
    mdl = model.maker(testing=True) if issubclass(model, BaseRomanDataModel) else model()
    asdf.AsdfFile({"test": mdl}).write_to(file_name)

    with asdf.open(file_name) as af:
        assert isinstance(af.tree["test"], model)
        model.model_validate(af.tree["test"])
