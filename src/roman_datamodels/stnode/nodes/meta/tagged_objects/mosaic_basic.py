from roman_datamodels.stnode import rad

from ...enums import InstrumentNameEntry
from ..untagged_scalars import WfiOpticalElement

__all__ = ["MosaicBasic"]


class MosaicBasic(rad.TaggedObjectNode):
    """
    Basic mosaic metadata keywords
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_basic-1.0.0"

    @rad.field
    def time_first_mjd(self) -> float:
        return self._get_node("time_first_mjd", lambda: rad.NONUM)

    @rad.field
    def time_last_mjd(self) -> float:
        return self._get_node("time_last_mjd", lambda: rad.NONUM)

    @rad.field
    def time_mean_mjd(self) -> float:
        return self._get_node("time_mean_mjd", lambda: rad.NONUM)

    @rad.field
    def max_exposure_time(self) -> float:
        return self._get_node("max_exposure_time", lambda: rad.NONUM)

    @rad.field
    def mean_exposure_time(self) -> float:
        return self._get_node("mean_exposure_time", lambda: rad.NONUM)

    @rad.field
    def visit(self) -> int:
        return self._get_node("visit", lambda: rad.NOINT)

    @rad.field
    def segment(self) -> int:
        return self._get_node("segment", lambda: rad.NOINT)

    @rad.field
    def pass_(self) -> int:
        return self._get_node("pass", lambda: rad.NOINT)

    @rad.field
    def program(self) -> int:
        return self._get_node("program", lambda: rad.NOINT)

    @rad.field
    def survey(self) -> str:
        return self._get_node("survey", lambda: rad.NOSTR)

    @rad.field
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)

    @rad.field
    def instrument(self) -> InstrumentNameEntry:
        return self._get_node("instrument", lambda: InstrumentNameEntry.WFI)

    @rad.field
    def location_name(self) -> str:
        return self._get_node("location_name", lambda: rad.NOSTR)

    @rad.field
    def product_type(self) -> str:
        return self._get_node("product_type", lambda: rad.NOSTR)
