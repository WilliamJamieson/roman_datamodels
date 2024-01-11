# Generated by RAD using generator based on datamodel-code-generator
#    source schema: reference_files/superbias-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from enum import Enum
from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._model import DataModel
from roman_datamodels.core.adaptors import NdArray, np

from ..ref_common import RefCommon


class reftype(Enum):
    BIAS = "BIAS"


class meta(RefCommon):
    schema_uri: ClassVar[None] = None
    reftype: reftype


class SuperbiasRefModel(DataModel):
    """
    Super-bias reference schema
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/reference_files/superbias-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/superbias-1.0.0"

    meta: meta
    data: Annotated[NdArray[np.float32, 2, (4096, 4096)], Field(title="2-D super-bias array")]
    dq: Annotated[NdArray[np.uint32, 2, (4096, 4096)], Field(title="2-D data quality array for all planes")]
    err: Annotated[NdArray[np.float32, 2, (4096, 4096)], Field(title="2-D Error array")]
