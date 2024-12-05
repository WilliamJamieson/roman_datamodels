from roman_datamodels.stnode import _core, _default

__all__ = ["Pointing"]


class Pointing(_core.TaggedObjectNode):
    """
    Spacecraft Pointing information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/pointing-1.0.0"

    @property
    def ra_v1(self) -> float:
        return self._get_node("ra_v1", lambda: _default.NONUM)

    @property
    def dec_v1(self) -> float:
        return self._get_node("dec_v1", lambda: _default.NONUM)

    @property
    def pa_v3(self) -> float:
        return self._get_node("pa_v3", lambda: _default.NONUM)

    @property
    def target_aperture(self) -> str:
        return self._get_node("target_aperture", lambda: _default.NOSTR)

    @property
    def target_ra(self) -> float:
        return self._get_node("target_ra", lambda: _default.NONUM)

    @property
    def target_dec(self) -> float:
        return self._get_node("target_dec", lambda: _default.NONUM)
