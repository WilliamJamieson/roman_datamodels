from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel, Number
from ..._defaults import default_constant_factory, default_num_value, default_str_value
from ..._uri import asdf_tag_uri, asdf_uri
from ._guidewindow_modes import GuidewindowModes, guidewindow_modes

__all__ = ["Guidestar"]


class Guidestar(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.GUIDESTAR.value
    _tag_uri: ClassVar = asdf_tag_uri.GUIDESTAR.value

    model_config = ConfigDict(
        title="Guide star window information",
    )

    gw_id: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="guide star window identifier",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(20)",
                    destination=[
                        "ScienceCommon.gw_id",
                        "GuideWindow.gw_id",
                    ],
                ),
            ),
        ),
    ]
    gw_fgs_mode: Annotated[
        GuidewindowModes,
        Field(
            default_factory=default_constant_factory(guidewindow_modes.WSM_ACQ_2.value),
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(18)",
                    destination=[
                        "ScienceCommon.gw_fgs_mode",
                        "GuideWindow.gw_fgs_mode",
                    ],
                ),
            ),
        ),
    ]
    gs_id: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="guide star identifier from the GSC2 catalog",
            description="guide star catalog id from the GSC2, field gsc2ID",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(20)",
                    destination=[
                        "ScienceCommon.gs_id",
                        "GuideWindow.gs_id",
                    ],
                ),
            ),
        ),
    ]
    gs_catalog_version: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="The version of the Guide Star Catalog",
            description=(
                'The version of the catalog that the guide stars are selected, currently  "GSC 2.4.2", SDF should populate'
                "this from the return value of CAT e.g. CAT=GSC242"
            ),
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(20)",
                    destination=[
                        "ScienceCommon.gs_catalog_version",
                    ],
                ),
            ),
        ),
    ]
    gs_ra: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] guide star right ascension",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_ra",
                        "GuideWindow.gs_ra",
                    ],
                ),
            ),
        ),
    ]
    gs_dec: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] guide star declination",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_dec",
                        "GuideWindow.gs_dec",
                    ],
                ),
            ),
        ),
    ]
    gs_ura: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] guide star right ascension uncertainty",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_ura",
                        "GuideWindow.gs_ura",
                    ],
                ),
            ),
        ),
    ]
    gs_udec: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[deg] guide star declination uncertainty",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_udec",
                        "GuideWindow.gs_udec",
                    ],
                ),
            ),
        ),
    ]
    gs_mag: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="guide star magnitude in detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_mag",
                        "GuideWindow.gs_mag",
                    ],
                ),
            ),
        ),
    ]
    gs_umag: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="guide star magnitude uncertainty",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_umag",
                        "GuideWindow.gs_umag",
                    ],
                ),
            ),
        ),
    ]
    data_start: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="MJD start time of guider data within this file",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.data_start",
                        "GuideWindow.data_start",
                    ],
                ),
            ),
        ),
    ]
    data_end: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="MJD end time of guider data within this file",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.data_end",
                        "GuideWindow.data_end",
                    ],
                ),
            ),
        ),
    ]
    gs_ctd_x: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[arcsec] guide star centroid x position in guider ideal frame",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_ctd_x",
                        "GuideWindow.gs_ctd_x",
                    ],
                ),
            ),
        ),
    ]
    gs_ctd_y: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[arcsec] guide star centroid y position in guider ideal frame",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_ctd_y",
                        "GuideWindow.gs_ctd_y",
                    ],
                ),
            ),
        ),
    ]
    gs_ctd_ux: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="uncertainty in the x position of the centroid",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_ctd_ux",
                        "GuideWindow.gs_ctd_ux",
                    ],
                ),
            ),
        ),
    ]
    gs_ctd_uy: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="uncertainty in the y position of the centroid",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_ctd_uy",
                        "GuideWindow.gs_ctd_uy",
                    ],
                ),
            ),
        ),
    ]
    gs_epoch: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Epoch of guide star coordinates",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(10)",
                    destination=[
                        "ScienceCommon.gs_epoch",
                        "GuideWindow.gs_epoch",
                    ],
                ),
            ),
        ),
    ]
    gs_mura: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[mas/yr] Guide star ICRS right ascension proper motion",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_mura",
                        "GuideWindow.gs_mura",
                    ],
                ),
            ),
        ),
    ]
    gs_mudec: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="[mas/yr] Guide star ICRS declination proper motion",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_mudec",
                        "GuideWindow.gs_mudec",
                    ],
                ),
            ),
        ),
    ]
    gs_para: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide star annual parallax",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_para",
                        "GuideWindow.gs_para",
                    ],
                ),
            ),
        ),
    ]
    gs_pattern_error: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="RMS of guide star position",
            description=(
                "RMS of guide star position in guide window from pattern matching (error on "
                "centroid not explicitly calculated, the FACE information takes all the centroids and "
                "calculates the error across the guiding pattern)"
            ),
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.gs_pattern_error",
                        "GuideWindow.gs_pattern_error",
                    ],
                ),
            ),
        ),
    ]
    gw_window_xstart: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide window x start position on the detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.gw_window_xstart",
                    ],
                ),
            ),
        ),
    ]
    gw_window_ystart: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide window y start position on the detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.gw_window_ystart",
                    ],
                ),
            ),
        ),
    ]
    gw_window_xstop: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide window x stop position on the detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.gw_window_xstop",
                    ],
                ),
            ),
        ),
    ]
    gw_window_ystop: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide window y stop position on the detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.gw_window_ystop",
                    ],
                ),
            ),
        ),
    ]
    gw_window_xsize: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide window size in the x direction in detector coordinates",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.gw_window_xsize",
                    ],
                ),
            ),
        ),
    ]
    gw_window_ysize: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide window size in the y direction in detector coordinates",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "ScienceCommon.gw_window_ysize",
                    ],
                ),
            ),
        ),
    ]
