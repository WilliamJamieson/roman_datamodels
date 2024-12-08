import numpy as np

from roman_datamodels.stnode import _default, rad

from ..meta import Common

__all__ = ["MsosStack"]


class MsosStack_Meta(rad.ImpliedNodeMixin, Common):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MsosStack

    @rad.rad_field
    def image_list(self) -> str:
        return self._get_node("image_list", lambda: _default.NOSTR)


class MsosStack(rad.DataModelNode):
    """
    Level 3 schema for SSC's MSOS stack products
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/msos_stack-1.0.0"

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

    @rad.rad_field
    def meta(self) -> MsosStack_Meta:
        return self._get_node("meta", MsosStack_Meta)

    @rad.rad_field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @rad.rad_field
    def uncertainty(self) -> np.ndarray:
        return self._get_node("uncertainty", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @rad.rad_field
    def mask(self) -> np.ndarray:
        return self._get_node("mask", lambda: np.zeros(self.array_shape, dtype=np.uint8))

    @rad.rad_field
    def coverage(self) -> np.ndarray:
        return self._get_node("coverage", lambda: np.zeros(self.array_shape, dtype=np.uint8))
