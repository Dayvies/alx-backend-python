#!/usr/bin/env python3
"""mixed  annotations"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """mixed annots"""
    s = float(v**2)
    return (k, s)
