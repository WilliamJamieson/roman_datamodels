import sys
from enum import unique

if sys.version_info < (3, 11):
    from strenum import StrEnum
else:
    from enum import StrEnum


__all__ = ["asdf_uri", "asdf_tag_uri", "asdf_extra_uri"]


class version(StrEnum):
    VERSION = "1.0.0"
    BASE = "asdf://stsci.edu/datamodels/roman/pydantic"


def _with_base(uri: str) -> str:
    """Add the base to the URI."""
    return f"{version.BASE.value}/{uri}"


@unique
class base_uri(StrEnum):
    # fmt: off
    SCHEMA = _with_base("schemas")
    TAG    = _with_base("tags")
    # fmt: on


def _with_version(uri: str) -> str:
    """Add the version to the URI."""
    return f"{uri}-{version.VERSION.value}"


def _schema_uri(name: str) -> str:
    """
    Return the schema URI.
    """
    return _with_version(f"{base_uri.SCHEMA.value}/{name}")


def _tag_uri(name: str) -> str:
    """
    Return the tag URI.
    """
    return _with_version(f"{base_uri.TAG.value}/{name}")


class asdf_uri(StrEnum):
    """Asdf Schema references URIs."""

    # fmt: off
    # MODEL URIs
    GUIDEWINDOW     = _schema_uri("guidewindow")
    RAMP            = _schema_uri("ramp")
    RAMP_FIT_OUTPUT = _schema_uri("ramp_fit_output")
    WFI_IMAGE       = _schema_uri("wfi_image")
    WFI_MOSAIC      = _schema_uri("wfi_mosaic")
    WFI_SCIENCE_RAW = _schema_uri("wfi_science_raw")

    # METADATA URIs
    APERTURE         = _schema_uri("aperture")
    CAL_STEP         = _schema_uri("cal_step")
    COORDINATES      = _schema_uri("coordinates")
    EPHEMERIS        = _schema_uri("ephemeris")
    EXPOSURE         = _schema_uri("exposure")
    GUIDESTAR        = _schema_uri("guidestar")
    OBSERVATION      = _schema_uri("observation")
    PHOTOMETRY       = _schema_uri("photometry")
    POINTING         = _schema_uri("pointing")
    PROGRAM          = _schema_uri("program")
    RESAMPLE         = _schema_uri("resample")
    SOURCE_DETECTION = _schema_uri("source_detection")
    TARGET           = _schema_uri("target")
    WCSINFO          = _schema_uri("wcsinfo")
    WFI_MODE         = _schema_uri("wfi_mode")

    # METADATA COLLECTIONS
    BASIC               = _schema_uri("basic")
    COMMON              = _schema_uri("common")
    # VARIANCE            = _schema_uri("variance")
    VELOCITY_ABERRATION = _schema_uri("velocity_aberration")
    VISIT               = _schema_uri("visit")

    # REFERENCE FILE URIs
    DARK             = _schema_uri("reference_files/dark")
    DISTORTION       = _schema_uri("reference_files/distortion")
    FLAT             = _schema_uri("reference_files/flat")
    GAIN             = _schema_uri("reference_files/gain")
    INVERSELINEARITY = _schema_uri("reference_files/inverselinearity")
    IPC              = _schema_uri("reference_files/ipc")
    LINEARITY        = _schema_uri("reference_files/linearity")
    MASK             = _schema_uri("reference_files/mask")
    PIXELAREA        = _schema_uri("reference_files/pixelarea")
    READNOISE        = _schema_uri("reference_files/readnoise")
    REFPIX           = _schema_uri("reference_files/refpix")
    SATURATION       = _schema_uri("reference_files/saturation")
    SUPERBIAS        = _schema_uri("reference_files/superbias")
    WFI_IMG_PHOTOM   = _schema_uri("reference_files/wfi_img_photom")

    # REFERENCE FILE METADATA
    REF_COMMON          = _schema_uri("reference_files/ref_common")
    REF_EXPOSURE_TYPE   = _schema_uri("reference_files/ref_exposure_type")
    REF_OPTICAL_ELEMENT = _schema_uri("reference_files/ref_optical_element")


    # MISC URIs
    ASSOCIATIONS = _schema_uri("associations")
    REF_FILE     = _schema_uri("ref_file")


    # SSC URIs
    MSOS_STACK = _schema_uri("msos_stack")
    # fmt: on


@unique
class asdf_tag_uri(StrEnum):
    """Tag URIs."""

    # fmt: off
    # MODEL TAGS
    GUIDEWINDOW     = _tag_uri("guidewindow")
    RAMP            = _tag_uri("ramp")
    RAMP_FIT_OUTPUT = _tag_uri("ramp_fit_output")
    WFI_IMAGE       = _tag_uri("wfi_image")
    WFI_MOSAIC      = _tag_uri("wfi_mosaic")
    WFI_SCIENCE_RAW = _tag_uri("wfi_science_raw")

    # METADATA TAGS
    APERTURE         = _tag_uri("aperture")
    CAL_STEP         = _tag_uri("cal_step")
    COORDINATES      = _tag_uri("coordinates")
    EPHEMERIS        = _tag_uri("ephemeris")
    EXPOSURE         = _tag_uri("exposure")
    GUIDESTAR        = _tag_uri("guidestar")
    OBSERVATION      = _tag_uri("observation")
    PHOTOMETRY       = _tag_uri("photometry")
    POINTING         = _tag_uri("pointing")
    PROGRAM          = _tag_uri("program")
    RESAMPLE         = _tag_uri("resample")
    SOURCE_DETECTION = _tag_uri("source_detection")
    TARGET           = _tag_uri("target")
    VISIT            = _tag_uri("visit")
    WCSINFO          = _tag_uri("wcsinfo")
    WFI_MODE         = _tag_uri("wfi_mode")

    # REFERENCE FILE TAGS
    DARK             = _tag_uri("reference_files/dark")
    DISTORTION       = _tag_uri("reference_files/distortion")
    FLAT             = _tag_uri("reference_files/flat")
    GAIN             = _tag_uri("reference_files/gain")
    INVERSELINEARITY = _tag_uri("reference_files/inverselinearity")
    IPC              = _tag_uri("reference_files/ipc")
    LINEARITY        = _tag_uri("reference_files/linearity")
    MASK             = _tag_uri("reference_files/mask")
    PIXELAREA        = _tag_uri("reference_files/pixelarea")
    READNOISE        = _tag_uri("reference_files/readnoise")
    REFPIX           = _tag_uri("reference_files/refpix")
    SATURATION       = _tag_uri("reference_files/saturation")
    SUPERBIAS        = _tag_uri("reference_files/superbias")
    WFI_IMG_PHOTOM   = _tag_uri("reference_files/wfi_img_photom")

    # MISC TAGS
    ASSOCIATIONS = _tag_uri("associations")
    REF_FILE     = _tag_uri("ref_file")

    # SSC TAGS
    MSOS_STACK = _tag_uri("msos_stack")
    # fmt: on


class asdf_extra_uri(StrEnum):
    """Extra asdf meta schema uris"""

    # fmt: off
    SCHEMA    = _with_version(_with_base("schemas/rad_schema"))
    EXTENSION = _with_version(_with_base("extensions/rad_extension"))
    # fmt: on
