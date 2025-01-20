from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import core, rad

__all__ = [
    "Associations",
    "AssociationsExptypeEntry",
]


class AssociationsExptypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return Associations_Products_Members

    @classmethod
    def asdf_property_name(cls) -> str:
        return "exptype"


class AssociationsExptypeEntry(AssociationsExptypeEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for exptype in associations
    """

    SCIENCE = "SCIENCE"
    CALIBRATION = "CALIBRATION"
    ENGINEERING = "ENGINEERING"


_Associations_Products_Members: TypeAlias = AssociationsExptypeEntry | str


class Associations_Products_Members(
    rad.ImpliedNodeMixin[_Associations_Products_Members], rad.ObjectNode[_Associations_Products_Members]
):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Associations_Products

    @property
    @rad.field
    def expname(self: rad.Node) -> str:
        return "file_0"

    @property
    @rad.field
    def exposerr(self: rad.Node) -> str:
        return "null"

    @property
    @rad.field
    def exptype(self: rad.Node) -> AssociationsExptypeEntry:
        return AssociationsExptypeEntry.SCIENCE


_Associations_Products: TypeAlias = core.LNode[Associations_Products_Members] | str


class Associations_Products(rad.ImpliedNodeMixin[_Associations_Products], rad.ObjectNode[_Associations_Products]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Associations

    @property
    @rad.field
    def name(self: rad.Node) -> str:
        return "product0"

    @property
    @rad.field
    def members(self: rad.Node) -> core.LNode[Associations_Products_Members]:
        return core.LNode([])


_Associations: TypeAlias = core.LNode[Associations_Products] | str


class Associations(rad.TaggedObjectNode[_Associations], rad.ArrayFieldMixin[_Associations]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/associations-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/associations-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/associations-1.0.0",
            }
        )

    @property
    def primary_array_shape(self) -> tuple[int] | None:
        """
        Override the default primary array shape as it does not have one
        """
        return None

    @property
    def default_array_shape(self) -> tuple[int, int, int]:
        return (2, 3, 1)

    @property
    def testing_array_shape(self) -> tuple[int, int, int, int]:
        return (3, 8, 5, 2)

    @property
    @rad.field
    def asn_id(self: rad.Node) -> str:
        return "o036"

    @property
    @rad.field
    def asn_pool(self: rad.Node) -> str:
        return "r00001_20200530t023154_pool"

    @property
    @rad.field
    def asn_type(self: rad.Node) -> str:
        return "image"

    @property
    @rad.field
    def asn_rule(self: rad.Node) -> str:
        return "candidate_Asn_Lv2Image_i2d"

    @property
    @rad.field
    def version_id(self: rad.Node) -> str:
        return "null"

    @property
    @rad.field
    def code_version(self: rad.Node) -> str:
        return "0.16.2.dev16+g640b0b7"

    @property
    @rad.field
    def degraded_status(self: rad.Node) -> str:
        return "No known degraded exposures in association."

    @property
    @rad.field
    def program(self: rad.Node) -> int:
        return 1

    @property
    @rad.field
    def target(self: rad.Node) -> int:
        return 16

    @property
    @rad.field
    def constraints(self: rad.Node) -> str:
        return (
            "DMSAttrConstraint({'name': 'program', 'sources': ['program'], "
            "'value': '001'})\nConstraint_TargetAcq({'name': 'target_acq', 'value': "
            "'target_acquisition'})\nDMSAttrConstraint({'name': 'science', "
            "'DMSAttrConstraint({'name': 'asn_candidate','sources': "
            "['asn_candidate'], 'value': \"\\\\('o036',\\\\ 'observation'\\\\)\"})"
        )

    # TODO: need to add a rule to extend typeguard to check the argument of the decorator
    #       currently this only checks that it is an LNode
    @property
    @rad.field
    def products(self: rad.Node) -> core.LNode[Associations_Products]:
        file_idx = 0
        products = []
        CHOICES = ["SCIENCE", "CALIBRATION", "ENGINEERING"]
        for product_idx, members in enumerate(self.array_shape):
            members_lst = []
            for member_idx in range(members):
                members_lst.append(
                    Associations_Products_Members(
                        {"expname": "file_" + str(file_idx) + ".asdf", "exposerr": "null", "exptype": CHOICES[member_idx % 3]}
                    )
                )
                file_idx += 1
            products.append(Associations_Products({"name": f"product{product_idx}", "members": core.LNode(members_lst)}))

        return core.LNode(products)
