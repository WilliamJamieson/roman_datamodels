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

    @property
    @rad.field
    def title(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def investigator_name(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def category(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def subcategory(self: rad.Node) -> ProgramSubcategoryEntry:
        return ProgramSubcategoryEntry.NONE

    @property
    @rad.field
    def science_category(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def continuation_id(self: rad.Node) -> int:
        return rad.NOINT
