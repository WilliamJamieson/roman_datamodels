from typing import Annotated, Any, Optional, Union

import numpy as np
from numpy.typing import DTypeLike
from pydantic import FilePath, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from pydantic_numpy.helper.annotation import NpArrayPydanticAnnotation, _data_type_resolver, _int_to_dim_type
from pydantic_numpy.model import MultiArrayNumpyFile

from ._adaptor_tags import asdf_tags

__all__ = ["NdArray"]


class _AsdfNdArrayPydanticAnnotation(NpArrayPydanticAnnotation):
    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _core_schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        schema = {
            "title": None,
            "tag": asdf_tags.ASDF_NDARRAY.value,
        }
        if cls.data_type is not None:
            schema["datatype"] = cls.data_type.__name__

        if cls.dimensions is not None:
            schema["ndim"] = cls.dimensions
        return schema


class _NdArray:
    @staticmethod
    def __getitem__(factory: tuple[DTypeLike, Optional[int], Optional[bool]]) -> type:
        if len(factory) < 1:
            raise TypeError("NdArray requires a dtype.")

        dtype: DTypeLike = factory[0]
        dimensions: Optional[int] = factory[1] if len(factory) > 1 else None
        strict_data_typing: bool = factory[2] if len(factory) > 2 else False

        return Annotated[
            Union[
                FilePath,
                MultiArrayNumpyFile,
                np.ndarray[
                    _int_to_dim_type[dimensions] if dimensions else Any,
                    np.dtype[dtype] if _data_type_resolver(dtype) else dtype,
                ],
            ],
            _AsdfNdArrayPydanticAnnotation.factory(data_type=dtype, dimensions=dimensions, strict_data_typing=strict_data_typing),
        ]


NdArray = _NdArray()
