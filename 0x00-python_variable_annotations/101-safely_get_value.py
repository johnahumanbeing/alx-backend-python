#!/usr/bin/env python3
""" more invloved type annotations
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, 
                    default: Union[T, None] = None) \
                    -> Union[Any, T]:
    """ get value from dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
