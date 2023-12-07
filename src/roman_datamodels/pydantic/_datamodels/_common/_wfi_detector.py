from typing import Annotated

from pydantic import Field

from ..._defaults import default_constant_factory
from ..._enums import StrEnum

__all__ = ["WfiDetector"]


class detector(StrEnum):
    WFI01 = "WFI01"
    WFI02 = "WFI02"
    WFI03 = "WFI03"
    WFI04 = "WFI04"
    WFI05 = "WFI05"
    WFI06 = "WFI06"
    WFI07 = "WFI07"
    WFI08 = "WFI08"
    WFI09 = "WFI09"
    WFI10 = "WFI10"
    WFI11 = "WFI11"
    WFI12 = "WFI12"
    WFI13 = "WFI13"
    WFI14 = "WFI14"
    WFI15 = "WFI15"
    WFI16 = "WFI16"
    WFI17 = "WFI17"
    WFI18 = "WFI18"


WfiDetector = Annotated[
    detector,
    Field(
        default_factory=default_constant_factory(detector.WFI01.value),
        title="Name of detector used to acquire the data",
    ),
]
