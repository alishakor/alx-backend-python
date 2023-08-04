#!/usr/bin/env python3
"""
    a script that returns the sum of a mixed
    list of integer and floating numbers
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        a type-annotated function sum_mixed_list which
        takes a list mxd_lst of integers and floats and
        returns their sum as a float
    """
    result = 0
    for element in mxd_lst:
        result += element
    return result
