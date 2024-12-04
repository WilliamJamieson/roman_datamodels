from roman_datamodels.stnode import _core, _default

__all__ = ["Program"]


class Program(_core.TaggedObjectNode):
    """
    Program information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/program-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "title",
            "investigator_name",
            "category",
            "subcategory",
            "science_category",
            "continuation_id",
        )

    @property
    def title(self) -> str:
        return self._get_node("title", lambda: _default.NOSTR)

    @property
    def investigator_name(self) -> str:
        return self._get_node("investigator_name", lambda: _default.NOSTR)

    @property
    def category(self) -> str:
        return self._get_node("category", lambda: _default.NOSTR)

    @property
    def subcategory(self) -> str:
        return self._get_node("subcategory", lambda: "None")

    @property
    def science_category(self) -> str:
        return self._get_node("science_category", lambda: _default.NOSTR)

    @property
    def continuation_id(self) -> int:
        return self._get_node("continuation_id", lambda: _default.NOINT)
