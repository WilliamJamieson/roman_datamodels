from typing import Annotated

from pydantic import Field

from ..._adaptors import AstropyTime
from ..._core import BaseDataModel
from ..._datamodels import common
from ..._enums import instrument, origin, pedigree, telescope

__all__ = ["RefCommon"]


class Instrument(BaseDataModel):
    name: Annotated[
        instrument,
        Field(
            json_schema_extra={
                "title": "Name of the instrument",
            },
        ),
    ]
    detector: common.WfiMode


class RefCommon(BaseDataModel):
    reftype: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Reference File Type",
            },
        ),
    ]
    pedigree: Annotated[
        pedigree,
        Field(
            json_schema_extra={
                "title": "The pedigree of the reference file",
            },
        ),
    ]
    description: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Description of the reference file",
            },
        ),
    ]
    author: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Author of the reference file",
            },
        ),
    ]
    useafter: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "Use after date of the reference file",
            },
        ),
    ]
    telescope: Annotated[
        telescope,
        Field(
            json_schema_extra={
                "title": "Telescope that reference file is used to calibrate",
            },
        ),
    ]
    origin: Annotated[
        origin,
        Field(
            json_schema_extra={
                "title": "Organization responsible for creating file",
            },
        ),
    ]
    instrument: Annotated[
        Instrument,
        Field(
            json_schema_extra={
                "title": "Instrument that reference file is used to calibrate",
            },
        ),
    ]
