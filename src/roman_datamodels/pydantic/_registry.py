__all__ = []


def _subcls_gen(cls):
    for subcls in cls.__subclasses__():
        yield subcls
        yield from _subcls_gen(subcls)


def _build_registry():
    from . import _core

    uri_models = {}
    tagged_models = {}
    data_models = {}
    ref_models = {}

    for model in _subcls_gen(_core.BaseRomanURIModel):
        if model.__name__.startswith("Base"):
            continue

        if issubclass(model, _core.BaseRomanURIModel):
            if model._uri in uri_models and issubclass(model, uri_models[model._uri]):
                continue
            else:
                uri_models[model._uri] = model

        if issubclass(model, _core.BaseRomanTaggedModel):
            if model._tag_uri in tagged_models and issubclass(model, tagged_models[model._tag_uri]):
                continue
            else:
                tagged_models[model._tag_uri] = model

        if issubclass(model, _core.BaseRomanStepModel):
            if model.__name__ in data_models and issubclass(model, data_models[model.__name__]):
                raise ValueError(f"Duplicate data model: {model.__name__}")
            else:
                data_models[model.__name__] = model

        if issubclass(model, _core.BaseRomanRefModel):
            if model.__name__ in ref_models and issubclass(model, ref_models[model.__name__]):
                raise ValueError(f"Duplicate ref model: {model.__name__}")
            else:
                ref_models[model.__name__] = model

    return {
        "URI_MODELS": uri_models,
        "TAGGED_MODELS": tagged_models,
        "DATA_MODELS": data_models,
        "REF_MODELS": ref_models,
    }


def __getattr__(name: str):
    model_registry = _build_registry()
    if name in model_registry:
        return model_registry[name]

    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
