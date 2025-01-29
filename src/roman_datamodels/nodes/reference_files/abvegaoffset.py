from types import MappingProxyType
from typing import TypeVar

from roman_datamodels.stnode import core, rad

from ..datamodels import OPTICAL_ELEMENTS
from .ref import RefCommonRef, RefTypeEntry

__all__ = ["AbvedgaoffsetRef_Data_PatternNode", "AbvegaoffsetRef", "AbvegaoffsetRef_Data", "AbvegaoffsetRef_Meta"]

_T = TypeVar("_T")


class AbvegaoffsetRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.ABVEGAOFFSET


class AbvegaoffsetRef_Data(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @rad.field
    def abvega_offset(self) -> float | None:
        return rad.NONUM


class AbvedgaoffsetRef_Data_PatternNode(core.PatternDNode[_T], rad.ImpliedNodeMixin):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @classmethod
    def asdf_implied_property_name(cls) -> str:
        return "data"

    @classmethod
    def asdf_key_pattern(cls) -> str:
        return "^(F062|F087|F106|F129|F146|F158|F184|F213|GRISM|PRISM|DARK)$"


class AbvegaoffsetRef(rad.TaggedObjectNode):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
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
        return AbvegaoffsetRef_Meta()

    @rad.field
    def data(self) -> AbvedgaoffsetRef_Data_PatternNode[AbvegaoffsetRef_Data]:
        return AbvedgaoffsetRef_Data_PatternNode({element: AbvegaoffsetRef_Data() for element in OPTICAL_ELEMENTS})
