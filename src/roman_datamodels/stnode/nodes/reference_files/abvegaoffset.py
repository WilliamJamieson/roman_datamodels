from roman_datamodels.stnode import _base, _core, _default

from ..meta import OPTICAL_ELEMENTS
from .ref import RefCommonRef

__all__ = ["AbvegaoffsetRef"]


class AbvegaoffsetRef_Meta(RefCommonRef):
    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "ABVEGAOFFSET")


class AbvegaoffsetRef_Data(_core.ObjectNode):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return ("abvega_offset",)

    @property
    def abvega_offset(self) -> float | None:
        return self._get_node("abvega_offset", lambda: _default.NONUM)


class AbvegaoffsetRef(_core.DataModelNode):
    """
    AB Vega Offset reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/abvegaoffset-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
        )

    @property
    def array_shape(self) -> tuple[int]:
        raise NotImplementedError("array_data is not implemented")

    @property
    def meta(self) -> AbvegaoffsetRef_Meta:
        return self._get_node("meta", AbvegaoffsetRef_Meta)

    @property
    def data(self) -> _base.DNode[str, AbvegaoffsetRef_Data]:
        def _default():
            return _base.DNode({element: AbvegaoffsetRef_Data() for element in OPTICAL_ELEMENTS})

        return self._get_node("data", _default)
