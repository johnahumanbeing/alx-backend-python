#!/usr/bin/env python3
""" Measure the runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime
        Args:
            n: iterations for coroutine
            max_delay: maximum delay time to await
                       coroutine
        Return: average runtime for coroutine
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
