#!/usr/bin/env python3
""" Tasks
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Function to call wait_random and return asyncio.Task
        Args:
            max_delay: maximum delay time to await
                       coroutine
        Return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
