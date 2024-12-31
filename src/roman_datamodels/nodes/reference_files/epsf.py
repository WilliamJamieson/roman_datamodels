from types import MappingProxyType

import numpy as np

from roman_datamodels.stnode import core, rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry

__all__ = ["EpsfRef"]


class EpsfRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return EpsfRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.EPSF

    @rad.field
    def oversample(self) -> int:
        return rad.NOINT

    @rad.field
    def spectral_type(self) -> core.LNode[str]:
        return core.LNode(["None"])

    @rad.field
    def defocus(self) -> core.LNode[int]:
        return core.LNode(list(range(1, 10)))

    @rad.field
    def pixel_x(self) -> core.LNode[float]:
        return core.LNode([float(i) for i in range(1, 10)])

    @rad.field
    def pixel_y(self) -> core.LNode[float]:
        return core.LNode([float(i) for i in range(1, 10)])


class EpsfRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    ePSF reference schema
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/epsf-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/epsf-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/epsf-1.0.0"
            }
        )

    @property
    def primary_array_name(self) -> str:
        return "psf"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (3, 6, 9, 361, 361)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (2, 2, 2, 2, 2)

    @rad.field
    def meta(self) -> EpsfRef_Meta:
        return EpsfRef_Meta()

    @rad.field
    def psf(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def extended_psf(self) -> np.ndarray:
        return np.zeros(self.array_shape[-2:], dtype=np.float32)
