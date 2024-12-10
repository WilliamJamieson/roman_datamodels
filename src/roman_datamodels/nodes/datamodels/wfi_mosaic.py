from types import MappingProxyType

import numpy as np
from gwcs import WCS

from roman_datamodels.stnode import rad

from .meta import (
    Basic,
    CalLogs,
    Coordinates,
    IndividualImageMeta,
    L3CalStep,
    MosaicAssociations,
    MosaicBasic,
    MosaicWcsinfo,
    Photometry,
    Program,
    RefFile,
    Resample,
)

__all__ = ["WfiMosaic"]


class WfiMosaic_Meta(rad.ImpliedNodeMixin, Basic):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return WfiMosaic

    @rad.field
    def asn(self) -> MosaicAssociations:
        return self._get_node("asn", MosaicAssociations)

    @rad.field
    def basic(self) -> MosaicBasic:
        return self._get_node("basic", MosaicBasic)

    @rad.field
    def cal_step(self) -> L3CalStep:
        return self._get_node("cal_step", L3CalStep)

    @rad.field
    def coordinates(self) -> Coordinates:
        return self._get_node("coordinates", Coordinates)

    @rad.field
    def individual_image_meta(self) -> IndividualImageMeta:
        return self._get_node("individual_image_meta", IndividualImageMeta)

    @rad.field
    def photometry(self) -> Photometry:
        return self._get_node("photometry", Photometry)

    @rad.field
    def program(self) -> Program:
        return self._get_node("program", Program)

    @rad.field
    def ref_file(self) -> RefFile:
        return self._get_node("ref_file", RefFile)

    @rad.field
    def resample(self) -> Resample:
        return self._get_node("resample", Resample)

    @rad.field
    def wcs(self) -> WCS | None:
        return self._get_node("wcs", rad.Wcs)

    @rad.field
    def wcsinfo(self) -> MosaicWcsinfo:
        return self._get_node("wcsinfo", MosaicWcsinfo)


class WfiMosaic(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    WFI Level 3 mosaics data
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/wfi_mosaic-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/wfi_mosaic-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/wfi_mosaic-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4088, 4088)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("data"):
            return self.data.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (4088, 4088)

    @property
    def _n_images(self) -> int:
        # The number of images in the mosaic comes from the context array
        if self._has_node("context"):
            return self.context.shape[0]

        # Allow for one to shrink/set the number of images
        if self._has_node("n_images"):
            return self._data["n_images"]

        # default fall-back
        return 2

    @rad.field
    def meta(self) -> WfiMosaic_Meta:
        return self._get_node("meta", WfiMosaic_Meta)

    @rad.field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def err(self) -> np.ndarray:
        return self._get_node("err", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def context(self) -> np.ndarray:
        return self._get_node("context", lambda: np.zeros((self._n_images, *self.array_shape), dtype=np.uint32))

    @rad.field
    def weight(self) -> np.ndarray:
        return self._get_node("weight", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def var_poisson(self) -> np.ndarray:
        return self._get_node("var_poisson", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def var_rnoise(self) -> np.ndarray:
        return self._get_node("var_rnoise", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def var_flat(self) -> np.ndarray:
        return self._get_node("var_flat", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def cal_logs(self) -> CalLogs:
        return self._get_node("cal_logs", CalLogs.default)
