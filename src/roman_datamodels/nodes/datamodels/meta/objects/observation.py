from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = ["Observation"]


_Observation: TypeAlias = int | str


class Observation(rad.TaggedObjectNode[_Observation]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/observation-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/observation-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/observation-1.0.0"
            }
        )

    @property
    @rad.field
    def observation_id(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def visit_id(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def program(self: rad.Node) -> int:
        return 1

    @property
    @rad.field
    def execution_plan(self: rad.Node) -> int:
        return 1

    # Note cannot use "pass" as a property name due to reserved keyword
    @property
    @rad.field
    def pass_(self: rad.Node) -> int:
        return 1

    @property
    @rad.field
    def segment(self: rad.Node) -> int:
        return 1

    @property
    @rad.field
    def observation(self: rad.Node) -> int:
        return 1

    @property
    @rad.field
    def visit(self: rad.Node) -> int:
        return 1

    @property
    @rad.field
    def visit_file_group(self: rad.Node) -> int:
        return 1

    @property
    @rad.field
    def visit_file_sequence(self: rad.Node) -> int:
        return 1

    @property
    @rad.field
    def visit_file_activity(self: rad.Node) -> str:
        return "01"

    @property
    @rad.field
    def exposure(self: rad.Node) -> int:
        return 1
