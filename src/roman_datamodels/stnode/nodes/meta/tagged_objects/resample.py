from roman_datamodels.stnode import _base, _core, _default

from ...enums import ResampleWeightTypeEntry

__all__ = ["Resample"]


class Resample(_core.TaggedObjectNode):
    """
    Resample information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/resample-1.0.0"

    @_core.rad_field
    def good_bits(self) -> str:
        return self._get_node("good_bits", lambda: "NA")

    @_core.rad_field
    def pixel_scale_ratio(self) -> float:
        return self._get_node("pixel_scale_ratio", lambda: _default.NONUM)

    @_core.rad_field
    def pixfrac(self) -> float:
        return self._get_node("pixfrac", lambda: _default.NONUM)

    @_core.rad_field
    def pointings(self) -> int:
        return self._get_node("pointings", lambda: _default.NOINT)

    @_core.rad_field
    def product_exposure_time(self) -> float:
        return self._get_node("product_exposure_time", lambda: _default.NONUM)

    @_core.rad_field
    def members(self) -> _base.LNode[str]:
        return self._get_node("members", lambda: _base.LNode([]))

    @_core.rad_field
    def weight_type(self) -> ResampleWeightTypeEntry:
        return self._get_node("weight_type", lambda: ResampleWeightTypeEntry.EXPTIME)
