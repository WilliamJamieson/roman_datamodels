from roman_datamodels.stnode import _default, rad

from ...enums import SkyBackgroundMethodEntry

__all__ = ["SkyBackground"]


class SkyBackground(rad.TaggedObjectNode):
    """
    Sky Background Information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/sky_background-1.0.0"

    @rad.rad_field
    def level(self) -> float | None:
        return self._get_node("level", lambda: _default.NONUM)

    @rad.rad_field
    def method(self) -> SkyBackgroundMethodEntry:
        return self._get_node("method", lambda: SkyBackgroundMethodEntry.NONE)

    @rad.rad_field
    def subtracted(self) -> bool:
        return self._get_node("subtracted", lambda: False)
