import numpy as np
from astropy.time import Time

from roman_datamodels.stnode import _default, core, rad

from ..untagged_scalars import FpsExposureType

__all__ = ["FpsExposure"]


class FpsExposure(rad.TaggedObjectNode):
    """
    FPS Exposure information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/exposure-1.0.0"

    @rad.rad_field
    def type(self) -> FpsExposureType:
        return self._get_node("type", lambda: FpsExposureType.WFI_IMAGE)

    @rad.rad_field
    def start_time(self) -> Time:
        return self._get_node("start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.rad_field
    def ngroups(self) -> int:
        return self._get_node("ngroups", lambda: 6)

    @rad.rad_field
    def nframes(self) -> int:
        return self._get_node("nframes", lambda: 8)

    @rad.rad_field
    def data_problem(self) -> bool:
        return self._get_node("data_problem", lambda: False)

    @rad.rad_field
    def frame_divisor(self) -> int:
        return self._get_node("frame_divisor", lambda: _default.NOINT)

    @rad.rad_field
    def groupgap(self) -> int:
        return self._get_node("groupgap", lambda: 0)

    @rad.rad_field
    def frame_time(self) -> float:
        return self._get_node("frame_time", lambda: _default.NONUM)

    @rad.rad_field
    def group_time(self) -> float:
        return self._get_node("group_time", lambda: _default.NONUM)

    @rad.rad_field
    def exposure_time(self) -> float:
        return self._get_node("exposure_time", lambda: _default.NONUM)

    @rad.rad_field
    def ma_table_name(self) -> str:
        return self._get_node("ma_table_name", lambda: _default.NOSTR)

    @rad.rad_field
    def ma_table_number(self) -> int:
        return self._get_node("ma_table_number", lambda: _default.NOINT)

    @rad.rad_field
    def read_pattern(self) -> core.LNode[core.LNode[int]]:
        def _default():
            base = np.arange(1, 56).reshape((-1, 1)).tolist()
            return core.LNode([core.LNode(row) for row in base])

        return self._get_node("read_pattern", _default)
