from types import MappingProxyType

import numpy as np

from roman_datamodels.stnode import core, rad

from ..datamodels import OPTICAL_ELEMENTS
from .ref import RefCommonRef, RefTypeEntry

__all__ = ["ApcorrRef"]


class ApcorrRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.APCORR


class ApcorrRef_Data(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @property
    def array_shape(self) -> tuple[int]:
        if self._has_node("ap_corrections"):
            return self.ap_corrections.shape

        if self._has_node("ee_fractions"):
            return self.ee_fractions.shape

        if self._has_node("ee_radii"):
            return self.ee_radii.shape

        return (10,)

    @rad.field
    def ap_corrections(self) -> np.ndarray | None:
        return np.zeros(self.array_shape, dtype=np.float64)

    @rad.field
    def ee_fractions(self) -> np.ndarray | None:
        return np.zeros(self.array_shape, dtype=np.float64)

    @rad.field
    def ee_radii(self) -> np.ndarray | None:
        return np.zeros(self.array_shape, dtype=np.float64)

    @rad.field
    def sky_background_rin(self) -> float | None:
        return rad.NONUM

    @rad.field
    def sky_background_rout(self) -> float | None:
        return rad.NONUM


class ApcorrRef_Data_PatternNode(core.PatternDNode, rad.ImpliedNodeMixin):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @classmethod
    def asdf_implied_property_name(cls) -> str:
        return "data"

    @classmethod
    def asdf_key_pattern(cls):
        return "^(F062|F087|F106|F129|F146|F158|F184|F213|GRISM|PRISM|DARK)$"


class ApcorrRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Aperture correction reference schema
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/apcorr-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/apcorr-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/apcorr-1.0.0"
            }
        )

    @property
    def primary_array_shape(self) -> tuple[int]:
        if self._has_node("data") and len(data := self._data["data"]) > 0:
            return next(iter(data.values())).array_shape

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
    def data(self) -> ApcorrRef_Data_PatternNode[str, ApcorrRef_Data]:
        return ApcorrRef_Data_PatternNode({element: ApcorrRef_Data() for element in OPTICAL_ELEMENTS})
