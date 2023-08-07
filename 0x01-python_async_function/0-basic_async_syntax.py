#!/usr/bin/env python3
"""a module that indicates the basics of async"""

import asyncio
import random


async def wait_random(max_delay=10):
    """a function that writes an asynchronous coroutine
       takes in an integer argument and return random delay

       Args(int): max_delay

       Returns(float): random delay
    """

    random_delay = random.uniform(1, 100)
    await asyncio.sleep(2)
    return random_delay
