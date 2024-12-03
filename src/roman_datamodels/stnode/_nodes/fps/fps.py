import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core

from .meta import (
    FpsCommon,
    FpsGroundtest,
)

__all__ = ["Fps"]


class Fps_Meta(FpsCommon):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "groundtest",
        )

    @property
    def groundtest(self) -> FpsGroundtest:
        return self._get_node("groundtest", FpsGroundtest)


class Fps(_core.DataModelNode):
    """
    FPS test data
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
            "amp33",
            "guidewindow",
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
    def meta(self) -> Fps_Meta:
        return self._get_node("meta", Fps_Meta)

    @property
    def data(self) -> u.Quantity:
        return self._get_node("data", u.Quantity(np.zeros(self.array_shape, dtype=np.uint16), unit=u.DN, dtype=np.uint16))

    @property
    def amp33(self) -> u.Quantity:
        return self._get_node(
            "amp33",
            u.Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16),
        )

    @property
    def amp33_reset_reads(self) -> u.Quantity:
        return self._get_node(
            "amp33_reset_reads",
            u.Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16),
        )

    @property
    def amp33_reference_read(self) -> u.Quantity:
        return self._get_node(
            "amp33_reference_read",
            u.Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16),
        )

    @property
    def guidewindow(self) -> u.Quantity:
        return self._get_node(
            "guidewindow",
            u.Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16),
        )

    @property
    def reference_read(self) -> u.Quantity:
        return self._get_node(
            "reference_read",
            u.Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16),
        )

    @property
    def reset_reads(self) -> u.Quantity:
        return self._get_node(
            "reset_reads",
            u.Quantity(np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16),
        )
