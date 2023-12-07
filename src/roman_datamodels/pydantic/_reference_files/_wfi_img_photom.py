from typing import Annotated, ClassVar, Dict, Literal, Optional

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity
from .._core import BaseRomanModel, BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_num_value
from .._enums import reftype
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon

__all__ = ["WfiImgPhotomRefModel"]


class WfiImgPhotomRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.PHOTOM],
        Field(
            default_factory=default_constant_factory(reftype.PHOTOM.value),
            title="Reference file type",
        ),
    ]


class PhotTableEntry(BaseRomanModel):
    model_config = ConfigDict()

    photmjsr: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.MJy / u.sr]],
        Field(
            title="Surface brightness, in MJy/steradian",
        ),
    ]
    uncertainty: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.MJy / u.sr]],
        Field(
            title="Uncertainty of surface brightness, in MJy/steradian",
        ),
    ]
    pixelareasr: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.sr]],
        Field(
            title="Nominal pixel area, in steradian",
        ),
    ]


PhotTableKey = Annotated[
    str,
    Field(
        pattern="^(F062|F087|F106|F129|F146|F158|F184|F213|GRISM|PRISM|DARK)$",
    ),
]


def default_phot_table_factory() -> dict[str, PhotTableEntry]:
    entries = (
        "F062",
        "F087",
        "F106",
        "F129",
        "F146",
        "F158",
        "F184",
        "F213",
        "GRISM",
        "PRISM",
        "DARK",
    )

    phot_table = {}
    for entry in entries:
        photmjsr = None
        uncertainty = None
        pixelareasr = 1.0e-13 * u.sr
        if entry not in ("GRISM", "PRISM", "DARK"):
            photmjsr = float(default_num_value.NONUM.value) * u.MJy / u.sr
            uncertainty = float(default_num_value.NONUM.value) * u.MJy / u.sr

        phot_table[entry] = PhotTableEntry(
            photmjsr=photmjsr,
            uncertainty=uncertainty,
            pixelareasr=pixelareasr,
        )

    return phot_table


class WfiImgPhotomRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.WFI_IMG_PHOTOM.value
    _tag_uri: ClassVar = asdf_tag_uri.WFI_IMG_PHOTOM.value

    model_config = ConfigDict(
        title="WFI imaging photometric reference schema",
    )

    meta: Annotated[
        WfiImgPhotomRefMeta,
        Field(
            default_factory=default_model_factory(WfiImgPhotomRefMeta),
            title="Photom reference metadata",
        ),
    ]
    phot_table: Annotated[
        Dict[PhotTableKey, PhotTableEntry],
        Field(
            default_factory=default_phot_table_factory,
            title="Photometric flux conversion factors table",
        ),
    ]
