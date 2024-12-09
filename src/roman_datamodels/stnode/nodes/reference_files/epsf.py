import numpy as np

from roman_datamodels.stnode import _default, core, rad

from ..enums import RefTypeEntry
from .ref import RefCommonRefOpticalElementRef

__all__ = ["EpsfRef"]


class EpsfRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return EpsfRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.EPSF)

    @rad.field
    def oversample(self) -> int:
        return self._get_node("oversample", lambda: _default.NOINT)

    @rad.field
    def spectral_type(self) -> core.LNode[str]:
        return self._get_node("spectral_type", lambda: core.LNode(["None"]))

    @rad.field
    def defocus(self) -> core.LNode[int]:
        return self._get_node("defocus", lambda: core.LNode(list(range(1, 10))))

    @rad.field
    def pixel_x(self) -> core.LNode[float]:
        return self._get_node("pixel_x", lambda: core.LNode([float(i) for i in range(1, 10)]))

    @rad.field
    def pixel_y(self) -> core.LNode[float]:
        return self._get_node("pixel_y", lambda: core.LNode([float(i) for i in range(1, 10)]))


class EpsfRef(rad.DataModelNode):
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
        return (3, 6, 9, 361, 361)

    @rad.field
    def meta(self) -> EpsfRef_Meta:
        return self._get_node("meta", EpsfRef_Meta)

    @rad.field
    def psf(self) -> np.ndarray:
        return self._get_node("psf", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def extended_psf(self) -> np.ndarray:
        return self._get_node("extended_psf", lambda: np.zeros(self.array_shape[-2:], dtype=np.float32))
