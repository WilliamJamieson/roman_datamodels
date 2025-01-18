from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt
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
from .meta.basic import _Basic

__all__ = ["WfiMosaic"]


_WfiMosaic_Meta: TypeAlias = (
    _Basic
    | MosaicAssociations
    | MosaicBasic
    | L3CalStep
    | Coordinates
    | IndividualImageMeta
    | Photometry
    | Program
    | RefFile
    | Resample
    | WCS
    | MosaicWcsinfo
    | None
)


class WfiMosaic_Meta(rad.ImpliedNodeMixin[_WfiMosaic_Meta], Basic[_WfiMosaic_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return WfiMosaic

    @rad.field
    def asn(self) -> MosaicAssociations:
        return MosaicAssociations()

    @rad.field
    def basic(self) -> MosaicBasic:
        return MosaicBasic()

    @rad.field
    def cal_step(self) -> L3CalStep:
        return L3CalStep()

    @rad.field
    def coordinates(self) -> Coordinates:
        return Coordinates()

    @rad.field
    def individual_image_meta(self) -> IndividualImageMeta:
        return IndividualImageMeta()

    @rad.field
    def photometry(self) -> Photometry:
        return Photometry()

    @rad.field
    def program(self) -> Program:
        return Program()

    @rad.field
    def ref_file(self) -> RefFile:
        return RefFile()

    @rad.field
    def resample(self) -> Resample:
        return Resample()

    @rad.field
    def wcs(self) -> WCS | None:
        return rad.Wcs()

    @rad.field
    def wcsinfo(self) -> MosaicWcsinfo:
        return MosaicWcsinfo()


_WfiMosaic: TypeAlias = WfiMosaic_Meta | CalLogs | npt.NDArray[np.float32] | npt.NDArray[np.uint32] | int


class WfiMosaic(rad.TaggedObjectNode[_WfiMosaic], rad.ArrayFieldMixin[_WfiMosaic]):
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
    def default_array_shape(self) -> tuple[int, int]:
        return (4088, 4088)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @property
    def _n_images(self) -> int:
        # The number of images in the mosaic comes from the context array
        if self._has_node("context"):
            n_images: int = self.context.shape[0]
            return n_images

        # Allow for one to shrink/set the number of images
        if self._has_node("_n_images"):
            # MyPy doesn't allow us to down cast to the specific type
            # we expect here
            return self._data["_n_images"]  # type: ignore[return-value]

        # default fall-back
        return 2

    @rad.field
    def meta(self) -> WfiMosaic_Meta:
        return WfiMosaic_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def err(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def context(self) -> npt.NDArray[np.uint32]:
        return np.zeros((self._n_images, *self.array_shape), dtype=np.uint32)

    @rad.field
    def weight(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def var_poisson(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def var_rnoise(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def var_flat(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def cal_logs(self) -> CalLogs:
        return CalLogs.default()
