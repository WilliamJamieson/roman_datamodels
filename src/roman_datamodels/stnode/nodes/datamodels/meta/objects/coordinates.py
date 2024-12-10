from enum import Enum
from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = [
    "Coordinates",
    "CoordinatesReferenceFrameEntry",
]


class CoordinatesReferenceFrameEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(self) -> type:
        return Coordinates

    @classmethod
    def asdf_property_name(self) -> str:
        return "reference_frame"


class CoordinatesReferenceFrameEntry(CoordinatesReferenceFrameEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible reference_frame entries
    """

    ICRS = "ICRS"


class Coordinates(rad.TaggedObjectNode):
    """
    Coordinate frame information
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/coordinates-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/coordinates-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/coordinates-1.0.0"
            }
        )

    @rad.field
    def reference_frame(self) -> CoordinatesReferenceFrameEntry:
        return self._get_node("reference_frame", lambda: CoordinatesReferenceFrameEntry.ICRS)
