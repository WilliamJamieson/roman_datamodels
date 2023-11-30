import sys

if sys.version_info < (3, 11):
    from strenum import StrEnum
else:
    from enum import StrEnum


__all__ = [
    "pedigree",
    "telescope",
    "origin",
    "instrument",
    "detector",
    "reftype",
    "exposure_type",
    "optical_element",
    "aperture",
    "calibration_status",
    "coordinates",
    "ephemeris_type",
    "guidewindow_modes",
    "survey",
    "target_type",
    "source_type",
    "engineering_quality",
    "pointing_engdb_quality",
    "exptype",
    "weight_type",
]


class pedigree(StrEnum):
    GROUND = "GROUND"
    MODEL = "MODEL"
    DUMMY = "DUMMY"
    SIMULATION = "SIMULATION"


class telescope(StrEnum):
    ROMAN = "ROMAN"


class origin(StrEnum):
    STSCI = "STSCI"
    IPAC = "IPAC/SSC"
    SSC = "IPAC/SSC"


class instrument(StrEnum):
    WFI = "WFI"


class detector(StrEnum):
    WFI01 = "WFI01"
    WFI02 = "WFI02"
    WFI03 = "WFI03"
    WFI04 = "WFI04"
    WFI05 = "WFI05"
    WFI06 = "WFI06"
    WFI07 = "WFI07"
    WFI08 = "WFI08"
    WFI09 = "WFI09"
    WFI10 = "WFI10"
    WFI11 = "WFI11"
    WFI12 = "WFI12"
    WFI13 = "WFI13"
    WFI14 = "WFI14"
    WFI15 = "WFI15"
    WFI16 = "WFI16"
    WFI17 = "WFI17"
    WFI18 = "WFI18"


class reftype(StrEnum):
    DARK = "DARK"
    DISTORTION = "DISTORTION"
    FLAT = "FLAT"
    GAIN = "GAIN"
    INVERSELINEARITY = "INVERSELINEARITY"
    IPC = "IPC"
    LINEARITY = "LINEARITY"
    MASK = "MASK"
    PIXELAREA = "PIXELAREA"
    READNOISE = "READNOISE"
    REFPIX = "REFPIX"
    SATURATION = "SATURATION"
    BIAS = "BIAS"
    PHOTOM = "PHOTOM"


class exposure_type(StrEnum):
    WFI_IMAGE = "WFI_IMAGE"
    WFI_GRISM = "WFI_GRISM"
    WFI_PRISM = "WFI_PRISM"
    WFI_DARK = "WFI_DARK"
    WFI_FLAT = "WFI_FLAT"
    WFI_WFSC = "WFI_WFSC"


class optical_element(StrEnum):
    F062 = "F062"
    F087 = "F087"
    F106 = "F106"
    F129 = "F129"
    F146 = "F146"
    F158 = "F158"
    F184 = "F184"
    F213 = "F213"
    GRISM = "GRISM"
    PRISM = "PRISM"
    DARK = "DARK"


class aperture(StrEnum):
    WFI_01_FULL = "WFI_01_FULL"
    WFI_02_FULL = "WFI_02_FULL"
    WFI_03_FULL = "WFI_03_FULL"
    WFI_04_FULL = "WFI_04_FULL"
    WFI_05_FULL = "WFI_05_FULL"
    WFI_06_FULL = "WFI_06_FULL"
    WFI_07_FULL = "WFI_07_FULL"
    WFI_08_FULL = "WFI_08_FULL"
    WFI_09_FULL = "WFI_09_FULL"
    WFI_10_FULL = "WFI_10_FULL"
    WFI_11_FULL = "WFI_11_FULL"
    WFI_12_FULL = "WFI_12_FULL"
    WFI_13_FULL = "WFI_13_FULL"
    WFI_14_FULL = "WFI_14_FULL"
    WFI_15_FULL = "WFI_15_FULL"
    WFI_16_FULL = "WFI_16_FULL"
    WFI_17_FULL = "WFI_17_FULL"
    WFI_18_FULL = "WFI_18_FULL"
    BORESIGHT = "BORESIGHT"
    CGI_CEN = "CGI_CEN"
    WFI_CEN = "WFI_CEN"


class calibration_status(StrEnum):
    NA = "N/A"
    COMPLETE = "COMPLETE"
    SKIPPED = "SKIPPED"
    INCOMPLETE = "INCOMPLETE"


class coordinates(StrEnum):
    ICRS = "ICRS"


class ephemeris_type(StrEnum):
    DEFINITIVE = "DEFINITIVE"
    PREDICTED = "PREDICTED"


class guidewindow_modes(StrEnum):
    WIM_ACQ = "WIM-ACQ"
    WIM_TRACK = "WIM-TRACK"
    WSM_ACQ_1 = "WSM-ACQ-1"
    WSM_ACQ_2 = "WSM-ACQ-2"
    WSM_TRACK = "WSM-TRACK"
    DEFOCUSED_MODERATE = "DEFOCUSED-MODERATE"
    DEFOCUSED_LARGE = "DEFOCUSED-LARGE"


class survey(StrEnum):
    HLS = "HLS"
    EMS = "EMS"
    SN = "SN"
    NA = "N/A"


class target_type(StrEnum):
    FIXED = "FIXED"
    MOVING = "MOVING"
    GENERIC = "GENERIC"


class source_type(StrEnum):
    POINT = "POINT"
    EXTENDED = "EXTENDED"
    UNKNOWN = "UNKNOWN"


class engineering_quality(StrEnum):
    OK = "OK"
    SUSPECT = "SUSPECT"


class pointing_engdb_quality(StrEnum):
    CALCULATED = "CALCULATED"
    PLANNED = "PLANNED"


class exptype(StrEnum):
    SCIENCE = "SCIENCE"
    CALIBRATED = "CALIBRATED"
    ENGINEERING = "ENGINEERING"


class weight_type(StrEnum):
    exptime = "exptime"
    ivm = "ivm"
