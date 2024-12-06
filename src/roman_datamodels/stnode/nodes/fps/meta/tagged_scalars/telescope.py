from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["FpsTelescope"]


class FpsTelescopeMixin(str, _core.TaggedScalarNode, _core.EnumNodeMixin):
    @classmethod
    def asdf_tag(cls):
        return "asdf://stsci.edu/datamodels/roman/tags/fps/telescope-1.0.0"


class FpsTelescope(FpsTelescopeMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Telescope used to acquire the data
    """

    ROMAN = "ROMAN"
