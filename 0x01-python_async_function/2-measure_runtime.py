#!/usr/bin/env python3
"""a module that measures the runtime"""

import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """a function that measures the total execution
       time for wait_n(n, max_delay)

       Args:
            n(int): number of delay times
            max_delay(int): Specified delay

       Returns:
            float: total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    Total_time = end_time - start_time
    return Total_time / n
