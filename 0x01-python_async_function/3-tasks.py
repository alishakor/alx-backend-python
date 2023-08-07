#!/usr/bin/env python3
"""a module that returns a task"""

import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """a function task_wait_random that takes in max_delay
       and returns asyncio.Task

       Args:
            max_delay(int): Specified delay

       Returns:
            asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
