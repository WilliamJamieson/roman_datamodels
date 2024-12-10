from astropy import units as u
from astropy.modeling import Model
from astropy.modeling.models import Shift

from roman_datamodels.stnode import rad

from ..enums import RefTypeEntry
from .ref import RefCommonRefOpticalElementRef

__all__ = ["DistortionRef"]


class DistortionRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return DistortionRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.DISTORTION)

    @rad.field
    def input_units(self) -> u.UnitBase:
        return self._get_node("input_units", lambda: u.pixel)

    @rad.field
    def output_units(self) -> u.UnitBase:
        return self._get_node("output_units", lambda: u.arcsec)


class DistortionRef(rad.TaggedObjectNode):
    """
    Distortion reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/distortion-1.0.0"

    @rad.field
    def meta(self) -> DistortionRef_Meta:
        return self._get_node("meta", DistortionRef_Meta)

    @rad.field
    def coordinate_distortion_transform(self) -> Model:
        return self._get_node("coordinate_distortion_transform", lambda: Shift(1) & Shift(2))
