from typing import Annotated, ClassVar

from astropy.time import Time
from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _adaptors, _core, _datamodels, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["RefCommon", "ref_type"]


class ref_type(_strenum.StrEnum):
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


class pedigree(_strenum.StrEnum):
    GROUND = "GROUND"
    MODEL = "MODEL"
    DUMMY = "DUMMY"
    SIMULATION = "SIMULATION"


class Instrument(_core.BaseRomanModel):
    name: Annotated[
        _datamodels.common.instrument,
        Field(
            default_factory=_defaults.default_constant_factory(_datamodels.common.instrument.WFI.value),
            title="Instrument used to acquire the data",
        ),
    ]
    detector: _datamodels.common.WfiDetector


class RefCommon(_core.BaseRomanURIModel):
    _uri: ClassVar = uri.asdf_uri.REF_COMMON.value

    model_config = ConfigDict(title="Common reference metadata properties")

    reftype: Annotated[
        ref_type,
        Field(
            default_factory=_defaults.default_constant_factory(ref_type.DARK.value),
            title="Reference File Type",
        ),
    ]
    pedigree: Annotated[
        pedigree,
        Field(
            default_factory=_defaults.default_constant_factory(pedigree.GROUND.value),
            title="The pedigree of the reference file",
        ),
    ]
    description: Annotated[
        str,
        Field(
            default_factory=_defaults.default_constant_factory("test description"),
            title="Description of the reference file",
        ),
    ]
    author: Annotated[
        str,
        Field(
            default_factory=_defaults.default_constant_factory("test author"),
            title="Author of the reference file",
        ),
    ]
    useafter: Annotated[
        _adaptors.AstropyTime,
        Field(
            default_factory=_defaults.default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="Use after date of the reference file",
        ),
    ]
    telescope: Annotated[
        _datamodels.common.telescope,
        Field(
            default_factory=_defaults.default_constant_factory(_datamodels.common.telescope.ROMAN.value),
            title="Telescope that reference file is used to calibrate",
        ),
    ]
    origin: Annotated[
        _datamodels.common.origin,
        Field(
            default_factory=_defaults.default_constant_factory(_datamodels.common.origin.STSCI.value),
            title="Organization responsible for creating file",
        ),
    ]
    instrument: Annotated[
        Instrument,
        Field(
            default_factory=_defaults.default_model_factory(Instrument),
        ),
    ]
