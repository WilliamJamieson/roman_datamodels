from astropy.time import Time

from roman_datamodels.stnode import _core
from roman_datamodels.stnode._nodes.untagged_scalars import ExposureType

__all__ = ["Exposure"]


class Exposure(_core.TaggedNode):
    """
    Exposure information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/exposure-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "type",
            "start_time",
            "mid_time",
            "end_time",
            "nresultants",
            "data_problem",
            "frame_time",
            "exposure_time",
            "effective_exposure_time",
            "ma_table_name",
            "ma_table_number",
            "read_pattern",
            "truncated",
        )

    @property
    def type(self) -> ExposureType:
        if not self._has_node("type"):
            self.type = ExposureType.WFI_IMAGE()
        return self._get_node("type")

    @property
    def start_time(self) -> Time:
        if not self._has_node("start_time"):
            self.start_time = Time("2020-01-01T00:00:00.0", format="isot", scale="utc")
        return self._get_node("start_time")

    @property
    def mid_time(self) -> Time:
        if not self._has_node("mid_time"):
            self.mid_time = Time("2020-01-01T01:00:00.0", format="isot", scale="utc")
        return self._get_node("mid_time")

    @property
    def end_time(self) -> Time:
        if not self._has_node("end_time"):
            self.end_time = Time("2020-01-01T02:00:00.0", format="isot", scale="utc")
        return self._get_node("end_time")

    @property
    def nresultants(self) -> int:
        if not self._has_node("nresultants"):
            self.nresultants = 6
        return self._get_node("nresultants")

    @property
    def data_problem(self) -> bool:
        if not self._has_node("data_problem"):
            self.data_problem = False
        return self._get_node("data_problem")

    @property
    def frame_time(self) -> float:
        if not self._has_node("frame_time"):
            self.frame_time = _core.NONUM
        return self._get_node("frame_time")

    @property
    def exposure_time(self) -> float:
        if not self._has_node("exposure_time"):
            self.exposure_time = _core.NONUM
        return self._get_node("exposure_time")

    @property
    def effective_exposure_time(self) -> float:
        if not self._has_node("effective_exposure_time"):
            self.effective_exposure_time = _core.NONUM
        return self._get_node("effective_exposure_time")

    @property
    def ma_table_name(self) -> str:
        if not self._has_node("ma_table_name"):
            self.ma_table_name = _core.NOSTR
        return self._get_node("ma_table_name")

    @property
    def ma_table_number(self) -> int:
        if not self._has_node("ma_table_number"):
            self.ma_table_number = _core.NONUM
        return self._get_node("ma_table_number")

    @property
    def read_pattern(self) -> list[list[int]]:
        if not self._has_node("read_pattern"):
            self.read_pattern = [[1], [2, 3], [4], [5, 6, 7, 8], [9, 10], [11]]
        return self._get_node("read_pattern")

    @property
    def truncated(self) -> bool:
        if not self._has_node("truncated"):
            self.truncated = False
        return self._get_node("truncated")
