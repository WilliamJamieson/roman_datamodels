from roman_datamodels.stnode import rad

__all__ = ["PrdVersion"]


class PrdVersion(str, rad.TaggedScalarNode):
    """
    S&OC PRD version number used in data processing
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/prd_version-1.0.0"
