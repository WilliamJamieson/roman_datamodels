import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core, _default

__all__ = ["FpsStatistics"]


class FpsStatistics(_core.TaggedObjectNode):
    """
    FPS Summary Statistics
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/statistics-1.0.0"

    @property
    def mean_counts_per_sec(self) -> u.Quantity | None:
        return self._get_node("mean_counts_per_sec", lambda: _default.NONUM * (u.DN / u.s))

    @property
    def median_counts_per_sec(self) -> u.Quantity | None:
        return self._get_node("median_counts_per_sec", lambda: _default.NONUM * (u.DN / u.s))

    @property
    def max_counts(self) -> u.Quantity | None:
        return self._get_node("max_counts", lambda: u.Quantity(_default.NONUM, u.DN, dtype=np.int32))

    @property
    def min_counts(self) -> u.Quantity | None:
        return self._get_node("min_counts", lambda: u.Quantity(_default.NONUM, u.DN, dtype=np.int32))
