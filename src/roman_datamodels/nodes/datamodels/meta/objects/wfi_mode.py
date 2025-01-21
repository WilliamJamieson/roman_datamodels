from types import MappingProxyType
from typing import ClassVar, TypeAlias, TypeVar

from roman_datamodels.stnode import core, rad

from ..scalars import WfiDetector, WfiOpticalElement

__all__ = ["InstrumentNameEntry", "WfiMode"]

_T = TypeVar("_T")


class InstrumentNameEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return WfiMode

    @classmethod
    def asdf_property_name(cls) -> str:
        return "name"


class InstrumentNameEntry(InstrumentNameEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for instrument name in schemas
    """

    WFI = "WFI"


class WfiModeMixin(core.AdditionalNodeMixin[_T]):
    """
    Extensions to the WfiMode class.
        Adds to indication properties
    """

    # Every optical element is a grating or a filter
    #   There are less gratings than filters so its easier to list out the
    #   gratings.
    _GRATING_OPTICAL_ELEMENTS: ClassVar = {"GRISM", "PRISM"}

    @property
    def filter(self) -> WfiOpticalElement | None:
        """
        Returns the filter if it is one, otherwise None
        """
        # I would add this as an abstract property here, but for some
        # reason that I can't figure out, it nukes defining it in the sub class
        element: WfiOpticalElement = self.optical_element  # type: ignore[assignment]

        if element in self._GRATING_OPTICAL_ELEMENTS:
            return None
        else:
            return element

    @property
    def grating(self) -> WfiOpticalElement | None:
        """
        Returns the grating if it is one, otherwise None
        """
        # I would add this as an abstract property here, but for some
        # reason that I can't figure out, it nukes defining it in the sub class
        element: WfiOpticalElement = self.optical_element  # type: ignore[assignment]

        if element in self._GRATING_OPTICAL_ELEMENTS:
            return element
        else:
            return None


_WfiMode: TypeAlias = InstrumentNameEntry | WfiDetector | WfiOpticalElement


class WfiMode(WfiModeMixin[_WfiMode], rad.TaggedObjectNode[_WfiMode]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/wfi_mode-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/wfi_mode-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/wfi_mode-1.0.0",
            }
        )

    @property
    @rad.field
    def name(self: rad.Node) -> InstrumentNameEntry:
        return InstrumentNameEntry.WFI

    @property
    @rad.field
    def detector(self: rad.Node) -> WfiDetector:
        return WfiDetector.WFI01

    @property
    @rad.field
    def optical_element(self: rad.Node) -> WfiOpticalElement:
        return WfiOpticalElement.F158
