from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_constant_factory, default_num_value
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Pointing"]


class Pointing(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.POINTING.value
    _tag_uri: ClassVar = asdf_tag_uri.POINTING.value

    model_config = ConfigDict(
        title="Spacecraft pointing information",
    )

    ra_v1: Annotated[
        float,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] RA of telescope V1 axis",
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
                        "ScienceCommon.ra_v1",
                        "GuideWindow.ra_v1",
                    ],
                ),
            ),
        ),
    ]
    dec_v1: Annotated[
        float,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] Dec of telescope V1 axis",
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
                        "ScienceCommon.dec_v1",
                        "GuideWindow.dec_v1",
                    ],
                ),
            ),
        ),
    ]
    pa_v3: Annotated[
        float,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] Position angle of telescope V3 axis",
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
                        "ScienceCommon.pa_v3",
                        "GuideWindow.pa_v3",
                    ],
                ),
            ),
        ),
    ]
