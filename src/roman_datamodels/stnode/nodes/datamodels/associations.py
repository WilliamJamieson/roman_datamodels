from enum import Enum

from roman_datamodels.stnode import core, rad

__all__ = [
    "Associations",
    "AssociationsExptypeEntry",
]


class AssociationsExptypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Associations_Products_Members

    @classmethod
    def asdf_property_name(cls) -> str:
        return "exptype"


class AssociationsExptypeEntry(AssociationsExptypeEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for exptype in associations
    """

    SCIENCE = "SCIENCE"
    CALIBRATION = "CALIBRATION"
    ENGINEERING = "ENGINEERING"


class Associations_Products_Members(rad.ImpliedNodeMixin, rad.ObjectNode):
    """The members of an association"""

    @classmethod
    def asdf_implied_by(cls) -> type:
        return Associations_Products

    @rad.field
    def expname(self) -> str:
        return self._get_node("expname", lambda: "file_0")

    @rad.field
    def exposerr(self) -> str:
        return self._get_node("exposerr", lambda: "null")

    @rad.field
    def exptype(self) -> AssociationsExptypeEntry:
        return self._get_node("exptype", lambda: AssociationsExptypeEntry.SCIENCE)


class Associations_Products(rad.ImpliedNodeMixin, rad.ObjectNode):
    """The products of an association"""

    @classmethod
    def asdf_implied_by(cls) -> type:
        return Associations

    @rad.field
    def name(self) -> str:
        return self._get_node("name", lambda: "product0")

    @rad.field
    def members(self) -> core.LNode[Associations_Products_Members]:
        return self._get_node("members", lambda: core.LNode([]))


class Associations(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Association table
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/associations-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/associations-1.0.0"

    @property
    def primary_array_shape(self) -> tuple[int] | None:
        """
        Override the default primary array shape as it does not have one
        """
        return None

    @property
    def default_array_shape(self) -> tuple[int]:
        return (2, 3, 1)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return self.default_array_shape

    @rad.field
    def asn_id(self) -> str:
        return self._get_node("asn_id", lambda: "o036")

    @rad.field
    def asn_pool(self) -> str:
        return self._get_node("asn_pool", lambda: "r00001_20200530t023154_pool")

    @rad.field
    def asn_type(self) -> str:
        return self._get_node("asn_type", lambda: "image")

    @rad.field
    def asn_rule(self) -> str:
        return self._get_node("asn_rule", lambda: "candidate_Asn_Lv2Image_i2d")

    @rad.field
    def version_id(self) -> str:
        return self._get_node("version_id", lambda: "null")

    @rad.field
    def code_version(self) -> str:
        return self._get_node("code_version", lambda: "0.16.2.dev16+g640b0b7")

    @rad.field
    def degraded_status(self) -> str:
        return self._get_node("degraded_status", lambda: "No known degraded exposures in association.")

    @rad.field
    def program(self) -> int:
        return self._get_node("program", lambda: 1)

    @rad.field
    def target(self) -> int:
        return self._get_node("target", lambda: 16)

    @rad.field
    def constraints(self) -> str:
        return self._get_node(
            "constraints",
            lambda: (
                "DMSAttrConstraint({'name': 'program', 'sources': ['program'], "
                "'value': '001'})\nConstraint_TargetAcq({'name': 'target_acq', 'value': "
                "'target_acquisition'})\nDMSAttrConstraint({'name': 'science', "
                "'DMSAttrConstraint({'name': 'asn_candidate','sources': "
                "['asn_candidate'], 'value': \"\\\\('o036',\\\\ 'observation'\\\\)\"})"
            ),
        )

    # TODO: need to add a rule to extend typeguard to check the argument of the decorator
    #       currently this only checks that it is an LNode
    @rad.field
    def products(self) -> core.LNode[Associations_Products]:
        def _default():
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

        return self._get_node("products", _default)
