# Generated by RAD using generator based on datamodel-code-generator
#    source schema: reference_files/ipc-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from enum import Enum
from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._model import DataModel
from roman_datamodels.core.adaptors import NdArray, np

from ..ref_common import RefCommon
from ..ref_optical_element import RefOpticalElement


class reftype(Enum):
    IPC = "IPC"


class meta(RefCommon, RefOpticalElement):
    schema_uri: ClassVar[None] = None
    reftype: reftype


class IpcRefModel(DataModel):
    """
    IPC kernel reference schema
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ipc-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/ipc-1.0.0"

    meta: meta
    data: Annotated[
        NdArray[np.float32, 2, (3, 3)],
        Field(
            description="Reference kernel used for convolving with data in order to correct\nfor interpixel capacitance\n",
            title="Interpixel capacitance correction kernel array",
        ),
    ]