#!/usr/bin/env python3
"""
Module doc
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes string & int / float, returns
    their tuple
    """
    return (k, v**2)