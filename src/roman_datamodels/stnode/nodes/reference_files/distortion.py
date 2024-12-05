from astropy import units as u
from astropy.modeling import Model
from astropy.modeling.models import Shift

from roman_datamodels.stnode import _core

from .ref import (
    RefCommonRef,
    RefOpticalElementRef,
)

__all__ = ["DistortionRef"]


class DistortionRef_Meta(_core.ImpliedNodeMixin, RefCommonRef, RefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return DistortionRef

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            *super(RefCommonRef, cls).asdf_required(),
            "input_units",
            "output_units",
        )

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "DISTORTION")

    @property
    def input_units(self) -> u.UnitBase:
        return self._get_node("input_units", lambda: u.pixel)

    @property
    def output_units(self) -> u.UnitBase:
        return self._get_node("output_units", lambda: u.arcsec)


class DistortionRef(_core.DataModelNode):
    """
    Distortion reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/distortion-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "coordinate_distortion_transform",
        )

    @property
    def array_shape(self) -> tuple[int]:
        raise NotImplementedError("array_shape is not implemented")

    @property
    def meta(self) -> DistortionRef_Meta:
        return self._get_node("meta", DistortionRef_Meta)

    @property
    def coordinate_distortion_transform(self) -> Model:
        return self._get_node("coordinate_distortion_transform", lambda: Shift(1) & Shift(2))
