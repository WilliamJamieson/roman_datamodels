from roman_datamodels.stnode import rad

__all__ = ["TvacWfiOpticalElement"]


class TvacWfiOpticalElementMixin(str, rad.SchemaScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/wfi_optical_element-1.0.0",)


class TvacWfiOpticalElement(TvacWfiOpticalElementMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
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
