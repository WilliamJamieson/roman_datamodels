from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel, Number
from ..._defaults import default_constant_factory
from ..._enums import aperture
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Aperture"]


class Aperture(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.APERTURE.value
    _tag_uri: ClassVar = asdf_tag_uri.APERTURE.value

    model_config = ConfigDict(
        title="Aperture Information",
    )

    name: Annotated[
        aperture,
        Field(
            default_factory=default_constant_factory(aperture.WFI_06_FULL.value),
            title="PRD science aperture used",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:aperture.AperName",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(40)",
                    destination=[
                        "ScienceCommon.aperture_name",
                        "GuideWindow.aperture_name",
                    ],
                ),
            ),
        ),
    ]
    position_angle: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(30.0),
            title="[deg] Position angle of aperture used",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(origin="TBD"),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.position_angle",
                        "GuideWindow.position_angle",
                    ],
                ),
            ),
        ),
    ]
