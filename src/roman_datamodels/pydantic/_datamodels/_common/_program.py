from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Program"]


class Program(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.PROGRAM.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.PROGRAM.value

    model_config = ConfigDict(
        title="Program information",
    )

    title: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Proposal title",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_program.title",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(200)",
                    destination=[
                        "ScienceCommon.program_title",
                        "GuideWindow.program_title",
                    ],
                ),
            ),
        ),
    ]
    pi_name: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Principle Investigator name",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(100)",
                    destination=[
                        "ScienceCommon.pi_name",
                        "GuideWindow.pi_name",
                    ],
                ),
            ),
        ),
    ]
    category: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Program category",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_program.category",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(6)",
                    destination=[
                        "ScienceCommon.program_category",
                        "GuideWindow.program_category",
                    ],
                ),
            ),
        ),
    ]
    subcategory: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Program subcategory",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_program.subcategory",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(6)",
                    destination=[
                        "ScienceCommon.program_subcategory",
                        "GuideWindow.program_subcategory",
                    ],
                ),
            ),
        ),
    ]
    science_category: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Science category assigned during TAC process",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_program.science_category",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(50)",
                    destination=[
                        "ScienceCommon.science_category",
                        "GuideWindow.science_category",
                    ],
                ),
            ),
        ),
    ]
    continuation_id: Annotated[
        int,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Continuation of previous Program",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_program.continuation_id",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.continuation_id",
                        "GuideWindow.continuation_id",
                    ],
                ),
            ),
        ),
    ]
