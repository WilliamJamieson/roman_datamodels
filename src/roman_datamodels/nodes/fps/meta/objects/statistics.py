from types import MappingProxyType

import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

__all__ = ["FpsStatistics"]


class FpsStatistics(rad.TaggedObjectNode):
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
    def mean_counts_per_sec(self) -> u.Quantity | None:
        return rad.NONUM * (u.DN / u.s)

    @rad.field
    def median_counts_per_sec(self) -> u.Quantity | None:
        return rad.NONUM * (u.DN / u.s)

    @rad.field
    def max_counts(self) -> u.Quantity | None:
        return u.Quantity(rad.NONUM, u.DN, dtype=np.int32)

    @rad.field
    def min_counts(self) -> u.Quantity | None:
        return u.Quantity(rad.NONUM, u.DN, dtype=np.int32)