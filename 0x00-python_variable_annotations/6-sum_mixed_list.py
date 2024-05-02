#!/usr/bin/env python3
""" Annotated sum_mixed_list function
    module
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of the list of floats
        Arguments:
            mxd_lst: List[Union[int, float]]
        Returns:
            sum of the list of floats
    """
    return sum(mxd_lst)
