from typing import Annotated, ClassVar

from astropy.time import Time
from pydantic import ConfigDict, Field

from ..._adaptors import AstropyTime
from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanURIModel
from ..._defaults import default_constant_factory, default_str_value
from ..._enums import StrEnum
from ..._uri import asdf_uri

__all__ = ["Basic", "telescope", "origin"]


class telescope(StrEnum):
    ROMAN = "ROMAN"


class origin(StrEnum):
    STSCI = "STSCI"
    IPAC = "IPAC/SSC"
    SSC = "IPAC/SSC"


class Basic(BaseRomanURIModel):
    _uri: ClassVar = asdf_uri.BASIC.value

    model_config = ConfigDict(
        title="Common metadata keywords",
    )

    calibration_software_version: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("9.9.0"),
            title="Calibration software version number",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.calibration_software_version",
                        "GuideWindow.calibration_software_version",
                    ],
                ),
            ),
        ),
    ]
    file_date: Annotated[
        AstropyTime,
        Field(
            default_factory=default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="Date this file was created (UTC)",
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
                        "ScienceCommon.filedate",
                        "GuideWindow.filedate",
                    ],
                ),
            ),
        ),
    ]
    filename: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Name of the file",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.filename",
                        "GuideWindow.filename",
                    ],
                ),
            ),
        ),
    ]
    # this is aliased to model_type, (model_* is protected by default)
    mdl_type: Annotated[
        str,
        Field(
            alias="model_type",
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Type of data model",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(50)",
                    destination=[
                        "ScienceCommon.model_type",
                        "GuideWindow.model_type",
                    ],
                ),
            ),
        ),
    ]
    origin: Annotated[
        origin,
        Field(
            default_factory=default_constant_factory(origin.STSCI.value),
            title="Organization responsible for creating file",
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
                        "ScienceCommon.origin",
                        "GuideWindow.origin",
                    ],
                ),
            ),
        ),
    ]
    prd_software_version: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("8.8.8"),
            title="S&OC PRD version number used in data processing",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.prd_software_version",
                        "GuideWindow.prd_software_version",
                    ],
                ),
            ),
        ),
    ]
    sdf_software_version: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("7.7.7"),
            title="SDF software version number",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.sdf_software_version",
                        "GuideWindow.sdf_software_version",
                    ],
                ),
            ),
        ),
    ]
    telescope: Annotated[
        telescope,
        Field(
            default_factory=default_constant_factory(telescope.ROMAN.value),
            title="Telescope used to acquire the data",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(5)",
                    destination=[
                        "ScienceCommon.telescope",
                        "GuideWindow.telescope",
                    ],
                ),
            ),
        ),
    ]
