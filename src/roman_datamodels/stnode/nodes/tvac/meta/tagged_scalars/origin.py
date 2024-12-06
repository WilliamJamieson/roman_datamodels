from __future__ import annotations

from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["TvacOrigin"]


class TvacOriginMixin(str, _core.TaggedScalarNode, _core.EnumNodeMixin):
    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/origin-1.0.0"


class TvacOrigin(TvacOriginMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Organization responsible for creating file
    """

    STSCI = "STSCI"
    IPAC_SSC = "IPAC/SSC"
