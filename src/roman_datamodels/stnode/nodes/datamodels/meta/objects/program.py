from enum import Enum

from roman_datamodels.stnode import rad

__all__ = [
    "Program",
    "ProgramSubcategoryEntry",
]


class ProgramSubcategoryEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Program

    @classmethod
    def asdf_property_name(cls) -> str:
        return "subcategory"


class ProgramSubcategoryEntry(ProgramSubcategoryEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
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


class Program(rad.TaggedObjectNode):
    """
    Program information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/program-1.0.0"

    @rad.field
    def title(self) -> str:
        return self._get_node("title", lambda: rad.NOSTR)

    @rad.field
    def investigator_name(self) -> str:
        return self._get_node("investigator_name", lambda: rad.NOSTR)

    @rad.field
    def category(self) -> str:
        return self._get_node("category", lambda: rad.NOSTR)

    @rad.field
    def subcategory(self) -> ProgramSubcategoryEntry:
        return self._get_node("subcategory", lambda: ProgramSubcategoryEntry.NONE)

    @rad.field
    def science_category(self) -> str:
        return self._get_node("science_category", lambda: rad.NOSTR)

    @rad.field
    def continuation_id(self) -> int:
        return self._get_node("continuation_id", lambda: rad.NOINT)
