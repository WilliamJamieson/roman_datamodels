from typing import Annotated, Any

from asdf_astropy.converters.time import TimeConverter
from astropy.time import Time
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema

from roman_datamodels.pydantic._schemas import astropy_time_schema

t_convert = TimeConverter()


__all__ = ["AstropyTime"]


class _AstropyTimePydanticAnnotation:
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        def validate_from_json(value: tuple) -> Time:
            return t_convert.from_yaml_tree(value[0], None, None)

        from_json_schema = core_schema.chain_schema(
            [
                astropy_time_schema,
                core_schema.no_info_plain_validator_function(validate_from_json),
            ]
        )

        from_python_schema = core_schema.union_schema(
            [
                core_schema.is_instance_schema(Time),
                from_json_schema,
            ]
        )

        def serialize_to_json(value: Time) -> dict:
            return t_convert.to_yaml_tree(value, None, None)

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
        return handler(astropy_time_schema)


AstropyTime = Annotated[Time, _AstropyTimePydanticAnnotation]
