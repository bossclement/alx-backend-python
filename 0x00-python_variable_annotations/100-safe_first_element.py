#!/usr/bin/env python3
"""
Module doc
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns a list if present exists
    """
    if lst:
        return lst[0]
    else:
        return None
