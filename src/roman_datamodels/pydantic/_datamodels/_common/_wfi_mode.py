from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

from . import _wfi_detector, _wfi_optical_element

__all__ = ["WfiMode", "instrument"]


class instrument(_strenum.StrEnum):
    WFI = "WFI"


class WfiMode(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.WFI_MODE.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.WFI_MODE.value

    model_config = ConfigDict(
        title="WFI observing configuration",
    )

    name: Annotated[
        instrument,
        Field(
            default_factory=_defaults.default_constant_factory(instrument.WFI.value),
            title="Instrument used to acquire the data",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(5)",
                    destination=[
                        "ScienceCommon.instrument_name",
                        "GuideWindow.instrument_name",
                    ],
                ),
            ),
        ),
    ]
    detector: Annotated[
        _wfi_detector.WfiDetector,
        Field(
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
                        "ScienceCommon.detector",
                        "GuideWindow.detector",
                    ],
                ),
            ),
        ),
    ]
    optical_element: Annotated[
        _wfi_optical_element.WfiOpticalElement,
        Field(
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
                        "ScienceCommon.optical_element",
                        "GuideWindow.optical_element",
                    ],
                ),
            ),
        ),
    ]
