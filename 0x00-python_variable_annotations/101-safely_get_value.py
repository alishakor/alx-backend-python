#!/usr/bin/env python3
"""a script that displays type annotation of
a function with unknown paramter and return values
"""
from typing import Mapping, Any, Union, T


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> \
                     Union[Any, T]:
    """type annonations added to function"""
    if key in dct:
        return dct[key]
    else:
        return default
