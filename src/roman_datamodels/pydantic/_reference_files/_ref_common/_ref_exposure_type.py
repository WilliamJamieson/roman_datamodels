from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _core, _datamodels, _defaults
from roman_datamodels.pydantic import _uri as uri

__all__ = ["RefExposureType"]


class Exposure(_core.BaseRomanModel):
    type: _datamodels.common.ExposureType
    p_exptype: Annotated[
        str,
        Field(
            default_factory=_defaults.default_constant_factory("WFI_IMAGE|WFI_GRISM|WFI_PRISM|"),
            title="Applicable exposure type",
            pattern="^((WFI_IMAGE|WFI_GRISM|WFI_PRISM|WFI_DARK|WFI_FLAT|WFI_WFSC)\\s*\\|\\s*)+$",
        ),
    ]


class RefExposureType(_core.BaseRomanURIModel):
    _uri: ClassVar = uri.asdf_uri.REF_EXPOSURE_TYPE.value

    model_config = ConfigDict(
        title="Type of data in the reference file exposure (viewing mode)",
    )

    exposure: Annotated[
        Exposure,
        Field(
            default_factory=_defaults.default_model_factory(Exposure),
        ),
    ]
