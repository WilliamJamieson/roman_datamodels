from roman_datamodels.stnode import _base, _core

__all__ = ["Associations"]


class Associations_Products_Members(_core.ImpliedNodeMixin, _core.ObjectNode):
    """The members of an association"""

    @classmethod
    def asdf_implied_by(cls) -> type:
        return Associations_Products

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "expname",
            "exposerr",
            "exptype",
        )

    @property
    def expname(self) -> str:
        return self._get_node("expname", lambda: "file_0")

    @property
    def exposerr(self) -> str:
        return self._get_node("exposerr", lambda: "null")

    @property
    def exptype(self) -> str:
        return self._get_node("exptype", lambda: "SCIENCE")


class Associations_Products(_core.ImpliedNodeMixin, _core.ObjectNode):
    """The products of an association"""

    @classmethod
    def asdf_implied_by(cls) -> type:
        return Associations

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "name",
            "members",
        )

    @property
    def name(self) -> str:
        return self._get_node("name", lambda: "product0")

    @property
    def members(self) -> _base.LNode[Associations_Products_Members]:
        return self._get_node("members", lambda: _base.LNode([]))


class Associations(_core.DataModelNode):
    """
    Association table
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/associations-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (2, 3, 1)

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "asn_id",
            "asn_pool",
            "asn_type",
            "asn_rule",
            "products",
        )

    @property
    def asn_id(self) -> str:
        return self._get_node("asn_id", lambda: "o036")

    @property
    def asn_pool(self) -> str:
        return self._get_node("asn_pool", lambda: "r00001_20200530t023154_pool")

    @property
    def asn_type(self) -> str:
        return self._get_node("asn_type", lambda: "image")

    @property
    def asn_rule(self) -> str:
        return self._get_node("asn_rule", lambda: "candidate_Asn_Lv2Image_i2d")

    @property
    def version_id(self) -> str:
        return self._get_node("version_id", lambda: "null")

    @property
    def code_version(self) -> str:
        return self._get_node("code_version", lambda: "0.16.2.dev16+g640b0b7")

    @property
    def degraded_status(self) -> str:
        return self._get_node("degraded_status", lambda: "No known degraded exposures in association.")

    @property
    def program(self) -> int:
        return self._get_node("program", lambda: 1)

    @property
    def target(self) -> int:
        return self._get_node("target", lambda: 16)

    @property
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

    @property
    def products(self) -> _base.LNode[Associations_Products]:
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
                products.append(Associations_Products({"name": f"product{product_idx}", "members": _base.LNode(members_lst)}))

            return _base.LNode(products)

        return self._get_node("products", _default)
