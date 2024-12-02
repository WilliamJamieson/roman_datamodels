from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["Origin"]


class Origin(str, _core.TaggedScalarNode):
    """
    Organization responsible for creating file
    """

    @classmethod
    def STSCI(cls) -> Origin:
        return cls("STSCI")

    @classmethod
    def STSCI_SOC(cls) -> Origin:
        return cls("STSCI/SOC")

    @classmethod
    def IPAC_SSC(cls) -> Origin:
        return cls("IPAC/SSC")

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/origin-1.0.0"
