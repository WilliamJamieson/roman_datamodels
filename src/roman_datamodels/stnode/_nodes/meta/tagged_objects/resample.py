from roman_datamodels.stnode import _core, _default

__all__ = ["Resample"]


class Resample(_core.TaggedObjectNode):
    """
    Resample information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/resample-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "good_bits",
            "members",
            "pixel_scale_ratio",
            "pixfrac",
            "weight_type",
        )

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
        return self._get_node("pointings", lambda: _default.NONUM)

    @property
    def product_exposure_time(self) -> float:
        return self._get_node("product_exposure_time", lambda: _default.NONUM)

    @property
    def members(self) -> list[str]:
        return self._get_node("members", lambda: [])

    @property
    def weight_type(self) -> str:
        return self._get_node("weight_type", lambda: "exptime")
