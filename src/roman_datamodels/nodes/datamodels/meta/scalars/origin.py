from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = [
    "Origin",
    "OriginMixin",
]


class OriginMixin(str, rad.TaggedScalarNode[str], rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/origin-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/origin-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/origin-1.0.0"
            }
        )


class Origin(OriginMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    STSCI = "STSCI"
    STSCI_SOC = "STSCI/SOC"
    IPAC_SSC = "IPAC/SSC"

    @classmethod
    def default(cls) -> Origin:
        return cls.STSCI_SOC
