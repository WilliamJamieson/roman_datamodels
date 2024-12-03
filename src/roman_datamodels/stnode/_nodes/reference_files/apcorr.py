import numpy as np

from roman_datamodels.stnode import _core, _default

from ..meta import OPTICAL_ELEMENTS
from .ref import RefCommonRef

__all__ = ["ApcorrRef"]


class ApcorrRefDataPatternproperties(_core.ObjectNode):
    @property
    def array_shape(self) -> tuple[int]:
        if self._has_node("ap_corrections"):
            return self.ap_corrections.shape

        if self._has_node("ee_fractions"):
            return self.ee_fractions.shape

        if self._has_node("ee_radii"):
            return self.ee_radii.shape

        return (10,)

    @property
    def ap_corrections(self) -> np.ndarray | None:
        return self._get_node("ap_corrections", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @property
    def ee_fractions(self) -> np.ndarray | None:
        return self._get_node("ee_fractions", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @property
    def ee_radii(self) -> np.ndarray | None:
        return self._get_node("ee_radii", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @property
    def sky_background_rin(self) -> float | None:
        return self._get_node("sky_background_rin", lambda: _default.NONUM)

    @property
    def sky_background_rout(self) -> float | None:
        return self._get_node("sky_background_rout", lambda: _default.NONUM)


class ApcorrRefMeta(RefCommonRef):
    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "APCORR")


class ApcorrRef(_core.DataModelNode):
    """
    Aperture correction reference schema
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/apcorr-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "data",
        )

    @property
    def array_shape(self) -> tuple[int]:
        if self._has_node("data") and len(data := self._data["data"]) > 0:
            return next(iter(data.values())).array_shape

        return (10,)

    @property
    def meta(self) -> ApcorrRefMeta:
        return self._get_node("meta", ApcorrRefMeta)

    @property
    def data(self) -> dict[str, ApcorrRefDataPatternproperties]:
        def _default():
            return {element: ApcorrRefDataPatternproperties() for element in OPTICAL_ELEMENTS}

        return self._get_node("data", _default)
