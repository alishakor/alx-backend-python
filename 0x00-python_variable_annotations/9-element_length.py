#!/usr/bin/env python3
"""
    a script that annotes a function
    and returns values with appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    """a typed-function that returns iterables
    """
    return [(i, len(i)) for i in lst]
