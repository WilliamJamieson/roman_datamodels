from types import MappingProxyType

from astropy.time import Time

from roman_datamodels.stnode import rad

from ..scalars import GuidewindowModes

__all__ = ["Guidestar"]


class Guidestar(rad.TaggedObjectNode):
    """
    Guidestar information
    """

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
        return "asdf://stsci.edu/datamodels/roman/tags/guidestar-1.0.0"

    @rad.field
    def guide_window_id(self) -> str:
        return self._get_node("guide_window_id", lambda: rad.NOSTR)

    @rad.field
    def guide_mode(self) -> GuidewindowModes:
        return self._get_node("guide_mode", lambda: GuidewindowModes.WSM_ACQ_2)

    @rad.field
    def data_start(self) -> Time:
        return self._get_node("data_start", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def data_end(self) -> Time:
        return self._get_node("data_end", lambda: Time("2020-01-01T01:00:00.0", format="isot", scale="utc"))

    @rad.field
    def window_xstart(self) -> int:
        return self._get_node("window_xstart", lambda: rad.NOINT)

    @rad.field
    def window_ystart(self) -> int:
        return self._get_node("window_ystart", lambda: rad.NOINT)

    @rad.field
    def window_xstop(self) -> int:
        return self._get_node("window_xstop", lambda: self.window_xstart + self.window_xsize)

    @rad.field
    def window_ystop(self) -> int:
        return self._get_node("window_ystop", lambda: self.window_ystart + self.window_ysize)

    @rad.field
    def window_xsize(self) -> int:
        return self._get_node("window_xsize", lambda: 170)

    @rad.field
    def window_ysize(self) -> int:
        return self._get_node("window_ysize", lambda: 24)

    @rad.field
    def guide_star_id(self) -> str:
        return self._get_node("guide_star_id", lambda: rad.NOSTR)

    @rad.field
    def gsc_version(self) -> str:
        return self._get_node("gsc_version", lambda: rad.NOSTR)

    @rad.field
    def ra(self) -> float:
        return self._get_node("ra", lambda: rad.NONUM)

    @rad.field
    def dec(self) -> float:
        return self._get_node("dec", lambda: rad.NONUM)

    @rad.field
    def ra_uncertainty(self) -> float:
        return self._get_node("ra_uncertainty", lambda: rad.NONUM)

    @rad.field
    def dec_uncertainty(self) -> float:
        return self._get_node("dec_uncertainty", lambda: rad.NONUM)

    @rad.field
    def fgs_magnitude(self) -> float:
        return self._get_node("fgs_magnitude", lambda: rad.NONUM)

    @rad.field
    def fgs_magnitude_uncertainty(self) -> float:
        return self._get_node("fgs_magnitude_uncertainty", lambda: rad.NONUM)

    @rad.field
    def centroid_x(self) -> float:
        return self._get_node("centroid_x", lambda: rad.NONUM)

    @rad.field
    def centroid_y(self) -> float:
        return self._get_node("centroid_y", lambda: rad.NONUM)

    @rad.field
    def centroid_x_uncertainty(self) -> float:
        return self._get_node("centroid_x_uncertainty", lambda: rad.NONUM)

    @rad.field
    def centroid_y_uncertainty(self) -> float:
        return self._get_node("centroid_y_uncertainty", lambda: rad.NONUM)

    @rad.field
    def epoch(self) -> str:
        return self._get_node("epoch", lambda: rad.NOSTR)

    @rad.field
    def proper_motion_ra(self) -> float:
        return self._get_node("proper_motion_ra", lambda: rad.NONUM)

    @rad.field
    def proper_motion_dec(self) -> float:
        return self._get_node("proper_motion_dec", lambda: rad.NONUM)

    @rad.field
    def parallax(self) -> float:
        return self._get_node("parallax", lambda: rad.NONUM)

    @rad.field
    def centroid_rms(self) -> float:
        return self._get_node("centroid_rms", lambda: rad.NONUM)
