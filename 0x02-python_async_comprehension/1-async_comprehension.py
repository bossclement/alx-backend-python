#!/usr/bin/env python3
"""
Module doc
"""
from typing import List
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]