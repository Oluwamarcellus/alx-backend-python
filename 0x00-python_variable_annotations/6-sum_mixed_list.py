#!/usr/bin/env pyton3
"""
6-sum_mixed_list module
"""
from typing import List


def sum_mixed_list(mxd_lst: List[(float | int)]) -> float:
    """
    a type-annotated function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float.
    """
    return sum(mxd_lst)