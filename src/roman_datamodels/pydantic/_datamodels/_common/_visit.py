from typing import Annotated, ClassVar

from astropy.time import Time
from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _adaptors, _archive, _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Visit"]


class engineering_quality(_strenum.StrEnum):
    OK = "OK"
    SUSPECT = "SUSPECT"


class pointing_engdb_quality(_strenum.StrEnum):
    CALCULATED = "CALCULATED"
    PLANNED = "PLANNED"


class Visit(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.VISIT.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.VISIT.value

    model_config = ConfigDict(
        title="Visit information",
    )

    engineering_quality: Annotated[
        engineering_quality,
        Field(
            default_factory=_defaults.default_constant_factory(engineering_quality.OK.value),
            title="Engineering data quality indicator from EngDB",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(10)",
                    destination=[
                        "ScienceCommon.engineering_quality",
                        "GuideWindow.engineering_quality",
                    ],
                ),
            ),
        ),
    ]
    pointing_engdb_quality: Annotated[
        pointing_engdb_quality,
        Field(
            default_factory=_defaults.default_constant_factory(pointing_engdb_quality.CALCULATED.value),
            title="Quality of pointing information from EngDB",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(10)",
                    destination=[
                        "ScienceCommon.pointing_engdb_quality",
                        "GuideWindow.pointing_engdb_quality",
                    ],
                ),
            ),
        ),
    ]
    type: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Visit type",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(30)",
                    destination=[
                        "ScienceCommon.visit_type",
                        "GuideWindow.visit_type",
                    ],
                ),
            ),
        ),
    ]
    start_time: Annotated[
        _adaptors.AstropyTime,
        Field(
            default_factory=_defaults.default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC visit start time",
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
                        "ScienceCommon.visit_start_time",
                        "GuideWindow.visit_start_time",
                    ],
                ),
            ),
        ),
    ]
    end_time: Annotated[
        _adaptors.AstropyTime,
        Field(
            default_factory=_defaults.default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC visit end time",
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
                        "ScienceCommon.visit_end_time",
                        "GuideWindow.visit_end_time",
                    ],
                ),
            ),
        ),
    ]
    status: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Status of a visit",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceCommon.visit_status",
                        "GuideWindow.visit_status",
                    ],
                ),
            ),
        ),
    ]
    total_exposures: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Total number of planned exposures in visit",
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
                        "ScienceCommon.visit_total_exposures",
                        "GuideWindow.visit_total_exposures",
                    ],
                ),
            ),
        ),
    ]
    internal_target: Annotated[
        bool,
        Field(
            default_factory=_defaults.default_constant_factory(False),
            title="At least one exposure in visit is internal",
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
                        "ScienceCommon.visit_internal_target",
                        "GuideWindow.visit_internal_target",
                    ],
                ),
            ),
        ),
    ]
    target_of_opportunity: Annotated[
        bool,
        Field(
            default_factory=_defaults.default_constant_factory(False),
            title="Visit scheduled as target of opportunity",
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
                        "ScienceCommon.target_of_opportunity",
                        "GuideWindow.target_of_opportunity",
                    ],
                ),
            ),
        ),
    ]
