from types import MappingProxyType

import numpy as np
from astropy.time import Time

from roman_datamodels.stnode import rad

from .meta import (
    Common,
    GuidewindowModes,
)

__all__ = ["Guidewindow"]


class Guidewindow_Meta(rad.ImpliedNodeMixin, Common):
    """Metadata for the guide window"""

    @classmethod
    def asdf_implied_by(cls) -> type:
        return Guidewindow

    @rad.field
    def gw_start_time(self) -> Time:
        return self._get_node("gw_start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def gw_end_time(self) -> Time:
        return self._get_node("gw_end_time", lambda: Time("2020-01-01T10:00:00.0", format="isot", scale="utc"))

    @rad.field
    def gw_frame_readout_time(self) -> float:
        return self._get_node("gw_frame_readout_time", lambda: rad.NONUM)

    @rad.field
    def gw_function_start_time(self) -> Time:
        return self._get_node("gw_function_start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def gw_function_end_time(self) -> Time:
        return self._get_node("gw_function_end_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def gw_acq_exec_stat(self) -> str:
        return self._get_node("gw_acq_exec_stat", lambda: "StatusRMTest619")

    @rad.field
    def pedestal_resultant_exp_time(self) -> float:
        return self._get_node("pedestal_resultant_exp_time", lambda: rad.NONUM)

    @rad.field
    def signal_resultant_exp_time(self) -> float:
        return self._get_node("signal_resultant_exp_time", lambda: rad.NONUM)

    @rad.field
    def gw_acq_number(self) -> int:
        return self._get_node("gw_acq_number", lambda: rad.NOINT)

    @rad.field
    def gw_science_file_source(self) -> str:
        return self._get_node("gw_science_file_source", lambda: rad.NOSTR)

    @rad.field
    def gw_mode(self) -> GuidewindowModes:
        return self._get_node("gw_mode", lambda: GuidewindowModes.WIM_ACQ)

    @rad.field
    def gw_window_xstart(self) -> int:
        return self._get_node("gw_window_xstart", lambda: rad.NOINT)

    @rad.field
    def gw_window_ystart(self) -> int:
        return self._get_node("gw_window_ystart", lambda: rad.NOINT)

    @rad.field
    def gw_window_xstop(self) -> int:
        return self._get_node("gw_window_xstop", lambda: self.gw_window_xstart + self.gw_window_xsize)

    @rad.field
    def gw_window_ystop(self) -> int:
        return self._get_node("gw_window_ystop", lambda: self.gw_window_xstart + self.gw_window_ysize)

    @rad.field
    def gw_window_xsize(self) -> int:
        return self._get_node("gw_window_xsize", lambda: 170)

    @rad.field
    def gw_window_ysize(self) -> int:
        return self._get_node("gw_window_ysize", lambda: 24)


class Guidewindow(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Guide window schema
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/guidewindow-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/guidewindow-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/guidewindow-1.0.0",
            }
        )

    @property
    def primary_array_name(self) -> str:
        """Primary array name"""
        return "signal_frames"

    @property
    def default_array_shape(self) -> tuple[int]:
        """Default shape of the data array"""
        return (2, 8, 16, 32, 32)

    @property
    def testing_array_shape(self) -> tuple[int]:
        """Shape of the data array for testing"""
        return (2, 2, 2, 2, 2)

    @rad.field
    def meta(self) -> Guidewindow_Meta:
        return self._get_node("meta", Guidewindow_Meta)

    @rad.field
    def pedestal_frames(self) -> np.ndarray:
        return self._get_node("pedestal_frames", lambda: np.zeros(self.array_shape, dtype=np.uint16))

    @rad.field
    def signal_frames(self) -> np.ndarray:
        return self._get_node("signal_frames", lambda: np.zeros(self.array_shape, dtype=np.uint16))

    @rad.field
    def amp33(self) -> np.ndarray:
        return self._get_node("amp33", lambda: np.zeros(self.array_shape, dtype=np.uint16))
