from types import MappingProxyType

from astropy.time import Time

from roman_datamodels.stnode import core, rad

from ..scalars import ExposureType

__all__ = ["Exposure"]


class Exposure(rad.TaggedObjectNode):
    """
    Exposure information
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/exposure-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {"asdf://stsci.edu/datamodels/roman/tags/exposure-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/exposure-1.0.0"}
        )

    @rad.field
    def type(self) -> ExposureType:
        return self._get_node("type", lambda: ExposureType.WFI_IMAGE)

    @rad.field
    def start_time(self) -> Time:
        return self._get_node("start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def mid_time(self) -> Time:
        return self._get_node("mid_time", lambda: Time("2020-01-01T01:00:00.0", format="isot", scale="utc"))

    @rad.field
    def end_time(self) -> Time:
        return self._get_node("end_time", lambda: Time("2020-01-01T02:00:00.0", format="isot", scale="utc"))

    @rad.field
    def nresultants(self) -> int:
        return self._get_node("nresultants", lambda: 6)

    @rad.field
    def data_problem(self) -> bool:
        return self._get_node("data_problem", lambda: False)

    @rad.field
    def frame_time(self) -> float:
        return self._get_node("frame_time", lambda: rad.NONUM)

    @rad.field
    def exposure_time(self) -> float:
        return self._get_node("exposure_time", lambda: rad.NONUM)

    @rad.field
    def effective_exposure_time(self) -> float:
        return self._get_node("effective_exposure_time", lambda: rad.NONUM)

    @rad.field
    def ma_table_name(self) -> str:
        return self._get_node("ma_table_name", lambda: rad.NOSTR)

    @rad.field
    def ma_table_number(self) -> int:
        return self._get_node("ma_table_number", lambda: rad.NOINT)

    @rad.field
    def read_pattern(self) -> core.LNode[core.LNode[int]]:
        return self._get_node(
            "read_pattern", lambda: core.LNode([core.LNode(read) for read in ([1], [2, 3], [4], [5, 6, 7, 8], [9, 10], [11])])
        )

    @rad.field
    def truncated(self) -> bool:
        return self._get_node("truncated", lambda: False)
