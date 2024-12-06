from roman_datamodels.stnode import _core, _default

__all__ = ["Pointing"]


class Pointing(_core.TaggedObjectNode):
    """
    Spacecraft Pointing information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/pointing-1.0.0"

    @_core.rad_field
    def ra_v1(self) -> float:
        return self._get_node("ra_v1", lambda: _default.NONUM)

    @_core.rad_field
    def dec_v1(self) -> float:
        return self._get_node("dec_v1", lambda: _default.NONUM)

    @_core.rad_field
    def pa_v3(self) -> float:
        return self._get_node("pa_v3", lambda: _default.NONUM)

    @_core.rad_field
    def target_aperture(self) -> str:
        return self._get_node("target_aperture", lambda: _default.NOSTR)

    @_core.rad_field
    def target_ra(self) -> float:
        return self._get_node("target_ra", lambda: _default.NONUM)

    @_core.rad_field
    def target_dec(self) -> float:
        return self._get_node("target_dec", lambda: _default.NONUM)
