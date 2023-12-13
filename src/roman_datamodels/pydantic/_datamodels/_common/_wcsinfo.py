from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Wcsinfo"]


class Wcsinfo(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.WCSINFO.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.WCSINFO.value

    model_config = ConfigDict(
        title="WCS parameters",
    )

    v2_ref: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[arcsec] Telescope v2 coordinate of the reference point",
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
                        "ScienceCommon.v2_ref",
                        "GuideWindow.v2_ref",
                    ],
                ),
            ),
        ),
    ]
    v3_ref: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[arcsec] Telescope v3 coordinate of the reference point",
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
                        "ScienceCommon.v3_ref",
                        "GuideWindow.v3_ref",
                    ],
                ),
            ),
        ),
    ]
    vparity: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Relative sense of rotation between Ideal xy and V2V3",
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
                        "ScienceCommon.vparity",
                        "GuideWindow.vparity",
                    ],
                ),
            ),
        ),
    ]
    v3yangle: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[deg] Angle from V3 axis to Ideal y axis",
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
                        "ScienceCommon.v3yangle",
                        "GuideWindow.v3yangle",
                    ],
                ),
            ),
        ),
    ]
    ra_ref: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[deg] Right ascension of the reference point",
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
                        "ScienceCommon.ra_ref",
                        "GuideWindow.ra_ref",
                    ],
                ),
            ),
        ),
    ]
    dec_ref: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[deg] Declination of the reference point",
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
                        "ScienceCommon.dec_ref",
                        "GuideWindow.dec_ref",
                    ],
                ),
            ),
        ),
    ]
    roll_ref: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[deg] V3 roll angle at the ref point (N over E)",
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
                        "ScienceCommon.roll_ref",
                        "GuideWindow.roll_ref",
                    ],
                ),
            ),
        ),
    ]
    s_region: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="spatial extent of the observation",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(max)",
                    destination=[
                        "ScienceCommon.s_region",
                        "GuideWindow.s_region",
                    ],
                ),
            ),
        ),
    ]
