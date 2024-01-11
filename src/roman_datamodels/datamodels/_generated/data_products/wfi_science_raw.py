# Generated by RAD using generator based on datamodel-code-generator
#    source schema: data_products/wfi_science_raw-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._model import DataModel
from roman_datamodels.core.adaptors import AstropyQuantity, NdArray, Unit, np

from .. import common


class WfiScienceRawModel(DataModel):
    """
    The schema for Level 1 WFI science data (both imaging and spectrographic).

    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/data_products/wfi_science_raw-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/data_products/wfi_science_raw-1.0.0"

    meta: common.Common
    data: Annotated[
        AstropyQuantity[np.uint16, 3, Unit("DN"), (8, 4096, 4096)],
        Field(title="Science data, including the border reference pixels."),
    ]
    amp33: Annotated[AstropyQuantity[np.uint16, 3, Unit("DN"), (8, 4096, 128)], Field(title="Amp 33 reference pixel data.")]
    resultantdq: Annotated[
        NdArray[np.uint8, 3, (8, 4096, 4096)] | None,
        Field(None, title="Optional 3-D data quality array (plane dq for each resultant)"),
    ]
