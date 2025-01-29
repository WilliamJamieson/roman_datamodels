from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["FpsOrigin", "FpsOriginMixin"]


class FpsOriginMixin(str, rad.TaggedScalarNode[str], rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/origin-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/origin-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/origin-1.0.0"
            }
        )


class FpsOrigin(FpsOriginMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    STSCI = "STSCI"
    IPAC_SSC = "IPAC/SSC"

    @classmethod
    def default(cls) -> FpsOrigin:
        return cls.STSCI
