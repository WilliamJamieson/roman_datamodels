from __future__ import annotations

from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["Origin"]


class OriginMixin(str, _core.TaggedScalarNode, _core.EnumNodeMixin):
    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/origin-1.0.0"


class Origin(OriginMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Organization responsible for creating file
    """

    STSCI = "STSCI"
    STSCI_SOC = "STSCI/SOC"
    IPAC_SSC = "IPAC/SSC"
