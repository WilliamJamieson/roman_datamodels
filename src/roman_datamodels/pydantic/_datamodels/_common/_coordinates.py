from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_constant_factory
from ..._enums import coordinates
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Coordinates"]


class Coordinates(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.COORDINATES.value
    _tag_uri: ClassVar = asdf_tag_uri.COORDINATES.value

    _optional_fields: ClassVar = ("reference_frame",)

    model_config = ConfigDict(
        title="Information about the coordinates in the file",
    )

    reference_frame: Annotated[
        coordinates,
        Field(
            default_factory=default_constant_factory(coordinates.ICRS.value),
            title="Reference frame",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(10)",
                    destination=[
                        "ScienceCommon.reference_frame",
                        "GuideWindow.reference_frame",
                    ],
                ),
            ),
        ),
    ]
