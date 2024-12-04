from astropy.time import Time

from roman_datamodels.stnode import _core, _default

from ..untagged_scalars import GuidewindowModes

__all__ = ["Guidestar"]


class Guidestar(_core.TaggedObjectNode):
    """
    Guidestar information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/guidestar-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "guide_window_id",
            "guide_mode",
            "data_start",
            "data_end",
            "window_xstart",
            "window_ystart",
            "window_xstop",
            "window_ystop",
            "window_xsize",
            "window_ysize",
            "guide_star_id",
            "gsc_version",
            "ra",
            "dec",
            "ra_uncertainty",
            "dec_uncertainty",
            "fgs_magnitude",
            "fgs_magnitude_uncertainty",
            "centroid_x",
            "centroid_y",
            "centroid_x_uncertainty",
            "centroid_y_uncertainty",
            "epoch",
            "proper_motion_ra",
            "proper_motion_dec",
            "parallax",
            "centroid_rms",
        )

    @property
    def guide_window_id(self) -> str:
        return self._get_node("guide_window_id", lambda: _default.NOSTR)

    @property
    def guide_mode(self) -> GuidewindowModes:
        return self._get_node("guide_mode", GuidewindowModes.WSM_ACQ_2)

    @property
    def data_start(self) -> Time:
        return self._get_node("data_start", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def data_end(self) -> Time:
        return self._get_node("data_end", lambda: Time("2020-01-01T01:00:00.0", format="isot", scale="utc"))

    @property
    def window_xstart(self) -> int:
        return self._get_node("window_xstart", lambda: _default.NOINT)

    @property
    def window_ystart(self) -> int:
        return self._get_node("window_ystart", lambda: _default.NOINT)

    @property
    def window_xstop(self) -> int:
        return self._get_node("window_xstop", lambda: self.window_xstart + self.window_xsize)

    @property
    def window_ystop(self) -> int:
        return self._get_node("window_ystop", lambda: self.window_ystart + self.window_ysize)

    @property
    def window_xsize(self) -> int:
        return self._get_node("window_xsize", lambda: 170)

    @property
    def window_ysize(self) -> int:
        return self._get_node("window_ysize", lambda: 24)

    @property
    def guide_star_id(self) -> str:
        return self._get_node("guide_star_id", lambda: _default.NOSTR)

    @property
    def gsc_version(self) -> str:
        return self._get_node("gsc_version", lambda: _default.NOSTR)

    @property
    def ra(self) -> float:
        return self._get_node("ra", lambda: _default.NONUM)

    @property
    def dec(self) -> float:
        return self._get_node("dec", lambda: _default.NONUM)

    @property
    def ra_uncertainty(self) -> float:
        return self._get_node("ra_uncertainty", lambda: _default.NONUM)

    @property
    def dec_uncertainty(self) -> float:
        return self._get_node("dec_uncertainty", lambda: _default.NONUM)

    @property
    def fgs_magnitude(self) -> float:
        return self._get_node("fgs_magnitude", lambda: _default.NONUM)

    @property
    def fgs_magnitude_uncertainty(self) -> float:
        return self._get_node("fgs_magnitude_uncertainty", lambda: _default.NONUM)

    @property
    def centroid_x(self) -> float:
        return self._get_node("centroid_x", lambda: _default.NONUM)

    @property
    def centroid_y(self) -> float:
        return self._get_node("centroid_y", lambda: _default.NONUM)

    @property
    def centroid_x_uncertainty(self) -> float:
        return self._get_node("centroid_x_uncertainty", lambda: _default.NONUM)

    @property
    def centroid_y_uncertainty(self) -> float:
        return self._get_node("centroid_y_uncertainty", lambda: _default.NONUM)

    @property
    def epoch(self) -> str:
        return self._get_node("epoch", lambda: _default.NOSTR)

    @property
    def proper_motion_ra(self) -> float:
        return self._get_node("proper_motion_ra", lambda: _default.NONUM)

    @property
    def proper_motion_dec(self) -> float:
        return self._get_node("proper_motion_dec", lambda: _default.NONUM)

    @property
    def parallax(self) -> float:
        return self._get_node("parallax", lambda: _default.NONUM)

    @property
    def centroid_rms(self) -> float:
        return self._get_node("centroid_rms", lambda: _default.NONUM)
