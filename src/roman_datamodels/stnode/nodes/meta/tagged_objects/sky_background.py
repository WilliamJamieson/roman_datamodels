from roman_datamodels.stnode import _core, _default

__all__ = ["SkyBackground"]


class SkyBackground(_core.TaggedObjectNode):
    """
    Sky Background Information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/sky_background-1.0.0"

    @_core.rad_field
    def level(self) -> float | None:
        return self._get_node("level", lambda: _default.NONUM)

    @_core.rad_field
    def method(self) -> str:
        return self._get_node("method", lambda: "None")

    @_core.rad_field
    def subtracted(self) -> bool:
        return self._get_node("subtracted", lambda: False)
