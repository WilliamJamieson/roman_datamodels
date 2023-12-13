from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _core, _datamodels, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _ref_common

__all__ = ["RefOpticalElement"]


class Instrument(_ref_common.Instrument):
    optical_element: _datamodels.common.WfiOpticalElement


class RefOpticalElement(_core.BaseRomanURIModel):
    _uri: ClassVar = uri.asdf_uri.REF_OPTICAL_ELEMENT.value

    model_config = ConfigDict(
        title="Name of the filter element used",
    )

    instrument: Annotated[
        Instrument,
        Field(
            default_factory=_defaults.default_model_factory(Instrument),
        ),
    ]
