from typing import Annotated

from pydantic import Field

from ..._defaults import default_constant_factory
from ..._enums import detector

__all__ = ["WfiDetector"]


WfiDetector = Annotated[
    detector,
    Field(
        default_factory=default_constant_factory(detector.WFI01.value),
        title="Name of detector used to acquire the data",
    ),
]
