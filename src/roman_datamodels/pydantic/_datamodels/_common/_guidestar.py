from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel, Number
from ._guidewindow_modes import GuidewindowModes

__all__ = ["Guidestar"]


class Guidestar(BaseDataModel):
    gw_id: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "guide star window identifier",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(20)",
                    "destination": [
                        "ScienceCommon.gw_id",
                        "GuideWindow.gw_id",
                    ],
                },
            },
        ),
    ]
    gw_fgs_mode: Annotated[
        GuidewindowModes,
        Field(
            json_schema_extra={
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(18)",
                    "destination": [
                        "ScienceCommon.gw_fgs_mode",
                        "GuideWindow.gw_fgs_mode",
                    ],
                },
            },
        ),
    ]
    gs_id: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "guide star identifier from the GSC2 catalog",
                "description": "guide star catalog id from the GSC2, field gsc2ID",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(20)",
                    "destination": [
                        "ScienceCommon.gs_id",
                        "GuideWindow.gs_id",
                    ],
                },
            },
        ),
    ]
    gs_catalog_version: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "The version of the Guide Star Catalog",
                "description": (
                    'The version of the catalog that the guide stars are selected, currently  "GSC 2.4.2", SDF should populate'
                    "this from the return value of CAT e.g. CAT=GSC242"
                ),
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(20)",
                    "destination": [
                        "ScienceCommon.gs_catalog_version",
                    ],
                },
            },
        ),
    ]
    gs_ra: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] guide star right ascension",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_ra",
                        "GuideWindow.gs_ra",
                    ],
                },
            },
        ),
    ]
    gs_dec: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] guide star declination",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_dec",
                        "GuideWindow.gs_dec",
                    ],
                },
            },
        ),
    ]
    gs_ura: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] guide star right ascension uncertainty",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_ura",
                        "GuideWindow.gs_ura",
                    ],
                },
            },
        ),
    ]
    gs_udec: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] guide star declination uncertainty",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_udec",
                        "GuideWindow.gs_udec",
                    ],
                },
            },
        ),
    ]
    gs_mag: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "guide star magnitude in detector",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_mag",
                        "GuideWindow.gs_mag",
                    ],
                },
            },
        ),
    ]
    gs_umag: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "guide star magnitude uncertainty",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_umag",
                        "GuideWindow.gs_umag",
                    ],
                },
            },
        ),
    ]
    data_start: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "MJD start time of guider data within this file",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.data_start",
                        "GuideWindow.data_start",
                    ],
                },
            },
        ),
    ]
    data_end: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "MJD end time of guider data within this file",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.data_end",
                        "GuideWindow.data_end",
                    ],
                },
            },
        ),
    ]
    gs_ctd_x: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[arcsec] guide star centroid x position in guider ideal frame",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_ctd_x",
                        "GuideWindow.gs_ctd_x",
                    ],
                },
            },
        ),
    ]
    gs_ctd_y: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[arcsec] guide star centroid y position in guider ideal frame",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_ctd_y",
                        "GuideWindow.gs_ctd_y",
                    ],
                },
            },
        ),
    ]
    gs_ctd_ux: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "uncertainty in the x position of the centroid",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_ctd_ux",
                        "GuideWindow.gs_ctd_ux",
                    ],
                },
            },
        ),
    ]
    gs_ctd_uy: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "uncertainty in the y position of the centroid",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_ctd_uy",
                        "GuideWindow.gs_ctd_uy",
                    ],
                },
            },
        ),
    ]
    gs_epoch: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Epoch of guide star coordinates",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": [
                        "ScienceCommon.gs_epoch",
                        "GuideWindow.gs_epoch",
                    ],
                },
            },
        ),
    ]
    gs_mura: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[mas/yr] Guide star ICRS right ascension proper motion",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_mura",
                        "GuideWindow.gs_mura",
                    ],
                },
            },
        ),
    ]
    gs_mudec: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[mas/yr] Guide star ICRS declination proper motion",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_mudec",
                        "GuideWindow.gs_mudec",
                    ],
                },
            },
        ),
    ]
    gs_para: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Guide star annual parallax",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_para",
                        "GuideWindow.gs_para",
                    ],
                },
            },
        ),
    ]
    gs_pattern_error: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "RMS of guide star position",
                "description": (
                    "RMS of guide star position in guide window from pattern matching (error on "
                    "centroid not explicitly calculated, the FACE information takes all the centroids and "
                    "calculates the error across the guiding pattern)"
                ),
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.gs_pattern_error",
                        "GuideWindow.gs_pattern_error",
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
                        "ScienceCommon.gw_window_xstart",
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
                        "ScienceCommon.gw_window_ystart",
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
                        "ScienceCommon.gw_window_xstop",
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
                        "ScienceCommon.gw_window_ystop",
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
                        "ScienceCommon.gw_window_xsize",
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
                        "ScienceCommon.gw_window_ysize",
                    ],
                },
            },
        ),
    ]
