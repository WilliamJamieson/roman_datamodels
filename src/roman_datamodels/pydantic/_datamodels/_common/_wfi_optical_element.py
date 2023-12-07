from typing import Annotated

from pydantic import Field

from ..._defaults import default_constant_factory
from ..._enums import optical_element

__all__ = ["WfiOpticalElement"]


WfiOpticalElement = Annotated[
    optical_element,
    Field(
        default_factory=default_constant_factory(optical_element.F158.value),
        title="name of the filter element used",
    ),
]
