import numpy as np
from astropy.time import Time

from roman_datamodels.stnode import _core, _default

from ..meta import (
    Common,
    GuidewindowModes,
)

__all__ = ["Guidewindow"]


class Guidewindow_Meta(Common):
    """Metadata for the guide window"""

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "gw_start_time",
            "gw_end_time",
            "gw_frame_readout_time",
            "gw_function_start_time",
            "gw_function_end_time",
            "gw_acq_exec_stat",
            "pedestal_resultant_exp_time",
            "signal_resultant_exp_time",
            "gw_acq_number",
            "gw_mode",
            "gw_window_xstart",
            "gw_window_ystart",
            "gw_window_xstop",
            "gw_window_ystop",
            "gw_window_xsize",
            "gw_window_ysize",
            "gw_science_file_source",
        )

    @property
    def gw_start_time(self) -> Time:
        return self._get_node("gw_start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def gw_end_time(self) -> Time:
        return self._get_node("gw_end_time", lambda: Time("2020-01-01T10:00:00.0", format="isot", scale="utc"))

    @property
    def gw_frame_readout_time(self) -> float:
        return self._get_node("gw_frame_readout_time", lambda: _default.NONUM)

    @property
    def gw_function_start_time(self) -> Time:
        return self._get_node("gw_function_start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def gw_function_end_time(self) -> Time:
        return self._get_node("gw_function_end_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def gw_acq_exec_stat(self) -> str:
        return self._get_node("gw_acq_exec_stat", lambda: "StatusRMTest619")

    @property
    def pedestal_resultant_exp_time(self) -> float:
        return self._get_node("pedestal_resultant_exp_time", lambda: _default.NONUM)

    @property
    def signal_resultant_exp_time(self) -> float:
        return self._get_node("signal_resultant_exp_time", lambda: _default.NONUM)

    @property
    def gw_acq_number(self) -> int:
        return self._get_node("gw_acq_number", lambda: _default.NONUM)

    @property
    def gw_science_file_source(self) -> str:
        return self._get_node("gw_science_file_source", lambda: _default.NOSTR)

    @property
    def gw_mode(self) -> GuidewindowModes:
        return self._get_node("gw_mode", GuidewindowModes.WIM_ACQ)

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
        return self._get_node("gw_window_ystop", lambda: self.gw_window_xstart + self.gw_window_ysize)

    @property
    def gw_window_xsize(self) -> int:
        return self._get_node("gw_window_xsize", lambda: 170)

    @property
    def gw_window_ysize(self) -> int:
        return self._get_node("gw_window_ysize", lambda: 24)


class Guidewindow(_core.DataModelNode):
    """
    Guide window schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/guidewindow-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "pedestal_frames",
            "signal_frames",
            "amp33",
        )

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("amp33"):
            return self.amp33.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (2, 8, 16, 32, 32)

    @property
    def meta(self) -> Guidewindow_Meta:
        return self._get_node("meta", Guidewindow_Meta)

    @property
    def pedestal_frames(self) -> np.ndarray:
        return self._get_node("pedestal_frames", np.zeros(self.array_shape, dtype=np.uint16))

    @property
    def signal_frames(self) -> np.ndarray:
        return self._get_node("signal_frames", np.zeros(self.array_shape, dtype=np.uint16))

    @property
    def amp33(self) -> np.ndarray:
        return self._get_node("amp33", np.zeros(self.array_shape, dtype=np.uint16))
