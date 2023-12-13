from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Observation"]


class survey(_strenum.StrEnum):
    HLS = "HLS"
    EMS = "EMS"
    SN = "SN"
    NA = "N/A"


class Observation(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.OBSERVATION.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.OBSERVATION.value

    model_config = ConfigDict(
        title="Observation identifiers",
    )

    obs_id: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Observation identifier",
            description=(
                "Programmatic observation identifier. The format is 'PPPPPCCAAASSSOOOVVVggsaaeeee' where "
                "'PPPPP' is the Program, 'CC' is the execution plan, 'AAA' is the pass, 'SSS' is the "
                "segment, 'OOO' is the Observation, 'VVV' is the Visit, 'gg' is the visit file group, "
                "'s' is the visit file sequence, 'aa' is the visit file activity, and 'eeee' is the "
                "exposure ID. The observation ID is the complete concatenation of visit_id + "
                "visit_file_statement (visit_file_group + visit_file_sequence + visit_file_activity) + "
                "exposure."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(28)",
                    destination=[
                        "ScienceCommon.obs_id",
                        "GuideWindow.obs_id",
                    ],
                ),
            ),
        ),
    ]
    visit_id: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Visit identifier",
            description=(
                "A unique identifier for a visit. The format is 'PPPPPCCAAASSSOOOVVV' where 'PPPPP' is the "
                "Program, 'CC' is the execution plan, 'AAA' is the pass, 'SSS' is the segment number, "
                "'OOO' is the Observation and 'VVV' is the Visit."
            ),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(19)",
                    destination=[
                        "ScienceCommon.visit_id",
                        "GuideWindow.visit_id",
                    ],
                ),
            ),
        ),
    ]
    program: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Program Number",
            description="Program number, defined range is 1..18445; included in obs_id and visit_id as 'PPPPP'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(19)",
                    destination=[
                        "ScienceCommon.program",
                        "GuideWindow.program",
                    ],
                ),
            ),
        ),
    ]
    execution_plan: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Execution Plan Number",
            description="Execution plan within the program, defined range is 1..99; included in obs_id and visit_id as 'CC'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="smallint",
                    destination=[
                        "ScienceCommon.execution_plan",
                        "GuideWindow.execution_plan",
                    ],
                ),
            ),
        ),
    ]
    pass_: Annotated[
        int,
        Field(
            alias="pass",
            default_factory=_defaults.default_num_factory,
            title="Pass Number",
            description="Pass number within execution plan, defined range is 1..999; included in obs_id and visit_id as 'AA'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="smallint",
                    destination=[
                        "ScienceCommon.pass",
                        "GuideWindow.pass",
                    ],
                ),
            ),
        ),
    ]
    segment: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Segment Number",
            description="Segment Number within pass, defined range is 1..999; included in obs_id and visit_id as 'SSS'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="smallint",
                    destination=[
                        "ScienceCommon.segment",
                        "GuideWindow.segment",
                    ],
                ),
            ),
        ),
    ]
    observation: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Observation Number",
            description="Observation number within the segment, defined range is 1..999; included in obs_id and visit_id as 'OOO'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="smallint",
                    destination=[
                        "ScienceCommon.observation",
                        "GuideWindow.observation",
                    ],
                ),
            ),
        ),
    ]
    visit: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Visit Number",
            description="Visit number within the observation, defined range of values is 1..999; included in obs_id and visit_id as 'VVV'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="smallint",
                    destination=[
                        "ScienceCommon.visit",
                        "GuideWindow.visit",
                    ],
                ),
            ),
        ),
    ]
    visit_file_group: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Sequence Group",
            description="Sequence group within the visit file, defined range of values is 1..99; included in obs_id as 'gg'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="smallint",
                    destination=[
                        "ScienceCommon.visit_file_group",
                        "GuideWindow.visit_file_group",
                    ],
                ),
            ),
        ),
    ]
    visit_file_sequence: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Visit File Sequence",
            description="Visit file sequence within the group, defined range of values is 1..5; included inobs_id as 's'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="smallint",
                    destination=[
                        "ScienceCommon.visit_file_sequence",
                        "GuideWindow.visit_file_sequence",
                    ],
                ),
            ),
        ),
    ]
    visit_file_activity: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Visit File Activity",
            description="Visit file activity within the sequence, defined range of values is 1..ZZ; included in obs_id as 'aa'.",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(2)",
                    destination=[
                        "ScienceCommon.visit_file_activity",
                        "GuideWindow.visit_file_activity",
                    ],
                ),
            ),
        ),
    ]
    exposure: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Exposure within the visit",
            description=("Exposure within the visit, defined range of values is 1..9999; included in obs_id as " "'eeee'."),
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="smallint",
                    destination=[
                        "ScienceCommon.exposure",
                        "GuideWindow.exposure",
                    ],
                ),
            ),
        ),
    ]
    template: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Observation template used",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_visit.template",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(50)",
                    destination=[
                        "ScienceCommon.template",
                        "GuideWindow.template",
                    ],
                ),
            ),
        ),
    ]
    observation_label: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Proposer label for the observation",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(max)",
                    destination=[
                        "ScienceCommon.observation_label",
                        "GuideWindow.observation_label",
                    ],
                ),
            ),
        ),
    ]
    survey: Annotated[
        survey,
        Field(
            default_factory=_defaults.default_constant_factory(survey.NA.value),
            title="Proposer label for the observation",
            json_schema_extra=_archive.Archive(
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "ScienceCommon.survey",
                        "GuideWindow.survey",
                    ],
                ),
            ),
        ),
    ]
