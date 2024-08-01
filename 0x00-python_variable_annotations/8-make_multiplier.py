#!/usr/bin/env python3
"""
Module doc
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns
    function that multiplies a float by multiplier
    """
    def multiplier_fn(number: float) -> float:
        """Multiplies a float by number"""
        return number * multiplier

    return multiplier_fn