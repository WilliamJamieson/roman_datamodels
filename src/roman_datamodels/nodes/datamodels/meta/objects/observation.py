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

    @rad.field
    def observation_id(self) -> str:
        return rad.NOSTR

    @rad.field
    def visit_id(self) -> str:
        return rad.NOSTR

    @rad.field
    def program(self) -> int:
        return 1

    @rad.field
    def execution_plan(self) -> int:
        return 1

    # Note cannot use "pass" as a property name due to reserved keyword
    @rad.field
    def pass_(self) -> int:
        return 1

    @rad.field
    def segment(self) -> int:
        return 1

    @rad.field
    def observation(self) -> int:
        return 1

    @rad.field
    def visit(self) -> int:
        return 1

    @rad.field
    def visit_file_group(self) -> int:
        return 1

    @rad.field
    def visit_file_sequence(self) -> int:
        return 1

    @rad.field
    def visit_file_activity(self) -> str:
        return "01"

    @rad.field
    def exposure(self) -> int:
        return 1
