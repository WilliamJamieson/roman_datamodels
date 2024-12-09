from roman_datamodels.stnode import _default, core, rad

from ...enums import ResampleWeightTypeEntry

__all__ = ["Resample"]


class Resample(rad.TaggedObjectNode):
    """
    Resample information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/resample-1.0.0"

    @rad.field
    def good_bits(self) -> str:
        return self._get_node("good_bits", lambda: "NA")

    @rad.field
    def pixel_scale_ratio(self) -> float:
        return self._get_node("pixel_scale_ratio", lambda: _default.NONUM)

    @rad.field
    def pixfrac(self) -> float:
        return self._get_node("pixfrac", lambda: _default.NONUM)

    @rad.field
    def pointings(self) -> int:
        return self._get_node("pointings", lambda: _default.NOINT)

    @rad.field
    def product_exposure_time(self) -> float:
        return self._get_node("product_exposure_time", lambda: _default.NONUM)

    @rad.field
    def members(self) -> core.LNode[str]:
        return self._get_node("members", lambda: core.LNode([]))

    @rad.field
    def weight_type(self) -> ResampleWeightTypeEntry:
        return self._get_node("weight_type", lambda: ResampleWeightTypeEntry.EXPTIME)
