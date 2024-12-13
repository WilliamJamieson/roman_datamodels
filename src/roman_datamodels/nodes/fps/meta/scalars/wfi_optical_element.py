from roman_datamodels.stnode import rad

__all__ = ["FpsWfiOpticalElement"]


class FpsWfiOpticalElementMixin(str, rad.SchemaScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/wfi_optical_element-1.0.0",)


class FpsWfiOpticalElement(FpsWfiOpticalElementMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    WFI Optical Element
    """

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
