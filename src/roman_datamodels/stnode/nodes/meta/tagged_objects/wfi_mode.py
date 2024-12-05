from typing import ClassVar

from roman_datamodels.stnode import _base, _core

from ..untagged_scalars import WfiDetector, WfiOpticalElement

__all__ = ["WfiMode"]


class WfiModeMixin(_base.AdditionalNodeMixin):
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


class WfiMode(WfiModeMixin, _core.TaggedObjectNode):
    """
    Roman WFI Instrument
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wfi_mode-1.0.0"

    @property
    def name(self) -> str:
        return self._get_node("name", lambda: "WFI")

    @property
    def detector(self) -> WfiDetector:
        return self._get_node("detector", WfiDetector.WFI01)

    @property
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", WfiOpticalElement.F158)
