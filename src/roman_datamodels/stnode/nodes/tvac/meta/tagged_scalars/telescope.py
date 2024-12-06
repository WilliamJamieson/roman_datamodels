from __future__ import annotations

from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["TvacTelescope"]


class TvacTelescopeMixin(str, _core.TaggedScalarNode, _core.EnumNodeMixin):
    """
    Telescope used to acquire the data
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/telescope-1.0.0"


class TvacTelescope(TvacTelescopeMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enumerate the telescopes
    """

    ROMAN = "ROMAN"
