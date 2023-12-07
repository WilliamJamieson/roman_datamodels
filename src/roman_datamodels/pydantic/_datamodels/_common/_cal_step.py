from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_constant_factory
from ..._enums import StrEnum
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["CalStep"]


class calibration_status(StrEnum):
    NA = "N/A"
    COMPLETE = "COMPLETE"
    SKIPPED = "SKIPPED"
    INCOMPLETE = "INCOMPLETE"


class CalStep(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.CAL_STEP.value
    _tag_uri: ClassVar = asdf_tag_uri.CAL_STEP.value

    model_config = ConfigDict(
        title="Calibration Status",
    )

    assign_wcs: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Assign World Coordinate System",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_assign_wcs",
                        "GuideWindow.s_assign_wcs",
                    ],
                ),
            ),
        ),
    ]
    flat_field: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Flat Field Step",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_flat_field",
                        "GuideWindow.s_flat_field",
                    ],
                ),
            ),
        ),
    ]
    dark: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Dark Subtraction",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_dark",
                        "GuideWindow.s_dark",
                    ],
                ),
            ),
        ),
    ]
    dq_init: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Data Quality Mask Step",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_dq_init",
                        "GuideWindow.s_dq_init",
                    ],
                ),
            ),
        ),
    ]
    jump: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Jump Detection Step",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_jump",
                        "GuideWindow.s_jump",
                    ],
                ),
            ),
        ),
    ]
    linearity: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Linearity Correction",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_linearity",
                        "GuideWindow.s_linearity",
                    ],
                ),
            ),
        ),
    ]
    photom: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Photometry Step",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_photom",
                        "GuideWindow.s_photom",
                    ],
                ),
            ),
        ),
    ]
    source_detection: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Source Detection Step",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_source_detection",
                        "GuideWindow.s_source_detection",
                    ],
                ),
            ),
        ),
    ]
    ramp_fit: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Ramp Fitting",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_ramp_fit",
                        "GuideWindow.s_ramp_fit",
                    ],
                ),
            ),
        ),
    ]
    refpix: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Reference Pixel Correction",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_refpix",
                        "GuideWindow.s_refpix",
                    ],
                ),
            ),
        ),
    ]
    saturation: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Saturation Checking",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_saturation",
                        "GuideWindow.s_saturation",
                    ],
                ),
            ),
        ),
    ]
    outlier_detection: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Outlier Detection",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_outlier_detection",
                        "GuideWindow.s_outlier_detection",
                    ],
                ),
            ),
        ),
    ]
    tweakreg: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Tweakreg Step",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_tweakreg",
                        "GuideWindow.s_tweakreg",
                    ],
                ),
            ),
        ),
    ]
    skymatch: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Sky Match Step",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_skymatch",
                        "GuideWindow.s_skymatch",
                    ],
                ),
            ),
        ),
    ]
    resample: Annotated[
        calibration_status,
        Field(
            default_factory=default_constant_factory(calibration_status.INCOMPLETE.value),
            title="Resample Step",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceRefData.s_resample",
                        "GuideWindow.s_resample",
                    ],
                ),
            ),
        ),
    ]
