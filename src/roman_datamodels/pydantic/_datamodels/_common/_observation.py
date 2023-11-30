from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel
from ..._enums import survey

__all__ = ["Observation"]


class Observation(BaseDataModel):
    obs_id: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Observation identifier",
                "description": (
                    "Programmatic observation identifier. The format is 'PPPPPCCAAASSSOOOVVVggsaaeeee' where "
                    "'PPPPP' is the Program, 'CC' is the execution plan, 'AAA' is the pass, 'SSS' is the "
                    "segment, 'OOO' is the Observation, 'VVV' is the Visit, 'gg' is the visit file group, "
                    "'s' is the visit file sequence, 'aa' is the visit file activity, and 'eeee' is the "
                    "exposure ID. The observation ID is the complete concatenation of visit_id + "
                    "visit_file_statement (visit_file_group + visit_file_sequence + visit_file_activity) + "
                    "exposure."
                ),
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(28)",
                    "destination": [
                        "ScienceCommon.obs_id",
                        "GuideWindow.obs_id",
                    ],
                },
            },
        ),
    ]
    visit_id: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Visit identifier",
                "description": (
                    "A unique identifier for a visit. The format is 'PPPPPCCAAASSSOOOVVV' where 'PPPPP' is the "
                    "Program, 'CC' is the execution plan, 'AAA' is the pass, 'SSS' is the segment number, "
                    "'OOO' is the Observation and 'VVV' is the Visit."
                ),
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(19)",
                    "destination": [
                        "ScienceCommon.visit_id",
                        "GuideWindow.visit_id",
                    ],
                },
            },
        ),
    ]
    program: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Program Number",
                "description": "Program number, defined range is 1..18445; included in obs_id and visit_id as 'PPPPP'.",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(19)",
                    "destination": [
                        "ScienceCommon.program",
                        "GuideWindow.program",
                    ],
                },
            },
        ),
    ]
    execution_plan: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Execution Plan Number",
                # fmt: off
                "description": (
                    "Execution plan within the program, defined range is 1..99; included in obs_id and "
                    "visit_id as 'CC'."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.execution_plan",
                        "GuideWindow.execution_plan",
                    ],
                },
            },
        ),
    ]
    # This will require an annoying fix
    pass_: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Pass Number",
                # fmt: off
                "description": (
                    "Pass number within execution plan, defined range is 1..999; included in obs_id and "
                    "visit_id as 'AA'."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.pass",
                        "GuideWindow.pass",
                    ],
                },
            },
        ),
    ]
    segment: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Segment Number",
                # fmt: off
                "description": (
                    "Segment Number within pass, defined range is 1..999; included in obs_id and visit_id as "
                    "'SSS'."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.segment",
                        "GuideWindow.segment",
                    ],
                },
            },
        ),
    ]
    observation: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Observation Number",
                # fmt: off
                "description": (
                    "Observation number within the segment, defined range is 1..999; included in obs_id and "
                    "visit_id as 'OOO'."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.observation",
                        "GuideWindow.observation",
                    ],
                },
            },
        ),
    ]
    visit: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Visit Number",
                "description": (
                    "Visit number within the observation, defined range of values is 1..999; included in "
                    "obs_id and visit_id as 'VVV'."
                ),
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.visit",
                        "GuideWindow.visit",
                    ],
                },
            },
        ),
    ]
    visit_file_group: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Sequence Group",
                # fmt: off
                "description": (
                    "Sequence group within the visit file, defined range of values is 1..99; included in "
                    "obs_id as 'gg'."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.visit_file_group",
                        "GuideWindow.visit_file_group",
                    ],
                },
            },
        ),
    ]
    visit_file_sequence: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Visit File Sequence",
                # fmt: off
                "description": (
                    "Visit file sequence within the group, defined range of values is 1..5; included in"
                    "obs_id as 's'."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.visit_file_sequence",
                        "GuideWindow.visit_file_sequence",
                    ],
                },
            },
        ),
    ]
    visit_file_activity: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Visit File Activity",
                # fmt: off
                "description": (
                    "Visit file activity within the sequence, defined range of values is 1..ZZ; included in "
                    "obs_id as 'aa'."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(2)",
                    "destination": [
                        "ScienceCommon.visit_file_activity",
                        "GuideWindow.visit_file_activity",
                    ],
                },
            },
        ),
    ]
    exposure: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Exposure within the visit",
                # fmt: off
                "description": (
                    "Exposure within the visit, defined range of values is 1..9999; included in obs_id as "
                    "'eeee'."
                ),
                # fmt: on
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "smallint",
                    "destination": [
                        "ScienceCommon.expousre",
                        "GuideWindow.exposure",
                    ],
                },
            },
        ),
    ]
    template: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Observation template used",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_visit.template",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(50)",
                    "destination": [
                        "ScienceCommon.template",
                        "GuideWindow.template",
                    ],
                },
            },
        ),
    ]
    observation_label: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Proposer label for the observation",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(max)",
                    "destination": [
                        "ScienceCommon.observation_label",
                        "GuideWindow.observation_label",
                    ],
                },
            },
        ),
    ]
    survey: Annotated[
        survey,
        Field(
            json_schema_extra={
                "title": "Proposer label for the observation",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceCommon.survey",
                        "GuideWindow.survey",
                    ],
                },
            },
        ),
    ]
