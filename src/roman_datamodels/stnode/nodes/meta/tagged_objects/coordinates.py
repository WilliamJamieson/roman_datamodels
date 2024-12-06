from roman_datamodels.stnode import _core

from ...enums import CoordinatesReferenceFrameEntry

__all__ = ["Coordinates"]


class Coordinates(_core.TaggedObjectNode):
    """
    Coordinate frame information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/coordinates-1.0.0"

    @_core.rad_field
    def reference_frame(self) -> CoordinatesReferenceFrameEntry:
        return self._get_node("reference_frame", lambda: CoordinatesReferenceFrameEntry.ICRS)
