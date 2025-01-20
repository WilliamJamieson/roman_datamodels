from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry
from .ref.ref_mixes import _RefCommonRefOpticalElementRef

__all__ = ["PixelareaRef"]


class PixelareaRef_Meta_Photometry(rad.ImpliedNodeMixin[float | None], rad.ObjectNode[float | None]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return PixelareaRef_Meta

    @property
    @rad.field
    def pixelarea_steradians(self: rad.Node) -> float | None:
        return rad.NONUM

    @property
    @rad.field
    def pixelarea_arcsecsq(self: rad.Node) -> float | None:
        return rad.NONUM


_PixelareaRef_Meta: TypeAlias = _RefCommonRefOpticalElementRef | PixelareaRef_Meta_Photometry


class PixelareaRef_Meta(rad.ImpliedNodeMixin[_PixelareaRef_Meta], RefCommonRefOpticalElementRef[_PixelareaRef_Meta]):  # type: ignore[misc]
    @classmethod
    def asdf_implied_by(cls) -> type:
        return PixelareaRef

    @property
    @rad.field
    def reftype(self: rad.Node) -> RefTypeEntry:
        return RefTypeEntry.AREA

    @property
    @rad.field
    def photometry(self: rad.Node) -> PixelareaRef_Meta_Photometry:
        return PixelareaRef_Meta_Photometry()


_PixelareaRef: TypeAlias = PixelareaRef_Meta | npt.NDArray[np.float32]


class PixelareaRef(rad.TaggedObjectNode[_PixelareaRef], rad.ArrayFieldMixin[_PixelareaRef]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/pixelarea-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/pixelarea-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/pixelarea-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @property
    @rad.field
    def meta(self: rad.Node) -> PixelareaRef_Meta:
        return PixelareaRef_Meta()

    @property
    @rad.field
    def data(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)
