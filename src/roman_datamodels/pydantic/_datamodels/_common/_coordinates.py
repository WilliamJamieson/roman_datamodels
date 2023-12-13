from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Coordinates"]


class coordinates(_strenum.StrEnum):
    ICRS = "ICRS"


class Coordinates(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.COORDINATES.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.COORDINATES.value

    _optional_fields: ClassVar = ("reference_frame",)

    model_config = ConfigDict(
        title="Information about the coordinates in the file",
    )

    reference_frame: Annotated[
        coordinates,
        Field(
            default_factory=_defaults.default_constant_factory(coordinates.ICRS.value),
            title="Reference frame",
            json_schema_extra=_archive.Archive(
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(10)",
                    destination=[
                        "ScienceCommon.reference_frame",
                        "GuideWindow.reference_frame",
                    ],
                ),
            ),
        ),
    ]
