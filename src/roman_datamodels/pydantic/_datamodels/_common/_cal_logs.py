from typing import Annotated

from pydantic import Field

from ..._defaults import default_constant_factory

__all__ = ["CalLogs"]


CalLogs = Annotated[
    list[str],
    Field(
        default_factory=default_constant_factory(
            [
                "2021-11-15T09:15:07.12Z :: FlatFieldStep :: INFO :: Completed",
                "2021-11-15T10:22.55.55Z :: RampFittingStep :: WARNING :: Wow, lots of Cosmic Rays detected",
            ]
        ),
        title="Calibration log messages",
    ),
]
