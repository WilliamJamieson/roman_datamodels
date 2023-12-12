from typing import Annotated, Callable, ClassVar, Optional

from pydantic import ConfigDict, Field

from .._core import BaseRomanModel, BaseRomanStepModel
from .._defaults import default_constant_factory
from .._strenum import StrEnum
from .._uri import asdf_tag_uri, asdf_uri

__all__ = ["AssociationsModel"]


class exptype(StrEnum):
    SCIENCE = "SCIENCE"
    CALIBRATION = "CALIBRATION"
    ENGINEERING = "ENGINEERING"


class Member(BaseRomanModel):
    expname: Annotated[str, Field()]
    exposerr: Annotated[Optional[float], Field()]
    exptype: Annotated[exptype, Field()]


class Product(BaseRomanModel):
    name: Annotated[str, Field()]
    members: Annotated[list[Member], Field()]


def _default_product_factory(shape) -> Callable[[], list[Product]]:
    def product_factory() -> list[Product]:
        products = []
        CHOICES = [exp.value for exp in exptype]

        file_idx = 0
        for product_idx, members in enumerate(shape):
            product_members = []
            for member_idx in range(members):
                product_members.append(
                    Member(
                        expname=f"file_{file_idx}.asdf",
                        exposerr=None,
                        exptype=CHOICES[member_idx % len(CHOICES)],
                    )
                )
                file_idx += 1

            products.append(
                Product(
                    name=f"product{product_idx}",
                    members=product_members,
                )
            )

        return products

    return product_factory


class AssociationsModel(BaseRomanStepModel):
    _uri: ClassVar = asdf_uri.ASSOCIATIONS.value
    _tag_uri: ClassVar = asdf_tag_uri.ASSOCIATIONS.value
    _optional_fields: ClassVar = ("version_id", "code_version", "degraded_status", "program", "target", "constraints")

    model_config = ConfigDict(
        title="Association table data model",
    )

    asn_id: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("o036"),
        ),
    ]
    asn_pool: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("r00001_20200530t023154_pool"),
        ),
    ]
    asn_type: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("image"),
        ),
    ]
    asn_rule: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("candidate_Asn_Lv2Image_i2d"),
        ),
    ]
    version_id: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("null"),
        ),
    ]
    code_version: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("0.16.2.dev16+g640b0b79"),
        ),
    ]
    degraded_status: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("No known degraded exposures in association."),
        ),
    ]
    program: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(1),
        ),
    ]
    target: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(16),
        ),
    ]
    constraints: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(
                "DMSAttrConstraint({'name': 'program', 'sources': ['program'], "
                "'value': '001'})\nConstraint_TargetAcq({'name': 'target_acq', 'value': "
                "'target_acquisition'})\nDMSAttrConstraint({'name': 'science', "
                "'DMSAttrConstraint({'name': 'asn_candidate','sources': "
                "['asn_candidate'], 'value': \"\\\\('o036',\\\\ 'observation'\\\\)\"})"
            ),
        ),
    ]
    products: Annotated[
        list[Product],
        Field(
            default_factory=_default_product_factory((2, 3, 1)),
        ),
    ]
