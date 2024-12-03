import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core

from .ref import RefCommonRef

__all__ = ["SaturationRef"]


class SaturationRefMeta(RefCommonRef):
    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "SATURATION")


class SaturationRef(_core.DataModelNode):
    """
    Saturation reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/saturation-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
            "dq",
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
        return (4096, 4096)

    @property
    def meta(self) -> SaturationRefMeta:
        return self._get_node("meta", SaturationRefMeta)

    @property
    def data(self) -> u.Quantity:
        return self._get_node("data", lambda: u.Quantity(np.zeros(self.array_shape, dtype=np.float32), u.DN, dtype=np.float32))

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", np.zeros(self.array_shape, dtype=np.uint32))
