from types import MappingProxyType
from typing import TypeAlias

import numpy as np
from astropy.units import DN, Quantity, s

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

    @property
    @rad.field
    def mean_counts_per_sec(self: rad.Node) -> Quantity | None:
        return rad.NONUM * (DN / s)

    @property
    @rad.field
    def median_counts_per_sec(self: rad.Node) -> Quantity | None:
        return rad.NONUM * (DN / s)

    @property
    @rad.field
    def max_counts(self: rad.Node) -> Quantity | None:
        return Quantity(rad.NONUM, DN, dtype=np.int32)

    @property
    @rad.field
    def min_counts(self: rad.Node) -> Quantity | None:
        return Quantity(rad.NONUM, DN, dtype=np.int32)
