from roman_datamodels.stnode import rad

__all__ = [
    "Coordinates",
    "CoordinatesReferenceFrameEntry",
    "CoordinatesReferenceFrameEntryMixin",
]


class CoordinatesReferenceFrameEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def _asdf_container(self) -> type:
        return Coordinates

    @classmethod
    def _asdf_property_name(cls) -> str:
        return "reference_frame"


class CoordinatesReferenceFrameEntry(CoordinatesReferenceFrameEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible reference_frame entries
    """

    ICRS = "ICRS"


class Coordinates(rad.TaggedObjectNode):
    @classmethod
    def _asdf_tag_uris(cls) -> dict[str, str]:
        return {
            "asdf://stsci.edu/datamodels/roman/tags/coordinates-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/coordinates-1.0.0"
        }

    @rad.field
    def reference_frame(self) -> CoordinatesReferenceFrameEntry:
        return CoordinatesReferenceFrameEntry.ICRS
