"""
This module exists due to the mixing of ref_common and ref_optical_element sharing the same field,
instrument. This meant I had to be extra careful in creating the class for this for everything to
work properly. Since this is reused in multiple places, I decided to make it a separate class.
It is its own module because it is a weird special case.
"""

from typing import TypeAlias, TypeVar

from roman_datamodels.stnode import rad

from ...datamodels import WfiOpticalElement
from .ref_common import RefCommonRef, RefCommonRef_Instrument, _RefCommonRef, _RefCommonRef_Instrument
from .ref_optical_element import RefOpticalElementRef, RefOpticalElementRef_Instrument

__all__ = ["RefCommonRefOpticalElementRef", "RefCommonRefOpticalElementRef_Instrument"]

_T = TypeVar("_T")

_RefCommonRefOpticalElementRef_Instrument: TypeAlias = _RefCommonRef_Instrument | WfiOpticalElement


class RefCommonRefOpticalElementRef_Instrument(
    RefCommonRef_Instrument[_RefCommonRefOpticalElementRef_Instrument],
    RefOpticalElementRef_Instrument,
    rad.ImpliedNodeMixin,
):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefCommonRefOpticalElementRef

    @classmethod
    def asdf_required(cls) -> set[str]:
        return {
            *super().asdf_required(),
            *RefCommonRef_Instrument.asdf_required(),
            *RefOpticalElementRef_Instrument.asdf_required(),
        }

    @property
    def schema_required(self) -> set[str]:
        return self.asdf_required()


_RefCommonRefOpticalElementRef: TypeAlias = _RefCommonRef | RefCommonRefOpticalElementRef_Instrument


class RefCommonRefOpticalElementRef(
    RefCommonRef[_RefCommonRefOpticalElementRef | _T], RefOpticalElementRef[_RefCommonRefOpticalElementRef | _T]
):
    @classmethod
    def asdf_required(cls) -> set[str]:
        return {
            *super().asdf_required(),
            *RefCommonRef.asdf_required(),
            *RefOpticalElementRef.asdf_required(),
        }

    @rad.field
    def instrument(self) -> RefCommonRefOpticalElementRef_Instrument:  # type: ignore[override]
        return RefCommonRefOpticalElementRef_Instrument()
