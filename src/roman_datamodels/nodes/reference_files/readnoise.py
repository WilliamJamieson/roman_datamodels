from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import (
    RefCommonRef,
    RefExposureTypeRef,
    RefTypeEntry,
)
from .ref.ref_common import _RefCommonRef
from .ref.ref_exposure_type import _RefExposureTypeRef

__all__ = ["ReadnoiseRef", "ReadnoiseRef_Meta"]


_ReadnoiseRef_Meta: TypeAlias = _RefCommonRef | _RefExposureTypeRef


class ReadnoiseRef_Meta(rad.ImpliedNodeMixin, RefCommonRef[_ReadnoiseRef_Meta], RefExposureTypeRef[_RefExposureTypeRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ReadnoiseRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.READNOISE


_Readnoiseref: TypeAlias = ReadnoiseRef_Meta | npt.NDArray[np.float32]


class ReadnoiseRef(rad.TaggedObjectNode[_Readnoiseref], rad.ArrayFieldMixin[_Readnoiseref]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/readnoise-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/readnoise-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/readnoise-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @rad.field
    def meta(self) -> ReadnoiseRef_Meta:
        return ReadnoiseRef_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)
