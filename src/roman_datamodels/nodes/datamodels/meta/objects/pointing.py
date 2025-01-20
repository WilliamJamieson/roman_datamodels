from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = ["Pointing"]


_Pointing: TypeAlias = float | str


class Pointing(rad.TaggedObjectNode[_Pointing]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/pointing-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {"asdf://stsci.edu/datamodels/roman/tags/pointing-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/pointing-1.0.0"}
        )

    @property
    @rad.field
    def ra_v1(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec_v1(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def pa_v3(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def target_aperture(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def target_ra(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def target_dec(self: rad.Node) -> float:
        return rad.NONUM
