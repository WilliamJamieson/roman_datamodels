from roman_datamodels.stnode import rad

__all__ = [
    "OPTICAL_ELEMENTS",
    "WfiOpticalElement",
]


class WfiOpticalElementMixin(str, rad.SchemaScalarNode[str], rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/wfi_optical_element-1.0.0",)


class WfiOpticalElement(WfiOpticalElementMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
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


OPTICAL_ELEMENTS = tuple(str(entry.value) for entry in WfiOpticalElement)
