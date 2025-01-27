from types import MappingProxyType
from typing import TypeAlias

from astropy.modeling import Model
from astropy.modeling.models import Shift

from roman_datamodels.stnode import rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry
from .ref.ref_mixes import _RefCommonRefOpticalElementRef

__all__ = ["DistortionRef"]


class DistortionRef_Meta(  # type: ignore[misc]
    rad.ImpliedNodeMixin[_RefCommonRefOpticalElementRef], RefCommonRefOpticalElementRef[_RefCommonRefOpticalElementRef]
):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return DistortionRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.DISTORTION


_Distortion_Ref: TypeAlias = DistortionRef_Meta | Model


class DistortionRef(rad.TaggedObjectNode[_Distortion_Ref]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/distortion-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/distortion-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/distortion-1.0.0"
            }
        )

    @rad.field
    def meta(self) -> DistortionRef_Meta:
        return DistortionRef_Meta()

    @rad.field
    def coordinate_distortion_transform(self) -> Model:
        # Astropy has not implemented type hints for modeling so MyPy will complain about this
        # until they do.
        return Shift(1) & Shift(2)  # type: ignore[no-any-return, no-untyped-call, operator]
