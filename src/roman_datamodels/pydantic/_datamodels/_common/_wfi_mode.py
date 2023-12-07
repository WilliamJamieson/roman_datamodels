from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_constant_factory
from ..._enums import StrEnum
from ..._uri import asdf_tag_uri, asdf_uri
from ._wfi_detector import WfiDetector
from ._wfi_optical_element import WfiOpticalElement

__all__ = ["WfiMode", "instrument"]


class instrument(StrEnum):
    WFI = "WFI"


class WfiMode(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.WFI_MODE.value
    _tag_uri: ClassVar = asdf_tag_uri.WFI_MODE.value

    model_config = ConfigDict(
        title="WFI observing configuration",
    )

    name: Annotated[
        instrument,
        Field(
            default_factory=default_constant_factory(instrument.WFI.value),
            title="Instrument used to acquire the data",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
        WfiDetector,
        Field(
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
                        "ScienceCommon.detector",
                        "GuideWindow.detector",
                    ],
                ),
            ),
        ),
    ]
    optical_element: Annotated[
        WfiOpticalElement,
        Field(
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
                        "ScienceCommon.optical_element",
                        "GuideWindow.optical_element",
                    ],
                ),
            ),
        ),
    ]
