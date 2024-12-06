from roman_datamodels.stnode import _core, _default

from ..untagged_scalars import FpsGuidewindowModes

__all__ = ["FpsGuidestar"]


class FpsGuidestar(_core.TaggedObjectNode):
    """
    FPS Guidestar information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/guidestar-1.0.0"

    @_core.rad_field
    def gw_id(self) -> str:
        return self._get_node("gw_id", lambda: _default.NOSTR)

    @_core.rad_field
    def gw_fgs_mode(self) -> FpsGuidewindowModes:
        return self._get_node("gw_fgs_mode", FpsGuidewindowModes.WSM_ACQ_2)

    @_core.rad_field
    def data_start(self) -> float:
        return self._get_node("data_start", lambda: _default.NONUM)

    @_core.rad_field
    def data_end(self) -> float:
        return self._get_node("data_end", lambda: _default.NONUM)

    @_core.rad_field
    def gw_window_xstart(self) -> int:
        return self._get_node("gw_window_xstart", lambda: _default.NOINT)

    @_core.rad_field
    def gw_window_ystart(self) -> int:
        return self._get_node("gw_window_ystart", lambda: _default.NOINT)

    @_core.rad_field
    def gw_window_xstop(self) -> int:
        return self._get_node("gw_window_xstop", lambda: self.gw_window_xstart + self.gw_window_xsize)

    @_core.rad_field
    def gw_window_ystop(self) -> int:
        return self._get_node("gw_window_ystop", lambda: self.gw_window_ystart + self.gw_window_ysize)

    @_core.rad_field
    def gw_window_xsize(self) -> int:
        return self._get_node("gw_window_xsize", lambda: 170)

    @_core.rad_field
    def gw_window_ysize(self) -> int:
        return self._get_node("gw_window_ysize", lambda: 24)
