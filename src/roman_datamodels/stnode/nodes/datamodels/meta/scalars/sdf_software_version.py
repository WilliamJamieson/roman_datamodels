from roman_datamodels.stnode import rad

__all__ = ["SdfSoftwareVersion"]


class SdfSoftwareVersion(str, rad.TaggedScalarNode):
    """
    SDF software version number
    """

    @classmethod
    def asdf_schema_uri(cls):
        return "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/sdf_software_version-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/sdf_software_version-1.0.0"
