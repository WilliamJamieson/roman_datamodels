from astropy import units as u
from astropy.modeling import Model
from astropy.modeling.models import Shift

from roman_datamodels.stnode import _core

from .ref import (
    RefCommonRef,
    RefOpticalElementRef,
)

__all__ = ["DistortionRef"]


class DistortionRefMeta(RefCommonRef, RefOpticalElementRef):
    @property
    def required(self) -> tuple[str]:
        return (
            *super().required,
            *super(RefCommonRef, self).required,
            "input_units",
            "output_units",
        )

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "DISTORTION")

    @property
    def input_units(self) -> u.Unit:
        return self._get_node("input_units", lambda: u.pixel)

    @property
    def output_units(self) -> u.Unit:
        return self._get_node("output_units", lambda: u.arcsec)


class DistortionRef(_core.DataModelNode):
    """
    Distortion reference schema
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/distortion-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "coordinate_distortion_transform",
        )

    @property
    def array_shape(self) -> tuple[int]:
        raise NotImplementedError("array_shape is not implemented")

    @property
    def meta(self) -> DistortionRefMeta:
        return self._get_node("meta", DistortionRefMeta)

    @property
    def coordinate_distortion_transform(self) -> Model:
        return self._get_node("coordinate_distortion_transform", lambda: Shift(1) & Shift(2))
