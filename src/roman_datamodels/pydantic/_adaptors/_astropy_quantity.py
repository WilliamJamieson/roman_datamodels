from typing import Annotated, Any, Optional

import astropy.units as u
from numpy.typing import DTypeLike
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from pydantic_numpy.helper.annotation import NpArrayPydanticAnnotation

from ._adaptor_tags import asdf_tags
from ._astropy_unit import Units, _AstropyUnitPydanticAnnotation
from ._ndarray import _AsdfNdArrayPydanticAnnotation

__all__ = ["AstropyQuantity"]


class _AstropyQuantityPydanticAnnotation(_AsdfNdArrayPydanticAnnotation, _AstropyUnitPydanticAnnotation):
    @classmethod
    def factory(
        cls, *, dtype: DTypeLike, unit: Units = None, dimensions: Optional[int] = None, strict_data_typing: bool = False
    ) -> type:
        symbols = cls._get_unit_symbols(unit)
        ndarray_type = super().factory(data_type=dtype, dimensions=dimensions, strict_data_typing=strict_data_typing)
        return type(
            f"_{ndarray_type.__name__}_{'_'.join(symbols)}",
            (cls,),
            {"symbols": symbols, "data_type": dtype, "dimensions": dimensions, "strict_data_typing": strict_data_typing},
        )

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        ndarray_schema = super().__get_pydantic_core_schema__(_source_type, _handler)
        unit_schema = super(NpArrayPydanticAnnotation, cls).__get_pydantic_core_schema__(_source_type, _handler).copy()

        astropy_quantity_schema = core_schema.typed_dict_schema(
            {
                "value": core_schema.typed_dict_field(ndarray_schema["python_schema"]),
                "unit": core_schema.typed_dict_field(unit_schema["python_schema"]),
            }
        )

        def validate_from_json(value: tuple) -> u.Quantity:
            return u.Quantity(value["value"], value["unit"], dtype=value["value"].dtype)

        from_json_schema = core_schema.chain_schema(
            [
                astropy_quantity_schema,
                core_schema.no_info_plain_validator_function(validate_from_json),
            ]
        )

        def validate_from_python(value: u.Quantity) -> dict[str, Any]:
            return {
                "value": value.value,
                "unit": value.unit,
            }

        from_python_schema = core_schema.union_schema(
            [
                core_schema.chain_schema(
                    [
                        core_schema.is_instance_schema(u.Quantity),
                        core_schema.no_info_before_validator_function(
                            function=validate_from_python,
                            schema=from_json_schema,
                        ),
                    ]
                ),
                from_json_schema,
            ]
        )

        return core_schema.json_or_python_schema(
            json_schema=from_json_schema,
            python_schema=from_python_schema,
            serialization=core_schema.plain_serializer_function_ser_schema(lambda value: value),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _core_schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        schema = {
            "title": None,
            "tag": asdf_tags.ASTROPY_QUANTITY.value,
        }
        if cls.symbols is None and cls.data_type is None and cls.dimensions is None:
            return schema

        properties_schema = {}

        if cls.symbols is not None:
            properties_schema["unit"] = super(NpArrayPydanticAnnotation, cls).__get_pydantic_json_schema__(_core_schema, handler)

        if cls.data_type is not None or cls.dimensions is not None:
            properties_schema["value"] = super().__get_pydantic_json_schema__(_core_schema, handler)

        schema["properties"] = properties_schema

        return schema


class _AstropyQuantity:
    @staticmethod
    def __getitem__(factory: tuple[DTypeLike, Units, Optional[int], Optional[bool]]) -> type:
        if len(factory) < 1:
            raise TypeError("AstropyQuantity requires a dtype.")

        dtype: DTypeLike = factory[0]
        unit: Units = factory[1] if len(factory) > 1 else None
        dimensions: Optional[int] = factory[2] if len(factory) > 2 else None
        strict_data_typing: bool = factory[3] if len(factory) > 3 else False

        return Annotated[
            u.Quantity,
            _AstropyQuantityPydanticAnnotation.factory(
                dtype=dtype, unit=unit, dimensions=dimensions, strict_data_typing=strict_data_typing
            ),
        ]


AstropyQuantity = _AstropyQuantity()
