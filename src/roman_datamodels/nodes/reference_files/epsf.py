from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import core, rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry
from .ref.ref_mixes import _RefCommonRefOpticalElementRef

__all__ = ["EpsfRef"]


class EpsfRef_Meta(  # type: ignore[misc]
    rad.ImpliedNodeMixin[_RefCommonRefOpticalElementRef], RefCommonRefOpticalElementRef[_RefCommonRefOpticalElementRef]
):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return EpsfRef

    @property
    @rad.field
    def reftype(self: rad.Node) -> RefTypeEntry:
        return RefTypeEntry.EPSF

    @property
    @rad.field
    def oversample(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def spectral_type(self: rad.Node) -> core.LNode[str]:
        return core.LNode(["None"])

    @property
    @rad.field
    def defocus(self: rad.Node) -> core.LNode[int]:
        return core.LNode(list(range(1, 10)))

    @property
    @rad.field
    def pixel_x(self: rad.Node) -> core.LNode[float]:
        return core.LNode([float(i) for i in range(1, 10)])

    @property
    @rad.field
    def pixel_y(self: rad.Node) -> core.LNode[float]:
        return core.LNode([float(i) for i in range(1, 10)])


_EpsfRef: TypeAlias = EpsfRef_Meta | npt.NDArray[np.float32]


class EpsfRef(rad.TaggedObjectNode[_EpsfRef], rad.ArrayFieldMixin[_EpsfRef]):
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
    def default_array_shape(self) -> tuple[int, int, int, int, int]:
        return (3, 6, 9, 361, 361)

    @property
    def testing_array_shape(self) -> tuple[int, int, int, int, int]:
        return (2, 2, 2, 2, 2)

    @property
    @rad.field
    def meta(self: rad.Node) -> EpsfRef_Meta:
        return EpsfRef_Meta()

    @property
    @rad.field
    def psf(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def extended_psf(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape[-2:], dtype=np.float32)
