from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["FpsTelescope"]


class FpsTelescope(str, _core.TaggedScalarNode):
    """
    Telescope used to acquire the data
    """

    @classmethod
    def ROMAN(cls) -> FpsTelescope:
        return cls("ROMAN")

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/fps/telescope-1.0.0"
