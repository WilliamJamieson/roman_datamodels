from __future__ import annotations

from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["Origin"]


class OriginMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uri(cls):
        return "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/origin-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/origin-1.0.0"


class Origin(OriginMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Organization responsible for creating file
    """

    STSCI = "STSCI"
    STSCI_SOC = "STSCI/SOC"
    IPAC_SSC = "IPAC/SSC"
