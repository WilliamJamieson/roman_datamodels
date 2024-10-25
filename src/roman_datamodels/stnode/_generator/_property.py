"""
This module contains the generator functions for generating the properties of the stnode classes.
"""

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
    return _GETTER_TEMPLATE.format(name=name, annotation=annotation) + _SETTER_TEMPLATE.format(name=name, annotation=annotation)
