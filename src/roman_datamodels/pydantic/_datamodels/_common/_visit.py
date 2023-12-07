from typing import Annotated, ClassVar

from astropy.time import Time
from pydantic import ConfigDict, Field

from ..._adaptors import AstropyTime
from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_constant_factory, default_num_value, default_str_value
from ..._enums import engineering_quality, pointing_engdb_quality
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Visit"]


class Visit(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.VISIT.value
    _tag_uri: ClassVar = asdf_tag_uri.VISIT.value

    model_config = ConfigDict(
        title="Visit information",
    )

    engineering_quality: Annotated[
        engineering_quality,
        Field(
            default=engineering_quality.OK.value,
            title="Engineering data quality indicator from EngDB",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(pointing_engdb_quality.CALCULATED.value),
            title="Quality of pointing information from EngDB",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Visit type",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        AstropyTime,
        Field(
            default_factory=default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC visit start time",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        AstropyTime,
        Field(
            default_factory=default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC visit end time",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Status of a visit",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Total number of planned exposures in visit",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(False),
            title="At least one exposure in visit is internal",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(False),
            title="Visit scheduled as target of opportunity",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nchar(1)",
                    destination=[
                        "ScienceCommon.target_of_opportunity",
                        "GuideWindow.target_of_opportunity",
                    ],
                ),
            ),
        ),
    ]
