from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel, Number
from ..._defaults import default_constant_factory, default_num_value, default_str_value
from ..._strenum import StrEnum
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Ephemeris"]


class ephemeris_type(StrEnum):
    DEFINITIVE = "DEFINITIVE"
    PREDICTED = "PREDICTED"


class Ephemeris(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.EPHEMERIS.value
    _tag_uri: ClassVar = asdf_tag_uri.EPHEMERIS.value

    model_config = ConfigDict(
        title="Ephemeris data information",
    )

    earth_angle: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[radians] Earth Angle",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[radians] Moon Angle",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Ephemeris reference frame",
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
                        "ScienceCommon.ephemeris_reference_frame",
                        "GuideWindow.ephermeris_reference_frame",
                    ],
                ),
            ),
        ),
    ]
    sun_angle: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[radians] Sun Angle",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(ephemeris_type.DEFINITIVE.value),
            title="Type of ephemeris",
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
                        "ScienceCommon.ephermeris_type",
                        "GuideWindow.ephemeris_type",
                    ],
                ),
            ),
        ),
    ]
    time: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="UTC time of position and velocity vectors in ephemeris (MJD)",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[km] X spatial coordinate of Roman",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[km] Y spatial coordinate of Roman",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[km] Z spatial coordinate of Roman",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[km/s] X component of Roman velocity",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[km/s] Y component of Roman velocity",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[km/s] Z component of Roman velocity",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.velocity_z",
                        "GuideWindow.velocity_z",
                    ],
                ),
            ),
        ),
    ]
