from typing import Annotated

from pydantic import Field

from ..._defaults import default_constant_factory
from ..._enums import StrEnum

__all__ = ["WfiOpticalElement"]


class optical_element(StrEnum):
    F062 = "F062"
    F087 = "F087"
    F106 = "F106"
    F129 = "F129"
    F146 = "F146"
    F158 = "F158"
    F184 = "F184"
    F213 = "F213"
    GRISM = "GRISM"
    PRISM = "PRISM"
    DARK = "DARK"


WfiOpticalElement = Annotated[
    optical_element,
    Field(
        default_factory=default_constant_factory(optical_element.F158.value),
        title="name of the filter element used",
    ),
]
