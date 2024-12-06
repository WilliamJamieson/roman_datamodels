from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["RefTypeEntry"]


class RefTypeEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_schema(cls) -> _core.RadSchema:
        return _core.RadSchema([])


class RefTypeEntry(RefTypeEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible ref_type entries
    -> this one doesn't actually exist but it is impled by each of the reftype entries
       in the reference_files schemas
    """

    ABVEGAOFFSET = "ABVEGAOFFSET"
    APCORR = "APCORR"
    DARK = "DARK"
    DISTORTION = "DISTORTION"
    EPSF = "EPSF"
    FLAT = "FLAT"
    GAIN = "GAIN"
    INVERSELINEARITY = "INVERSELINEARITY"
    IPC = "IPC"
    LINEARITY = "LINEARITY"
    MASK = "MASK"
    AREA = "AREA"  # for pixelarea
    READNOISE = "READNOISE"
    REFPIX = "REFPIX"
    SATURATION = "SATURATION"
    BIAS = "BIAS"  # for superbias
    PHOTOM = "PHOTOM"  # for wfi_img_photom
    NA = "N/A"  # for a default value in ref_common
