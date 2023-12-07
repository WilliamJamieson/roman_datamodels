from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._core import BaseRomanModel, BaseRomanURIModel
from ..._datamodels import common
from ..._defaults import default_constant_factory, default_model_factory
from ..._uri import asdf_uri

__all__ = ["RefExposureType"]


class Exposure(BaseRomanModel):
    type: common.ExposureType
    p_exptype: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("WFI_IMAGE|WFI_GRISM|WFI_PRISM|"),
            title="Applicable exposure type",
            pattern="^((WFI_IMAGE|WFI_GRISM|WFI_PRISM|WFI_DARK|WFI_FLAT|WFI_WFSC)\\s*\\|\\s*)+$",
        ),
    ]


class RefExposureType(BaseRomanURIModel):
    _uri: ClassVar = asdf_uri.REF_EXPOSURE_TYPE.value

    model_config = ConfigDict(
        title="Type of data in the reference file exposure (viewing mode)",
    )

    exposure: Annotated[
        Exposure,
        Field(
            default_factory=default_model_factory(Exposure),
        ),
    ]
