from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel

__all__ = ["SourceDetection"]


class SourceDetection(BaseDataModel):
    tweakreg_catalog_name: Annotated[str, Field()]
