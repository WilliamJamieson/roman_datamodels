from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanModel, BaseRomanTaggedModel
from ..._defaults import default_constant_factory, default_model_factory, default_str_value
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["RefFile"]


class Crds(BaseRomanModel):
    _optional_fields: ClassVar = ("sw_version", "context_used")

    sw_version: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Version of CRDS file selection software used",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.crds_software_version",
                        "GuideWindow.crds_software_version",
                    ],
                ),
            ),
        ),
    ]
    context_used: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="CRDS context (.pmap) used to select ref files",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.crds_context_used",
                        "GuideWindow.crds_context_used",
                    ],
                ),
            ),
        ),
    ]


class RefFile(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.REF_FILE.value
    _tag_uri: ClassVar = asdf_tag_uri.REF_FILE.value

    _optional_fields: ClassVar = (
        "crds",
        "dark",
        "distortion",
        "mask",
        "flat",
        "gain",
        "readnoise",
        "linearity",
        "photom",
        "area",
        "saturation",
    )

    model_config = ConfigDict(
        title="Reference file information",
    )

    crds: Annotated[
        Crds,
        Field(
            default_factory=default_model_factory(Crds),
            title="CRDS Parameters",
        ),
    ]
    dark: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Dark reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_dark",
                        "GuideWindow.r_dark",
                    ],
                ),
            ),
        ),
    ]
    distortion: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Distortion reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_distortion",
                        "GuideWindow.r_distortion",
                    ],
                ),
            ),
        ),
    ]
    mask: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Mask reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_mask",
                        "GuideWindow.r_mask",
                    ],
                ),
            ),
        ),
    ]
    flat: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Flat reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_flat",
                        "GuideWindow.r_flat",
                    ],
                ),
            ),
        ),
    ]
    gain: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Gain reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_gain",
                        "GuideWindow.r_gain",
                    ],
                ),
            ),
        ),
    ]
    readnoise: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Readnoise reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_readnoise",
                        "GuideWindow.r_readnoise",
                    ],
                ),
            ),
        ),
    ]
    linearity: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="linearity reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_linearity",
                        "GuideWindow.r_linearity",
                    ],
                ),
            ),
        ),
    ]
    photom: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Photometry reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_photom",
                        "GuideWindow.r_photom",
                    ],
                ),
            ),
        ),
    ]
    area: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Area reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_area",
                        "GuideWindow.r_area",
                    ],
                ),
            ),
        ),
    ]
    saturation: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NA.value),
            title="Saturation reference file location",
            json_schema_extra=Archive(
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "ScienceCommon.r_saturation",
                        "GuideWindow.r_saturation",
                    ],
                ),
            ),
        ),
    ]
