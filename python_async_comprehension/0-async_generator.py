#!/usr/bin/env python3
"""
async_generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    This function generates a sequence of 10 random numbers between 0 and 10,
    with a 1-second delay between each number.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
