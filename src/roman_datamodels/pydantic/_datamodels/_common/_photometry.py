from typing import Annotated, Optional

import astropy.units as u
import numpy as np
from pydantic import Field

from ..._adaptors import AstropyQuantity
from ..._core import BaseDataModel

__all__ = ["Photometry"]


class Photometry(BaseDataModel):
    conversion_megajanskys: Annotated[
        Optional[AstropyQuantity[np.float64, u.MJy / u.sr, 0]],
        Field(
            json_schema_extra={
                "title": "Flux density (MJy/steradian) producing 1 cps",
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.conversion_megajanskys",
                    ],
                },
            },
        ),
    ]
    conversion_microjanskys: Annotated[
        Optional[AstropyQuantity[np.float64, u.uJy / (u.arcsec**2), 0]],
        Field(
            json_schema_extra={
                "title": "Flux density (uJy/arcsec2) producing 1 cps",
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.conversion_microjanskys",
                    ],
                },
            },
        ),
    ]
    pixelarea_steradians: Annotated[
        Optional[AstropyQuantity[np.float64, u.sr, 0]],
        Field(
            json_schema_extra={
                "title": "Nominal pixel area in steradians",
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.pixelarea_steradians",
                    ],
                },
            },
        ),
    ]
    pixelarea_arcsecsq: Annotated[
        Optional[AstropyQuantity[np.float64, u.arcsec**2, 0]],
        Field(
            json_schema_extra={
                "title": "Nominal pixel area in arcsec^2",
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.pixelarea_arcsecsq",
                    ],
                },
            },
        ),
    ]
    conversion_megajanskys_uncertainty: Annotated[
        Optional[AstropyQuantity[np.float64, u.MJy / u.sr, 0]],
        Field(
            json_schema_extra={
                "title": "Uncertainty in flux density conversion to MJy/steradians",
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.conversion_megajanskys_uncertainty",
                    ],
                },
            },
        ),
    ]
    conversion_microjanskys_uncertainty: Annotated[
        Optional[AstropyQuantity[np.float64, u.uJy / (u.arcsec**2), 0]],
        Field(
            json_schema_extra={
                "title": "Uncertainty in flux density conversion to uJy/arcsec2",
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.conversion_microjanskys_uncertainty",
                    ],
                },
            },
        ),
    ]
