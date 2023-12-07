from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_constant_factory, default_num_value, default_str_value
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Program"]


class Program(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.PROGRAM.value
    _tag_uri: ClassVar = asdf_tag_uri.PROGRAM.value

    model_config = ConfigDict(
        title="Program information",
    )

    title: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Proposal title",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_program.title",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Principle Investigator name",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Program category",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_program.category",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Program subcategory",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_program.subcategory",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Science category assigned during TAC process",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_program.science_category",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Continuation of previous Program",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_program.continuation_id",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.continuation_id",
                        "GuideWindow.continuation_id",
                    ],
                ),
            ),
        ),
    ]
