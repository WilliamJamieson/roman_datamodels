from typing import Annotated

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, AstropyTime
from .._core import BaseRomanDataModel, Number
from ._common import Common, GuidewindowModes

__all__ = ["GuidewindowModel"]


class GuidewindowMeta(Common):
    gw_start_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "UTC time at the start of the guide window exposure",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "GuideWindow.gw_start_time",
                    ],
                },
            },
        ),
    ]
    gw_end_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "UTC time at the end of the guide window exposure",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "GuideWindow.gw_end_time",
                    ],
                },
            },
        ),
    ]
    gw_frame_readout_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "The readout time for the guide window frame",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "GuideWindow.gw_frame_readout_time",
                    ],
                },
            },
        ),
    ]
    gw_function_start_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "Observatory UTC time at guider function start",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "GuideWindow.gw_function_start_time",
                    ],
                },
            },
        ),
    ]
    gw_function_end_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "Observatory UTC time at guider function end",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "GuideWindow.gw_function_end_time",
                    ],
                },
            },
        ),
    ]
    gw_acq_exec_stat: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Guide star window acquisition status",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "GuideWindow.gw_acq_exec_stat",
                    ],
                },
            },
        ),
    ]
    pedestal_resultant_exp_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Total exposure time for the guide window pedestal frames",
                # fmt: off
                "description": (
                    "The cumulative exposure time for all the guide window "
                    "pedestal frames"
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "GuideWindow.pedestal_resultant_exp_time",
                    ],
                },
            },
        ),
    ]
    signal_resultant_exp_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Total exposure time for the guide window resultant frames",
                # fmt: off
                "description": (
                    "The cumulative exposure time for all the guide window "
                    "resultant frames"
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "GuideWindow.signal_resultant_exp_time",
                    ],
                },
            },
        ),
    ]
    gw_acq_number: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": 'Guide Window ID "Q"',
                # fmt: off
                "description": (
                    "A single digit representing the guide star acquisition "
                    "number within the visit"
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "GuideWindow.gw_acq_number",
                    ],
                },
            },
        ),
    ]
    gw_science_file_source: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "The science data associated with this guide window",
                # fmt: off
                "description": (
                    "The science data file that is associated with this guide window, "
                    'e.g. "r0000101001001001001_01101_0001_WFI01_uncal.asdf"'
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "GuideWindow.gw_science_file_source",
                    ],
                },
            },
        ),
    ]
    gw_mode: Annotated[
        GuidewindowModes,
        Field(
            json_schema_extra={
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(18)",
                    "destination": [
                        "GuideWindow.gw_mode",
                    ],
                },
            },
        ),
    ]
    gw_window_xstart: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Guide window x start position on the detector",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "GuideWindow.gw_window_xstart",
                    ],
                },
            },
        ),
    ]
    gw_window_ystart: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Guide window y start position on the detector",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "GuideWindow.gw_window_ystart",
                    ],
                },
            },
        ),
    ]
    gw_window_xstop: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Guide window x stop position on the detector",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "GuideWindow.gw_window_xstop",
                    ],
                },
            },
        ),
    ]
    gw_window_ystop: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Guide window y stop position on the detector",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "GuideWindow.gw_window_ystop",
                    ],
                },
            },
        ),
    ]
    gw_window_xsize: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Guide window size in the x direction in detector coordinates",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "GuideWindow.gw_window_xsize",
                    ],
                },
            },
        ),
    ]
    gw_window_ysize: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Guide window size in the y direction in detector coordinates",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Science Data Formatting",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "GuideWindow.gw_window_ysize",
                    ],
                },
            },
        ),
    ]


class GuidewindowModel(BaseRomanDataModel):
    meta: Annotated[
        GuidewindowMeta,
        Field(
            json_schema_extra={
                "title": "Guidewindow metadata",
            },
        ),
    ]
    pedestal_frames: Annotated[
        AstropyQuantity[np.uint16, u.DN, 5],
        Field(
            json_schema_extra={
                "title": "Pedestal frames",
                # fmt: off
                "description": (
                    "Reconstituted and oriented pedestal frame GW images. "
                    "Dimensions: num_frames, num_combined_resultants "
                    "(or num_uncombined_resultants), num_reads, x, y"
                ),
                # fmt: on
            },
        ),
    ]
    signal_frames: Annotated[
        AstropyQuantity[np.uint16, u.DN, 5],
        Field(
            json_schema_extra={
                "title": "Signal frames",
                # fmt: off
                "description": (
                    "Reconstituted and oriented signal frames. Dimensions: num_frames, "
                    "num_combined_resultants (or num_uncombined_resultants), "
                    "num_reads, x, y"
                ),
                # fmt: on
            },
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.uint16, u.DN, 5],
        Field(
            json_schema_extra={
                "title": "Signal frames",
                # fmt: off
                "description": (
                    "Amp 33 reference pixel data. Dimensions: num_frames, "
                    "num_combined_resultants (or num_uncombined_resultants), "
                    "num_reads, x, y"
                ),
                # fmt: on
            },
        ),
    ]
