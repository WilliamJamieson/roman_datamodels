from types import MappingProxyType
from typing import TypeAlias, cast

import numpy as np
import numpy.typing as npt
from astropy.time import Time

from roman_datamodels.stnode import rad

from .meta import (
    Common,
    GuidewindowModes,
)
from .meta.common import _Common

__all__ = ["Guidewindow"]


_Guidewindow_Meta: TypeAlias = _Common | GuidewindowModes | Time | str | int | float


class Guidewindow_Meta(rad.ImpliedNodeMixin[_Guidewindow_Meta], Common[_Guidewindow_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Guidewindow

    @property
    @rad.field
    def gw_start_time(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def gw_end_time(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T10:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def gw_frame_readout_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def gw_function_start_time(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def gw_function_end_time(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def gw_acq_exec_stat(self: rad.Node) -> str:
        return "StatusRMTest619"

    @property
    @rad.field
    def pedestal_resultant_exp_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def signal_resultant_exp_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def gw_acq_number(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def gw_science_file_source(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def gw_mode(self: rad.Node) -> GuidewindowModes:
        return GuidewindowModes.WIM_ACQ

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
        return cast(int, self.gw_window_xstart) + cast(int, self.gw_window_xsize)

    @property
    @rad.field
    def gw_window_ystop(self: rad.Node) -> int:
        return cast(int, self.gw_window_xstart) + cast(int, self.gw_window_ysize)

    @property
    @rad.field
    def gw_window_xsize(self: rad.Node) -> int:
        return 170

    @property
    @rad.field
    def gw_window_ysize(self: rad.Node) -> int:
        return 24


_Guidewindow: TypeAlias = Guidewindow_Meta | npt.NDArray[np.uint16]


class Guidewindow(rad.TaggedObjectNode[_Guidewindow], rad.ArrayFieldMixin[_Guidewindow]):
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
    def default_array_shape(self) -> tuple[int, int, int, int, int]:
        """Default shape of the data array"""
        return (2, 8, 16, 32, 32)

    @property
    def testing_array_shape(self) -> tuple[int, int, int, int, int]:
        """Shape of the data array for testing"""
        return (2, 2, 2, 2, 2)

    @property
    @rad.field
    def meta(self: rad.Node) -> Guidewindow_Meta:
        return Guidewindow_Meta()

    @property
    @rad.field
    def pedestal_frames(self: rad.Node) -> npt.NDArray[np.uint16]:
        return np.zeros(self.array_shape, dtype=np.uint16)

    @property
    @rad.field
    def signal_frames(self: rad.Node) -> npt.NDArray[np.uint16]:
        return np.zeros(self.array_shape, dtype=np.uint16)

    @property
    @rad.field
    def amp33(self: rad.Node) -> npt.NDArray[np.uint16]:
        return np.zeros(self.array_shape, dtype=np.uint16)
