import sys
from enum import IntEnum
from typing import Any, Callable, Optional

import numpy as np
from astropy.units import Quantity
from numpy.typing import DTypeLike

from ._adaptors import Units
from ._config import ShapeConfigManager

if sys.version_info < (3, 11):
    from strenum import StrEnum
else:
    from enum import StrEnum

__all__ = [
    "default_num_value",
    "default_str_value",
    "default_constant_factory",
    "default_model_factory",
    "default_quantity_factory",
    "default_ndarray_factory",
]


class default_num_value(IntEnum):
    NONUM = -999999


class default_str_value(StrEnum):
    NOSTR = "dummy value"
    NA = "N/A"


def default_constant_factory(constant: Any) -> Callable[[], Any]:
    """Factory for a default constant value.

    This avoids the need to strip the default value from the schema.
    """

    def _default_constant_factory() -> Any:
        return constant

    return _default_constant_factory


def default_model_factory(cls: type) -> Callable[[], Any]:
    def _default_model_factory() -> Any:
        return cls()

    return _default_model_factory


def default_ndarray_factory(
    config: ShapeConfigManager, dtype: DTypeLike, property: Optional[str] = None
) -> Callable[[], np.ndarray]:
    def _default_ndarray_factory() -> np.ndarray:
        shape = config.shape

        if property is not None:
            if hasattr(shape, property):
                shape = getattr(shape, property)
            else:
                raise ValueError(f"Shape has no property {property}")

        if shape == ():
            return np.array(config.fill, dtype=dtype)

        return np.full(shape, config.fill, dtype=dtype)

    return _default_ndarray_factory


def default_quantity_factory(
    config: ShapeConfigManager, dtype: DTypeLike, unit: Units, property: Optional[str] = None
) -> Callable[[], Quantity]:
    array_factory = default_ndarray_factory(config, dtype, property)

    def _default_quantity_factory() -> Quantity:
        return Quantity(array_factory(), unit=unit, dtype=dtype)

    return _default_quantity_factory
