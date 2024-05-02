#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """This function measures the runtime of an asynchronous operation.
    It starts a timer, runs the async_comprehension function four times
    concurrently, and then stops the timer, returning the elapsed time."""
    runtime = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    return time.time() - runtime
