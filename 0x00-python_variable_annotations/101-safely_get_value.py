#!/usr/bin/env python3
"""
Module doc
"""
from typing import Sequence, Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return a value in a dictionary
    or default value
    """
    return dct.get(key, default)
