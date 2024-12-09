from roman_datamodels.stnode import _default, rad

__all__ = ["VelocityAberration"]


class VelocityAberration(rad.TaggedObjectNode):
    """
    Velocity aberration information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/velocity_aberration-1.0.0"

    @rad.field
    def ra_reference(self) -> float:
        return self._get_node("ra_reference", lambda: _default.NONUM)

    @rad.field
    def dec_reference(self) -> float:
        return self._get_node("dec_reference", lambda: _default.NONUM)

    @rad.field
    def scale_factor(self) -> float:
        return self._get_node("scale_factor", lambda: 1.0)
