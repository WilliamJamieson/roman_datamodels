from roman_datamodels.stnode import _default, rad

from ...enums import ProgramSubcategoryEntry

__all__ = ["Program"]


class Program(rad.TaggedObjectNode):
    """
    Program information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/program-1.0.0"

    @rad.rad_field
    def title(self) -> str:
        return self._get_node("title", lambda: _default.NOSTR)

    @rad.rad_field
    def investigator_name(self) -> str:
        return self._get_node("investigator_name", lambda: _default.NOSTR)

    @rad.rad_field
    def category(self) -> str:
        return self._get_node("category", lambda: _default.NOSTR)

    @rad.rad_field
    def subcategory(self) -> ProgramSubcategoryEntry:
        return self._get_node("subcategory", lambda: ProgramSubcategoryEntry.NONE)

    @rad.rad_field
    def science_category(self) -> str:
        return self._get_node("science_category", lambda: _default.NOSTR)

    @rad.rad_field
    def continuation_id(self) -> int:
        return self._get_node("continuation_id", lambda: _default.NOINT)
