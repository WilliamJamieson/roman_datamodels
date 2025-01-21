from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

from ..scalars import FpsGuidewindowModes

__all__ = ["FpsGuidestar"]


_FpsGuidestar: TypeAlias = str | FpsGuidewindowModes | float | int


class FpsGuidestar(rad.TaggedObjectNode[_FpsGuidestar]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/guidestar-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/guidestar-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/guidestar-1.0.0"
            }
        )

    @rad.field
    def gw_id(self) -> str:
        return rad.NOSTR

    @rad.field
    def gw_fgs_mode(self) -> FpsGuidewindowModes:
        return FpsGuidewindowModes.WSM_ACQ_2

    @rad.field
    def data_start(self) -> float:
        return rad.NONUM

    @rad.field
    def data_end(self) -> float:
        return rad.NONUM

    @rad.field
    def gw_window_xstart(self) -> int:
        return rad.NOINT

    @rad.field
    def gw_window_ystart(self) -> int:
        return rad.NOINT

    @rad.field
    def gw_window_xstop(self) -> int:
        # MyPy cannot determine that these fields are the type defined in type alias
        return self.gw_window_xstart + self.gw_window_xsize  # type: ignore[no-any-return]

    @rad.field
    def gw_window_ystop(self) -> int:
        # MyPy cannot determine that these fields are the type defined in type alias
        return self.gw_window_ystart + self.gw_window_ysize  # type: ignore[no-any-return]

    @rad.field
    def gw_window_xsize(self) -> int:
        return 170

    @rad.field
    def gw_window_ysize(self) -> int:
        return 24
