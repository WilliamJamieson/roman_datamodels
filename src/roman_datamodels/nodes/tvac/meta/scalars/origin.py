from __future__ import annotations

from roman_datamodels.stnode import rad

__all__ = ["TvacOrigin", "TvacOriginMixin"]


class TvacOriginMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    @classmethod
    def _asdf_tag_uris(cls) -> dict[str, str]:
        return {
            "asdf://stsci.edu/datamodels/roman/tags/tvac/origin-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/origin-1.0.0"
        }


class TvacOrigin(TvacOriginMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    STSCI = "STSCI"
    IPAC_SSC = "IPAC/SSC"

    @classmethod
    def default(cls) -> TvacOrigin:
        return cls.STSCI
