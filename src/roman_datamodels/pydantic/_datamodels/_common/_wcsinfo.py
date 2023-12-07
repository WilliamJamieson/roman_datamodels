from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel, Number
from ..._defaults import default_constant_factory, default_num_value, default_str_value
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Wcsinfo"]


class Wcsinfo(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.WCSINFO.value
    _tag_uri: ClassVar = asdf_tag_uri.WCSINFO.value

    model_config = ConfigDict(
        title="WCS parameters",
    )

    v2_ref: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[arcsec] Telescope v2 coordinate of the reference point",
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
                        "ScienceCommon.v2_ref",
                        "GuideWindow.v2_ref",
                    ],
                ),
            ),
        ),
    ]
    v3_ref: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[arcsec] Telescope v3 coordinate of the reference point",
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Relative sense of rotation between Ideal xy and V2V3",
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
                        "ScienceCommon.vparity",
                        "GuideWindow.vparity",
                    ],
                ),
            ),
        ),
    ]
    v3yangle: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] Angle from V3 axis to Ideal y axis",
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
                        "ScienceCommon.v3yangle",
                        "GuideWindow.v3yangle",
                    ],
                ),
            ),
        ),
    ]
    ra_ref: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] Right ascension of the reference point",
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
                        "ScienceCommon.ra_ref",
                        "GuideWindow.ra_ref",
                    ],
                ),
            ),
        ),
    ]
    dec_ref: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] Declination of the reference point",
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
                        "ScienceCommon.dec_ref",
                        "GuideWindow.dec_ref",
                    ],
                ),
            ),
        ),
    ]
    roll_ref: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] V3 roll angle at the ref point (N over E)",
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="spatial extent of the observation",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(max)",
                    destination=[
                        "ScienceCommon.s_region",
                        "GuideWindow.s_region",
                    ],
                ),
            ),
        ),
    ]
