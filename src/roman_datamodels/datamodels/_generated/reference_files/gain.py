# Generated by RAD using generator based on datamodel-code-generator
#    source schema: reference_files/gain-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from enum import Enum
from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._model import DataModel
from roman_datamodels.core.adaptors import AstropyQuantity, Unit, np

from ..ref_common import RefCommon


class reftype(Enum):
    GAIN = "GAIN"


class meta(RefCommon):
    schema_uri: ClassVar[None] = None
    reftype: reftype


class GainRefModel(DataModel):
    """
    Gain reference schema
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/reference_files/gain-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/gain-1.0.0"

    meta: meta
    data: Annotated[AstropyQuantity[np.float32, 2, Unit("electron / DN"), (4096, 4096)], Field(title="The detector gain map")]
