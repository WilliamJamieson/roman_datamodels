"""
This module provides DataModel classes for the Roman reference files.
"""

from __future__ import annotations

from typing import ClassVar

from ._core import DataModel

__all__ = (
    "AbvegaoffsetRefModel",
    "ApcorrRefModel",
    "DarkRefModel",
    "DarkdecaysignalRefModel",
    "DetectorstatusRefModel",
    "DistortionRefModel",
    "EpsfRefModel",
    "EtcRefModel",
    "FlatRefModel",
    "GainRefModel",
    "IntegralnonlinearityRefModel",
    "InverselinearityRefModel",
    "IpcRefModel",
    "LinearityRefModel",
    "MATableRefModel",
    "MaskRefModel",
    "PixelareaRefModel",
    "ReadnoiseRefModel",
    "RefpixRefModel",
    "SaturationRefModel",
    "SkycellsRefModel",
    "SuperbiasRefModel",
    "WfiImgPhotomRefModel",
)


class AbvegaoffsetRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/abvegaoffset-*"


class ApcorrRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/apcorr-*"


class DarkRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/dark-*"


class DarkdecaysignalRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/darkdecaysignal-*"


class DetectorstatusRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/detectorstatus-*"


class DistortionRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/distortion-*"


class EpsfRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/epsf-*"


class EtcRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/etc-*"


class FlatRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/flat-*"


class GainRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/gain-*"


class IntegralnonlinearityRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/integralnonlinearity-*"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "value"


class InverselinearityRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/inverselinearity-*"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "coeffs"


class IpcRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/ipc-*"


class LinearityRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/linearity-*"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "coeffs"


class MaskRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/mask-*"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "dq"


class MATableRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/matable-*"


class PixelareaRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/pixelarea-*"


class ReadnoiseRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/readnoise-*"


class RefpixRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/refpix-*"


class SaturationRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/saturation-*"


class SkycellsRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/skycells-*"


class SuperbiasRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/superbias-*"


class WfiImgPhotomRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/wfi_img_photom-*"
