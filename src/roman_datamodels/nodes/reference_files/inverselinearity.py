from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry
from .ref.ref_common import _RefCommonRef

__all__ = ["InverselinearityRef", "InverselinearityRef_Meta"]


class InverselinearityRef_Meta(rad.ImpliedNodeMixin, RefCommonRef[_RefCommonRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return InverselinearityRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.INVERSELINEARITY


_InverselinearityRef: TypeAlias = InverselinearityRef_Meta | npt.NDArray[np.float32] | npt.NDArray[np.uint32]


class InverselinearityRef(rad.TaggedObjectNode[_InverselinearityRef], rad.ArrayFieldMixin[_InverselinearityRef]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/inverselinearity-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/inverselinearity-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/inverselinearity-1.0.0"
            }
        )

    @property
    def primary_array_name(self) -> str:
        return "coeffs"

    @property
    def default_array_shape(self) -> tuple[int, int, int]:
        return (2, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int, int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> InverselinearityRef_Meta:
        return InverselinearityRef_Meta()

    @rad.field
    def coeffs(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape[1:], dtype=np.uint32)
