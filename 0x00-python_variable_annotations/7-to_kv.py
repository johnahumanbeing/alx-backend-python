#!/usr/bin/env python3
""" Annotated to_kv function
    module
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple
        Arguments:
            k: str
            v: Union[int, float]
        Returns:
            Tuple[str, float]
    """
    return (k, v * v)
