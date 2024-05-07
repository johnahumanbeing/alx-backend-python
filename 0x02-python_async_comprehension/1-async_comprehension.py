#!/usr/bin/env python3
""" Async Comprehensions
"""

import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """ Async Comprehensions
        Returns: List of random numbers between 0 and 10
    """
    generator = __import__('0-async_generator').async_generator
    return [i async for i in generator()]
