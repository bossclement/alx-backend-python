#!/usr/bin/env python3
"""
Module doc
"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    Takes array of floats & ints and
    returns their sum
    """
    return sum(input_list)