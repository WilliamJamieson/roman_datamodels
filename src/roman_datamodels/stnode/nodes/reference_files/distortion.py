from astropy import units as u
from astropy.modeling import Model
from astropy.modeling.models import Shift

from roman_datamodels.stnode import _core

from .ref import RefCommonRefOpticalElementRef

__all__ = ["DistortionRef"]


class DistortionRef_Meta(_core.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return DistortionRef

    @_core.rad_field
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "DISTORTION")

    @_core.rad_field
    def input_units(self) -> u.UnitBase:
        return self._get_node("input_units", lambda: u.pixel)

    @_core.rad_field
    def output_units(self) -> u.UnitBase:
        return self._get_node("output_units", lambda: u.arcsec)


class DistortionRef(_core.DataModelNode):
    """
    Distortion reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/distortion-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        raise NotImplementedError("array_shape is not implemented")

    @_core.rad_field
    def meta(self) -> DistortionRef_Meta:
        return self._get_node("meta", DistortionRef_Meta)

    @_core.rad_field
    def coordinate_distortion_transform(self) -> Model:
        return self._get_node("coordinate_distortion_transform", lambda: Shift(1) & Shift(2))
