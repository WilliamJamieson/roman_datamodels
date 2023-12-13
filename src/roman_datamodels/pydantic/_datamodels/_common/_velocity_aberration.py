from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

__all__ = ["VelocityAberration"]


class VelocityAberration(_core.BaseRomanURIModel):
    _uri: ClassVar = uri.asdf_uri.VELOCITY_ABERRATION.value

    model_config = ConfigDict(
        title="Velocity aberration correction information",
    )

    ra_offset: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Velocity aberration right ascension offset",
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
            default_factory=_defaults.default_num_factory,
            title="Velocity aberration declination offset",
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
            default_factory=_defaults.default_num_factory,
            title="Velocity aberration scale factor",
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
                        "ScienceCommon.scale_factor",
                        "GuideWindow.scale_factor",
                    ],
                ),
            ),
        ),
    ]
