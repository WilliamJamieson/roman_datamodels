from roman_datamodels.stnode import _base, _core, _default

__all__ = ["Resample"]


class Resample(_core.TaggedObjectNode):
    """
    Resample information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/resample-1.0.0"

    @property
    def good_bits(self) -> str:
        return self._get_node("good_bits", lambda: "NA")

    @property
    def pixel_scale_ratio(self) -> float:
        return self._get_node("pixel_scale_ratio", lambda: _default.NONUM)

    @property
    def pixfrac(self) -> float:
        return self._get_node("pixfrac", lambda: _default.NONUM)

    @property
    def pointings(self) -> int:
        return self._get_node("pointings", lambda: _default.NOINT)

    @property
    def product_exposure_time(self) -> float:
        return self._get_node("product_exposure_time", lambda: _default.NONUM)

    @property
    def members(self) -> _base.LNode[str]:
        return self._get_node("members", lambda: _base.LNode([]))

    @property
    def weight_type(self) -> str:
        return self._get_node("weight_type", lambda: "exptime")
