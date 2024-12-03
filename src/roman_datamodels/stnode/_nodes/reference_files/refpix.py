import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core

from .ref import RefCommonRef

__all__ = ["RefpixRef"]


class RefpixRefMeta(RefCommonRef):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "input_units",
            "output_units",
        )

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "REFPIX")

    @property
    def input_units(self) -> u.Unit:
        return self._get_node("input_units", lambda: u.DN)

    @property
    def output_units(self) -> u.Unit:
        return self._get_node("output_units", lambda: u.DN)


class RefpixRef(_core.DataModelNode):
    """
    Reference pixel correction reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/refpix-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "gamma",
            "zeta",
            "alpha",
        )

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("gamma"):
            return self.gamma.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (32, 286721)

    @property
    def meta(self) -> RefpixRefMeta:
        return self._get_node("meta", RefpixRefMeta)

    @property
    def gamma(self) -> np.ndarray:
        return self._get_node("gamma", lambda: np.zeros(self.array_shape, dtype=np.complex128))

    @property
    def zeta(self) -> np.ndarray:
        return self._get_node("zeta", lambda: np.zeros(self.array_shape, dtype=np.complex128))

    @property
    def alpha(self) -> np.ndarray:
        return self._get_node("alpha", lambda: np.zeros(self.array_shape, dtype=np.complex128))
