"""
ndarray schema for asdf ndarrays (sort of) it requires some effort to make it work for arrays other than inline
"""
from typing import Annotated, Any

import numpy as np
from asdf.core._converters.ndarray import NDArrayConverter
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema

from roman_datamodels.pydantic._schemas import asdf_ndarray_schema

nd_convert = NDArrayConverter()


class _AsdfNdarrayPydanticAnnotation:
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        def validate_from_json(value: tuple) -> np.ndarray:
            from asdf import AsdfFile
            from asdf.config import config_context
            from asdf.extension._serialization_context import create

            val = {this: that for this, that in value[0].items() if that is not None}

            with config_context() as config:
                config.all_array_storage = "inline"
                context = create(AsdfFile())

                return nd_convert.from_yaml_tree(val, None, context)._make_array()

        from_json_schema = core_schema.chain_schema(
            [
                asdf_ndarray_schema,
                core_schema.no_info_plain_validator_function(validate_from_json),
            ]
        )

        from_python_schema = core_schema.union_schema(
            [
                core_schema.is_instance_schema(np.ndarray),
                from_json_schema,
            ]
        )

        def serialize_to_json(value: np.ndarray) -> dict:
            from asdf import AsdfFile
            from asdf.config import config_context
            from asdf.extension._serialization_context import create

            with config_context() as config:
                config.all_array_storage = "inline"
                context = create(AsdfFile())

                return nd_convert.to_yaml_tree(value, None, context)

        return core_schema.json_or_python_schema(
            json_schema=from_json_schema,
            python_schema=from_python_schema,
            serialization=core_schema.plain_serializer_function_ser_schema(serialize_to_json),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _core_schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        return handler(asdf_ndarray_schema)


PydanticAsdfNdarray = Annotated[np.ndarray, _AsdfNdarrayPydanticAnnotation]
