from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt
from gwcs import WCS

from roman_datamodels.stnode import rad

from .meta import (
    CalLogs,
    Common,
    L2CalStep,
    OutlierDetection,
    Photometry,
    SkyBackground,
    SourceCatalog,
    Statistics,
    Wcsinfo,
)
from .meta.common import _Common

__all__ = ["WfiImage"]


_WfiImage_Meta: TypeAlias = (
    _Common
    | SkyBackground
    | CalLogs
    | L2CalStep
    | OutlierDetection
    | Photometry
    | SourceCatalog
    | Statistics
    | WCS
    | Wcsinfo
    | None
)


class WfiImage_Meta(rad.ImpliedNodeMixin[_WfiImage_Meta], Common[_WfiImage_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return WfiImage

    @rad.field
    def background(self) -> SkyBackground:
        return SkyBackground()

    @rad.field
    def cal_logs(self) -> CalLogs:
        return CalLogs.default()

    @rad.field
    def cal_step(self) -> L2CalStep:
        return L2CalStep()

    @rad.field
    def outlier_detection(self) -> OutlierDetection:
        return OutlierDetection()

    @rad.field
    def photometry(self) -> Photometry:
        return Photometry()

    @rad.field
    def source_catalog(self) -> SourceCatalog:
        return SourceCatalog()

    @rad.field
    def statistics(self) -> Statistics:
        return Statistics()

    @rad.field
    def wcs(self) -> WCS | None:
        return rad.Wcs()

    @rad.field
    def wcsinfo(self) -> Wcsinfo:
        return Wcsinfo()


_WfiImage: TypeAlias = WfiImage_Meta | npt.NDArray[np.float32] | npt.NDArray[np.uint32] | npt.NDArray[np.uint16]


class WfiImage(rad.TaggedObjectNode[_WfiImage], rad.ArrayFieldMixin[_WfiImage]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/wfi_image-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/wfi_image-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/wfi_image-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4088, 4088)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @property
    def _n_groups(self) -> int:
        # The number of groups used for the image
        if self._has_node("amp33"):
            n_groups: int = self.amp33.shape[0]
            return n_groups

        # Allow for one to shrink/set the number of groups
        if self._has_node("_n_groups"):
            # MyPy doesn't allow us to down cast to the specific type
            # we expect here
            return self._data["_n_groups"]  # type: ignore[return-value]

        # default fall-back
        return 8

    @rad.field
    def meta(self) -> WfiImage_Meta:
        return WfiImage_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape, dtype=np.uint32)

    @rad.field
    def err(self) -> npt.NDArray[np.float32]:
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
    def amp33(self) -> npt.NDArray[np.uint16]:
        return np.zeros((self._n_groups, self.array_shape[0], 128), dtype=np.uint16)

    @rad.field
    def border_ref_pix_left(self) -> npt.NDArray[np.float32]:
        return np.zeros((self._n_groups, self.array_shape[0] + 8, 4), dtype=np.float32)

    @rad.field
    def border_ref_pix_right(self) -> npt.NDArray[np.float32]:
        return np.zeros((self._n_groups, self.array_shape[0] + 8, 4), dtype=np.float32)

    @rad.field
    def border_ref_pix_top(self) -> npt.NDArray[np.float32]:
        return np.zeros((self._n_groups, 4, self.array_shape[1] + 8), dtype=np.float32)

    @rad.field
    def border_ref_pix_bottom(self) -> npt.NDArray[np.float32]:
        # I think it should be 4, self.array_shape[1] + 8
        return np.zeros((self._n_groups, 4, self.array_shape[1] + 8), dtype=np.float32)

    @rad.field
    def dq_border_ref_pix_left(self) -> npt.NDArray[np.uint32]:
        return np.zeros((self.array_shape[0] + 8, 4), dtype=np.uint32)

    @rad.field
    def dq_border_ref_pix_right(self) -> npt.NDArray[np.uint32]:
        return np.zeros((self.array_shape[0] + 8, 4), dtype=np.uint32)

    @rad.field
    def dq_border_ref_pix_top(self) -> npt.NDArray[np.uint32]:
        return np.zeros((4, self.array_shape[1] + 8), dtype=np.uint32)

    @rad.field
    def dq_border_ref_pix_bottom(self) -> npt.NDArray[np.uint32]:
        return np.zeros((4, self.array_shape[1] + 8), dtype=np.uint32)
