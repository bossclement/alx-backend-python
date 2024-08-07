#!/usr/bin/env python3
'''
Module doc
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Will execute async_comprehension four
    times in parallel using asyncio.gather
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for n in range(4)))
    end = time.time()
    return end - start
