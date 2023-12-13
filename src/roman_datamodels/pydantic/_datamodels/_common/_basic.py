from typing import Annotated, ClassVar

from astropy.time import Time
from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _adaptors, _archive, _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Basic", "telescope", "origin"]


class telescope(_strenum.StrEnum):
    ROMAN = "ROMAN"


class origin(_strenum.StrEnum):
    STSCI = "STSCI"
    IPAC = "IPAC/SSC"
    SSC = "IPAC/SSC"


class Basic(_core.BaseRomanURIModel):
    _uri: ClassVar = uri.asdf_uri.BASIC.value

    model_config = ConfigDict(
        title="Common metadata keywords",
    )

    calibration_software_version: Annotated[
        str,
        Field(
            default_factory=_defaults.default_constant_factory("9.9.0"),
            title="Calibration software version number",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
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
        _adaptors.AstropyTime,
        Field(
            default_factory=_defaults.default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="Date this file was created (UTC)",
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
            default_factory=_defaults.default_str_factory,
            title="Name of the file",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
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
            default_factory=_defaults.default_str_factory,
            title="Type of data model",
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
            default_factory=_defaults.default_constant_factory(origin.STSCI.value),
            title="Organization responsible for creating file",
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
            default_factory=_defaults.default_constant_factory("8.8.8"),
            title="S&OC PRD version number used in data processing",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
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
            default_factory=_defaults.default_constant_factory("7.7.7"),
            title="SDF software version number",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
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
            default_factory=_defaults.default_constant_factory(telescope.ROMAN.value),
            title="Telescope used to acquire the data",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(5)",
                    destination=[
                        "ScienceCommon.telescope",
                        "GuideWindow.telescope",
                    ],
                ),
            ),
        ),
    ]
