"""
This module contains the generator functions for generating the properties of the stnode classes.
"""

from enum import StrEnum

__all__ = ["create_property"]

_GETTER_TEMPLATE = """
@property
def {name}(self) -> {annotation}:
    return self._data.get("{name}")
"""

_SETTER_TEMPLATE = """
@{name}.setter
def {name}(self, value: {annotation}) -> None:
    self._set_data("{name}", value)
"""


class ReservedNames(StrEnum):
    """
    A class to hold reserved names (banned by the python language), used by RAD
    """

    pass_ = "pass"

    @classmethod
    def get_name(cls, name: str) -> str:
        if name in cls:
            return f"{name}_"

        return name


def create_property(name: str, annotation: str) -> str:
    """
    Generate a property entry for a class

    Parameters
    ----------
    name: str
        The name of the property
    annotation: str
        The type annotation for the property

    Returns
    -------
    A property string
    """
    name = ReservedNames.get_name(name)

    return _GETTER_TEMPLATE.format(name=name, annotation=annotation) + _SETTER_TEMPLATE.format(name=name, annotation=annotation)
