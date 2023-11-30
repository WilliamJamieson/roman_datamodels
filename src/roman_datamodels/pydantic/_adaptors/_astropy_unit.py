import warnings
from typing import Annotated, Any, ClassVar, Optional, Union

import astropy.units as u
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import SchemaValidator, core_schema

__all__ = ["Unit", "AstropyUnit"]


Unit = Union[
    u.CompositeUnit,
    u.IrreducibleUnit,
    u.NamedUnit,
    u.PrefixUnit,
    u.Unit,
    u.UnrecognizedUnit,
    u.function.mixin.IrreducibleFunctionUnit,
    u.function.mixin.RegularFunctionUnit,
]
astropy_unit_schema = core_schema.str_schema(pattern="[\x00-\x7f]*")


def _get_unit_symbol(unit: Union[Unit, str]) -> str:
    if isinstance(unit, str):
        return unit

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=u.UnitsWarning)

        try:
            return unit.to_string(format="vounit")
        except (u.UnitsError, ValueError):
            return unit.to_string()


class _AstropyUnitPydanticAnnotation:
    symbol: ClassVar[Optional[str]] = None

    @classmethod
    def _get_unit_symbol(cls, unit: Unit) -> str:
        symbol = None if unit is None else _get_unit_symbol(unit)
        v = SchemaValidator(core_schema.nullable_schema(astropy_unit_schema))
        v.validate_python(symbol)

        return symbol

    @classmethod
    def factory(cls, *, unit: Optional[Unit] = None) -> type:
        symbol = cls._get_unit_symbol(unit)

        return type(cls.__name__ if symbol is None else f"{cls.__name__}_{symbol}", (cls,), {"symbol": symbol})

    @classmethod
    def _unit_schema(cls) -> core_schema.CoreSchema:
        return astropy_unit_schema if cls.symbol is None else core_schema.literal_schema([cls.symbol])

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        def validate_from_json(value: tuple) -> Any:
            return u.Unit(value[0], parse_strict="silent")

        from_json_schema = core_schema.chain_schema(
            [
                cls._unit_schema(),
                core_schema.no_info_plain_validator_function(validate_from_json),
            ]
        )

        from_python_schema = core_schema.union_schema(
            [
                core_schema.chain_schema(
                    [
                        core_schema.is_instance_schema(Unit),
                        core_schema.no_info_before_validator_function(
                            function=_get_unit_symbol,
                            schema=cls._unit_schema(),
                        ),
                    ]
                ),
                from_json_schema,
            ]
        )

        serializer_schema = core_schema.plain_serializer_function_ser_schema(_get_unit_symbol)

        return core_schema.json_or_python_schema(
            json_schema=from_json_schema,
            python_schema=from_python_schema,
            serialization=serializer_schema,
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _core_schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        return handler(cls._unit_schema())


class _AstropyUnit:
    """Hack to make it look like it has the style of a type annotation."""

    @staticmethod
    def __getitem__(unit: Optional[Unit] = None) -> Unit:
        return Annotated[type(unit), _AstropyUnitPydanticAnnotation.factory(unit=unit)]


AstropyUnit = _AstropyUnit()
