from types import MappingProxyType
from typing import TypeAlias, cast

from astropy.time import Time

from roman_datamodels.stnode import rad

from ..scalars import GuidewindowModes

__all__ = ["Guidestar"]


_Guidestar: TypeAlias = GuidewindowModes | Time | int | float | str


class Guidestar(rad.TaggedObjectNode[_Guidestar]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/guidestar-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/guidestar-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/guidestar-1.0.0"
            }
        )

    @property
    @rad.field
    def guide_window_id(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def guide_mode(self: rad.Node) -> GuidewindowModes:
        return GuidewindowModes.WSM_ACQ_2

    @property
    @rad.field
    def data_start(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def data_end(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T01:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def window_xstart(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def window_ystart(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def window_xstop(self: rad.Node) -> int:
        return cast(int, self.window_xstart) + cast(int, self.window_xsize)

    @property
    @rad.field
    def window_ystop(self: rad.Node) -> int:
        return cast(int, self.window_ystart) + cast(int, self.window_ysize)

    @property
    @rad.field
    def window_xsize(self: rad.Node) -> int:
        return 170

    @property
    @rad.field
    def window_ysize(self: rad.Node) -> int:
        return 24

    @property
    @rad.field
    def guide_star_id(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def gsc_version(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def ra(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def ra_uncertainty(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec_uncertainty(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def fgs_magnitude(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def fgs_magnitude_uncertainty(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def centroid_x(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def centroid_y(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def centroid_x_uncertainty(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def centroid_y_uncertainty(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def epoch(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def proper_motion_ra(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def proper_motion_dec(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def parallax(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def centroid_rms(self: rad.Node) -> float:
        return rad.NONUM
