from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

from ..scalars import WfiOpticalElement
from .wfi_mode import InstrumentNameEntry

__all__ = ["MosaicBasic"]


_MosaicBasic: TypeAlias = WfiOpticalElement | InstrumentNameEntry | float | int | str


class MosaicBasic(rad.TaggedObjectNode[_MosaicBasic]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/mosaic_basic-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/mosaic_basic-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/mosaic_basic-1.0.0"
            }
        )

    @property
    @rad.field
    def time_first_mjd(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def time_last_mjd(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def time_mean_mjd(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def max_exposure_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def mean_exposure_time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def visit(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def segment(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def pass_(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def program(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def survey(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def optical_element(self: rad.Node) -> WfiOpticalElement:
        return WfiOpticalElement.F158

    @property
    @rad.field
    def instrument(self: rad.Node) -> InstrumentNameEntry:
        return InstrumentNameEntry.WFI

    @property
    @rad.field
    def location_name(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def product_type(self: rad.Node) -> str:
        return rad.NOSTR
