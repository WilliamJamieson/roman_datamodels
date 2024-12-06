from roman_datamodels.stnode import _base, _core, _default

from ..enums import RefTypeEntry
from ..meta import OPTICAL_ELEMENTS
from .ref import RefCommonRef

__all__ = ["AbvegaoffsetRef"]


class AbvegaoffsetRef_Meta(_core.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @_core.rad_field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.ABVEGAOFFSET)


class AbvegaoffsetRef_Data(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @_core.rad_field
    def abvega_offset(self) -> float | None:
        return self._get_node("abvega_offset", lambda: _default.NONUM)


class AbvegaoffsetRef(_core.DataModelNode):
    """
    AB Vega Offset reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/abvegaoffset-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        raise NotImplementedError("array_data is not implemented")

    @_core.rad_field
    def meta(self) -> AbvegaoffsetRef_Meta:
        return self._get_node("meta", AbvegaoffsetRef_Meta)

    @_core.rad_field
    def data(self) -> _base.DNode[str, AbvegaoffsetRef_Data]:
        def _default():
            return _base.DNode({element: AbvegaoffsetRef_Data() for element in OPTICAL_ELEMENTS})

        return self._get_node("data", _default)
