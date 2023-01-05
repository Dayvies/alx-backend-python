#!/usr/bin/env python3
"""callable functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """callable func"""
    def x(n: float):
        """multiplies"""
        return multiplier * n
    return x
