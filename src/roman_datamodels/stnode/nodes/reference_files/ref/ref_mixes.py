"""
This module exists due to the mixing of ref_common and ref_optical_element sharing the same field,
instrument. This meant I had to be extra careful in creating the class for this for everything to
work properly. Since this is reused in multiple places, I decided to make it a separate class.
It is its own module because it is a weird special case.
"""

from roman_datamodels.stnode import rad

from .ref_common import RefCommonRef, RefCommonRef_Instrument
from .ref_optical_element import RefOpticalElementRef, RefOpticalElementRef_Instrument

__all__ = ["RefCommonRefOpticalElementRef"]


class RefCommonRefOpticalElementRef_Instrument(RefCommonRef_Instrument, RefOpticalElementRef_Instrument, rad.ImpliedNodeMixin):
    @classmethod
    def asdf_implied_by(cls):
        return RefCommonRefOpticalElementRef

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return {
            *super().asdf_required(),
            *RefCommonRef_Instrument.asdf_required(),
            *RefOpticalElementRef_Instrument.asdf_required(),
        }


class RefCommonRefOpticalElementRef(RefCommonRef, RefOpticalElementRef):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return {
            *super().asdf_required(),
            *RefCommonRef.asdf_required(),
            *RefOpticalElementRef.asdf_required(),
        }

    @rad.field
    def instrument(self) -> RefCommonRefOpticalElementRef_Instrument:
        return self._get_node("instrument", RefCommonRefOpticalElementRef_Instrument)
