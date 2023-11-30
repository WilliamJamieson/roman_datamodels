from enum import auto
from sys import version_info

from pydantic_core import core_schema

if version_info < (3, 11):
    from strenum import StrEnum
else:
    from enum import StrEnum


class scalar_dtype(StrEnum):
    int8 = auto()
    int16 = auto()
    int32 = auto()
    int64 = auto()
    uint8 = auto()
    uint16 = auto()
    uint32 = auto()
    uint64 = auto()
    float32 = auto()
    float64 = auto()
    complex64 = auto()
    complex128 = auto()
    bool8 = auto()


class scalar_str_dtype(StrEnum):
    ascii = auto()
    ucs4 = auto()


class byteorder(StrEnum):
    big = auto()
    little = auto()


asdf_ndarray_schema = core_schema.definitions_schema(
    core_schema.definition_reference_schema("ndarray"),
    [
        core_schema.union_schema(
            [
                core_schema.definition_reference_schema("ndarray_object"),
                core_schema.definition_reference_schema("inline_data"),
            ],
            ref="ndarray",
        ),
        core_schema.model_fields_schema(
            {
                "source": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.union_schema(
                            [
                                core_schema.int_schema(),
                                core_schema.str_schema(),
                            ]
                        ),
                        default=None,
                    )
                ),
                "data": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.definition_reference_schema("inline_data"),
                        default=None,
                    )
                ),
                "shape": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.list_schema(
                            core_schema.union_schema(
                                [
                                    core_schema.int_schema(ge=0),
                                    core_schema.literal_schema(["*"]),
                                ]
                            )
                        ),
                        default=None,
                    )
                ),
                "datatype": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.definition_reference_schema("datatype"),
                        default=None,
                    )
                ),
                "byteorder": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.definition_reference_schema("byteorder"),
                        default=None,
                    )
                ),
                "offset": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.int_schema(ge=0),
                        default=0,
                    )
                ),
                "strides": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.list_schema(
                            core_schema.union_schema(
                                [
                                    core_schema.int_schema(ge=1),
                                    core_schema.int_schema(le=-1),
                                ]
                            )
                        ),
                        default=None,
                    )
                ),
                "mask": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.union_schema(
                            [
                                core_schema.definition_reference_schema("number"),
                                # add complex later
                                core_schema.definition_reference_schema("ndarray"),
                                # core_schema.model_fields_schema(
                                #     {
                                #         "datatype": core_schema.model_field(
                                #             core_schema.literal_schema([scalar_dtype.bool8.value])
                                #         )
                                #     },
                                #     extra_behavior="allow",
                                #     extras_schema=core_schema.definition_reference_schema("ndarray")
                                # )
                            ]
                        ),
                        default=None,
                    )
                ),
            },
            ref="ndarray_object",
        ),
        core_schema.list_schema(core_schema.definition_reference_schema("inline_data_item"), ref="inline_data"),
        core_schema.nullable_schema(
            core_schema.union_schema(
                [
                    core_schema.definition_reference_schema("number"),
                    core_schema.str_schema(),
                    core_schema.definition_reference_schema("inline_data"),
                    # Add complex later
                    core_schema.bool_schema(),
                ]
            ),
            ref="inline_data_item",
        ),
        core_schema.union_schema(
            [
                core_schema.definition_reference_schema("scalar_datatype"),
                core_schema.definition_reference_schema("array_datatype"),
            ],
            ref="datatype",
        ),
        core_schema.list_schema(core_schema.definition_reference_schema("array_item_datatype"), ref="array_datatype"),
        core_schema.union_schema(
            [
                core_schema.definition_reference_schema("scalar_datatype"),
                core_schema.definition_reference_schema("object_datatype"),
            ],
            ref="array_item_datatype",
        ),
        core_schema.model_fields_schema(
            {
                "name": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.str_schema(pattern="[A-Za-z_][A-Za-z0-9_]*"),
                        default=None,
                    ),
                ),
                "datatype": core_schema.model_field(core_schema.definition_reference_schema("datatype")),
                "byteorder": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.with_default_schema(
                            core_schema.definition_reference_schema("byteorder"),
                            default=None,
                        ),
                        default=None,
                    )
                ),
                "shape": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.definition_reference_schema("shape"),
                        default=None,
                    )
                ),
            },
            ref="object_datatype",
        ),
        core_schema.literal_schema([e.value for e in byteorder], ref="byteorder"),
        core_schema.list_schema(core_schema.int_schema(ge=0), ref="shape"),
        core_schema.union_schema(
            [
                core_schema.definition_reference_schema("scalar_dtype"),
                core_schema.definition_reference_schema("scalar_str_dtype"),
            ],
            ref="scalar_datatype",
        ),
        core_schema.literal_schema([e.value for e in scalar_dtype], ref="scalar_dtype"),
        core_schema.tuple_positional_schema(
            [core_schema.definition_reference_schema("str_dtype"), core_schema.int_schema(ge=0)], ref="scalar_str_dtype"
        ),
        core_schema.literal_schema([e.value for e in scalar_str_dtype], ref="str_dtype"),
        core_schema.union_schema([core_schema.int_schema(), core_schema.float_schema()], ref="number"),
    ],
)
