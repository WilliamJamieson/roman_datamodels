from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel, Number
from ..._enums import source_type, target_type

__all__ = ["Target"]


class Target(BaseDataModel):
    proposer_name: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Proposer's name for the target",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.target_name",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(100)",
                    "destination": [
                        "ScienceCommon.proposer_target_name",
                        "GuideWindow.proposer_target_name",
                    ],
                },
            },
        ),
    ]
    catalog_name: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Standard astronomical catalog name for target",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.standard_target_name",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(256)",
                    "destination": [
                        "ScienceCommon.catalog_name",
                        "GuideWindow.catalog_name",
                    ],
                },
            },
        ),
    ]
    type: Annotated[
        target_type,
        Field(
            json_schema_extra={
                "title": "Type of target",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.target_type",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": [
                        "ScienceCommon.target_type",
                        "GuideWindow.target_type",
                    ],
                },
            },
        ),
    ]
    ra: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Target RA at mid time of exposure",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.ra_computed",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.ra",
                        "GuideWindow.ra",
                    ],
                },
            },
        ),
    ]
    dec: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Target Dec at mid time of exposure",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.dec_computed",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.dec",
                        "GuideWindow.dec",
                    ],
                },
            },
        ),
    ]
    ra_uncertainty: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Target RA uncertainty",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.ra_uncertainty_computed",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.ra_uncertainty",
                        "GuideWindow.ra_uncertainty",
                    ],
                },
            },
        ),
    ]
    dec_uncertainty: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Target Dec uncertainty",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.dec_uncertainty_computed",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.dec_uncertainty",
                        "GuideWindow.dec_uncertainty",
                    ],
                },
            },
        ),
    ]
    proper_motion_ra: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Target proper motion in RA",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.ra_proper_motion",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.proper_motion_ra",
                        "GuideWindow.proper_motion_ra",
                    ],
                },
            },
        ),
    ]
    proper_motion_dec: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Target proper motion in Dec",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.dec_proper_motion",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.proper_motion_dec",
                        "GuideWindow.proper_motion_dec",
                    ],
                },
            },
        ),
    ]
    proper_motion_epoch: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Target proper motion epoch",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.epoch",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.proper_motion_epoch",
                        "GuideWindow.proper_motion_epoch",
                    ],
                },
            },
        ),
    ]
    proposer_ra: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Proposer's target RA",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.ra_literal",
                        "function": "hms_to_degrees",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.proposer_ra",
                        "GuideWindow.proposer_ra",
                    ],
                },
            },
        ),
    ]
    proposer_dec: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Proposer's target Dec",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_target.dec_literal",
                        "function": "hms_to_degrees",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.proposer_dec",
                        "GuideWindow.proposer_dec",
                    ],
                },
            },
        ),
    ]
    source_type: Annotated[
        source_type,
        Field(
            json_schema_extra={
                "title": "Source type used for calibration",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(8)",
                    "destination": [
                        "ScienceCommon.source_type",
                        "GuideWindow.source_type",
                    ],
                },
            },
        ),
    ]
