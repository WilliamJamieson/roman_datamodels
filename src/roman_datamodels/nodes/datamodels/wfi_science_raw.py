from types import MappingProxyType

import numpy as np

from roman_datamodels.stnode import rad

from .meta import Common

__all__ = ["WfiScienceRaw"]


class WfiScienceRaw_Meta(rad.ImpliedNodeMixin, Common):
    """
    The metadata for the WfiScienceRaw node
    -> only exists so that model_type can be correctly inferred
    """

    @classmethod
    def asdf_implied_by(cls) -> type:
        return WfiScienceRaw


class WfiScienceRaw(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Basic Roman Raw Science
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/wfi_science_raw-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/wfi_science_raw-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/wfi_science_raw-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> WfiScienceRaw_Meta:
        return WfiScienceRaw_Meta()

    @rad.field
    def data(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.uint16)

    @rad.field
    def amp33(self) -> np.ndarray:
        return np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16)

    @rad.field
    def resultantdq(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.uint8)
