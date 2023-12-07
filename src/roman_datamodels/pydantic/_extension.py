from asdf.extension import Extension

# Import all the models so they get registered
from . import _datamodels  # noqa: F401
from . import _reference_files  # noqa: F401
from ._converter import RomanDataModelConverter
from ._registry import TAGGED_MODELS
from ._uri import asdf_extra_uri

# Add all the models to the converter
RomanDataModelConverter.from_registry(TAGGED_MODELS)


class RomanPydanticExtension(Extension):
    extension_uri = asdf_extra_uri.EXTENSION.value
    converters = [RomanDataModelConverter()]
    tags = list(TAGGED_MODELS.keys())
