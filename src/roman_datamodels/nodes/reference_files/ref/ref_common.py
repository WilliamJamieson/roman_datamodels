from typing import TypeAlias, TypeVar

from astropy.time import Time

from roman_datamodels.stnode import core, rad

from ...datamodels import InstrumentNameEntry, Telescope, WfiDetector, WfiOpticalElement

__all__ = [
    "RefCommonPedigreeEntry",
    "RefCommonRef",
    "RefTypeEntry",
]

# So that when we inherit from this we can include it's parts too
_T = TypeVar("_T")


class RefTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_schema(cls) -> rad.RadSchema:
        return rad.RadSchema({})


class RefTypeEntry(RefTypeEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
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


class RefCommonPedigreeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return RefCommonRef

    @classmethod
    def asdf_property_name(cls) -> str:
        return "pedigree"


class RefCommonPedigreeEntry(RefCommonPedigreeEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for pedigree in ref_common
    """

    GROUND = "GROUND"
    MODEL = "MODEL"
    DUMMY = "DUMMY"
    SIMULATION = "SIMULATION"


_RefCommonRef_InstrumentMixin: TypeAlias = WfiOpticalElement | None


class RefCommonRef_InstrumentMixin(core.AdditionalNodeMixin[_RefCommonRef_InstrumentMixin | _T]):
    """Mixin things present in the constructors not present in the schema"""

    @property
    @rad.field
    def optical_element(self: rad.Node) -> WfiOpticalElement:
        return WfiOpticalElement.F158

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("optical_element",)


_RefCommonRef_Instrument: TypeAlias = _RefCommonRef_InstrumentMixin | InstrumentNameEntry | WfiDetector


class RefCommonRef_Instrument(
    RefCommonRef_InstrumentMixin[_RefCommonRef_InstrumentMixin | _T],
    rad.ImpliedNodeMixin[_RefCommonRef_Instrument | _T],
    rad.ObjectNode[_RefCommonRef_Instrument | _T],
):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefCommonRef

    @property
    @rad.field
    def name(self: rad.Node) -> InstrumentNameEntry:
        return InstrumentNameEntry.WFI

    @property
    @rad.field
    def detector(self: rad.Node) -> WfiDetector:
        return WfiDetector.WFI01


_RefCommonRef: TypeAlias = RefTypeEntry | RefCommonPedigreeEntry | RefCommonRef_Instrument[_RefCommonRef_Instrument] | Time | str


class RefCommonRef(rad.SchemaObjectNode[_RefCommonRef | _T]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_common-1.0.0",)

    @property
    @rad.field
    def reftype(self: rad.Node) -> RefTypeEntry:
        return RefTypeEntry.NA

    @property
    @rad.field
    def pedigree(self: rad.Node) -> RefCommonPedigreeEntry:
        return RefCommonPedigreeEntry.GROUND

    @property
    @rad.field
    def description(self: rad.Node) -> str:
        return "blah blah blah"

    @property
    @rad.field
    def author(self: rad.Node) -> str:
        return "test system"

    @property
    @rad.field
    def useafter(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def telescope(self: rad.Node) -> Telescope | str:
        return Telescope.ROMAN

    @property
    @rad.field
    def origin(self: rad.Node) -> str:
        return "STSCI"

    @property
    @rad.field
    def instrument(self: rad.Node) -> RefCommonRef_Instrument[_RefCommonRef_Instrument]:
        return RefCommonRef_Instrument()
