#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List
import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    This function returns a list of random_nbs from the
    async_generator function using an asynchronous comprehension.
    """
    random_nbs = [random_nbs async for random_nbs in async_generator()]
    return random_nbs
