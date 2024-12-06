import numpy as np

from roman_datamodels.stnode import _base, _core, _default

from ..meta import OPTICAL_ELEMENTS
from .ref import RefCommonRef

__all__ = ["ApcorrRef"]


class ApcorrRef_Data(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @property
    def array_shape(self) -> tuple[int]:
        if self._has_node("ap_corrections"):
            return self.ap_corrections.shape

        if self._has_node("ee_fractions"):
            return self.ee_fractions.shape

        if self._has_node("ee_radii"):
            return self.ee_radii.shape

        return (10,)

    @_core.rad_field
    def ap_corrections(self) -> np.ndarray | None:
        return self._get_node("ap_corrections", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @_core.rad_field
    def ee_fractions(self) -> np.ndarray | None:
        return self._get_node("ee_fractions", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @_core.rad_field
    def ee_radii(self) -> np.ndarray | None:
        return self._get_node("ee_radii", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @_core.rad_field
    def sky_background_rin(self) -> float | None:
        return self._get_node("sky_background_rin", lambda: _default.NONUM)

    @_core.rad_field
    def sky_background_rout(self) -> float | None:
        return self._get_node("sky_background_rout", lambda: _default.NONUM)


class ApcorrRef_Meta(_core.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @_core.rad_field
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "APCORR")


class ApcorrRef(_core.DataModelNode):
    """
    Aperture correction reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/apcorr-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        if self._has_node("data") and len(data := self._data["data"]) > 0:
            return next(iter(data.values())).array_shape

        return (10,)

    @_core.rad_field
    def meta(self) -> ApcorrRef_Meta:
        return self._get_node("meta", ApcorrRef_Meta)

    @_core.rad_field
    def data(self) -> _base.DNode[str, ApcorrRef_Data]:
        def _default():
            return _base.DNode({element: ApcorrRef_Data() for element in OPTICAL_ELEMENTS})

        return self._get_node("data", _default)
