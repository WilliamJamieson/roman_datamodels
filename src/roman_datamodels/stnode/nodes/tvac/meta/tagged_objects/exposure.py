import numpy as np
from astropy.time import Time

from roman_datamodels.stnode import core, rad

from ..untagged_scalars import TvacExposureType

__all__ = ["TvacExposure"]


class TvacExposure(rad.TaggedObjectNode):
    """
    Tvac Exposure information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/exposure-1.0.0"

    @rad.field
    def type(self) -> TvacExposureType:
        return self._get_node("type", lambda: TvacExposureType.WFI_IMAGE)

    @rad.field
    def start_time(self) -> Time:
        return self._get_node("start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def ngroups(self) -> int:
        return self._get_node("ngroups", lambda: 6)

    @rad.field
    def nframes(self) -> int:
        return self._get_node("nframes", lambda: 8)

    @rad.field
    def data_problem(self) -> bool:
        return self._get_node("data_problem", lambda: False)

    @rad.field
    def frame_divisor(self) -> int:
        return self._get_node("frame_divisor", lambda: rad.NOINT)

    @rad.field
    def groupgap(self) -> int:
        return self._get_node("groupgap", lambda: 0)

    @rad.field
    def frame_time(self) -> float:
        return self._get_node("frame_time", lambda: rad.NONUM)

    @rad.field
    def group_time(self) -> float:
        return self._get_node("group_time", lambda: rad.NONUM)

    @rad.field
    def exposure_time(self) -> float:
        return self._get_node("exposure_time", lambda: rad.NONUM)

    @rad.field
    def ma_table_name(self) -> str:
        return self._get_node("ma_table_name", lambda: rad.NOSTR)

    @rad.field
    def ma_table_number(self) -> int:
        return self._get_node("ma_table_number", lambda: rad.NOINT)

    @rad.field
    def read_pattern(self) -> core.LNode[core.LNode[int]]:
        def _default():
            base = np.arange(1, 56).reshape((-1, 1)).tolist()
            return core.LNode([core.LNode(row) for row in base])

        return self._get_node("read_pattern", _default)
