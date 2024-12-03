from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["FpsOrigin"]


class FpsOrigin(str, _core.TaggedScalarNode):
    """
    Organization responsible for creating file
    """

    @classmethod
    def STSCI(cls) -> FpsOrigin:
        return cls("STSCI")

    @classmethod
    def IPAC_SSC(cls) -> FpsOrigin:
        return cls("IPAC/SSC")

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/origin-1.0.0"
