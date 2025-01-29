from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .meta import (
    Common,
    L2CalStep,
)
from .meta.common import _Common

__all__ = ["Ramp", "Ramp_Meta"]


_Ramp_Meta: TypeAlias = _Common | L2CalStep


class Ramp_Meta(rad.ImpliedNodeMixin[_Ramp_Meta], Common[_Ramp_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Ramp

    @rad.field
    def cal_step(self) -> L2CalStep:
        return L2CalStep()


_Ramp: TypeAlias = Ramp_Meta | npt.NDArray[np.float32] | npt.NDArray[np.uint32] | npt.NDArray[np.uint8] | npt.NDArray[np.uint16]


class Ramp(rad.TaggedObjectNode[_Ramp], rad.ArrayFieldMixin[_Ramp]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/ramp-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {"asdf://stsci.edu/datamodels/roman/tags/ramp-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/ramp-1.0.0"}
        )

    @property
    def default_array_shape(self) -> tuple[int, int, int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int, int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> Ramp_Meta:
        return Ramp_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.full(self.array_shape, 1.0, dtype=np.float32)

    @rad.field
    def pixeldq(self) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape[1:], dtype=np.uint32)

    @rad.field
    def groupdq(self) -> npt.NDArray[np.uint8]:
        return np.zeros(self.array_shape, dtype=np.uint8)

    @rad.field
    def err(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def amp33(self) -> npt.NDArray[np.uint16]:
        return np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16)

    @rad.field
    def border_ref_pix_left(self) -> npt.NDArray[np.float32]:
        return np.zeros((self.array_shape[0], self.array_shape[1], 4), dtype=np.float32)

    @rad.field
    def border_ref_pix_right(self) -> npt.NDArray[np.float32]:
        return np.zeros((self.array_shape[0], self.array_shape[1], 4), dtype=np.float32)

    @rad.field
    def border_ref_pix_top(self) -> npt.NDArray[np.float32]:
        return np.zeros((self.array_shape[0], 4, self.array_shape[2]), dtype=np.float32)

    @rad.field
    def border_ref_pix_bottom(self) -> npt.NDArray[np.float32]:
        return np.zeros((self.array_shape[0], 4, self.array_shape[2]), dtype=np.float32)

    @rad.field
    def dq_border_ref_pix_left(self) -> npt.NDArray[np.uint32]:
        return np.zeros((self.array_shape[1], 4), dtype=np.uint32)

    @rad.field
    def dq_border_ref_pix_right(self) -> npt.NDArray[np.uint32]:
        return np.zeros((self.array_shape[1], 4), dtype=np.uint32)

    @rad.field
    def dq_border_ref_pix_top(self) -> npt.NDArray[np.uint32]:
        return np.zeros((4, self.array_shape[2]), dtype=np.uint32)

    @rad.field
    def dq_border_ref_pix_bottom(self) -> npt.NDArray[np.uint32]:
        return np.zeros((4, self.array_shape[2]), dtype=np.uint32)
