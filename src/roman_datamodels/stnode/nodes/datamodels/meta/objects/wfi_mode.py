from enum import Enum
from typing import ClassVar

from roman_datamodels.stnode import core, rad

from ..scalars import WfiDetector, WfiOpticalElement

__all__ = ["InstrumentNameEntry", "WfiMode"]


class InstrumentNameEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return WfiMode

    @classmethod
    def asdf_property_name(cls) -> str:
        return "name"


class InstrumentNameEntry(InstrumentNameEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for instrument name in schemas
    """

    WFI = "WFI"


class WfiModeMixin(core.AdditionalNodeMixin):
    """
    Extensions to the WfiMode class.
        Adds to indication properties
    """

    # Every optical element is a grating or a filter
    #   There are less gratings than filters so its easier to list out the
    #   gratings.
    _GRATING_OPTICAL_ELEMENTS: ClassVar = {"GRISM", "PRISM"}

    @property
    def filter(self):
        """
        Returns the filter if it is one, otherwise None
        """
        if self.optical_element in self._GRATING_OPTICAL_ELEMENTS:
            return None
        else:
            return self.optical_element

    @property
    def grating(self):
        """
        Returns the grating if it is one, otherwise None
        """
        if self.optical_element in self._GRATING_OPTICAL_ELEMENTS:
            return self.optical_element
        else:
            return None


class WfiMode(WfiModeMixin, rad.TaggedObjectNode):
    """
    Roman WFI Instrument
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wfi_mode-1.0.0"

    @rad.field
    def name(self) -> InstrumentNameEntry:
        return self._get_node("name", lambda: InstrumentNameEntry.WFI)

    @rad.field
    def detector(self) -> WfiDetector:
        return self._get_node("detector", lambda: WfiDetector.WFI01)

    @rad.field
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)
