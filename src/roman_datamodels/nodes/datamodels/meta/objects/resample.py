from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import core, rad

__all__ = [
    "Resample",
    "ResampleWeightTypeEntry",
]


class ResampleWeightTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return Resample

    @classmethod
    def asdf_property_name(cls) -> str:
        return "weight_type"


class ResampleWeightTypeEntry(ResampleWeightTypeEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for resample weight type
    """

    EXPTIME = "exptime"
    IVM = "ivm"


_Resample: TypeAlias = ResampleWeightTypeEntry | core.LNode[str] | float | int | str | None


class Resample(rad.TaggedObjectNode[_Resample]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/resample-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/resample-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/resample-1.0.0",
            }
        )

    @property
    @rad.field
    def good_bits(self: rad.Node) -> str:
        return "NA"

    @property
    @rad.field
    def pixel_scale_ratio(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def pixfrac(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def pointings(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def product_exposure_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def members(self: rad.Node) -> core.LNode[str]:
        return core.LNode([])

    @property
    @rad.field
    def weight_type(self: rad.Node) -> ResampleWeightTypeEntry:
        return ResampleWeightTypeEntry.EXPTIME
