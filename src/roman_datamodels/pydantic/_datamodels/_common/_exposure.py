from typing import Annotated

from pydantic import Field

from ..._adaptors import AstropyTime
from ..._core import BaseDataModel, Number
from ._exposure_type import ExposureType

__all__ = ["Exposure"]


class Exposure(BaseDataModel):
    id: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Exposure id number within visit",
                "description": "The exposure number for a given visit id",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.exposure_id",
                        "GuideWindow.exposure_id",
                    ],
                },
            },
        ),
    ]
    type: Annotated[
        ExposureType,
        Field(
            json_schema_extra={
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(25)",
                    "destination": [
                        "ScienceCommon.exposure_type",
                        "GuideWindow.exposure_type",
                    ],
                },
            },
        ),
    ]
    start_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "UTC exposure start time",
                # fmt: off
                "description": (
                    "This is a python date-time object that records the "
                    "time at the start of the exposure in UTC."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "ScienceCommon.exposure_start_time",
                        "GuideWindow.exposure_start_time",
                    ],
                },
            },
        ),
    ]
    mid_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "UTC exposure mid time",
                # fmt: off
                "description": (
                    "This is a python date-time object that records the "
                    "time at the middle of the exposure in UTC."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "ScienceCommon.exposure_mid_time",
                        "GuideWindow.exposure_mid_time",
                    ],
                },
            },
        ),
    ]
    end_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "UTC exposure end time",
                # fmt: off
                "description": (
                    "This is a python date-time object that records the "
                    "time at the end of the exposure in UTC."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "ScienceCommon.exposure_end_time",
                        "GuideWindow.exposure_end_time",
                    ],
                },
            },
        ),
    ]
    start_time_mjd: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[d] exposure start time in MJD",
                "description": (
                    "This records the time at the start of the exposure using the "
                    "Modified Julian Date (MJD). This is used in the archive catalog for"
                    "multi-mission matching."
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
                        "ScienceCommon.exposure_start_time_mjd",
                        "GuideWindow.exposure_start_time_mjd",
                    ],
                },
            },
        ),
    ]
    mid_time_mjd: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[d] exposure mid time in MJD",
                "description": (
                    "This records the time at the midpoint of the exposure using the "
                    "Modified Julian Date (MJD). This is used in the archive catalog for"
                    "multi-mission matching."
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
                        "ScienceCommon.exposure_mid_time_mjd",
                        "GuideWindow.exposure_mid_time_mjd",
                    ],
                },
            },
        ),
    ]
    end_time_mjd: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[d] exposure end time in MJD",
                "description": (
                    "This records the time at the end of the exposure using the "
                    "Modified Julian Date (MJD). This is used in the archive catalog for"
                    "multi-mission matching."
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
                        "ScienceCommon.exposure_end_time_mjd",
                        "GuideWindow.exposure_end_time_mjd",
                    ],
                },
            },
        ),
    ]
    start_time_tdb: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[d] TDB time of exposure start in MJD",
                "description": (
                    "This records the time at the start of the exposure using "
                    "the Modified Julian Date for the Barycentric Dynamical Time system "
                    "(TDB, Temps Dynamique Barycentrique), a relativistic coordinate "
                    "time scale."
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
                        "ScienceCommon.exposure_start_time_tdb",
                        "GuideWindow.exposure_start_time_tdb",
                    ],
                },
            },
        ),
    ]
    mid_time_tdb: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[d] TDB time of exposure mid in MJD",
                "description": (
                    "This records the time at the midpoint of the exposure using "
                    "the Modified Julian Date for the Barycentric Dynamical Time system "
                    "(TDB, Temps Dynamique Barycentrique), a relativistic coordinate "
                    "time scale."
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
                        "ScienceCommon.exposure_mid_time_tdb",
                        "GuideWindow.exposure_mid_time_tdb",
                    ],
                },
            },
        ),
    ]
    end_time_tdb: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[d] TDB time of exposure end in MJD",
                "description": (
                    "This records the time at the end of the exposure using "
                    "the Modified Julian Date for the Barycentric Dynamical Time system "
                    "(TDB, Temps Dynamique Barycentrique), a relativistic coordinate "
                    "time scale."
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
                        "ScienceCommon.exposure_end_time_tdb",
                        "GuideWindow.exposure_end_time_tdb",
                    ],
                },
            },
        ),
    ]
    ngroups: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Number of groups in integration",
                "description": (
                    "This is the number of resultant frames in the exposure "
                    "that are transmitted to the ground. The WFI data always has the "
                    "number of integrations=1."
                ),
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.exposure_ngroups",
                        "GuideWindow.exposure_ngroups",
                    ],
                },
            },
        ),
    ]
    nframes: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Number of frames per group",
                # fmt: off
                "description": (
                    "This is the number of science frames that are combined to "
                    "produce a resultant frame."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.exposure_nframes",
                        "GuideWindow.exposure_nframes",
                    ],
                },
            },
        ),
    ]
    data_problem: Annotated[
        bool,
        Field(
            json_schema_extra={
                "title": "Science telemetry indicated a problem",
                # fmt: off
                "description": (
                    "This is a flag to indicate that the science telemetry "
                    "experienced a problem."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nchar(1)",
                    "destination": [
                        "ScienceCommon.exposure_data_problem",
                        "GuideWindow.exposure_data_problem",
                    ],
                },
            },
        ),
    ]
    sca_number: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Sensor Chip Assembly number",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.exposure_sca_number",
                        "GuideWindow.exposure_sca_number",
                    ],
                },
            },
        ),
    ]
    gain_factor: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Gain scale factor",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.exposure_gain_factor",
                        "GuideWindow.exposure_gain_factor",
                    ],
                },
            },
        ),
    ]
    integration_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[s] Effective integration time",
                "description": "The effective time that the sensor has been exposed to the sky.",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.exposure_integration_time",
                        "GuideWindow.exposure_integration_time",
                    ],
                },
            },
        ),
    ]
    elapsed_exposure_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[s] Total elapsed exposure time",
                "description": (
                    "The time between the start of the first Reset/Read Science Frame of an Exposure "
                    "and the completion of the final Read Only Science Frame of that Exposure."
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
                        "ScienceCommon.elapsed_exposure_time",
                        "GuideWindow.elapsed_exposure_time",
                    ],
                },
            },
        ),
    ]
    frame_divisor: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Divisor applied to frame-averaged groups",
                # fmt: off
                "description": (
                    "This is the number of reads per resultant. Its use depends upon the definition "
                    "in the MA table."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.exposure_frame_divisor",
                        "GuideWindow.exposure_frame_divisor",
                    ],
                },
            },
        ),
    ]
    groupgap: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Number of frames dropped between groups",
                "description": 'This is the number of reads that are "dropped" and not used in the resultant.',
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.exposure_groupgap",
                        "GuideWindow.exposure_groupgap",
                    ],
                },
            },
        ),
    ]
    frame_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[s] Time between frames",
                "description": (
                    "The time between the end of one read and the start of the next read. This "
                    "depends on the MA table being used."
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
                        "ScienceCommon.exposure_frame_time",
                        "GuideWindow.exposure_frame_time",
                    ],
                },
            },
        ),
    ]
    group_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[s] Time between groups",
                "description": (
                    "The time that is the sum of the reads that are used to construct a resultant. "
                    "This will depend on the MA table being used."
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
                        "ScienceCommon.exposure_group_time",
                        "GuideWindow.exposure_group_time",
                    ],
                },
            },
        ),
    ]
    exposure_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[s] exposure time",
                "description": (
                    "The time between the start of the first Reset/Read Science Frame of an Exposure "
                    "and the completion of the final Read Only Science Frame of that Exposure."
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
                        "ScienceCommon.exposure_time",
                        "GuideWindow.exposure_time",
                    ],
                },
            },
        ),
    ]
    effective_exposure_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[s] Effective exposure time",
                "description": "The time that the detector is collecting photons that are used in the resultants.",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.effective_exposure_time",
                        "GuideWindow.effective_exposure_time",
                    ],
                },
            },
        ),
    ]
    duration: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[s] Total duration of exposure",
                "description": (
                    "The time that the detector is dedicated to an exposure. This includes any overhead "
                    "and times for dropped frames etc."
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
                        "ScienceCommon.exposure_duration",
                        "GuideWindow.exposure_duration",
                    ],
                },
            },
        ),
    ]
    ma_table_name: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Identifier for the multi-accumulation table used",
                # fmt: off
                "description": (
                    "The name of the MA table used for the exposure as defined by the "
                    "PRD (Project Reference Database)"
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(50)",
                    "destination": [
                        "ScienceCommon.ma_table_name",
                        "GuideWindow.ma_table_name",
                    ],
                },
            },
        ),
    ]
    ma_table_number: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Numerical identifier for the multi-accumulation table used",
                "description": (
                    "The number of the MA table used for the exposure as defined by the "
                    "PRD (Project Reference Database). This is used for matching the exposure "
                    "to the appropriate calibration data."
                ),
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.ma_table_number",
                        "GuideWindow.ma_table_number",
                    ],
                },
            },
        ),
    ]
    level0_compressed: Annotated[
        bool,
        Field(
            json_schema_extra={
                "title": "Level 0 data was compressed",
                # fmt: off
                "description": (
                    "A flag to indicate that the exposure has data that needed to be decompressed by "
                    "the ground system."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nchar(1)",
                    "destination": [
                        "ScienceCommon.exposure_level0_compressed",
                        "GuideWindow.exposure_level0_compressed",
                    ],
                },
            },
        ),
    ]
    read_pattern: Annotated[
        list[list[int]],
        Field(
            json_schema_extra={
                "title": "Pattern of reads",
                # fmt: off
                "description": (
                    "Enumeration of detector reads to resultants making up the L1 data downlinked "
                    "from the observatory"
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(3500)",
                    "destination": [
                        "ScienceCommon.read_pattern",
                        "GuideWindow.read_pattern",
                    ],
                },
            },
        ),
    ]
    truncated: Annotated[
        bool,
        Field(
            json_schema_extra={
                "title": "MA Tables were truncated",
                "description": "This is a flag to indicate that the the MA table was truncated.",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nchar(1)",
                    "destination": [
                        "ScienceCommon.exposure_truncated",
                    ],
                },
            },
        ),
    ]
