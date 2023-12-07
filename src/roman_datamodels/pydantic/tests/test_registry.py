import pytest
from pydantic import BaseModel

from roman_datamodels.pydantic._core import BaseRomanDataModel, BaseRomanRefModel, BaseRomanTaggedModel, BaseRomanURIModel
from roman_datamodels.pydantic._registry import DATA_MODELS, REF_MODELS, TAGGED_MODELS, TAGGED_TYPES, URI_MODELS, URI_TYPES
from roman_datamodels.pydantic._uri import asdf_tag_uri, asdf_uri, base_uri


@pytest.mark.parametrize(("uri", "model"), URI_MODELS.items())
def test_uri_models(uri, model):
    assert uri in asdf_uri
    assert uri.startswith(base_uri.SCHEMA)
    assert issubclass(model, BaseRomanURIModel)


@pytest.mark.parametrize(("uri", "type_"), URI_TYPES.items())
def test_uri_types(uri, type_):
    assert uri in asdf_uri
    assert uri.startswith(base_uri.SCHEMA)
    assert not issubclass(type(type_), BaseModel)


@pytest.mark.parametrize(("tag_uri", "model"), TAGGED_MODELS.items())
def test_tagged_models(tag_uri, model):
    assert tag_uri in asdf_tag_uri
    assert tag_uri.startswith(base_uri.TAG)
    assert issubclass(model, BaseRomanTaggedModel)


@pytest.mark.parametrize(("tag_uri", "type_"), TAGGED_TYPES.items())
def test_tagged_types(tag_uri, type_):
    assert tag_uri in asdf_tag_uri
    assert tag_uri.startswith(base_uri.TAG)
    assert not issubclass(type(type_), BaseModel)


def test_all_uris_registered():
    assert set(asdf_uri) == set(URI_MODELS.keys()).union(set(URI_TYPES.keys()))


def test_all_tags_registered():
    assert set(asdf_tag_uri) == set(TAGGED_MODELS.keys()).union(set(TAGGED_TYPES.keys()))


@pytest.mark.parametrize("model", DATA_MODELS.values())
def test_data_models(model):
    assert issubclass(model, BaseRomanDataModel)

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

    assert model.__name__ not in DATA_MODELS
    assert model not in DATA_MODELS.values()


def test_datamodels_distinct_from_refmodels():
    assert set(DATA_MODELS.keys()).isdisjoint(set(REF_MODELS.keys()))
