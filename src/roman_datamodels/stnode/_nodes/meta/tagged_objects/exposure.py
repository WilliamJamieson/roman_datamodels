from astropy.time import Time

from roman_datamodels.stnode import _core, _default

from ..untagged_scalars import ExposureType

__all__ = ["Exposure"]


class Exposure(_core.TaggedObjectNode):
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
        return self._get_node("type", ExposureType.WFI_IMAGE)

    @property
    def start_time(self) -> Time:
        return self._get_node("start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def mid_time(self) -> Time:
        return self._get_node("mid_time", lambda: Time("2020-01-01T01:00:00.0", format="isot", scale="utc"))

    @property
    def end_time(self) -> Time:
        return self._get_node("end_time", lambda: Time("2020-01-01T02:00:00.0", format="isot", scale="utc"))

    @property
    def nresultants(self) -> int:
        return self._get_node("nresultants", lambda: 6)

    @property
    def data_problem(self) -> bool:
        return self._get_node("data_problem", lambda: False)

    @property
    def frame_time(self) -> float:
        return self._get_node("frame_time", lambda: _default.NONUM)

    @property
    def exposure_time(self) -> float:
        return self._get_node("exposure_time", lambda: _default.NONUM)

    @property
    def effective_exposure_time(self) -> float:
        return self._get_node("effective_exposure_time", lambda: _default.NONUM)

    @property
    def ma_table_name(self) -> str:
        return self._get_node("ma_table_name", lambda: _default.NOSTR)

    @property
    def ma_table_number(self) -> int:
        return self._get_node("ma_table_number", lambda: _default.NONUM)

    @property
    def read_pattern(self) -> list[list[int]]:
        return self._get_node("read_pattern", lambda: [[1], [2, 3], [4], [5, 6, 7, 8], [9, 10], [11]])

    @property
    def truncated(self) -> bool:
        return self._get_node("truncated", lambda: False)
