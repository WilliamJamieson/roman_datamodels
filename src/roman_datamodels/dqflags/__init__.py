"""Roman Data Quality Flags

A full description of the data quality flags can be found in the
:external+romancal:ref:`romancal data quality flags documentation <data_quality_flags>`.


Implementation
--------------

The flags are implemented as "bit flags": Each flag is assigned a bit position
in a byte, or multi-byte word, of memory. If that bit is set, the flag assigned
to that bit is interpreted as being set or active.

The data structure that stores bit flags is just the standard Python `int`,
which provides 32 bits. Bits of an integer are most easily referred to using
the formula ``2**bit_number`` where ``bit_number`` is the 0-index bit of interest.

The flags themselves are defined by the ``shareddq.yaml``, ``pixeldq.yaml``, and
``groupdq.yaml`` files in this directory. ``shareddq.yaml`` holds the flags common
to both the pixel and group flags, while the other two files hold the flags specific
to each together with the numpy dtype backing the enum. A flag's value is ``2**bit``,
where a ``null`` bit corresponds to a value of ``0``.
"""

# Something with pickling of multiclassed enums was changed in 3.11 + allowing
# us to directly use the numpy scalar type as the enum mixin rather than a python `int`.
from enum import Enum, unique
from importlib.resources import files

from asdf.tags.core.ndarray import asdf_datatype_to_numpy_dtype
from yaml import safe_load

__all__ = ["group", "pixel"]


class _DQFlag(Enum):
    @property
    def bit_value(self):
        value = int(self.value)
        if value == 0:
            return None
        if value & (value - 1):
            msg = f"{self.name} does not have a single bit value"
            raise ValueError(msg)
        return value.bit_length() - 1


def _load(name):
    """Load one of the dqflags yaml specifications."""
    return safe_load((files(__name__) / f"{name}.yaml").read_text())


def _create_flags(spec, shared_flags):
    """Build a numpy backed bit flag enum from a dqflags yaml specification."""

    name = spec["name"].strip()
    flags = shared_flags | spec["flags"]
    dtype = asdf_datatype_to_numpy_dtype(spec["dtype"].strip())

    metacls = type(_DQFlag)
    bases = (dtype.type, _DQFlag)
    namespace = metacls.__prepare__(name, bases)
    namespace["__doc__"] = spec["description"].strip()
    namespace["__module__"] = __name__
    # -1 sorts the null bit (GOOD) ahead of bit 0
    for flag_name, flag in sorted(flags.items(), key=lambda item: -1 if item[1]["bit"] is None else item[1]["bit"]):
        namespace[flag_name] = 0 if flag["bit"] is None else 2 ** flag["bit"]

    cls = unique(metacls(name, bases, namespace))
    for flag_name, flag in flags.items():
        cls[flag_name].__doc__ = flag["description"].strip()

    return cls


_shared_flags = _load("shareddq")["flags"]

pixel = _create_flags(_load("pixeldq"), _shared_flags)

group = _create_flags(_load("groupdq"), _shared_flags)
