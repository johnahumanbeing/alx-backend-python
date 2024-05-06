#!/usr/bin/env python3
""" Tasks
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Function to call task_wait_random n times
        Args:
            n: itrations for coroutine
            max_delay: maximum delay time to await
                       coroutine
        Return: list of delay time for each coroutine
    """
    delay = await asyncio.gather(*(task_wait_random(max_delay)
                                 for _ in range(n)))
    return sorted(delay)
