from roman_datamodels.stnode import rad

__all__ = ["Pointing"]


class Pointing(rad.TaggedObjectNode):
    """
    Spacecraft Pointing information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/pointing-1.0.0"

    @rad.field
    def ra_v1(self) -> float:
        return self._get_node("ra_v1", lambda: rad.NONUM)

    @rad.field
    def dec_v1(self) -> float:
        return self._get_node("dec_v1", lambda: rad.NONUM)

    @rad.field
    def pa_v3(self) -> float:
        return self._get_node("pa_v3", lambda: rad.NONUM)

    @rad.field
    def target_aperture(self) -> str:
        return self._get_node("target_aperture", lambda: rad.NOSTR)

    @rad.field
    def target_ra(self) -> float:
        return self._get_node("target_ra", lambda: rad.NONUM)

    @rad.field
    def target_dec(self) -> float:
        return self._get_node("target_dec", lambda: rad.NONUM)
