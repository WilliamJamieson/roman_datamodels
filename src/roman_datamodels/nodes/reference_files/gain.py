from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry
from .ref.ref_common import _RefCommonRef

__all__ = ["GainRef", "GainRef_Meta"]


class GainRef_Meta(rad.ImpliedNodeMixin, RefCommonRef[_RefCommonRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return GainRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.GAIN


_GainRef: TypeAlias = GainRef_Meta | npt.NDArray[np.float32]


class GainRef(rad.TaggedObjectNode[_GainRef], rad.ArrayFieldMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/gain-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/gain-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/gain-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @rad.field
    def meta(self) -> GainRef_Meta:
        return GainRef_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)
