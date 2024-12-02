from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from roman_datamodels.stnode import _core, _default

from ..meta import (
    CalLogs,
    Common,
    OutlierDetection,
    Photometry,
    SkyBackground,
    SourceDetection,
    Statistics,
    Wcsinfo,
)

if TYPE_CHECKING:
    from gwcs import WCS

__all__ = ["WfiImage"]


class WfiImageMeta(Common):
    """Common metadata for WfiImage"""

    @property
    def required(self) -> tuple[str]:
        return (
            *super().required,
            "photometry",
            "wcs",
        )

    @property
    def background(self) -> SkyBackground:
        return self._get_node("background", SkyBackground)

    @property
    def cal_logs(self) -> CalLogs:
        return self._get_node("cal_logs", CalLogs)

    @property
    def outlier_detection(self) -> OutlierDetection:
        return self._get_node("outlier_detection", OutlierDetection)

    @property
    def photometry(self) -> Photometry:
        return self._get_node("photometry", Photometry)

    @property
    def source_detection(self) -> SourceDetection:
        return self._get_node("source_detection", SourceDetection)

    @property
    def statistics(self) -> Statistics:
        return self._get_node("statistics", Statistics)

    @property
    def wcs(self) -> WCS | None:
        return self._get_node("wcs", _default.Wcs)

    @property
    def wcsinfo(self) -> Wcsinfo:
        return self._get_node("wcsinfo", Wcsinfo)


class WfiImage(_core.DataModelNode):
    """
    Wfi level 2 image information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wfi_image-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "data",
            "dq",
            "err",
            "var_poisson",
            "var_rnoise",
            "amp33",
            "border_ref_pix_left",
            "border_ref_pix_right",
            "border_ref_pix_top",
            "border_ref_pix_bottom",
            "dq_border_ref_pix_left",
            "dq_border_ref_pix_right",
            "dq_border_ref_pix_top",
            "dq_border_ref_pix_bottom",
        )

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("data"):
            return self.data.shape

        # Allow for one to shrink the data size default
        if self._has_node("shape"):
            return self._data["shape"]

        # default fall-back
        return (4088, 4088)

    @property
    def n_groups(self) -> int:
        # The number of groups used for the image
        if self._has_node("amp33"):
            return self.amp33.shape[0]

        # Allow for one to shrink/set the number of groups
        if self._has_node("n_groups"):
            return self._data["n_groups"]

        # default fall-back
        return 8

    @property
    def meta(self) -> WfiImageMeta:
        return self._get_node("meta", WfiImageMeta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape, dtype=np.uint32))

    @property
    def err(self) -> np.ndarray:
        return self._get_node("err", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def var_poisson(self) -> np.ndarray:
        return self._get_node("var_poisson", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def var_rnoise(self) -> np.ndarray:
        return self._get_node("var_rnoise", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def var_flat(self) -> np.ndarray:
        return self._get_node("var_flat", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def amp33(self) -> np.ndarray:
        return self._get_node("amp33", lambda: np.zeros((self.n_groups, 4096, 128), dtype=np.float32))

    @property
    def border_ref_pix_left(self) -> np.ndarray:
        return self._get_node(
            "border_ref_pix_left", lambda: np.zeros((self.n_groups, self.array_shape[0] + 8, 4), dtype=np.float32)
        )

    @property
    def border_ref_pix_right(self) -> np.ndarray:
        return self._get_node(
            "border_ref_pix_right", lambda: np.zeros((self.n_groups, self.array_shape[0] + 8, 4), dtype=np.float32)
        )

    @property
    def border_ref_pix_top(self) -> np.ndarray:
        # I think it should be 4, self.array_shape[1] + 8
        return self._get_node(
            "border_ref_pix_top", lambda: np.zeros((self.n_groups, self.array_shape[0] + 8, 4), dtype=np.float32)
        )

    @property
    def border_ref_pix_bottom(self) -> np.ndarray:
        # I think it should be 4, self.array_shape[1] + 8
        return self._get_node(
            "border_ref_pix_bottom", lambda: np.zeros((self.n_groups, self.array_shape[0] + 8, 4), dtype=np.float32)
        )

    @property
    def dq_border_ref_pix_left(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_left", lambda: np.zeros((self.array_shape[0] + 8, 4), dtype=np.uint32))

    @property
    def dq_border_ref_pix_right(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_right", lambda: np.zeros((self.array_shape[0] + 8, 4), dtype=np.uint32))

    @property
    def dq_border_ref_pix_top(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_top", lambda: np.zeros((4, self.array_shape[1] + 8), dtype=np.uint32))

    @property
    def dq_border_ref_pix_bottom(self) -> np.ndarray:
        return self._get_node("dq_border_ref_pix_bottom", lambda: np.zeros((4, self.array_shape[1] + 8), dtype=np.uint32))
