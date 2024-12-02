from roman_datamodels.stnode import _core, _default

__all__ = ["Rcs"]


class Rcs(_core.TaggedObjectNode):
    """
    Relative Calibration System Information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/rcs-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "active",
            "electronics",
            "bank",
            "led",
            "counts",
        )

    @property
    def active(self) -> bool:
        return self._get_node("active", lambda: False)

    @property
    def electronics(self) -> str | None:
        return self._get_node("electronics", lambda: "A")

    @property
    def bank(self) -> str | None:
        return self._get_node("bank", lambda: "1")

    @property
    def led(self) -> str | None:
        return self._get_node("led", lambda: "1")

    @property
    def counts(self) -> int:
        return self._get_node("counts", lambda: _default.NONUM)
