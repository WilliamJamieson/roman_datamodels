from astropy.time import Time

from roman_datamodels.stnode import _core
from roman_datamodels.stnode._nodes.untagged_scalars import GuidewindowModes

# from .guidewindow_modes import GuidewindowModes

__all__ = ["Guidestar"]


class Guidestar(_core.TaggedNode):
    """
    Guidestar information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/guidestar-1.0.0"

    @property
    def required(self) -> tuple[str]:
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
        if not self._has_node("guide_window_id"):
            self.guide_window_id = _core.NOSTR
        return self._get_node("guide_window_id")

    @property
    def guide_mode(self) -> GuidewindowModes:
        if not self._has_node("guide_mode"):
            self.guide_mode = GuidewindowModes.WIM_ACQ_2()
        return self._get_node("guide_mode")

    @property
    def data_start(self) -> Time:
        if not self._has_node("data_start"):
            self.data_start = Time("2020-01-01T00:00:00.0", format="isot", scale="utc")
        return self._get_node("data_start")

    @property
    def data_end(self) -> float:
        if not self._has_node("data_end"):
            self.data_end = Time("2020-01-01T01:00:00.0", format="isot", scale="utc")
        return self._get_node("data_end")

    @property
    def window_xstart(self) -> int:
        if not self._has_node("window_xstart"):
            self.window_xstart = _core.NONUM
        return self._get_node("window_xstart")

    @property
    def window_ystart(self) -> int:
        if not self._has_node("window_ystart"):
            self.window_ystart = _core.NONUM
        return self._get_node("window_ystart")

    @property
    def window_xstop(self) -> int:
        if not self._has_node("window_xstop"):
            self.window_xstop = self.window_xstart + self.window_xsize
        return self._get_node("window_xstop")

    @property
    def window_ystop(self) -> int:
        if not self._has_node("window_ystop"):
            self.window_ystop = self.window_ystart + self.window_ysize
        return self._get_node("window_ystop")

    @property
    def window_xsize(self) -> int:
        if not self._has_node("window_xsize"):
            self.window_xsize = 170
        return self._get_node("window_xsize")

    @property
    def window_ysize(self) -> int:
        if not self._has_node("window_ysize"):
            self.window_ysize = 24
        return self._get_node("window_ysize")

    @property
    def guide_star_id(self) -> str:
        if not self._has_node("guide_star_id"):
            self.guide_star_id = _core.NOSTR
        return self._get_node("guide_star_id")

    @property
    def gsc_version(self) -> str:
        if not self._has_node("gsc_version"):
            self.gsc_version = _core.NOSTR
        return self._get_node("gsc_version")

    @property
    def ra(self) -> float:
        if not self._has_node("ra"):
            self.ra = _core.NONUM
        return self._get_node("ra")

    @property
    def dec(self) -> float:
        if not self._has_node("dec"):
            self.dec = _core.NONUM
        return self._get_node("dec")

    @property
    def ra_uncertainty(self) -> float:
        if not self._has_node("ra_uncertainty"):
            self.ra_uncertainty = _core.NONUM
        return self._get_node("ra_uncertainty")

    @property
    def dec_uncertainty(self) -> float:
        if not self._has_node("dec_uncertainty"):
            self.dec_uncertainty = _core.NONUM
        return self._get_node("dec_uncertainty")

    @property
    def fgs_magnitude(self) -> float:
        if not self._has_node("fgs_magnitude"):
            self.fgs_magnitude = _core.NONUM
        return self._get_node("fgs_magnitude")

    @property
    def fgs_magnitude_uncertainty(self) -> float:
        if not self._has_node("fgs_magnitude_uncertainty"):
            self.fgs_magnitude_uncertainty = _core.NONUM
        return self._get_node("fgs_magnitude_uncertainty")

    @property
    def centroid_x(self) -> float:
        if not self._has_node("centroid_x"):
            self.centroid_x = _core.NONUM
        return self._get_node("centroid_x")

    @property
    def centroid_y(self) -> float:
        if not self._has_node("centroid_y"):
            self.centroid_y = _core.NONUM
        return self._get_node("centroid_y")

    @property
    def centroid_x_uncertainty(self) -> float:
        if not self._has_node("centroid_x_uncertainty"):
            self.centroid_x_uncertainty = _core.NONUM
        return self._get_node("centroid_x_uncertainty")

    @property
    def centroid_y_uncertainty(self) -> float:
        if not self._has_node("centroid_y_uncertainty"):
            self.centroid_y_uncertainty = _core.NONUM
        return self._get_node("centroid_y_uncertainty")

    @property
    def epoch(self) -> str:
        if not self._has_node("epoch"):
            self.epoch = _core.NOSTR
        return self._get_node("epoch")

    @property
    def proper_motion_ra(self) -> float:
        if not self._has_node("proper_motion_ra"):
            self.proper_motion_ra = _core.NONUM
        return self._get_node("proper_motion_ra")

    @property
    def proper_motion_dec(self) -> float:
        if not self._has_node("proper_motion_dec"):
            self.proper_motion_dec = _core.NONUM
        return self._get_node("proper_motion_dec")

    @property
    def parallax(self) -> float:
        if not self._has_node("parallax"):
            self.parallax = _core.NONUM
        return self._get_node("parallax")

    @property
    def centroid_rms(self) -> float:
        if not self._has_node("centroid_rms"):
            self.centroid_rms = _core.NONUM
        return self._get_node("centroid_rms")
