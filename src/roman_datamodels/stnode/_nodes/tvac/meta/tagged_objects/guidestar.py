from roman_datamodels.stnode import _core, _default

from ..untagged_scalars import TvacGuidewindowModes

__all__ = ["TvacGuidestar"]


class TvacGuidestar(_core.TaggedObjectNode):
    """
    Tvac Guidestar information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/guidestar-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "gw_id",
            "gw_fgs_mode",
            "data_start",
            "data_end",
            "gw_window_xstart",
            "gw_window_ystart",
            "gw_window_xstop",
            "gw_window_ystop",
            "gw_window_xsize",
            "gw_window_ysize",
        )

    @property
    def gw_id(self) -> str:
        return self._get_node("gw_id", lambda: _default.NOSTR)

    @property
    def gw_fgs_mode(self) -> TvacGuidewindowModes:
        return self._get_node("gw_fgs_mode", TvacGuidewindowModes.WSM_ACQ_2)

    @property
    def data_start(self) -> float:
        return self._get_node("data_start", lambda: _default.NONUM)

    @property
    def data_end(self) -> float:
        return self._get_node("data_end", lambda: _default.NONUM)

    @property
    def gw_window_xstart(self) -> int:
        return self._get_node("gw_window_xstart", lambda: _default.NONUM)

    @property
    def gw_window_ystart(self) -> int:
        return self._get_node("gw_window_ystart", lambda: _default.NONUM)

    @property
    def gw_window_xstop(self) -> int:
        return self._get_node("gw_window_xstop", lambda: self.gw_window_xstart + self.gw_window_xsize)

    @property
    def gw_window_ystop(self) -> int:
        return self._get_node("gw_window_ystop", lambda: self.gw_window_ystart + self.gw_window_ysize)

    @property
    def gw_window_xsize(self) -> int:
        return self._get_node("gw_window_xsize", lambda: 170)

    @property
    def gw_window_ysize(self) -> int:
        return self._get_node("gw_window_ysize", lambda: 24)
