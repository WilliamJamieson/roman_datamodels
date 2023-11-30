from typing import Optional

from numpy.typing import DTypeLike
from pydantic_numpy import np_array_pydantic_annotated_typing

__all__ = ["NdArray"]


class _NdArray:
    @staticmethod
    def __getitem__(factory: tuple[DTypeLike, Optional[int], Optional[bool]]) -> type:
        if len(factory) < 1:
            raise TypeError("NdArray requires a dtype.")

        dtype: DTypeLike = factory[0]
        dimensions: Optional[int] = factory[1] if len(factory) > 1 else None
        strict_data_typing: bool = factory[2] if len(factory) > 2 else False

        return np_array_pydantic_annotated_typing(data_type=dtype, dimensions=dimensions, strict_data_typing=strict_data_typing)


NdArray = _NdArray()
