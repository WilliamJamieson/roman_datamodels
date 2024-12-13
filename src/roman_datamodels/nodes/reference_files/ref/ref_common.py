from astropy.time import Time

from roman_datamodels.stnode import core, rad

from ...datamodels import InstrumentNameEntry, Telescope, WfiDetector, WfiOpticalElement

__all__ = [
    "RefCommonPedigreeEntry",
    "RefCommonRef",
    "RefTypeEntry",
]


class RefTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_schema(cls) -> rad.RadSchema:
        return rad.RadSchema([])


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


class RefCommonPedigreeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
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


class RefCommonRef_InstrumentMixin(core.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @rad.field
    def optical_element(self) -> WfiOpticalElement | str:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("optical_element",)


class RefCommonRef_Instrument(RefCommonRef_InstrumentMixin, rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefCommonRef

    @rad.field
    def name(self) -> InstrumentNameEntry:
        return self._get_node("name", lambda: InstrumentNameEntry.WFI)

    @rad.field
    def detector(self) -> WfiDetector:
        return self._get_node("detector", lambda: WfiDetector.WFI01)


class RefCommonRef(rad.SchemaObjectNode):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_common-1.0.0",)

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.NA)

    @rad.field
    def pedigree(self) -> RefCommonPedigreeEntry:
        return self._get_node("pedigree", lambda: RefCommonPedigreeEntry.GROUND)

    @rad.field
    def description(self) -> str:
        return self._get_node("description", lambda: "blah blah blah")

    @rad.field
    def author(self) -> str:
        return self._get_node("author", lambda: "test system")

    @rad.field
    def useafter(self) -> Time:
        return self._get_node("useafter", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def telescope(self) -> Telescope | str:
        return self._get_node("telescope", lambda: Telescope.ROMAN)

    @rad.field
    def origin(self) -> str:
        return self._get_node("origin", lambda: "STSCI")

    @rad.field
    def instrument(self) -> RefCommonRef_Instrument:
        return self._get_node("instrument", RefCommonRef_Instrument)
