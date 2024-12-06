from roman_datamodels.stnode import _core, _default

__all__ = ["Rcs"]


class Rcs(_core.TaggedObjectNode):
    """
    Relative Calibration System Information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/rcs-1.0.0"

    @_core.rad_field
    def active(self) -> bool:
        return self._get_node("active", lambda: False)

    @_core.rad_field
    def electronics(self) -> str | None:
        return self._get_node("electronics", lambda: "A")

    @_core.rad_field
    def bank(self) -> str | None:
        return self._get_node("bank", lambda: "1")

    @_core.rad_field
    def led(self) -> str | None:
        return self._get_node("led", lambda: "1")

    @_core.rad_field
    def counts(self) -> int:
        return self._get_node("counts", lambda: _default.NOINT)
