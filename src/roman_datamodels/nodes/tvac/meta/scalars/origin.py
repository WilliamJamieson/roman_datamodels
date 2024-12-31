from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["TvacOrigin"]


class TvacOriginMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/origin-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/origin-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/origin-1.0.0"
            }
        )


class TvacOrigin(TvacOriginMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    STSCI = "STSCI"
    IPAC_SSC = "IPAC/SSC"

    @classmethod
    def default(cls) -> TvacOrigin:
        return cls.STSCI
