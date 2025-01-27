from types import MappingProxyType
from typing import TypeAlias, TypeVar, cast

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import core, rad

from ..datamodels import OPTICAL_ELEMENTS
from .ref import RefCommonRef, RefTypeEntry
from .ref.ref_common import _RefCommonRef

__all__ = ["ApcorrRef"]


_T = TypeVar("_T")


class ApcorrRef_Meta(rad.ImpliedNodeMixin[_RefCommonRef], RefCommonRef[_RefCommonRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.APCORR


_ApcorrRef_Data: TypeAlias = npt.NDArray[np.float64] | float | None


class ApcorrRef_Data(rad.ImpliedNodeMixin[_ApcorrRef_Data], rad.ObjectNode[_ApcorrRef_Data]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @property
    def array_shape(self) -> tuple[int, ...]:
        if self._has_node("ap_corrections") and self.ap_corrections is not None:
            array_shape: tuple[int, ...] = self.ap_corrections.shape
            return array_shape

        if self._has_node("ee_fractions") and self.ee_fractions is not None:
            array_shape = self.ee_fractions.shape
            return array_shape

        if self._has_node("ee_radii") and self.ee_radii is not None:
            array_shape = self.ee_radii.shape
            return array_shape

        return (10,)

    @rad.field
    def ap_corrections(self) -> npt.NDArray[np.float64] | None:
        return np.zeros(self.array_shape, dtype=np.float64)

    @rad.field
    def ee_fractions(self) -> npt.NDArray[np.float64] | None:
        return np.zeros(self.array_shape, dtype=np.float64)

    @rad.field
    def ee_radii(self) -> npt.NDArray[np.float64] | None:
        return np.zeros(self.array_shape, dtype=np.float64)

    @rad.field
    def sky_background_rin(self) -> float | None:
        return rad.NONUM

    @rad.field
    def sky_background_rout(self) -> float | None:
        return rad.NONUM


class ApcorrRef_Data_PatternNode(core.PatternDNode[_T], rad.ImpliedNodeMixin[_T]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @classmethod
    def asdf_implied_property_name(cls) -> str:
        return "data"

    @classmethod
    def asdf_key_pattern(cls) -> str:
        return "^(F062|F087|F106|F129|F146|F158|F184|F213|GRISM|PRISM|DARK)$"


_ApcorrRef: TypeAlias = ApcorrRef_Meta | ApcorrRef_Data_PatternNode[ApcorrRef_Data]


class ApcorrRef(rad.TaggedObjectNode[_ApcorrRef], rad.ArrayFieldMixin[_ApcorrRef]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/apcorr-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/apcorr-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/apcorr-1.0.0"
            }
        )

    @property
    def primary_array_shape(self) -> tuple[int, ...] | None:
        if self._has_node("data") and len(data := self._data["data"]) > 0:
            # MyPy is getting confused here this done correctly in this case
            return cast(tuple[int, ...], next(iter(data.values())).array_shape)  # type: ignore[union-attr]

        return None

    @property
    def default_array_shape(self) -> tuple[int]:
        return (10,)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (10,)

    @rad.field
    def meta(self) -> ApcorrRef_Meta:
        return ApcorrRef_Meta()

    @rad.field
    def data(self) -> ApcorrRef_Data_PatternNode[ApcorrRef_Data]:
        return ApcorrRef_Data_PatternNode({element: ApcorrRef_Data() for element in OPTICAL_ELEMENTS})
