"""
This module provides a means to build in checks for the type annotations on
node fields. This is done by using the `typeguard`, which when enabled will
check the type annotations on all function calls where decorated.

Note in order to avoid a dependency on `typeguard` this module falls back on
a identity decorator (does nothing) when `typeguard` is not available. Moreover,
this decorator is only applied when the `pytest` module is imported BEFORE this
module is imported.

By default even when typeguard is installed, and pytest has been import first,
the decorator will still default to suppressing the type checks. This is so that
in places where we are not explicitly testing the type annotations, we don't
have to concern ourselves with the type checks being correct. To enable the
type checks, the `enable_typeguard` context manager can be used. A fixture is
also provided for use in testing which enables typeguard for the duration of
the test.
"""

import sys
from functools import wraps
from typing import TypeVar

from ._config import get_config

__all__ = ["type_checked"]


_T = TypeVar("_T")


def _type_checked(target: _T, **kwargs) -> _T:
    """Default identity decorator"""
    return target if target else typechecked


# If pytest is imported start trying to build the typeguard decorator
if "pytest" in sys.modules:
    try:
        from typeguard import suppress_type_checks, typechecked
    except ImportError:
        # If typeguard is not available, fall back to the identity decorator
        type_checked = _type_checked
    else:
        # If typeguard is available, build the decorator
        def surpress_check(function):
            """Function wrapper that enables us to turn on/off typeguard checks suppression"""

            @wraps(function)
            def wrapper(*args, **kwargs):
                """Pull the global flag to determine if we should suppress type checks"""

                # If typeguard is not enabled, suppress the type checks
                if not get_config().typeguard_enabled:
                    with suppress_type_checks():
                        return function(*args, **kwargs)

                # Otherwise do nothing to the function
                return function(*args, **kwargs)

            return wrapper

        def type_checked(function):
            """
            Decorator to check the type annotations on a function
                This simply strings suppress_check on top of typechecked
            """
            return surpress_check(typechecked(function))
else:
    # If no pytest, fall back to the identity decorator
    type_checked = _type_checked