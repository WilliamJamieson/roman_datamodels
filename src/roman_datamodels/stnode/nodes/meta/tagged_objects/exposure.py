from astropy.time import Time

from roman_datamodels.stnode import _default, core, rad

from ..untagged_scalars import ExposureType

__all__ = ["Exposure"]


class Exposure(rad.TaggedObjectNode):
    """
    Exposure information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/exposure-1.0.0"

    @rad.rad_field
    def type(self) -> ExposureType:
        return self._get_node("type", lambda: ExposureType.WFI_IMAGE)

    @rad.rad_field
    def start_time(self) -> Time:
        return self._get_node("start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.rad_field
    def mid_time(self) -> Time:
        return self._get_node("mid_time", lambda: Time("2020-01-01T01:00:00.0", format="isot", scale="utc"))

    @rad.rad_field
    def end_time(self) -> Time:
        return self._get_node("end_time", lambda: Time("2020-01-01T02:00:00.0", format="isot", scale="utc"))

    @rad.rad_field
    def nresultants(self) -> int:
        return self._get_node("nresultants", lambda: 6)

    @rad.rad_field
    def data_problem(self) -> bool:
        return self._get_node("data_problem", lambda: False)

    @rad.rad_field
    def frame_time(self) -> float:
        return self._get_node("frame_time", lambda: _default.NONUM)

    @rad.rad_field
    def exposure_time(self) -> float:
        return self._get_node("exposure_time", lambda: _default.NONUM)

    @rad.rad_field
    def effective_exposure_time(self) -> float:
        return self._get_node("effective_exposure_time", lambda: _default.NONUM)

    @rad.rad_field
    def ma_table_name(self) -> str:
        return self._get_node("ma_table_name", lambda: _default.NOSTR)

    @rad.rad_field
    def ma_table_number(self) -> int:
        return self._get_node("ma_table_number", lambda: _default.NOINT)

    @rad.rad_field
    def read_pattern(self) -> core.LNode[core.LNode[int]]:
        return self._get_node(
            "read_pattern", lambda: core.LNode([core.LNode(read) for read in ([1], [2, 3], [4], [5, 6, 7, 8], [9, 10], [11])])
        )

    @rad.rad_field
    def truncated(self) -> bool:
        return self._get_node("truncated", lambda: False)
