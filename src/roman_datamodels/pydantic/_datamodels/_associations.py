from typing import Annotated

from pydantic import Field

from .._core import BaseDataModel, BaseRomanDataModel
from .._enums import exptype

__all__ = ["AssociationsModel"]


class Member(BaseDataModel):
    expname: Annotated[str, Field()]
    exposerr: Annotated[float, Field()]
    exptype: Annotated[exptype, Field()]


class Product(BaseDataModel):
    name: Annotated[str, Field()]
    members: Annotated[list[Member], Field()]


class AssociationsModel(BaseRomanDataModel):
    asn_id: Annotated[str, Field()]
    asn_pool: Annotated[str, Field()]
    asn_type: Annotated[str, Field()]
    asn_rule: Annotated[str, Field()]
    version_id: Annotated[str, Field()]
    code_version: Annotated[str, Field()]
    degrated_status: Annotated[str, Field()]
    program: Annotated[int, Field()]
    target: Annotated[int, Field()]
    constraints: Annotated[str, Field()]
    product: Annotated[Product, Field()]
