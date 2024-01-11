# Generated by RAD using generator based on datamodel-code-generator
#    source schema: ref_exposure_type-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._base import BaseDataModel

from . import exposure_type


class exposure(BaseDataModel):
    schema_uri: ClassVar[None] = None
    type: exposure_type.ExposureType
    p_exptype: Annotated[
        str,
        Field(
            pattern="^((WFI_IMAGE|WFI_GRISM|WFI_PRISM|WFI_DARK|WFI_FLAT|WFI_WFSC)\\s*\\|\\s*)+$",
            title="Applicable exposure type.",
        ),
    ]


class RefExposureType(BaseDataModel):
    """
    Type of data in the reference file exposure (viewing mode)
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/ref_exposure_type-1.0.0"

    exposure: exposure
