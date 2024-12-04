from roman_datamodels.stnode import _core, _default

__all__ = ["Observation"]


class Observation(_core.TaggedObjectNode):
    """
    Observation information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/observation-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "observation_id",
            "visit_id",
            "program",
            "execution_plan",
            "pass_",
            "segment",
            "observation",
            "visit",
            "visit_file_group",
            "visit_file_sequence",
            "visit_file_activity",
            "exposure",
        )

    @property
    def observation_id(self) -> str:
        return self._get_node("observation_id", lambda: _default.NOSTR)

    @property
    def visit_id(self) -> str:
        return self._get_node("visit_id", lambda: _default.NOSTR)

    @property
    def program(self) -> int:
        return self._get_node("program", lambda: 1)

    @property
    def execution_plan(self) -> int:
        return self._get_node("execution_plan", lambda: 1)

    # Note cannot use "pass" as a property name due to reserved keyword
    @property
    def pass_(self) -> int:
        return self._get_node("pass", lambda: 1)

    @property
    def segment(self) -> int:
        return self._get_node("segment", lambda: 1)

    @property
    def observation(self) -> int:
        return self._get_node("observation", lambda: 1)

    @property
    def visit(self) -> int:
        return self._get_node("visit", lambda: 1)

    @property
    def visit_file_group(self) -> int:
        return self._get_node("visit_file_group", lambda: 1)

    @property
    def visit_file_sequence(self) -> int:
        return self._get_node("visit_file_sequence", lambda: 1)

    @property
    def visit_file_activity(self) -> str:
        return self._get_node("visit_file_activity", lambda: "01")

    @property
    def exposure(self) -> int:
        return self._get_node("exposure", lambda: 1)
