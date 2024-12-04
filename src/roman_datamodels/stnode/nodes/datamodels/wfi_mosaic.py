import numpy as np
from gwcs import WCS

from roman_datamodels.stnode import _core, _default

from ..meta import (
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


class WfiMosaic_Meta(Basic):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "asn",
            "basic",
            "cal_step",
            "photometry",
            "program",
            "resample",
            "wcs",
            "wcsinfo",
        )

    @property
    def asn(self) -> MosaicAssociations:
        return self._get_node("asn", MosaicAssociations)

    @property
    def basic(self) -> MosaicBasic:
        return self._get_node("basic", MosaicBasic)

    @property
    def cal_step(self) -> L3CalStep:
        return self._get_node("cal_step", L3CalStep)

    @property
    def coordinates(self) -> Coordinates:
        return self._get_node("coordinates", Coordinates)

    @property
    def individual_image_meta(self) -> IndividualImageMeta:
        return self._get_node("individual_image_meta", IndividualImageMeta)

    @property
    def photometry(self) -> Photometry:
        return self._get_node("photometry", Photometry)

    @property
    def program(self) -> Program:
        return self._get_node("program", Program)

    @property
    def ref_file(self) -> RefFile:
        return self._get_node("ref_file", RefFile)

    @property
    def resample(self) -> Resample:
        return self._get_node("resample", Resample)

    @property
    def wcs(self) -> WCS | None:
        return self._get_node("wcs", _default.Wcs)

    @property
    def wcsinfo(self) -> MosaicWcsinfo:
        return self._get_node("wcsinfo", MosaicWcsinfo)


class WfiMosaic(_core.DataModelNode):
    """
    WFI Level 3 mosaics data
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wfi_mosaic-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
            "context",
            "err",
            "weight",
            "var_poisson",
            "var_rnoise",
            "cal_logs",
        )

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

    @property
    def meta(self) -> WfiMosaic_Meta:
        return self._get_node("meta", WfiMosaic_Meta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def err(self) -> np.ndarray:
        return self._get_node("err", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def context(self) -> np.ndarray:
        return self._get_node("context", lambda: np.zeros((self._n_images, *self.array_shape), dtype=np.uint32))

    @property
    def weight(self) -> np.ndarray:
        return self._get_node("weight", lambda: np.zeros(self.array_shape, dtype=np.float32))

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
    def cal_logs(self) -> CalLogs:
        return self._get_node("cal_logs", CalLogs.default)
