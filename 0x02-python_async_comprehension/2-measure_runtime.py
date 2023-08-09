#!/usr/bin/env python3

"""a module that measures runtime"""
import asyncio
from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures time"""
    start_time = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time()
    total_time = end_time - start_time
    return total_time
