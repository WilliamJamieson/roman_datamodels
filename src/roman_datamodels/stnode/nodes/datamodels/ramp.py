import numpy as np

from roman_datamodels.stnode import rad

from .meta import (
    Common,
    L2CalStep,
)

__all__ = ["Ramp"]


class Ramp_Meta(rad.ImpliedNodeMixin, Common):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Ramp

    @rad.field
    def cal_step(self) -> L2CalStep:
        return self._get_node("cal_step", L2CalStep)


class Ramp(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Ramp schema
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/ramp-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ramp-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8, 8)

    @rad.field
    def meta(self) -> Ramp_Meta:
        return self._get_node("meta", Ramp_Meta)

    @rad.field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.full(self.array_shape, 1.0, dtype=np.float32))

    @rad.field
    def pixeldq(self) -> np.ndarray:
        return self._get_node("pixeldq", lambda: np.zeros(self.array_shape[1:], dtype=np.uint32))

    @rad.field
    def groupdq(self) -> np.ndarray:
        return self._get_node("groupdq", lambda: np.zeros(self.array_shape, dtype=np.uint8))

    @rad.field
    def err(self) -> np.ndarray:
        return self._get_node("err", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def amp33(self) -> np.ndarray:
        return self._get_node("amp33", lambda: np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16))

    @rad.field
    def border_ref_pix_left(self) -> np.ndarray:
        return self._get_node(
            "border_ref_pix_left", lambda: np.zeros((self.array_shape[0], self.array_shape[1], 4), dtype=np.float32)
        )

    @rad.field
    def border_ref_pix_right(self) -> np.ndarray:
        return self._get_node(
            "border_ref_pix_right", lambda: np.zeros((self.array_shape[0], self.array_shape[1], 4), dtype=np.float32)
        )

    @rad.field
    def border_ref_pix_top(self) -> np.ndarray:
        return self._get_node(
            "border_ref_pix_top", lambda: np.zeros((self.array_shape[0], 4, self.array_shape[2]), dtype=np.float32)
        )

    @rad.field
    def border_ref_pix_bottom(self) -> np.ndarray:
        return self._get_node(
            "border_ref_pix_bottom", lambda: np.zeros((self.array_shape[0], 4, self.array_shape[2]), dtype=np.float32)
        )

    @rad.field
    def dq_border_ref_pix_left(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_left", lambda: np.zeros((self.array_shape[1], 4), dtype=np.uint32))

    @rad.field
    def dq_border_ref_pix_right(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_right", lambda: np.zeros((self.array_shape[1], 4), dtype=np.uint32))

    @rad.field
    def dq_border_ref_pix_top(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_top", lambda: np.zeros((4, self.array_shape[2]), dtype=np.uint32))

    @rad.field
    def dq_border_ref_pix_bottom(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_bottom", lambda: np.zeros((4, self.array_shape[2]), dtype=np.uint32))
