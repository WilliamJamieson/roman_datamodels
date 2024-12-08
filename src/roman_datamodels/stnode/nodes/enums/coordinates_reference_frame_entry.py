from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["CoordinatesReferenceFrameEntry"]


class CoordinatesReferenceFrameEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(self) -> type:
        from ..meta import Coordinates

        return Coordinates

    @classmethod
    def asdf_property_name(self) -> str:
        return "reference_frame"


class CoordinatesReferenceFrameEntry(CoordinatesReferenceFrameEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible reference_frame entries
    """

    ICRS = "ICRS"
