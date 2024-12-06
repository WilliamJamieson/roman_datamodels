from roman_datamodels.stnode import _core, _default

__all__ = ["Program"]


class Program(_core.TaggedObjectNode):
    """
    Program information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/program-1.0.0"

    @_core.rad_field
    def title(self) -> str:
        return self._get_node("title", lambda: _default.NOSTR)

    @_core.rad_field
    def investigator_name(self) -> str:
        return self._get_node("investigator_name", lambda: _default.NOSTR)

    @_core.rad_field
    def category(self) -> str:
        return self._get_node("category", lambda: _default.NOSTR)

    @_core.rad_field
    def subcategory(self) -> str:
        return self._get_node("subcategory", lambda: "None")

    @_core.rad_field
    def science_category(self) -> str:
        return self._get_node("science_category", lambda: _default.NOSTR)

    @_core.rad_field
    def continuation_id(self) -> int:
        return self._get_node("continuation_id", lambda: _default.NOINT)
