"""
This module defines all of the source catalog DataModels, these are separated from
    the other DataModels because they have some unique methods and properties in
    addition to them being treated slightly differently in the pipeline.
"""

from __future__ import annotations

from re import match
from typing import ClassVar

from asdf.tags.core.ndarray import asdf_datatype_to_numpy_dtype

from roman_datamodels._stnode import FakeDataBuilder, get_keyword

from ._core import DataModel, ParquetSupport, PipelineStep

__all__ = (
    "ForcedImageSourceCatalogModel",
    "ForcedMosaicSourceCatalogModel",
    "ImageSourceCatalogModel",
    "MosaicSourceCatalogModel",
    "MultibandSourceCatalogModel",
    "SourceCatalog",
)


class SourceCatalog(PipelineStep, ParquetSupport):
    """
    Mixin class for source catalog DataModels
        This class provides the additional methods are needed working with source
        catalogs and their schemas.
    """

    __slots__ = ()

    def create_empty_catalog(self, aperture_radii=None, filters=None):
        """
        Create an empty but valid source catalog table

        Parameters
        ----------
        aperture_radii: list of int (optional)
            Aperture radii in tenths of an arcsecond.

        filters: list of str (optional)
            List of filters (for example: "f184")

        Returns
        -------
        Table
        """
        if aperture_radii:
            aperture_radii = [f"{i:02}" for i in aperture_radii]

        return FakeDataBuilder.make_empty_catalog(self._instance.get_schema(), aperture_radii=aperture_radii, filters=filters)

    def get_column_definition(self, name):
        """
        Get the definition of a named column in the catalog table.

        This function parses the "definitions" part of the catalog
        schema and returns the parsed content.

        Parameters
        ----------
        name: str
            Column name, may contain aperture radisu or filter/band or prefixed
            with ``forced_``.

        Returns
        -------
        dict or None
            Dictionary containing unit, description, and datatype information
            or None if the name does not match any definition.
        """

        if name.startswith("forced_"):
            _, name = name.split("forced_", maxsplit=1)

        definitions = get_keyword(self._instance.get_schema()["properties"]["source_catalog"], "definitions")
        for def_name, definition in definitions.items():
            # TODO: Can this be replaced with a python match statement?
            if "~radius~" in def_name:
                def_name = def_name.replace("~radius~", r"[0-9]{2}")
            if "_~band~" in def_name:
                def_name = def_name.replace("_~band~", r"(_f[0-9]{3}|)")
            if "~band~" in def_name:
                def_name = def_name.replace("~band~", r"(f[0-9]{3}|)")
            if match(f"^{def_name}$", name):
                return {
                    "unit": definition["unit"],
                    "description": definition["description"],
                    "datatype": asdf_datatype_to_numpy_dtype(
                        definition["properties"]["data"]["properties"]["datatype"]["enum"][0]
                    ),
                }


class ImageSourceCatalogModel(SourceCatalog, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/image_source_catalog-*"


class ForcedImageSourceCatalogModel(SourceCatalog, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/forced_image_source_catalog-*"


class MosaicSourceCatalogModel(SourceCatalog, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/mosaic_source_catalog-*"


class ForcedMosaicSourceCatalogModel(SourceCatalog, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/forced_mosaic_source_catalog-*"


class MultibandSourceCatalogModel(SourceCatalog, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/multiband_source_catalog-*"
