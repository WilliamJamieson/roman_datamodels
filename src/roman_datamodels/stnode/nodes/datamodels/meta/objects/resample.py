from enum import Enum

from roman_datamodels.stnode import core, rad

__all__ = [
    "Resample",
    "ResampleWeightTypeEntry",
]


class ResampleWeightTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Resample

    @classmethod
    def asdf_property_name(cls) -> str:
        return "weight_type"


class ResampleWeightTypeEntry(ResampleWeightTypeEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for resample weight type
    """

    EXPTIME = "exptime"
    IVM = "ivm"


class Resample(rad.TaggedObjectNode):
    """
    Resample information
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/resample-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/resample-1.0.0"

    @rad.field
    def good_bits(self) -> str:
        return self._get_node("good_bits", lambda: "NA")

    @rad.field
    def pixel_scale_ratio(self) -> float:
        return self._get_node("pixel_scale_ratio", lambda: rad.NONUM)

    @rad.field
    def pixfrac(self) -> float:
        return self._get_node("pixfrac", lambda: rad.NONUM)

    @rad.field
    def pointings(self) -> int:
        return self._get_node("pointings", lambda: rad.NOINT)

    @rad.field
    def product_exposure_time(self) -> float:
        return self._get_node("product_exposure_time", lambda: rad.NONUM)

    @rad.field
    def members(self) -> core.LNode[str]:
        return self._get_node("members", lambda: core.LNode([]))

    @rad.field
    def weight_type(self) -> ResampleWeightTypeEntry:
        return self._get_node("weight_type", lambda: ResampleWeightTypeEntry.EXPTIME)
