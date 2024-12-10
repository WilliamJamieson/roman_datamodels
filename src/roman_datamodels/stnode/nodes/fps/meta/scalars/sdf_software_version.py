from roman_datamodels.stnode import rad

__all__ = ["FpsSdfSoftwareVersion"]


class FpsSdfSoftwareVersion(str, rad.TaggedScalarNode):
    """
    SDF software version number
    """

    @classmethod
    def asdf_schema_uri(clas):
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/sdf_software_version-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/sdf_software_version-1.0.0"
