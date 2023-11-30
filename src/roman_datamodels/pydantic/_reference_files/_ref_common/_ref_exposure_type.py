from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel
from ..._datamodels import common

__all__ = ["RefExposureType"]


class RefExposureType(BaseDataModel):
    type: common.ExposureType
    p_exptype: Annotated[
        str,
        Field(
            json_schema_extra={"title": "Type of data in the exposure (programmatic mode)"},
            pattern="^((WFI_IMAGE|WFI_GRISM|WFI_PRISM|WFI_DARK|WFI_FLAT|WFI_WFSC)\\s*\\|\\s*)+$",
        ),
    ]
