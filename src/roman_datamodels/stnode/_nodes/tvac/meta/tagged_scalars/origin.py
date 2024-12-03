from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["TvacOrigin"]


class TvacOrigin(str, _core.TaggedScalarNode):
    """
    Organization responsible for creating file
    """

    @classmethod
    def STSCI(cls) -> TvacOrigin:
        return cls("STSCI")

    @classmethod
    def IPAC_SSC(cls) -> TvacOrigin:
        return cls("IPAC/SSC")

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/fps/origin-1.0.0"
