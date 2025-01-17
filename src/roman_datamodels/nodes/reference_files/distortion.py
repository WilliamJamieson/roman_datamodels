from types import MappingProxyType

from astropy.modeling import Model
from astropy.modeling.models import Shift

from roman_datamodels.stnode import rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry

__all__ = ["DistortionRef"]


class DistortionRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return DistortionRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.DISTORTION


class DistortionRef(rad.TaggedObjectNode):
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
        return Shift(1) & Shift(2)
