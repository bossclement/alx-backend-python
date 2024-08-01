#!/usr/bin/env python3
"""
Module doc
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return array length
    """
    return [(i, len(i)) for i in lst]
