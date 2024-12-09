import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _default, rad

__all__ = ["FpsStatistics"]


class FpsStatistics(rad.TaggedObjectNode):
    """
    FPS Summary Statistics
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/statistics-1.0.0"

    @rad.field
    def mean_counts_per_sec(self) -> u.Quantity | None:
        return self._get_node("mean_counts_per_sec", lambda: _default.NONUM * (u.DN / u.s))

    @rad.field
    def median_counts_per_sec(self) -> u.Quantity | None:
        return self._get_node("median_counts_per_sec", lambda: _default.NONUM * (u.DN / u.s))

    @rad.field
    def max_counts(self) -> u.Quantity | None:
        return self._get_node("max_counts", lambda: u.Quantity(_default.NONUM, u.DN, dtype=np.int32))

    @rad.field
    def min_counts(self) -> u.Quantity | None:
        return self._get_node("min_counts", lambda: u.Quantity(_default.NONUM, u.DN, dtype=np.int32))
