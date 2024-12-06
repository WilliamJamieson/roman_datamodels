from roman_datamodels.stnode import _core

from .ref_common import RefCommonRef, RefCommonRef_Instrument
from .ref_optical_element import RefOpticalElementRef, RefOpticalElementRef_Instrument

__all__ = ["RefCommonRefOpticalElementRef"]


class RefCommonRefOpticalElementRef_Instrument(RefCommonRef_Instrument, RefOpticalElementRef_Instrument, _core.ImpliedNodeMixin):
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

    @property
    def instrument(self) -> RefCommonRefOpticalElementRef_Instrument:
        return self._get_node("instrument", RefCommonRefOpticalElementRef_Instrument)
