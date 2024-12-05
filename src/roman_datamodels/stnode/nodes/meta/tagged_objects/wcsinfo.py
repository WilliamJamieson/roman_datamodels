from roman_datamodels.stnode import _core, _default

__all__ = ["Wcsinfo"]


class Wcsinfo(_core.TaggedObjectNode):
    """
    Wcsinfo information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wcsinfo-1.0.0"

    @property
    def aperture_name(self) -> str:
        return self._get_node("aperture_name", lambda: "WFI01_FULL")

    @property
    def pa_aperture(self) -> float:
        return self._get_node("pa_aperture", lambda: _default.NONUM)

    @property
    def v2_ref(self) -> float:
        return self._get_node("v2_ref", lambda: _default.NONUM)

    @property
    def v3_ref(self) -> float:
        return self._get_node("v3_ref", lambda: _default.NONUM)

    @property
    def vparity(self) -> int:
        return self._get_node("vparity", lambda: -1)

    @property
    def v3yangle(self) -> float:
        return self._get_node("v3yangle", lambda: _default.NONUM)

    @property
    def ra_ref(self) -> float:
        return self._get_node("ra_ref", lambda: _default.NONUM)

    @property
    def dec_ref(self) -> float:
        return self._get_node("dec_ref", lambda: _default.NONUM)

    @property
    def roll_ref(self) -> float:
        return self._get_node("roll_ref", lambda: _default.NONUM)

    @property
    def s_region(self) -> str:
        return self._get_node("s_region", lambda: _default.NOSTR)
