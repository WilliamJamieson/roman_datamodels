from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Pointing"]


class Pointing(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.POINTING.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.POINTING.value

    model_config = ConfigDict(
        title="Spacecraft pointing information",
    )

    ra_v1: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="[deg] RA of telescope V1 axis",
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
            default_factory=_defaults.default_num_factory,
            title="[deg] Dec of telescope V1 axis",
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
            default_factory=_defaults.default_num_factory,
            title="[deg] Position angle of telescope V3 axis",
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
                        "ScienceCommon.pa_v3",
                        "GuideWindow.pa_v3",
                    ],
                ),
            ),
        ),
    ]
