import numpy as np

from roman_datamodels.stnode import _core, _default

from .ref import (
    RefCommonRef,
    RefOpticalElementRef,
)

__all__ = ["EpsfRef"]


class EpsfRef_Meta(RefCommonRef, RefOpticalElementRef):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            *super(RefCommonRef, cls).asdf_required(),
            "pixel_x",
            "pixel_y",
        )

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "EPSF")

    @property
    def oversample(self) -> int:
        return self._get_node("oversample", lambda: _default.NONUM)

    @property
    def spectral_type(self) -> list[str]:
        return self._get_node("spectral_type", lambda: ["None"])

    @property
    def defocus(self) -> list[int]:
        return self._get_node("defocus", lambda: np.arange(1, 10).tolist())

    @property
    def pixel_x(self) -> list[float]:
        return self._get_node("pixel_x", lambda: np.arange(1, 10, dtype=np.float32).tolist())

    @property
    def pixel_y(self) -> list[float]:
        return self._get_node("pixel_y", lambda: np.arange(1, 10, dtype=np.float32).tolist())


class EpsfRef(_core.DataModelNode):
    """
    ePSF reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/epsf-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "psf",
        )

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
        return self._coerce(EpsfRef_Meta, self._get_node("meta", coerce=False), "meta")

    @property
    def psf(self) -> np.ndarray:
        return self._get_node("psf", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def extended_psf(self) -> np.ndarray:
        return self._get_node("extended_psf", lambda: np.zeros(self.array_shape[-2:], dtype=np.float32))
