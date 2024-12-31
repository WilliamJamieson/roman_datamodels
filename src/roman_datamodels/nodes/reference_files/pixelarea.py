from types import MappingProxyType

import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry

__all__ = ["PixelareaRef"]


class PixelareaRef_Meta_Photometry(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return PixelareaRef_Meta

    @rad.field
    def pixelarea_steradians(self) -> u.Quantity | None:
        return float(rad.NONUM) * u.sr

    @rad.field
    def pixelarea_arcsecsq(self) -> u.Quantity | None:
        return float(rad.NONUM) * u.arcsec**2


class PixelareaRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return PixelareaRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.AREA

    @rad.field
    def photometry(self) -> PixelareaRef_Meta_Photometry:
        return PixelareaRef_Meta_Photometry()


class PixelareaRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Pixel area reference schema
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/pixelarea-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/pixelarea-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/pixelarea-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> PixelareaRef_Meta:
        return PixelareaRef_Meta()

    @rad.field
    def data(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.float32)
