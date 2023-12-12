import pytest

from roman_datamodels.pydantic._core import BaseRomanRefModel, BaseRomanStepModel, BaseRomanTaggedModel, BaseRomanURIModel
from roman_datamodels.pydantic._registry import REF_MODELS, STEP_MODELS, TAGGED_MODELS, URI_MODELS
from roman_datamodels.pydantic._uri import asdf_tag_uri, asdf_uri, base_uri


@pytest.mark.parametrize(("uri", "model"), URI_MODELS.items())
def test_uri_models(uri, model):
    assert uri in asdf_uri
    assert uri.startswith(base_uri.SCHEMA)
    assert issubclass(model, BaseRomanURIModel)


@pytest.mark.parametrize(("tag_uri", "model"), TAGGED_MODELS.items())
def test_tagged_models(tag_uri, model):
    assert tag_uri in asdf_tag_uri
    assert tag_uri.startswith(base_uri.TAG)
    assert issubclass(model, BaseRomanTaggedModel)


def test_all_uris_registered():
    assert set(asdf_uri) == set(URI_MODELS.keys())


def test_all_tags_registered():
    assert set(asdf_tag_uri) == set(TAGGED_MODELS.keys())


@pytest.mark.parametrize("model", STEP_MODELS.values())
def test_data_models(model):
    assert issubclass(model, BaseRomanStepModel)

    assert model._uri in URI_MODELS
    assert model is URI_MODELS[model._uri]

    assert model._tag_uri in TAGGED_MODELS
    assert model is TAGGED_MODELS[model._tag_uri]

    assert model.__name__ not in REF_MODELS
    assert model not in REF_MODELS.values()


@pytest.mark.parametrize("model", REF_MODELS.values())
def test_ref_models(model):
    assert issubclass(model, BaseRomanRefModel)

    assert model._uri in URI_MODELS
    assert model is URI_MODELS[model._uri]

    assert model._tag_uri in TAGGED_MODELS
    assert model is TAGGED_MODELS[model._tag_uri]

    assert model.__name__ not in STEP_MODELS
    assert model not in STEP_MODELS.values()


def test_datamodels_distinct_from_refmodels():
    assert set(STEP_MODELS.keys()).isdisjoint(set(REF_MODELS.keys()))
