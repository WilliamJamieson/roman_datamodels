from typing import Annotated, ClassVar, Optional

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from ..._adaptors import AstropyQuantity
from ..._archive import Archive, ArchiveCatalog
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_quantity_factory
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Photometry"]


_SHAPE = ()


class Photometry(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.PHOTOMETRY.value
    _tag_uri: ClassVar = asdf_tag_uri.PHOTOMETRY.value

    model_config = ConfigDict(
        title="Photometry information",
    )

    conversion_megajanskys: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.MJy / u.sr]],
        Field(
            default_factory=default_quantity_factory(np.float64, _SHAPE, u.MJy / u.sr),
            title="Flux density (MJy/steradian) producing 1 cps",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.conversion_megajanskys",
                    ],
                ),
            ),
        ),
    ]
    conversion_microjanskys: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.uJy / (u.arcsec**2)]],
        Field(
            default_factory=default_quantity_factory(np.float64, _SHAPE, u.uJy / (u.arcsec**2)),
            title="Flux density (uJy/arcsec2) producing 1 cps",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.conversion_microjanskys",
                    ],
                ),
            ),
        ),
    ]
    pixelarea_steradians: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.sr]],
        Field(
            default_factory=default_quantity_factory(np.float64, _SHAPE, u.sr),
            title="Nominal pixel area in steradians",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.pixelarea_steradians",
                    ],
                ),
            ),
        ),
    ]
    pixelarea_arcsecsq: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.arcsec**2]],
        Field(
            default_factory=default_quantity_factory(np.float64, _SHAPE, u.arcsec**2),
            title="Nominal pixel area in arcsec^2",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.pixelarea_arcsecsq",
                    ],
                ),
            ),
        ),
    ]
    conversion_megajanskys_uncertainty: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.MJy / u.sr]],
        Field(
            default_factory=default_quantity_factory(np.float64, _SHAPE, u.MJy / u.sr),
            title="Uncertainty in flux density conversion to MJy/steradians",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.conversion_megajanskys_uncertainty",
                    ],
                ),
            ),
        ),
    ]
    conversion_microjanskys_uncertainty: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.uJy / (u.arcsec**2)]],
        Field(
            default_factory=default_quantity_factory(np.float64, _SHAPE, u.uJy / (u.arcsec**2)),
            title="Uncertainty in flux density conversion to uJy/arcsec2",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.conversion_microjanskys_uncertainty",
                    ],
                ),
            ),
        ),
    ]
