from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = [
    "Program",
    "ProgramSubcategoryEntry",
]


class ProgramSubcategoryEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return Program

    @classmethod
    def asdf_property_name(cls) -> str:
        return "subcategory"


class ProgramSubcategoryEntry(ProgramSubcategoryEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible program subcategories
    """

    CAL = "CAL"
    CGI = "CGI"
    CR = "CR"
    DR = "DR"
    GBTD = "GBTD"
    HLTD = "HLTD"
    HLWA = "HLWA"
    OR = "OR"
    WFI = "WFI"
    WFSC = "WFSC"
    NONE = "None"


_Program: TypeAlias = ProgramSubcategoryEntry | str | int


class Program(rad.TaggedObjectNode[_Program]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/program-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/program-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/program-1.0.0",
            }
        )

    @rad.field
    def title(self) -> str:
        return rad.NOSTR

    @rad.field
    def investigator_name(self) -> str:
        return rad.NOSTR

    @rad.field
    def category(self) -> str:
        return rad.NOSTR

    @rad.field
    def subcategory(self) -> ProgramSubcategoryEntry:
        return ProgramSubcategoryEntry.NONE

    @rad.field
    def science_category(self) -> str:
        return rad.NOSTR

    @rad.field
    def continuation_id(self) -> int:
        return rad.NOINT
