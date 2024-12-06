from roman_datamodels.stnode import _core, _default

__all__ = ["Observation"]


class Observation(_core.TaggedObjectNode):
    """
    Observation information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/observation-1.0.0"

    @_core.rad_field
    def observation_id(self) -> str:
        return self._get_node("observation_id", lambda: _default.NOSTR)

    @_core.rad_field
    def visit_id(self) -> str:
        return self._get_node("visit_id", lambda: _default.NOSTR)

    @_core.rad_field
    def program(self) -> int:
        return self._get_node("program", lambda: 1)

    @_core.rad_field
    def execution_plan(self) -> int:
        return self._get_node("execution_plan", lambda: 1)

    # Note cannot use "pass" as a property name due to reserved keyword
    @_core.rad_field
    def pass_(self) -> int:
        return self._get_node("pass", lambda: 1)

    @_core.rad_field
    def segment(self) -> int:
        return self._get_node("segment", lambda: 1)

    @_core.rad_field
    def observation(self) -> int:
        return self._get_node("observation", lambda: 1)

    @_core.rad_field
    def visit(self) -> int:
        return self._get_node("visit", lambda: 1)

    @_core.rad_field
    def visit_file_group(self) -> int:
        return self._get_node("visit_file_group", lambda: 1)

    @_core.rad_field
    def visit_file_sequence(self) -> int:
        return self._get_node("visit_file_sequence", lambda: 1)

    @_core.rad_field
    def visit_file_activity(self) -> str:
        return self._get_node("visit_file_activity", lambda: "01")

    @_core.rad_field
    def exposure(self) -> int:
        return self._get_node("exposure", lambda: 1)
