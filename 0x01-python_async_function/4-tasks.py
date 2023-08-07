#!/usr/bin/env python3
"""a module that executes multiple coroutines"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a function that spawn task_wait_random n times with the
       specified max_delay

       Args:
            n(int): number of delay times
            max_delay(int): Specified delay

       Returns:
            List[float]: Sorted List of all delays
    """
    delay_list = []
    for i in range(n):
        delay_time = await task_wait_random(max_delay)
        delay_list.append(delay_time)
    return sorted(delay_list)
