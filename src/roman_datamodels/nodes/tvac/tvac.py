from types import MappingProxyType
from typing import TypeAlias

import numpy as np
from astropy.units import DN, Quantity  # type: ignore[attr-defined]

from roman_datamodels.stnode import rad

from .meta import (
    TvacCommon,
    TvacGroundtest,
)
from .meta.common import _TvacCommon

__all__ = ["Tvac", "Tvac_Meta"]


_Tvac_Meta: TypeAlias = _TvacCommon | TvacGroundtest


class Tvac_Meta(rad.ImpliedNodeMixin[_Tvac_Meta], TvacCommon[_Tvac_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Tvac

    @rad.field
    def groundtest(self) -> TvacGroundtest:
        return TvacGroundtest()


_Tvac: TypeAlias = Tvac_Meta | Quantity


class Tvac(rad.TaggedObjectNode[_Tvac], rad.ArrayFieldMixin[_Tvac]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {"asdf://stsci.edu/datamodels/roman/tags/tvac-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac-1.0.0"}
        )

    @property
    def default_array_shape(self) -> tuple[int, int, int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int, int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> Tvac_Meta:
        return Tvac_Meta()

    @rad.field
    def data(self) -> Quantity:
        return Quantity(np.zeros(self.array_shape, dtype=np.uint16), unit=DN, dtype=np.uint16)

    @rad.field
    def amp33(self) -> Quantity:
        return Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=DN, dtype=np.uint16)

    @rad.field
    def amp33_reset_reads(self) -> Quantity:
        return Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=DN, dtype=np.uint16)

    @rad.field
    def amp33_reference_read(self) -> Quantity:
        return Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=DN, dtype=np.uint16)

    @rad.field
    def guidewindow(self) -> Quantity:
        return Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=DN, dtype=np.uint16)

    @rad.field
    def reference_read(self) -> Quantity:
        return Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=DN, dtype=np.uint16)

    @rad.field
    def reset_reads(self) -> Quantity:
        return Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=DN, dtype=np.uint16)
