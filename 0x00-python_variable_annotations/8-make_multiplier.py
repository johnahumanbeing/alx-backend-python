#!/usr/bin/env python3
""" Annotated make_multiplier function
    module
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier
        Arguments:
            multiplier: float
        Returns:
            a function that multiplies a float by multiplier
    """
    def multiply(n: float) -> float:
        """ Returns the product of n and multiplier
            Arguments:
                n: float
            Returns:
                product of n and multiplier
        """
        return n * multiplier
    return multiply
