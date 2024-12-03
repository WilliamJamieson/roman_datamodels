import numpy as np

from roman_datamodels.stnode import _core

from ..meta import (
    Common,
    L2CalStep,
)

__all__ = ["Ramp"]


class Ramp_Meta(Common):
    @property
    def cal_step(self) -> L2CalStep:
        return self._get_node("cal_step", L2CalStep)


class Ramp(_core.DataModelNode):
    """
    Ramp schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ramp-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
            "pixeldq",
            "groupdq",
            "err",
            "amp33",
            "border_ref_pix_left",
            "border_ref_pix_right",
            "border_ref_pix_top",
            "border_ref_pix_bottom",
            "dq_border_ref_pix_left",
            "dq_border_ref_pix_right",
            "dq_border_ref_pix_top",
            "dq_border_ref_pix_bottom",
        )

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("data"):
            return self.data.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (8, 4096, 4096)

    @property
    def meta(self) -> Ramp_Meta:
        return self._get_node("meta", Ramp_Meta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", np.full(self.array_shape, 1.0, dtype=np.float32))

    @property
    def pixeldq(self) -> np.ndarray:
        return self._get_node("pixeldq", np.zeros(self.array_shape[1:], dtype=np.uint32))

    @property
    def groupdq(self) -> np.ndarray:
        return self._get_node("groupdq", np.zeros(self.array_shape, dtype=np.uint8))

    @property
    def err(self) -> np.ndarray:
        return self._get_node("err", np.zeros(self.array_shape, dtype=np.float32))

    @property
    def amp33(self) -> np.ndarray:
        return self._get_node("amp33", np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16))

    @property
    def border_ref_pix_left(self) -> np.ndarray:
        return self._get_node("border_ref_pix_left", np.zeros((self.array_shape[0], self.array_shape[1], 4), dtype=np.float32))

    @property
    def border_ref_pix_right(self) -> np.ndarray:
        return self._get_node("border_ref_pix_right", np.zeros((self.array_shape[0], self.array_shape[1], 4), dtype=np.float32))

    @property
    def border_ref_pix_top(self) -> np.ndarray:
        return self._get_node("border_ref_pix_top", np.zeros((self.array_shape[0], 4, self.array_shape[2]), dtype=np.float32))

    @property
    def border_ref_pix_bottom(self) -> np.ndarray:
        return self._get_node("border_ref_pix_bottom", np.zeros((self.array_shape[0], 4, self.array_shape[2]), dtype=np.float32))

    @property
    def dq_border_ref_pix_left(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_left", np.zeros((self.array_shape[1], 4), dtype=np.uint32))

    @property
    def dq_border_ref_pix_right(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_right", np.zeros((self.array_shape[1], 4), dtype=np.uint32))

    @property
    def dq_border_ref_pix_top(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_top", np.zeros((4, self.array_shape[2]), dtype=np.uint32))

    @property
    def dq_border_ref_pix_bottom(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_bottom", np.zeros((4, self.array_shape[2]), dtype=np.uint32))
