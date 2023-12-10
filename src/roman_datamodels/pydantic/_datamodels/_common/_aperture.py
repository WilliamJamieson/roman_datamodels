from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_constant_factory
from ..._strenum import StrEnum
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Aperture"]


class aperture(StrEnum):
    WFI_01_FULL = "WFI_01_FULL"
    WFI_02_FULL = "WFI_02_FULL"
    WFI_03_FULL = "WFI_03_FULL"
    WFI_04_FULL = "WFI_04_FULL"
    WFI_05_FULL = "WFI_05_FULL"
    WFI_06_FULL = "WFI_06_FULL"
    WFI_07_FULL = "WFI_07_FULL"
    WFI_08_FULL = "WFI_08_FULL"
    WFI_09_FULL = "WFI_09_FULL"
    WFI_10_FULL = "WFI_10_FULL"
    WFI_11_FULL = "WFI_11_FULL"
    WFI_12_FULL = "WFI_12_FULL"
    WFI_13_FULL = "WFI_13_FULL"
    WFI_14_FULL = "WFI_14_FULL"
    WFI_15_FULL = "WFI_15_FULL"
    WFI_16_FULL = "WFI_16_FULL"
    WFI_17_FULL = "WFI_17_FULL"
    WFI_18_FULL = "WFI_18_FULL"
    BORESIGHT = "BORESIGHT"
    CGI_CEN = "CGI_CEN"
    WFI_CEN = "WFI_CEN"


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
        float,
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
