from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry
from .ref.ref_common import _RefCommonRef

__all__ = ["RefpixRef"]


class RefpixRef_Meta(rad.ImpliedNodeMixin[_RefCommonRef], RefCommonRef[_RefCommonRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefpixRef

    @property
    @rad.field
    def reftype(self: rad.Node) -> RefTypeEntry:
        return RefTypeEntry.REFPIX


_RefPixRef: TypeAlias = RefpixRef_Meta | npt.NDArray[np.complex128]


class RefpixRef(rad.TaggedObjectNode[_RefPixRef], rad.ArrayFieldMixin[_RefPixRef]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/refpix-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/refpix-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/refpix-1.0.0"
            }
        )

    @property
    def primary_array_name(self) -> str:
        return "gamma"

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (32, 286721)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (32, 840)  # Chosen as the minimum size to do real testing

    @property
    @rad.field
    def meta(self: rad.Node) -> RefpixRef_Meta:
        return RefpixRef_Meta()

    @property
    @rad.field
    def gamma(self: rad.Node) -> npt.NDArray[np.complex128]:
        return np.zeros(self.array_shape, dtype=np.complex128)

    @property
    @rad.field
    def zeta(self: rad.Node) -> npt.NDArray[np.complex128]:
        return np.zeros(self.array_shape, dtype=np.complex128)

    @property
    @rad.field
    def alpha(self: rad.Node) -> npt.NDArray[np.complex128]:
        return np.zeros(self.array_shape, dtype=np.complex128)
