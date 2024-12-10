from types import MappingProxyType

import numpy as np

from roman_datamodels.stnode import rad

from .meta import Common

__all__ = ["MsosStack"]


class MsosStack_Meta(rad.ImpliedNodeMixin, Common):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MsosStack

    @rad.field
    def image_list(self) -> str:
        return self._get_node("image_list", lambda: rad.NOSTR)


class MsosStack(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Level 3 schema for SSC's MSOS stack products
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/msos_stack-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/msos_stack-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/msos_stack-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> MsosStack_Meta:
        return self._get_node("meta", MsosStack_Meta)

    @rad.field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @rad.field
    def uncertainty(self) -> np.ndarray:
        return self._get_node("uncertainty", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @rad.field
    def mask(self) -> np.ndarray:
        return self._get_node("mask", lambda: np.zeros(self.array_shape, dtype=np.uint8))

    @rad.field
    def coverage(self) -> np.ndarray:
        return self._get_node("coverage", lambda: np.zeros(self.array_shape, dtype=np.uint8))
