from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["TvacOrigin"]


class TvacOriginMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uri(cls):
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/origin-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/origin-1.0.0"


class TvacOrigin(TvacOriginMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Organization responsible for creating file
    """

    STSCI = "STSCI"
    IPAC_SSC = "IPAC/SSC"
