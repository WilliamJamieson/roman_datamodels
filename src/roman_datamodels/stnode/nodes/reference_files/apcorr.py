import numpy as np

from roman_datamodels.stnode import core, rad

from ..enums import RefTypeEntry
from ..meta import OPTICAL_ELEMENTS
from .ref import RefCommonRef

__all__ = ["ApcorrRef"]


class ApcorrRef_Data(rad.ImpliedNodeMixin, rad.ObjectNode):
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

    @rad.field
    def ap_corrections(self) -> np.ndarray | None:
        return self._get_node("ap_corrections", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @rad.field
    def ee_fractions(self) -> np.ndarray | None:
        return self._get_node("ee_fractions", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @rad.field
    def ee_radii(self) -> np.ndarray | None:
        return self._get_node("ee_radii", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @rad.field
    def sky_background_rin(self) -> float | None:
        return self._get_node("sky_background_rin", lambda: rad.NONUM)

    @rad.field
    def sky_background_rout(self) -> float | None:
        return self._get_node("sky_background_rout", lambda: rad.NONUM)


class ApcorrRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ApcorrRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.APCORR)


class ApcorrRef(rad.DataModelNode):
    """
    Aperture correction reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/apcorr-1.0.0"

    @property
    def primary_array_shape(self) -> tuple[int]:
        if self._has_node("data") and len(data := self._data["data"]) > 0:
            return next(iter(data.values())).array_shape

        return None

    @property
    def default_array_shape(self) -> tuple[int]:
        return (10,)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (10,)

    @rad.field
    def meta(self) -> ApcorrRef_Meta:
        return self._get_node("meta", ApcorrRef_Meta)

    @rad.field
    def data(self) -> core.DNode[str, ApcorrRef_Data]:
        def _default():
            return core.DNode({element: ApcorrRef_Data() for element in OPTICAL_ELEMENTS})

        return self._get_node("data", _default)
