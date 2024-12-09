from roman_datamodels.stnode import _default, rad

from ...enums import WcsinfoApertureNameEntry, WcsinfoVparityEntry

__all__ = ["Wcsinfo"]


class Wcsinfo(rad.TaggedObjectNode):
    """
    Wcsinfo information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wcsinfo-1.0.0"

    @rad.field
    def aperture_name(self) -> WcsinfoApertureNameEntry:
        return self._get_node("aperture_name", lambda: WcsinfoApertureNameEntry.WFI01_FULL)

    @rad.field
    def pa_aperture(self) -> float:
        return self._get_node("pa_aperture", lambda: _default.NONUM)

    @rad.field
    def v2_ref(self) -> float:
        return self._get_node("v2_ref", lambda: _default.NONUM)

    @rad.field
    def v3_ref(self) -> float:
        return self._get_node("v3_ref", lambda: _default.NONUM)

    @rad.field
    def vparity(self) -> WcsinfoVparityEntry:
        return self._get_node("vparity", lambda: WcsinfoVparityEntry.REVERSED)

    @rad.field
    def v3yangle(self) -> float:
        return self._get_node("v3yangle", lambda: _default.NONUM)

    @rad.field
    def ra_ref(self) -> float:
        return self._get_node("ra_ref", lambda: _default.NONUM)

    @rad.field
    def dec_ref(self) -> float:
        return self._get_node("dec_ref", lambda: _default.NONUM)

    @rad.field
    def roll_ref(self) -> float:
        return self._get_node("roll_ref", lambda: _default.NONUM)

    @rad.field
    def s_region(self) -> str:
        return self._get_node("s_region", lambda: _default.NOSTR)
