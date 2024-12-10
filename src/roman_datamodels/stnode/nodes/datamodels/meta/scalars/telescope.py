from __future__ import annotations

from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["Telescope"]


class TelescopeMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/telescope-1.0.0"


class Telescope(TelescopeMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Telescope used to acquire the data
    """

    ROMAN = "ROMAN"
