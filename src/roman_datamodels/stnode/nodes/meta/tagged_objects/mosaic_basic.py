from roman_datamodels.stnode import _core, _default

from ...enums import InstrumentNameEntry
from ..untagged_scalars import WfiOpticalElement

__all__ = ["MosaicBasic"]


class MosaicBasic(_core.TaggedObjectNode):
    """
    Basic mosaic metadata keywords
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_basic-1.0.0"

    @_core.rad_field
    def time_first_mjd(self) -> float:
        return self._get_node("time_first_mjd", lambda: _default.NONUM)

    @_core.rad_field
    def time_last_mjd(self) -> float:
        return self._get_node("time_last_mjd", lambda: _default.NONUM)

    @_core.rad_field
    def time_mean_mjd(self) -> float:
        return self._get_node("time_mean_mjd", lambda: _default.NONUM)

    @_core.rad_field
    def max_exposure_time(self) -> float:
        return self._get_node("max_exposure_time", lambda: _default.NONUM)

    @_core.rad_field
    def mean_exposure_time(self) -> float:
        return self._get_node("mean_exposure_time", lambda: _default.NONUM)

    @_core.rad_field
    def visit(self) -> int:
        return self._get_node("visit", lambda: _default.NOINT)

    @_core.rad_field
    def segment(self) -> int:
        return self._get_node("segment", lambda: _default.NOINT)

    @_core.rad_field
    def pass_(self) -> int:
        return self._get_node("pass", lambda: _default.NOINT)

    @_core.rad_field
    def program(self) -> int:
        return self._get_node("program", lambda: _default.NOINT)

    @_core.rad_field
    def survey(self) -> str:
        return self._get_node("survey", lambda: _default.NOSTR)

    @_core.rad_field
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)

    @_core.rad_field
    def instrument(self) -> InstrumentNameEntry:
        return self._get_node("instrument", lambda: InstrumentNameEntry.WFI)

    @_core.rad_field
    def location_name(self) -> str:
        return self._get_node("location_name", lambda: _default.NOSTR)

    @_core.rad_field
    def product_type(self) -> str:
        return self._get_node("product_type", lambda: _default.NOSTR)
