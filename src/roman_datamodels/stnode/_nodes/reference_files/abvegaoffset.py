from roman_datamodels.stnode import _core, _default

from ..meta import OPTICAL_ELEMENTS
from .ref import RefCommonRef

__all__ = ["AbvegaoffsetRef"]


class AbvegaoffsetRefMeta(RefCommonRef):
    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "ABVEGAOFFSET")


class AbvegaoffsetRefDataPatternproperties(_core.ObjectNode):
    @property
    def required(self) -> tuple[str]:
        return ("abvega_offset",)

    @property
    def abvega_offset(self) -> float | None:
        return self._get_node("abvega_offset", lambda: _default.NONUM)


class AbvegaoffsetRef(_core.DataModelNode):
    """
    AB Vega Offset reference schema
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/abvegaoffset-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "data",
        )

    @property
    def array_data(self) -> tuple[int]:
        raise NotImplementedError("array_data is not implemented")

    @property
    def meta(self) -> AbvegaoffsetRefMeta:
        return self._get_node("meta", AbvegaoffsetRefMeta)

    @property
    def data(self) -> dict[str, AbvegaoffsetRefDataPatternproperties]:
        def _default():
            return {element: AbvegaoffsetRefDataPatternproperties() for element in OPTICAL_ELEMENTS}

        return self._get_node("data", _default)
