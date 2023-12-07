from typing import Annotated

from pydantic import Field

from ..._defaults import default_constant_factory
from ..._enums import exposure_type

__all__ = ["ExposureType"]

ExposureType = Annotated[
    exposure_type,
    Field(
        default_factory=default_constant_factory(exposure_type.WFI_IMAGE.value),
        title="Type of data in the exposure (viewing mode)",
    ),
]
