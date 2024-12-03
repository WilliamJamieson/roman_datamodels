import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core

from .ref import RefCommonRef

__all__ = ["InverselinearityRef"]


class InverselinearityRefMeta(RefCommonRef):
    @property
    def required(self) -> tuple[str]:
        return (
            *super().required,
            "input_units",
            "output_units",
        )

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "INVERSELINEARITY")

    @property
    def input_units(self) -> u.Unit:
        return self._get_node("input_units", lambda: u.DN)

    @property
    def output_units(self) -> u.Unit:
        return self._get_node("output_units", lambda: u.DN)


class InverselinearityRef(_core.DataModelNode):
    """
    Inverse linearity correction reference schema
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/inverselinearity-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "coeffs",
            "dq",
        )

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("coeffs"):
            return self.coeffs.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (2, 4096, 4096)

    @property
    def meta(self) -> InverselinearityRefMeta:
        return self._coerce(InverselinearityRefMeta, self._get_node("meta", coerce=False), "meta")

    @property
    def coeffs(self) -> np.ndarray:
        return self._get_node("coeffs", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", np.zeros(self.array_shape[1:], dtype=np.uint32))
