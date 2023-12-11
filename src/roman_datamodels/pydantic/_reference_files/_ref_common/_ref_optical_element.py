from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._core import BaseRomanURIModel
from ..._datamodels import common
from ..._defaults import default_model_factory
from ..._uri import asdf_uri
from . import _ref_common as ref_common

__all__ = ["RefOpticalElement"]


class Instrument(ref_common.Instrument):
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
