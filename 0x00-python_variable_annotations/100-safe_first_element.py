#!/usr/bin/env python3
"""a script that shows correct duck-typed annotation
"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> [Union[Any, None]]:
    """a list with unknown type of element"""
    if lst:
        return lst[0]
    else:
        return None
