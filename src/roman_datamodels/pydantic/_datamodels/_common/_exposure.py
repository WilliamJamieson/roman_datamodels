from typing import Annotated, ClassVar

from astropy.time import Time
from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _adaptors, _archive, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _exposure_type

__all__ = ["Exposure"]


class Exposure(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.EXPOSURE.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.EXPOSURE.value

    _optional_fields: ClassVar = ("truncated",)

    model_config = ConfigDict(
        title="Exposure Information",
    )

    id: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Exposure id number within visit",
            description="The exposure number for a given visit id",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.exposure_id",
                        "GuideWindow.exposure_id",
                    ],
                ),
            ),
        ),
    ]
    type: Annotated[
        _exposure_type.ExposureType,
        Field(
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(25)",
                    destination=[
                        "ScienceCommon.exposure_type",
                        "GuideWindow.exposure_type",
                    ],
                ),
            )
        ),
    ]
    start_time: Annotated[
        _adaptors.AstropyTime,
        Field(
            default_factory=_defaults.default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC exposure start time",
            description="This is a python date-time object that records the time at the start of the exposure in UTC.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="datetime2",
                    destination=[
                        "ScienceCommon.exposure_start_time",
                        "GuideWindow.exposure_start_time",
                    ],
                ),
            ),
        ),
    ]
    mid_time: Annotated[
        _adaptors.AstropyTime,
        Field(
            default_factory=_defaults.default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC exposure mid time",
            description=("This is a python date-time object that records the " "time at the middle of the exposure in UTC."),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="datetime2",
                    destination=[
                        "ScienceCommon.exposure_mid_time",
                        "GuideWindow.exposure_mid_time",
                    ],
                ),
            ),
        ),
    ]
    end_time: Annotated[
        _adaptors.AstropyTime,
        Field(
            default_factory=_defaults.default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC exposure end time",
            description=("This is a python date-time object that records the " "time at the end of the exposure in UTC."),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="datetime2",
                    destination=[
                        "ScienceCommon.exposure_end_time",
                        "GuideWindow.exposure_end_time",
                    ],
                ),
            ),
        ),
    ]
    start_time_mjd: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[d] exposure start time in MJD",
            description=(
                "This records the time at the start of the exposure using the "
                "Modified Julian Date (MJD). This is used in the archive catalog for"
                "multi-mission matching."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_start_time_mjd",
                        "GuideWindow.exposure_start_time_mjd",
                    ],
                ),
            ),
        ),
    ]
    mid_time_mjd: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[d] exposure mid time in MJD",
            description=(
                "This records the time at the midpoint of the exposure using the "
                "Modified Julian Date (MJD). This is used in the archive catalog for"
                "multi-mission matching."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_mid_time_mjd",
                        "GuideWindow.exposure_mid_time_mjd",
                    ],
                ),
            ),
        ),
    ]
    end_time_mjd: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[d] exposure end time in MJD",
            description=(
                "This records the time at the end of the exposure using the "
                "Modified Julian Date (MJD). This is used in the archive catalog for"
                "multi-mission matching."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_end_time_mjd",
                        "GuideWindow.exposure_end_time_mjd",
                    ],
                ),
            ),
        ),
    ]
    start_time_tdb: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[d] TDB time of exposure start in MJD",
            description=(
                "This records the time at the start of the exposure using "
                "the Modified Julian Date for the Barycentric Dynamical Time system "
                "(TDB, Temps Dynamique Barycentrique), a relativistic coordinate "
                "time scale."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_start_time_tdb",
                        "GuideWindow.exposure_start_time_tdb",
                    ],
                ),
            ),
        ),
    ]
    mid_time_tdb: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[d] TDB time of exposure mid in MJD",
            description=(
                "This records the time at the midpoint of the exposure using "
                "the Modified Julian Date for the Barycentric Dynamical Time system "
                "(TDB, Temps Dynamique Barycentrique), a relativistic coordinate "
                "time scale."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_mid_time_tdb",
                        "GuideWindow.exposure_mid_time_tdb",
                    ],
                ),
            ),
        ),
    ]
    end_time_tdb: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[d] TDB time of exposure end in MJD",
            description=(
                "This records the time at the end of the exposure using "
                "the Modified Julian Date for the Barycentric Dynamical Time system "
                "(TDB, Temps Dynamique Barycentrique), a relativistic coordinate "
                "time scale."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_end_time_tdb",
                        "GuideWindow.exposure_end_time_tdb",
                    ],
                ),
            ),
        ),
    ]
    ngroups: Annotated[
        int,
        Field(
            default_factory=_defaults.default_constant_factory(6),
            title="Number of groups in integration",
            description=(
                "This is the number of resultant frames in the exposure "
                "that are transmitted to the ground. The WFI data always has the "
                "number of integrations=1."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:exposure.NGroups",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.exposure_ngroups",
                        "GuideWindow.exposure_ngroups",
                    ],
                ),
            ),
        ),
    ]
    nframes: Annotated[
        int,
        Field(
            default_factory=_defaults.default_constant_factory(8),
            title="Number of frames per group",
            description=("This is the number of science frames that are combined to " "produce a resultant frame."),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.exposure_nframes",
                        "GuideWindow.exposure_nframes",
                    ],
                ),
            ),
        ),
    ]
    data_problem: Annotated[
        bool,
        Field(
            default_factory=_defaults.default_constant_factory(False),
            title="Science telemetry indicated a problem",
            description=("This is a flag to indicate that the science telemetry " "experienced a problem."),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nchar(1)",
                    destination=[
                        "ScienceCommon.exposure_data_problem",
                        "GuideWindow.exposure_data_problem",
                    ],
                ),
            ),
        ),
    ]
    sca_number: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Sensor Chip Assembly number",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.exposure_sca_number",
                        "GuideWindow.exposure_sca_number",
                    ],
                ),
            ),
        ),
    ]
    gain_factor: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Gain scale factor",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_gain_factor",
                        "GuideWindow.exposure_gain_factor",
                    ],
                ),
            ),
        ),
    ]
    integration_time: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[s] Effective integration time",
            description="The effective time that the sensor has been exposed to the sky.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_integration_time",
                        "GuideWindow.exposure_integration_time",
                    ],
                ),
            ),
        ),
    ]
    elapsed_exposure_time: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[s] Total elapsed exposure time",
            description=(
                "The time between the start of the first Reset/Read Science Frame of an Exposure "
                "and the completion of the final Read Only Science Frame of that Exposure."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.elapsed_exposure_time",
                        "GuideWindow.elapsed_exposure_time",
                    ],
                ),
            ),
        ),
    ]
    frame_divisor: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Divisor applied to frame-averaged groups",
            description=("This is the number of reads per resultant. Its use depends upon the definition " "in the MA table."),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.exposure_frame_divisor",
                        "GuideWindow.exposure_frame_divisor",
                    ],
                ),
            ),
        ),
    ]
    groupgap: Annotated[
        int,
        Field(
            default_factory=_defaults.default_constant_factory(0),
            title="Number of frames dropped between groups",
            description='This is the number of reads that are "dropped" and not used in the resultant.',
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.exposure_groupgap",
                        "GuideWindow.exposure_groupgap",
                    ],
                ),
            ),
        ),
    ]
    frame_time: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[s] Time between frames",
            description=(
                "The time between the end of one read and the start of the next read. This " "depends on the MA table being used."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_frame_time",
                        "GuideWindow.exposure_frame_time",
                    ],
                ),
            ),
        ),
    ]
    group_time: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[s] Time between groups",
            description=(
                "The time that is the sum of the reads that are used to construct a resultant. "
                "This will depend on the MA table being used."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_group_time",
                        "GuideWindow.exposure_group_time",
                    ],
                ),
            ),
        ),
    ]
    exposure_time: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[s] exposure time",
            description=(
                "The time between the start of the first Reset/Read Science Frame of an Exposure "
                "and the completion of the final Read Only Science Frame of that Exposure."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_time",
                        "GuideWindow.exposure_time",
                    ],
                ),
            ),
        ),
    ]
    effective_exposure_time: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[s] Effective exposure time",
            description="The time that the detector is collecting photons that are used in the resultants.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.effective_exposure_time",
                        "GuideWindow.effective_exposure_time",
                    ],
                ),
            ),
        ),
    ]
    duration: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[s] Total duration of exposure",
            description=(
                "The time that the detector is dedicated to an exposure. This includes any overhead "
                "and times for dropped frames etc."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.exposure_duration",
                        "GuideWindow.exposure_duration",
                    ],
                ),
            ),
        ),
    ]
    ma_table_name: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Identifier for the multi-accumulation table used",
            description=("The name of the MA table used for the exposure as defined by the " "PRD (Project Reference Database)"),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(50)",
                    destination=[
                        "ScienceCommon.ma_table_name",
                        "GuideWindow.ma_table_name",
                    ],
                ),
            ),
        ),
    ]
    ma_table_number: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Numerical identifier for the multi-accumulation table used",
            description=(
                "The number of the MA table used for the exposure as defined by the "
                "PRD (Project Reference Database). This is used for matching the exposure "
                "to the appropriate calibration data."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.ma_table_number",
                        "GuideWindow.ma_table_number",
                    ],
                ),
            ),
        ),
    ]
    level0_compressed: Annotated[
        bool,
        Field(
            default_factory=_defaults.default_constant_factory(True),
            title="Level 0 data was compressed",
            description=("A flag to indicate that the exposure has data that needed to be decompressed by " "the ground system."),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nchar(1)",
                    destination=[
                        "ScienceCommon.exposure_level0_compressed",
                        "GuideWindow.exposure_level0_compressed",
                    ],
                ),
            ),
        ),
    ]
    read_pattern: Annotated[
        list[list[int]],
        Field(
            default_factory=_defaults.default_constant_factory([[1], [2, 3], [4], [5, 6, 7, 8], [9, 10], [11]]),
            title="Pattern of reads",
            description=("Enumeration of detector reads to resultants making up the L1 data downlinked " "from the observatory"),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(50)",
                    destination=[
                        "ScienceCommon.read_pattern",
                        "GuideWindow.read_pattern",
                    ],
                ),
            ),
        ),
    ]
    truncated: Annotated[
        bool,
        Field(
            default_factory=_defaults.default_constant_factory(False),
            title="MA tables were truncated",
            description="This is a flag to indicate that the the MA table was truncated.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nchar(1)",
                    destination=[
                        "ScienceCommon.exposure_truncated",
                        "GuideWindow.exposure_truncated",
                    ],
                ),
            ),
        ),
    ]
