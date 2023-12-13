from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Aperture"]


class aperture(_strenum.StrEnum):
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


class Aperture(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.APERTURE.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.APERTURE.value

    model_config = ConfigDict(
        title="Aperture Information",
    )

    name: Annotated[
        aperture,
        Field(
            default_factory=_defaults.default_constant_factory(aperture.WFI_06_FULL.value),
            title="PRD science aperture used",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:aperture.AperName",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
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
            default_factory=_defaults.default_constant_factory(30.0),
            title="[deg] Position angle of aperture used",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(origin="TBD"),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.position_angle",
                        "GuideWindow.position_angle",
                    ],
                ),
            ),
        ),
    ]
