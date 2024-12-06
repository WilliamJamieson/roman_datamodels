from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["FpsOrigin"]


class FpsOriginMixin(str, _core.TaggedScalarNode, _core.EnumNodeMixin):
    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/origin-1.0.0"


class FpsOrigin(FpsOriginMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Organization responsible for creating file
    """

    STSCI = "STSCI"
    IPAC_SSC = "IPAC/SSC"
