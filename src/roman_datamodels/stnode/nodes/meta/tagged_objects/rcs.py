from roman_datamodels.stnode import _core, _default

from ...enums import RcsBankEntry, RcsElectronicsEntry, RcsLedEntry

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
    def electronics(self) -> RcsElectronicsEntry | None:
        return self._get_node("electronics", lambda: RcsElectronicsEntry.A)

    @_core.rad_field
    def bank(self) -> RcsBankEntry | None:
        return self._get_node("bank", lambda: RcsBankEntry.ONE)

    @_core.rad_field
    def led(self) -> RcsLedEntry | None:
        return self._get_node("led", lambda: RcsLedEntry.ONE)

    @_core.rad_field
    def counts(self) -> int:
        return self._get_node("counts", lambda: _default.NOINT)
