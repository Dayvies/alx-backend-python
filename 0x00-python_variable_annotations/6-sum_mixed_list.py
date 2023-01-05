#!/usr/bin/env python3
"""mixed  annotations"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum mixed list"""
    x: float = float(sum(mxd_lst))
    return x
