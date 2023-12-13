from typing import Annotated

from pydantic import Field

from roman_datamodels.pydantic import _defaults, _strenum

__all__ = ["ExposureType"]


class exposure_type(_strenum.StrEnum):
    WFI_IMAGE = "WFI_IMAGE"
    WFI_GRISM = "WFI_GRISM"
    WFI_PRISM = "WFI_PRISM"
    WFI_DARK = "WFI_DARK"
    WFI_FLAT = "WFI_FLAT"
    WFI_WFSC = "WFI_WFSC"


ExposureType = Annotated[
    exposure_type,
    Field(
        default_factory=_defaults.default_constant_factory(exposure_type.WFI_IMAGE.value),
        title="Type of data in the exposure (viewing mode)",
    ),
]
