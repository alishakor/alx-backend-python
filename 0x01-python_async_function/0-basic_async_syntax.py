#!/usr/bin/env python3
"""a module that indicates the basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """a function that writes an asynchronous coroutine
       takes in an integer argument and return random delay

       Args(int): max_delay

       Returns(float): random delay
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
