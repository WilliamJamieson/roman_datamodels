"""
This module contains the enums used in the datamodels.

It exists simply to provide a statically available external reference module for
all the enums. A test is used to ensure that all the employed enums are actually
available in this module.
"""
from ._datamodels._associations import exptype
from ._datamodels._common._aperture import aperture
from ._datamodels._common._basic import origin, telescope
from ._datamodels._common._cal_step import calibration_status
from ._datamodels._common._coordinates import coordinates
from ._datamodels._common._ephemeris import ephemeris_type
from ._datamodels._common._exposure_type import exposure_type
from ._datamodels._common._guidewindow_modes import guidewindow_modes
from ._datamodels._common._observation import survey
from ._datamodels._common._resample import weight_type
from ._datamodels._common._target import source_type, target_type
from ._datamodels._common._visit import engineering_quality, pointing_engdb_quality
from ._datamodels._common._wfi_detector import detector
from ._datamodels._common._wfi_mode import instrument
from ._datamodels._common._wfi_optical_element import optical_element
from ._reference_files._ref_common._ref_common import pedigree, reftype

__all__ = [
    "exptype",
    "aperture",
    "origin",
    "telescope",
    "calibration_status",
    "coordinates",
    "ephemeris_type",
    "exposure_type",
    "guidewindow_modes",
    "survey",
    "weight_type",
    "source_type",
    "target_type",
    "engineering_quality",
    "pointing_engdb_quality",
    "detector",
    "optical_element",
    "instrument",
    "pedigree",
    "reftype",
]
