from types import MappingProxyType

from roman_datamodels.stnode import core, rad

from ..datamodels import OPTICAL_ELEMENTS
from .ref import RefCommonRef, RefTypeEntry

__all__ = ["AbvegaoffsetRef"]


class AbvegaoffsetRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.ABVEGAOFFSET)


class AbvegaoffsetRef_Data(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @rad.field
    def abvega_offset(self) -> float | None:
        return self._get_node("abvega_offset", lambda: rad.NONUM)


class AbvegaoffsetRef(rad.TaggedObjectNode):
    """
    AB Vega Offset reference schema
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/abvegaoffset-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/abvegaoffset-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/abvegaoffset-1.0.0"
            }
        )

    @rad.field
    def meta(self) -> AbvegaoffsetRef_Meta:
        return self._get_node("meta", AbvegaoffsetRef_Meta)

    @rad.field
    def data(self) -> core.DNode[str, AbvegaoffsetRef_Data]:
        def _default():
            return core.DNode({element: AbvegaoffsetRef_Data() for element in OPTICAL_ELEMENTS})

        return self._get_node("data", _default)
