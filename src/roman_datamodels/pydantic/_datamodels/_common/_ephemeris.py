from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Ephemeris"]


class ephemeris_type(_strenum.StrEnum):
    DEFINITIVE = "DEFINITIVE"
    PREDICTED = "PREDICTED"


class Ephemeris(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.EPHEMERIS.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.EPHEMERIS.value

    model_config = ConfigDict(
        title="Ephemeris data information",
    )

    earth_angle: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[radians] Earth Angle",
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
                        "ScienceCommon.earth_angle",
                        "GuideWindow.earth_angle",
                    ],
                ),
            ),
        ),
    ]
    moon_angle: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[radians] Moon Angle",
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
                        "ScienceCommon.moon_angle",
                        "GuideWindow.moon_angle",
                    ],
                ),
            ),
        ),
    ]
    ephemeris_reference_frame: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Ephemeris reference frame",
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
                        "ScienceCommon.ephemeris_reference_frame",
                        "GuideWindow.ephermeris_reference_frame",
                    ],
                ),
            ),
        ),
    ]
    sun_angle: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[radians] Sun Angle",
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
                        "ScienceCommon.sun_angle",
                        "GuideWindow.sun_angle",
                    ],
                ),
            ),
        ),
    ]
    type: Annotated[
        ephemeris_type,
        Field(
            default_factory=_defaults.default_constant_factory(ephemeris_type.DEFINITIVE.value),
            title="Type of ephemeris",
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
                        "ScienceCommon.ephermeris_type",
                        "GuideWindow.ephemeris_type",
                    ],
                ),
            ),
        ),
    ]
    time: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="UTC time of position and velocity vectors in ephemeris (MJD)",
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
                        "ScienceCommon.ephemeris_time",
                        "GuideWindow.ephermeris_time",
                    ],
                ),
            ),
        ),
    ]
    spatial_x: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[km] X spatial coordinate of Roman",
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
                        "ScienceCommon.spatial_x",
                        "GuideWindow.spatial_x",
                    ],
                ),
            ),
        ),
    ]
    spatial_y: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[km] Y spatial coordinate of Roman",
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
                        "ScienceCommon.spatial_y",
                        "GuideWindow.spatial_y",
                    ],
                ),
            ),
        ),
    ]
    spatial_z: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[km] Z spatial coordinate of Roman",
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
                        "ScienceCommon.spatial_z",
                        "GuideWindow.spatial_z",
                    ],
                ),
            ),
        ),
    ]
    velocity_x: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[km/s] X component of Roman velocity",
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
                        "ScienceCommon.velocity_x",
                        "GuideWindow.velocity_x",
                    ],
                ),
            ),
        ),
    ]
    velocity_y: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[km/s] Y component of Roman velocity",
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
                        "ScienceCommon.velocity_y",
                        "GuideWindow.velocity_y",
                    ],
                ),
            ),
        ),
    ]
    velocity_z: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[km/s] Z component of Roman velocity",
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
                        "ScienceCommon.velocity_z",
                        "GuideWindow.velocity_z",
                    ],
                ),
            ),
        ),
    ]
