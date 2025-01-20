from types import MappingProxyType
from typing import TypeAlias

from astropy.time import Time

from roman_datamodels.stnode import core, rad

from ..scalars import ExposureType

__all__ = ["Exposure"]


_Exposure: TypeAlias = ExposureType | Time | int | float | str | core.LNode[core.LNode[int]]


class Exposure(rad.TaggedObjectNode[_Exposure]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/exposure-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {"asdf://stsci.edu/datamodels/roman/tags/exposure-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/exposure-1.0.0"}
        )

    @property
    @rad.field
    def type(self: rad.Node) -> ExposureType:
        return ExposureType.WFI_IMAGE

    @property
    @rad.field
    def start_time(self: rad.Node) -> Time:
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")

    @property
    @rad.field
    def mid_time(self: rad.Node) -> Time:
        return Time("2020-01-01T01:00:00.0", format="isot", scale="utc")

    @property
    @rad.field
    def end_time(self: rad.Node) -> Time:
        return Time("2020-01-01T02:00:00.0", format="isot", scale="utc")

    @property
    @rad.field
    def nresultants(self: rad.Node) -> int:
        return 6

    @property
    @rad.field
    def data_problem(self: rad.Node) -> bool:
        return False

    @property
    @rad.field
    def frame_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def exposure_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def effective_exposure_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def ma_table_name(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def ma_table_number(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def read_pattern(self: rad.Node) -> core.LNode[core.LNode[int]]:
        return core.LNode([core.LNode(read) for read in ([1], [2, 3], [4], [5, 6, 7, 8], [9, 10], [11])])

    @property
    @rad.field
    def truncated(self: rad.Node) -> bool:
        return False
