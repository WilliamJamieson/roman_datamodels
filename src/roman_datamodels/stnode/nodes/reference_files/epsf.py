import numpy as np

from roman_datamodels.stnode import _base, _core, _default

from .ref import (
    RefCommonRef,
    RefOpticalElementRef,
)

__all__ = ["EpsfRef"]


class EpsfRef_Meta(_core.ImpliedNodeMixin, RefCommonRef, RefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return EpsfRef

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "EPSF")

    @property
    def oversample(self) -> int:
        return self._get_node("oversample", lambda: _default.NOINT)

    @property
    def spectral_type(self) -> _base.LNode[str]:
        return self._get_node("spectral_type", lambda: _base.LNode(["None"]))

    @property
    def defocus(self) -> _base.LNode[int]:
        return self._get_node("defocus", lambda: _base.LNode(list(range(1, 10))))

    @property
    def pixel_x(self) -> _base.LNode[float]:
        return self._get_node("pixel_x", lambda: _base.LNode([float(i) for i in range(1, 10)]))

    @property
    def pixel_y(self) -> _base.LNode[float]:
        return self._get_node("pixel_y", lambda: _base.LNode([float(i) for i in range(1, 10)]))


class EpsfRef(_core.DataModelNode):
    """
    ePSF reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/epsf-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("psf"):
            return self.psf.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (2, 4096, 4096)

    @property
    def meta(self) -> EpsfRef_Meta:
        return self._get_node("meta", EpsfRef_Meta)

    @property
    def psf(self) -> np.ndarray:
        return self._get_node("psf", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def extended_psf(self) -> np.ndarray:
        return self._get_node("extended_psf", lambda: np.zeros(self.array_shape[-2:], dtype=np.float32))
