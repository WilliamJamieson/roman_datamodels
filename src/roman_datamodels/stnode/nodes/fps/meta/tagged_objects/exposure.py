import numpy as np
from astropy.time import Time

from roman_datamodels.stnode import _base, _core, _default

from ..untagged_scalars import FpsExposureType

__all__ = ["FpsExposure"]


class FpsExposure(_core.TaggedObjectNode):
    """
    FPS Exposure information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/exposure-1.0.0"

    @property
    def type(self) -> FpsExposureType:
        return self._get_node("type", FpsExposureType.WFI_IMAGE)

    @property
    def start_time(self) -> Time:
        return self._get_node("start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def ngroups(self) -> int:
        return self._get_node("ngroups", lambda: 6)

    @property
    def nframes(self) -> int:
        return self._get_node("nframes", lambda: 8)

    @property
    def data_problem(self) -> bool:
        return self._get_node("data_problem", lambda: False)

    @property
    def frame_divisor(self) -> int:
        return self._get_node("frame_divisor", lambda: _default.NOINT)

    @property
    def groupgap(self) -> int:
        return self._get_node("groupgap", lambda: 0)

    @property
    def frame_time(self) -> float:
        return self._get_node("frame_time", lambda: _default.NONUM)

    @property
    def group_time(self) -> float:
        return self._get_node("group_time", lambda: _default.NONUM)

    @property
    def exposure_time(self) -> float:
        return self._get_node("exposure_time", lambda: _default.NONUM)

    @property
    def ma_table_name(self) -> str:
        return self._get_node("ma_table_name", lambda: _default.NOSTR)

    @property
    def ma_table_number(self) -> int:
        return self._get_node("ma_table_number", lambda: _default.NOINT)

    @property
    def read_pattern(self) -> _base.LNode[_base.LNode[int]]:
        def _default():
            base = np.arange(1, 56).reshape((-1, 1)).tolist()
            return _base.LNode([_base.LNode(row) for row in base])

        return self._get_node("read_pattern", _default)
