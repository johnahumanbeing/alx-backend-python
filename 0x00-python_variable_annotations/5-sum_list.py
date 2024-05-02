#!/usr/bin/env python3
""" Annotated sum_list function
    module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of the list of floats
        Arguments:
            input_list: List[float]
        Returns:
            sum of the list of floats
    """
    return sum(input_list)
