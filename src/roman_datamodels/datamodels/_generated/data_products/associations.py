# Generated by RAD using generator based on datamodel-code-generator
#    source schema: data_products/associations-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from enum import Enum
from typing import ClassVar

from roman_datamodels.core._base import BaseDataModel
from roman_datamodels.core._extended import _AssociationsModel


class Exptype(Enum):
    SCIENCE = "SCIENCE"
    CALIBRATION = "CALIBRATION"
    ENGINEERING = "ENGINEERING"


class Member(BaseDataModel):
    schema_uri: ClassVar[None] = None
    expname: str
    exposerr: str
    exptype: Exptype


class Product(BaseDataModel):
    schema_uri: ClassVar[None] = None
    name: str
    members: list[Member]


class AssociationsModel(_AssociationsModel):
    """
    Association table data model
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/data_products/associations-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/data_products/associations-1.0.0"

    asn_id: str
    asn_pool: str
    asn_type: str
    asn_rule: str
    version_id: str | None = None
    code_version: str | None = None
    degraded_status: str | None = None
    program: int | None = None
    target: int | None = None
    constraints: str | None = None
    products: list[Product]