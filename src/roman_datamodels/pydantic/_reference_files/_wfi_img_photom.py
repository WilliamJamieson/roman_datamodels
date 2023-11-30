from typing import Annotated, Dict, Literal, Optional

import astropy.units as u
from pydantic import Field

from .._adaptors import AstropyQuantity
from .._core import BaseDataModel, BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon

__all__ = ["WfiImgPhotomRefModel"]


class WfiImgPhotomRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.PHOTOM],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]


class PhotTableEntry(BaseDataModel):
    photmjsr: Annotated[
        Optional[AstropyQuantity[float, u.MJy / u.sr, 0]],
        Field(
            json_schema_extra={
                "title": "Surface brightness, in MJy/steradian",
            },
        ),
    ]
    uncertainty: Annotated[
        Optional[AstropyQuantity[float, u.MJy / u.sr, 0]],
        Field(
            json_schema_extra={
                "title": "Uncertainty of surface brightness, in MJy/steradian",
            },
        ),
    ]
    pixelareasr: Annotated[
        Optional[AstropyQuantity[float, u.sr, 0]],
        Field(
            json_schema_extra={
                "title": "Nominal pixel area, in steradian",
            },
        ),
    ]


PhotTableKey = Annotated[
    str,
    Field(
        pattern="^(F062|F087|F106|F129|F146|F158|F184|F213|GRISM|PRISM|DARK)$",
    ),
]


class WfiImgPhotomRefModel(BaseRomanRefModel):
    meta: Annotated[
        WfiImgPhotomRefMeta,
        Field(
            json_schema_extra={
                "title": "Photom reference metadata",
            },
        ),
    ]
    phot_table: Annotated[
        Dict[PhotTableKey, PhotTableEntry],
        Field(
            json_schema_extra={
                "title": "Photometric flux conversion factors table",
            },
        ),
    ]
