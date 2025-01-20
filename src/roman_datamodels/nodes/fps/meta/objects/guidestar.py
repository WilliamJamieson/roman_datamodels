from types import MappingProxyType
from typing import TypeAlias, cast

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

    @property
    @rad.field
    def gw_id(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def gw_fgs_mode(self: rad.Node) -> FpsGuidewindowModes:
        return FpsGuidewindowModes.WSM_ACQ_2

    @property
    @rad.field
    def data_start(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def data_end(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def gw_window_xstart(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def gw_window_ystart(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def gw_window_xstop(self: rad.Node) -> int:
        # MyPy cannot determine that these fields are the type defined in type alias
        return cast(int, self.gw_window_xstart) + cast(int, self.gw_window_xsize)

    @property
    @rad.field
    def gw_window_ystop(self: rad.Node) -> int:
        # MyPy cannot determine that these fields are the type defined in type alias
        return cast(int, self.gw_window_ystart) + cast(int, self.gw_window_ysize)

    @property
    @rad.field
    def gw_window_xsize(self: rad.Node) -> int:
        return 170

    @property
    @rad.field
    def gw_window_ysize(self: rad.Node) -> int:
        return 24
