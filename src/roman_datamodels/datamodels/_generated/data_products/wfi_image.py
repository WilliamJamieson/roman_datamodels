# Generated by RAD using generator based on datamodel-code-generator
#    source schema: data_products/wfi_image-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._base import BaseDataModel
from roman_datamodels.core._model import DataModel
from roman_datamodels.core.adaptors import AstropyQuantity, NdArray, Unit, np

from .. import photometry
from ..common import Common


class source_detection(BaseDataModel):
    """
    Source catalog generated by the Source Detection Step for TweakReg.
    """

    schema_uri: ClassVar[None] = None
    tweakreg_catalog_name: str


class meta(Common):
    schema_uri: ClassVar[None] = None
    photometry: photometry.Photometry
    source_detection: Annotated[
        source_detection | None, Field(None, title="Source catalog generated by the Source Detection Step for TweakReg.")
    ]


class WfiImageModel(DataModel):
    """
    The schema for WFI Level 2 images.

    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/data_products/wfi_image-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/data_products/wfi_image-1.0.0"

    meta: meta
    data: Annotated[
        AstropyQuantity[np.float32, 2, Unit("electron / s"), (4088, 4088)],
        Field(title="Science data, excluding border reference pixels."),
    ]
    dq: NdArray[np.uint32, 2, (4088, 4088)]
    err: AstropyQuantity[np.float32, 2, Unit("electron / s"), (4088, 4088)]
    var_poisson: AstropyQuantity[np.float32, 2, Unit("electron2 / s2"), (4088, 4088)]
    var_rnoise: AstropyQuantity[np.float32, 2, Unit("electron2 / s2"), (4088, 4088)]
    var_flat: AstropyQuantity[np.float32, 2, Unit("electron2 / s2"), (4088, 4088)] | None = None
    amp33: Annotated[AstropyQuantity[np.uint16, 3, Unit("DN"), (8, 4096, 128)], Field(title="Amp 33 reference pixel data")]
    border_ref_pix_left: Annotated[
        AstropyQuantity[np.float32, 3, Unit("DN"), (8, 4096, 4)],
        Field(title="Original border reference pixels, on left (from viewers perspective)."),
    ]
    border_ref_pix_right: Annotated[
        AstropyQuantity[np.float32, 3, Unit("DN"), (8, 4096, 4)],
        Field(title="Original border reference pixels, on right (from viewers perspective)."),
    ]
    border_ref_pix_top: Annotated[
        AstropyQuantity[np.float32, 3, Unit("DN"), (8, 4, 4096)], Field(title="Original border reference pixels, on top.")
    ]
    border_ref_pix_bottom: Annotated[
        AstropyQuantity[np.float32, 3, Unit("DN"), (8, 4, 4096)], Field(title="Original border reference pixels, on bottom.")
    ]
    dq_border_ref_pix_left: Annotated[
        NdArray[np.uint32, 2, (4096, 4)], Field(title="DQ for border reference pixels, on left (from viewers perspective).")
    ]
    dq_border_ref_pix_right: Annotated[
        NdArray[np.uint32, 2, (4096, 4)], Field(title="DQ for border reference pixels, on right (from viewers perspective).")
    ]
    dq_border_ref_pix_top: Annotated[NdArray[np.uint32, 2, (4, 4096)], Field(title="DQ for border reference pixels, on top.")]
    dq_border_ref_pix_bottom: Annotated[
        NdArray[np.uint32, 2, (4, 4096)], Field(title="DQ for border reference pixels, on bottom.")
    ]
    cal_logs: Annotated[list[str], Field(title="Calibration log messages")]
