#!/usr/bin/env python3
"""
Module doc
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time() - start
    return end
