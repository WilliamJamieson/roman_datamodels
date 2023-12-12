from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanURIModel
from ..._defaults import default_num_factory
from ..._uri import asdf_uri

__all__ = ["VelocityAberration"]


class VelocityAberration(BaseRomanURIModel):
    _uri: ClassVar = asdf_uri.VELOCITY_ABERRATION.value

    model_config = ConfigDict(
        title="Velocity aberration correction information",
    )

    ra_offset: Annotated[
        float,
        Field(
            default_factory=default_num_factory,
            title="Velocity aberration right ascension offset",
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
                        "ScienceCommon.ra_offset",
                        "GuideWindow.ra_offset",
                    ],
                ),
            ),
        ),
    ]
    dec_offset: Annotated[
        float,
        Field(
            default_factory=default_num_factory,
            title="Velocity aberration declination offset",
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
                        "ScienceCommon.dec_offset",
                        "GuideWindow.dec_offset",
                    ],
                ),
            ),
        ),
    ]
    scale_factor: Annotated[
        float,
        Field(
            default_factory=default_num_factory,
            title="Velocity aberration scale factor",
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
                        "ScienceCommon.scale_factor",
                        "GuideWindow.scale_factor",
                    ],
                ),
            ),
        ),
    ]
