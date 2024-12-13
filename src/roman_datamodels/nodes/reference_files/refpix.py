from types import MappingProxyType

import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry

__all__ = ["RefpixRef"]


class RefpixRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefpixRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.REFPIX)

    @rad.field
    def input_units(self) -> u.UnitBase:
        return self._get_node("input_units", lambda: u.DN)

    @rad.field
    def output_units(self) -> u.UnitBase:
        return self._get_node("output_units", lambda: u.DN)


class RefpixRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Reference pixel correction reference schema
    """

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
    def default_array_shape(self) -> tuple[int]:
        return (32, 286721)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (32, 840)  # Chosen as the minimum size to do real testing

    @rad.field
    def meta(self) -> RefpixRef_Meta:
        return self._get_node("meta", RefpixRef_Meta)

    @rad.field
    def gamma(self) -> np.ndarray:
        return self._get_node("gamma", lambda: np.zeros(self.array_shape, dtype=np.complex128))

    @rad.field
    def zeta(self) -> np.ndarray:
        return self._get_node("zeta", lambda: np.zeros(self.array_shape, dtype=np.complex128))

    @rad.field
    def alpha(self) -> np.ndarray:
        return self._get_node("alpha", lambda: np.zeros(self.array_shape, dtype=np.complex128))
