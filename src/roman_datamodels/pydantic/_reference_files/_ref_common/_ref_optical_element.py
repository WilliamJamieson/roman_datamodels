from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._core import BaseRomanModel, BaseRomanURIModel
from ..._datamodels import common
from ..._defaults import default_model_factory
from ..._uri import asdf_uri

__all__ = ["RefOpticalElement"]


class Instrument(BaseRomanModel):
    optical_element: common.WfiOpticalElement


class RefOpticalElement(BaseRomanURIModel):
    _uri: ClassVar = asdf_uri.REF_OPTICAL_ELEMENT.value

    model_config = ConfigDict(
        title="Name of the filter element used",
    )

    instrument: Annotated[
        Instrument,
        Field(
            default_factory=default_model_factory(Instrument),
        ),
    ]
