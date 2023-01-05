#!/usr/bin/env python3
"""Iterator annotations"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Iterator sequences"""
    return [(i, len(i)) for i in lst]
