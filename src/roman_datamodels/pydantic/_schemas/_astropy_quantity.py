from pydantic_core import core_schema

astropy_unit_schema = core_schema.str_schema(pattern="[\x00-\x7f]*")
