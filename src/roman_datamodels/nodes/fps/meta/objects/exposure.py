from types import MappingProxyType

import numpy as np
from astropy.time import Time

from roman_datamodels.stnode import core, rad

from ..scalars import FpsExposureType

__all__ = ["FpsExposure"]


class FpsExposure(rad.TaggedObjectNode):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/exposure-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/exposure-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/exposure-1.0.0"
            }
        )

    @rad.field
    def type(self) -> FpsExposureType:
        return FpsExposureType.WFI_IMAGE

    @rad.field
    def start_time(self) -> Time:
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")

    @rad.field
    def ngroups(self) -> int:
        return 6

    @rad.field
    def nframes(self) -> int:
        return 8

    @rad.field
    def data_problem(self) -> bool:
        return False

    @rad.field
    def frame_divisor(self) -> int:
        return rad.NOINT

    @rad.field
    def groupgap(self) -> int:
        return 0

    @rad.field
    def frame_time(self) -> float:
        return rad.NONUM

    @rad.field
    def group_time(self) -> float:
        return rad.NONUM

    @rad.field
    def exposure_time(self) -> float:
        return rad.NONUM

    @rad.field
    def ma_table_name(self) -> str:
        return rad.NOSTR

    @rad.field
    def ma_table_number(self) -> int:
        return rad.NOINT

    @rad.field
    def read_pattern(self) -> core.LNode[core.LNode[int]]:
        base = np.arange(1, 56).reshape((-1, 1)).tolist()
        return core.LNode([core.LNode(row) for row in base])
