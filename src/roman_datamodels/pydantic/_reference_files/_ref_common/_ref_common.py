from typing import Annotated, ClassVar

from astropy.time import Time
from pydantic import ConfigDict, Field

from ..._adaptors import AstropyTime
from ..._core import BaseRomanModel, BaseRomanURIModel
from ..._datamodels import common
from ..._defaults import default_constant_factory, default_model_factory
from ..._strenum import StrEnum
from ..._uri import asdf_uri

__all__ = ["RefCommon", "reftype"]


class reftype(StrEnum):
    DARK = "DARK"
    DISTORTION = "DISTORTION"
    FLAT = "FLAT"
    GAIN = "GAIN"
    INVERSELINEARITY = "INVERSELINEARITY"
    IPC = "IPC"
    LINEARITY = "LINEARITY"
    MASK = "MASK"
    PIXELAREA = "PIXELAREA"
    READNOISE = "READNOISE"
    REFPIX = "REFPIX"
    SATURATION = "SATURATION"
    BIAS = "BIAS"
    PHOTOM = "PHOTOM"


class pedigree(StrEnum):
    GROUND = "GROUND"
    MODEL = "MODEL"
    DUMMY = "DUMMY"
    SIMULATION = "SIMULATION"


class Instrument(BaseRomanModel):
    name: Annotated[
        common.instrument,
        Field(
            default_factory=default_constant_factory(common.instrument.WFI.value),
            title="Instrument used to acquire the data",
        ),
    ]
    detector: common.WfiDetector


class RefCommon(BaseRomanURIModel):
    _uri: ClassVar = asdf_uri.REF_COMMON.value

    model_config = ConfigDict(title="Common reference metadata properties")

    reftype: Annotated[
        reftype,
        Field(
            default_factory=default_constant_factory(reftype.DARK.value),
            title="Reference File Type",
        ),
    ]
    pedigree: Annotated[
        pedigree,
        Field(
            default_factory=default_constant_factory(pedigree.GROUND.value),
            title="The pedigree of the reference file",
        ),
    ]
    description: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("test description"),
            title="Description of the reference file",
        ),
    ]
    author: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("test author"),
            title="Author of the reference file",
        ),
    ]
    useafter: Annotated[
        AstropyTime,
        Field(
            default_factory=default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="Use after date of the reference file",
        ),
    ]
    telescope: Annotated[
        common.telescope,
        Field(
            default_factory=default_constant_factory(common.telescope.ROMAN.value),
            title="Telescope that reference file is used to calibrate",
        ),
    ]
    origin: Annotated[
        common.origin,
        Field(
            default_factory=default_constant_factory(common.origin.STSCI.value),
            title="Organization responsible for creating file",
        ),
    ]
    instrument: Annotated[
        Instrument,
        Field(
            default_factory=default_model_factory(Instrument),
        ),
    ]