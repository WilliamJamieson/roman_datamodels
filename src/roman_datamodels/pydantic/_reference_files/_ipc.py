from typing import Annotated, Literal

import numpy as np
from pydantic import Field

from .._adaptors import NdArray
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon, RefOpticalElement

__all__ = ["IpcRefModel"]


class IpcRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.IPC],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]


class IpcRefModel(BaseRomanRefModel):
    meta: Annotated[
        IpcRefMeta,
        Field(
            json_schema_extra={
                "title": "IPC reference metadata",
            },
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            json_schema_extra={
                "title": "Interpixel capacitance correction kernel array",
                "description": (
                    "Reference kernel used for convolving with data in order to correct " "for interpixel capacitance"
                ),
            },
        ),
    ]
