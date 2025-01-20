from types import MappingProxyType
from typing import TypeAlias, TypeVar

from roman_datamodels.stnode import core, rad

from ..datamodels import OPTICAL_ELEMENTS
from .ref import RefCommonRef, RefTypeEntry
from .ref.ref_common import _RefCommonRef

__all__ = ["AbvegaoffsetRef"]

_T = TypeVar("_T")


class AbvegaoffsetRef_Meta(rad.ImpliedNodeMixin[_RefCommonRef], RefCommonRef[_RefCommonRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @property
    @rad.field
    def reftype(self: rad.Node) -> RefTypeEntry:
        return RefTypeEntry.ABVEGAOFFSET


class AbvegaoffsetRef_Data(rad.ImpliedNodeMixin[float | None], rad.ObjectNode[float | None]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @property
    @rad.field
    def abvega_offset(self: rad.Node) -> float | None:
        return rad.NONUM


class AbvedgaoffsetRef_Data_PatternNode(core.PatternDNode[_T], rad.ImpliedNodeMixin[_T]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return AbvegaoffsetRef

    @classmethod
    def asdf_implied_property_name(cls) -> str:
        return "data"

    @classmethod
    def asdf_key_pattern(cls) -> str:
        return "^(F062|F087|F106|F129|F146|F158|F184|F213|GRISM|PRISM|DARK)$"


_AbvegaoffsetRef: TypeAlias = AbvegaoffsetRef_Data | AbvedgaoffsetRef_Data_PatternNode[AbvegaoffsetRef_Data]


class AbvegaoffsetRef(rad.TaggedObjectNode[_AbvegaoffsetRef]):
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

    @property
    @rad.field
    def meta(self: rad.Node) -> AbvegaoffsetRef_Meta:
        return AbvegaoffsetRef_Meta()

    @property
    @rad.field
    def data(self: rad.Node) -> AbvedgaoffsetRef_Data_PatternNode[AbvegaoffsetRef_Data]:
        return AbvedgaoffsetRef_Data_PatternNode({element: AbvegaoffsetRef_Data() for element in OPTICAL_ELEMENTS})
