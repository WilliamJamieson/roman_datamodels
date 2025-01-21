from types import MappingProxyType
from typing import TypeAlias

import numpy as np
from astropy.time import Time

from roman_datamodels.stnode import core, rad

from ..scalars import FpsExposureType

__all__ = ["FpsExposure"]


_FpsExposure: TypeAlias = FpsExposureType | Time | int | float | str | bool | core.LNode[core.LNode[int]]


class FpsExposure(rad.TaggedObjectNode[_FpsExposure]):
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

    @property
    @rad.field
    def type(self: rad.Node) -> FpsExposureType:
        return FpsExposureType.WFI_IMAGE

    @property
    @rad.field
    def start_time(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def ngroups(self: rad.Node) -> int:
        return 6

    @property
    @rad.field
    def nframes(self: rad.Node) -> int:
        return 8

    @property
    @rad.field
    def data_problem(self: rad.Node) -> bool:
        return False

    @property
    @rad.field
    def frame_divisor(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def groupgap(self: rad.Node) -> int:
        return 0

    @property
    @rad.field
    def frame_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def group_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def exposure_time(self: rad.Node) -> float:
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
        base = np.arange(1, 56).reshape((-1, 1)).tolist()
        return core.LNode([core.LNode(row) for row in base])
