from types import MappingProxyType
from typing import TypeAlias

import numpy as np
from astropy.units import DN, Quantity  # type: ignore[attr-defined]

from roman_datamodels.stnode import rad

from .meta import (
    FpsCommon,
    FpsGroundtest,
)
from .meta.common import _FpsCommon

__all__ = ["Fps", "Fps_Meta"]


_Fps_Meta: TypeAlias = _FpsCommon | FpsGroundtest


class Fps_Meta(rad.ImpliedNodeMixin, FpsCommon[_Fps_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Fps

    @rad.field
    def groundtest(self) -> FpsGroundtest:
        return FpsGroundtest()


_Fps: TypeAlias = Fps_Meta | Quantity


class Fps(rad.TaggedObjectNode[_Fps], rad.ArrayFieldMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {"asdf://stsci.edu/datamodels/roman/tags/fps-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps-1.0.0"}
        )

    @property
    def default_array_shape(self) -> tuple[int, int, int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int, int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> Fps_Meta:
        return Fps_Meta()

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
