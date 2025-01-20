from types import MappingProxyType
from typing import TypeAlias, cast

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

    @property
    @rad.field
    def background(self: rad.Node) -> SkyBackground:
        return SkyBackground()

    @property
    @rad.field
    def cal_logs(self: rad.Node) -> CalLogs:
        return CalLogs.default()

    @property
    @rad.field
    def cal_step(self: rad.Node) -> L2CalStep:
        return L2CalStep()

    @property
    @rad.field
    def outlier_detection(self: rad.Node) -> OutlierDetection:
        return OutlierDetection()

    @property
    @rad.field
    def photometry(self: rad.Node) -> Photometry:
        return Photometry()

    @property
    @rad.field
    def source_catalog(self: rad.Node) -> SourceCatalog:
        return SourceCatalog()

    @property
    @rad.field
    def statistics(self: rad.Node) -> Statistics:
        return Statistics()

    @property
    @rad.field
    def wcs(self: rad.Node) -> WCS | None:
        return rad.Wcs()

    @property
    @rad.field
    def wcsinfo(self: rad.Node) -> Wcsinfo:
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
            return cast(int, self._data["_n_groups"])

        # default fall-back
        return 8

    @property
    @rad.field
    def meta(self: rad.Node) -> WfiImage_Meta:
        return WfiImage_Meta()

    @property
    @rad.field
    def data(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def dq(self: rad.Node) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape, dtype=np.uint32)

    @property
    @rad.field
    def err(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def var_poisson(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def var_rnoise(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def var_flat(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def amp33(self: rad.Node) -> npt.NDArray[np.uint16]:
        return np.zeros((self._n_groups, self.array_shape[0], 128), dtype=np.uint16)

    @property
    @rad.field
    def border_ref_pix_left(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros((self._n_groups, self.array_shape[0] + 8, 4), dtype=np.float32)

    @property
    @rad.field
    def border_ref_pix_right(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros((self._n_groups, self.array_shape[0] + 8, 4), dtype=np.float32)

    @property
    @rad.field
    def border_ref_pix_top(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros((self._n_groups, 4, self.array_shape[1] + 8), dtype=np.float32)

    @property
    @rad.field
    def border_ref_pix_bottom(self: rad.Node) -> npt.NDArray[np.float32]:
        # I think it should be 4, self.array_shape[1] + 8
        return np.zeros((self._n_groups, 4, self.array_shape[1] + 8), dtype=np.float32)

    @property
    @rad.field
    def dq_border_ref_pix_left(self: rad.Node) -> npt.NDArray[np.uint32]:
        return np.zeros((self.array_shape[0] + 8, 4), dtype=np.uint32)

    @property
    @rad.field
    def dq_border_ref_pix_right(self: rad.Node) -> npt.NDArray[np.uint32]:
        return np.zeros((self.array_shape[0] + 8, 4), dtype=np.uint32)

    @property
    @rad.field
    def dq_border_ref_pix_top(self: rad.Node) -> npt.NDArray[np.uint32]:
        return np.zeros((4, self.array_shape[1] + 8), dtype=np.uint32)

    @property
    @rad.field
    def dq_border_ref_pix_bottom(self: rad.Node) -> npt.NDArray[np.uint32]:
        return np.zeros((4, self.array_shape[1] + 8), dtype=np.uint32)
