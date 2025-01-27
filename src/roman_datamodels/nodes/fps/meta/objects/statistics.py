from types import MappingProxyType
from typing import TypeAlias, cast

import numpy as np
from astropy.units import DN, Quantity, s  # type: ignore[attr-defined]

from roman_datamodels.stnode import rad

__all__ = ["FpsStatistics"]

_FpsStatistics: TypeAlias = Quantity | None


class FpsStatistics(rad.TaggedObjectNode[_FpsStatistics]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/statistics-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/statistics-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/statistics-1.0.0"
            }
        )

    @rad.field
    def mean_counts_per_sec(self) -> Quantity | None:
        return cast(Quantity, rad.NONUM * (DN / s))

    @rad.field
    def median_counts_per_sec(self) -> Quantity | None:
        return cast(Quantity, rad.NONUM * (DN / s))

    @rad.field
    def max_counts(self) -> Quantity | None:
        return Quantity(rad.NONUM, DN, dtype=np.int32)

    @rad.field
    def min_counts(self) -> Quantity | None:
        return Quantity(rad.NONUM, DN, dtype=np.int32)
