from roman_datamodels.stnode import _core, _default

from ..untagged_scalars import WfiOpticalElement

__all__ = ["MosaicBasic"]


class MosaicBasic(_core.TaggedObjectNode):
    """
    Basic mosaic metadata keywords
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_basic-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "time_first_mjd",
            "time_last_mjd",
            "time_mean_mjd",
            "max_exposure_time",
            "mean_exposure_time",
            "visit",
            "segment",
            "pass",
            "program",
            "survey",
            "optical_element",
            "instrument",
            "location_name",
            "product_type",
        )

    @property
    def time_first_mjd(self) -> float:
        return self._get_node("time_first_mjd", lambda: _default.NONUM)

    @property
    def time_last_mjd(self) -> float:
        return self._get_node("time_last_mjd", lambda: _default.NONUM)

    @property
    def time_mean_mjd(self) -> float:
        return self._get_node("time_mean_mjd", lambda: _default.NONUM)

    @property
    def max_exposure_time(self) -> float:
        return self._get_node("max_exposure_time", lambda: _default.NONUM)

    @property
    def mean_exposure_time(self) -> float:
        return self._get_node("mean_exposure_time", lambda: _default.NONUM)

    @property
    def visit(self) -> int:
        return self._get_node("visit", lambda: _default.NONUM)

    @property
    def segment(self) -> int:
        return self._get_node("segment", lambda: _default.NONUM)

    @property
    def pass_(self) -> int:
        return self._get_node("pass", lambda: _default.NONUM)

    @property
    def program(self) -> str:
        return self._get_node("program", lambda: _default.NOSTR)

    @property
    def survey(self) -> str:
        return self._get_node("survey", lambda: _default.NOSTR)

    @property
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", WfiOpticalElement.F158)

    @property
    def instrument(self) -> str:
        return self._get_node("instrument", lambda: "WFI")

    @property
    def location_name(self) -> str:
        return self._get_node("location_name", lambda: _default.NOSTR)

    @property
    def product_type(self) -> str:
        return self._get_node("product_type", lambda: _default.NOSTR)
